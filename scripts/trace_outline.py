#!/usr/bin/env python3
"""
Extract outline from a logo PNG → clean SVG.
Uses only Pillow (no numpy/opencv/potrace required).

Steps:
1. Threshold RGBA image to binary mask (foreground vs background)
2. Moore neighborhood contour tracing to find boundaries
3. Ramer-Douglas-Peucker simplification to reduce points
4. Output as SVG path
"""

from PIL import Image
import sys


def image_to_mask(img, threshold=240):
    """Convert RGBA image to binary mask. Returns 2D list of bools."""
    gray = img.convert("L")
    w, h = gray.size
    pixels = gray.load()
    # True = foreground (dark), False = background (light)
    mask = []
    for y in range(h):
        row = []
        for x in range(w):
            row.append(pixels[x, y] < threshold)
        mask.append(row)
    return mask, w, h


def pad_mask(mask, w, h):
    """Add 1px border of False around mask to ensure contours close."""
    new_mask = [[False] * (w + 2)]
    for row in mask:
        new_mask.append([False] + row + [False])
    new_mask.append([False] * (w + 2))
    return new_mask, w + 2, h + 2


def find_contours(mask, w, h):
    """Find all contours using Moore neighborhood tracing."""
    visited_edges = set()
    contours = []

    # 8-connectivity neighbors: clockwise from right
    #   3 2 1
    #   4 . 0
    #   5 6 7
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    for sy in range(h):
        for sx in range(w):
            # Find a foreground pixel adjacent to background (entry from left)
            if not mask[sy][sx] and sx + 1 < w and mask[sy][sx + 1]:
                start = (sx + 1, sy)
                if start in visited_edges:
                    continue

                # Trace this contour
                contour = []
                cx, cy = start
                backtrack_dir = 4  # came from left

                first = True
                while True:
                    contour.append((cx, cy))
                    visited_edges.add((cx, cy))

                    # Search for next boundary pixel
                    search_start = (backtrack_dir + 1) % 8
                    found = False
                    for i in range(8):
                        d = (search_start + i) % 8
                        nx, ny = cx + dx[d], cy + dy[d]
                        if 0 <= nx < w and 0 <= ny < h and mask[ny][nx]:
                            backtrack_dir = (d + 4) % 8
                            cx, cy = nx, ny
                            found = True
                            break

                    if not found:
                        break  # isolated pixel

                    if (cx, cy) == start and not first:
                        break
                    first = False

                if len(contour) >= 10:  # skip tiny noise
                    contours.append(contour)

    return contours


def rdp_simplify(points, epsilon):
    """Ramer-Douglas-Peucker line simplification."""
    if len(points) <= 2:
        return points

    # Find the point with the maximum distance from the line start-end
    sx, sy = points[0]
    ex, ey = points[-1]

    max_dist = 0
    max_idx = 0

    line_len_sq = (ex - sx) ** 2 + (ey - sy) ** 2

    for i in range(1, len(points) - 1):
        px, py = points[i]
        if line_len_sq == 0:
            dist = ((px - sx) ** 2 + (py - sy) ** 2) ** 0.5
        else:
            t = max(0, min(1, ((px - sx) * (ex - sx) + (py - sy) * (ey - sy)) / line_len_sq))
            proj_x = sx + t * (ex - sx)
            proj_y = sy + t * (ey - sy)
            dist = ((px - proj_x) ** 2 + (py - proj_y) ** 2) ** 0.5
        if dist > max_dist:
            max_dist = dist
            max_idx = i

    if max_dist > epsilon:
        left = rdp_simplify(points[:max_idx + 1], epsilon)
        right = rdp_simplify(points[max_idx:], epsilon)
        return left[:-1] + right
    else:
        return [points[0], points[-1]]


def contour_to_svg_path(contour, offset_x=-1, offset_y=-1):
    """Convert contour points to SVG path d attribute."""
    if not contour:
        return ""
    parts = [f"M{contour[0][0] + offset_x},{contour[0][1] + offset_y}"]
    for x, y in contour[1:]:
        parts.append(f"L{x + offset_x},{y + offset_y}")
    parts.append("Z")
    return "".join(parts)


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "logo.png"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "logo_outline.svg"
    epsilon = float(sys.argv[3]) if len(sys.argv) > 3 else 1.5

    print(f"Loading {input_path}...")
    img = Image.open(input_path)
    orig_w, orig_h = img.size
    print(f"  Size: {orig_w}x{orig_h}, Mode: {img.mode}")

    print("Creating binary mask...")
    mask, w, h = image_to_mask(img, threshold=240)

    print("Padding mask...")
    mask, w, h = pad_mask(mask, w, h)

    print("Tracing contours...")
    sys.setrecursionlimit(50000)
    contours = find_contours(mask, w, h)
    print(f"  Found {len(contours)} contours")

    # Sort by size (largest first)
    contours.sort(key=len, reverse=True)

    for i, c in enumerate(contours[:10]):
        print(f"  Contour {i}: {len(c)} points")

    print(f"Simplifying (epsilon={epsilon})...")
    simplified = []
    for c in contours:
        s = rdp_simplify(c, epsilon)
        if len(s) >= 4:
            simplified.append(s)

    total_points = sum(len(s) for s in simplified)
    print(f"  {len(simplified)} contours, {total_points} total points")

    print(f"Writing {output_path}...")
    paths = "\n".join(
        f'  <path d="{contour_to_svg_path(c)}" />'
        for c in simplified
    )

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {orig_w} {orig_h}" width="{orig_w}" height="{orig_h}">
  <style>
    path {{ fill: none; stroke: #E8930C; stroke-width: 2; }}
  </style>
{paths}
</svg>'''

    with open(output_path, "w") as f:
        f.write(svg)

    import os
    size = os.path.getsize(output_path)
    print(f"Done! {size:,} bytes ({size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
