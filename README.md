**[한국어](README.ko.md)**

# DABEL5 — Dyson Swarm Engineering

**Open engineering design for a self-replicating Dyson swarm at Earth–Sun L5, built from asteroid resources.**

Website: [dabel5.org](https://dabel5.org)

---

## What is DABEL5?

DABEL5 (**D**yson modules, **A**steroid **B**elt & **E**arth **L5**) is an open engineering design that answers a simple question: *can we build a Dyson swarm using only existing technology and asteroid materials?*

Not fusion. Not antimatter. Not breakthroughs that don't exist yet. Turbines (1884), iron-nickel batteries (1901), zone refining (1952), 28nm semiconductors (2011) — proven technologies that become optimal when the constraints are self-replication and space environment.

## Design overview

| Section | Description |
|---------|-------------|
| [Why?](https://dabel5.org/why/) | First-principles arguments behind every design choice |
| [Power](https://dabel5.org/power/) | 1 km² mirror → 1.2 GW solar thermal → 370 MW turbine electricity |
| [Factory](https://dabel5.org/factory/) | Vacuum smelting, slag-to-silicon, 28nm TPU fabrication |
| [Mining](https://dabel5.org/mining/) | Asteroid 1986 DA — 3 km of nickel-iron, Earth approach in 2038 |
| [Transport](https://dabel5.org/transport/) | Orbital mechanics, NTP, solar sail, transfer window logistics |
| [Habitat](https://dabel5.org/habitat/) | O'Neill cylinder, artificial gravity, closed-loop ecology |
| [Computing](https://dabel5.org/computing/) | Smelting slag → Si → 28nm TPU — one module = 30,000 H100-class |
| [Climate](https://dabel5.org/climate/) | Fe-Ni sunshade at SEL1 — 2 million km² reverses 2°C warming |
| [Detail](https://dabel5.org/detail/) | Specs, calculations, numbers with sources |

## Key numbers

```
Module mirror area:     1 km²
Solar thermal input:    1.2 GW
Electrical output:      370 MW (turbine, 30%)
Thermal cascade:        1,600°C → 600°C → 200°C → 30°C
Thermal storage:        51,000 t molten Fe-Ni, 58 × r=3m units, ~145 Wh/kg
AI compute:             ~30,000 H100-equivalent (28nm TPU × 1.48M)
Crew per module:        ~3,000
Target asteroid:        1986 DA (M-type, ⌀3 km, 90%+ Fe-Ni)
Bootstrap location:     Earth-Moon L5 → Sun-Earth L5
Self-replication:       270,000 modules from one asteroid
```

## Languages

Available in 12 languages: [English](https://dabel5.org) · [한국어](https://dabel5.org/ko/) · [中文](https://dabel5.org/zh/) · [日本語](https://dabel5.org/ja/) · [Español](https://dabel5.org/es/) · [Português](https://dabel5.org/pt/) · [Français](https://dabel5.org/fr/) · [Deutsch](https://dabel5.org/de/) · [Русский](https://dabel5.org/ru/) · [Bahasa Indonesia](https://dabel5.org/id/) · [العربية](https://dabel5.org/ar/) · [עברית](https://dabel5.org/he/)

## Tech stack

- [Hugo](https://gohugo.io/) static site generator — no external theme, custom layouts
- AWS S3 + CloudFront + Route53 + ACM
- Infrastructure as code (Terraform)
- Dark theme, responsive, RTL support (Arabic, Hebrew)

## Repository structure

```
content/           12-language content (Markdown)
layouts/           Hugo templates (no external theme)
assets/css/        Single CSS file (dark theme, RTL)
static/images/     WebP images
deployments/       Terraform infrastructure
hugo.toml          Hugo configuration
Makefile           Build and deploy commands
```

## Build

```bash
hugo server -D          # Local development (localhost:1313)
hugo --minify           # Production build → public/
```

## License

- Content (`content/`, `static/images/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- Code (everything else): [MIT](LICENSE)

## Author

[Park Jun Woo](https://parkjunwoo.com)
