# SEO 분석 보고서: dabel5.org (사이트 전체)

**분석일:** 2026-02-24 (2차, 최종)
**점수:** B+ (80/100)

---

## 카테고리별 점수

| 카테고리 | 점수 |
|---------|------|
| 크롤링/인덱싱 | 95/100 |
| 다국어 SEO | 98/100 |
| 구조화 데이터 | 90/100 |
| OG/소셜 태그 | 85/100 |
| 콘텐츠 SEO | 60/100 |
| 이미지 SEO | 30/100 |
| 내부 링크 | 40/100 |
| 성능/보안 | 95/100 |

**기술 SEO는 우수. 콘텐츠 보강(이미지, 내부 링크, 섹션 메타)이 최우선 과제.**

---

## 잘된 점

- **hreflang 완벽 구현**: HTML `<head>` 12개 언어 + `x-default=en`, sitemap.xml에도 `xhtml:link` hreflang 포함
- **canonical URL**: 모든 페이지에 `<link rel="canonical">` 존재
- **OG/Twitter 태그 완비**: `og:title`, `og:description`, `og:image`, `og:type`, `og:locale` + alternates, `twitter:card=summary_large_image`
- **og-image.webp**: 1200x630 (Google 권장 사이즈 정확히 일치), 18KB (경량)
- **Schema.org**: `WebSite` (홈), `Article` + `publisher` (글), `BreadcrumbList` (섹션 글), `ProfilePage` (about)
- **robots.txt**: Sitemap 디렉티브 포함, `/languages/` 12개 언어 경로 Disallow
- **sitemap.xml**: sitemapindex → 12개 언어 하위 사이트맵, 에러 0, 경고 0
- **CSS minify + fingerprint**: `main.min.{hash}.css` (24KB 원본)
- **HTML minify**: `hugo --minify` 적용, 홈페이지 ~10KB
- **RTL 지원**: `dir="rtl"` ar/he 자동 적용
- **taxonomy noindex**: 태그 페이지 `<meta name="robots" content="noindex, follow">`
- **콘텐츠 파리티**: 12개 언어 × 20파일 = 240파일, 완벽한 번역 커버리지
- **아티클 SEO**: title, date, tags, summary, author, authorLink 모두 존재 (9개 why 글)
- **성능**: 외부 폰트 없음, 렌더 블로킹 JS 없음, CloudFront CDN + HTTPS
- **GSC**: 사이트맵 제출 완료 (2026-02-24), 에러 0

---

## Google Search Console 현황

| 항목 | 값 |
|------|-----|
| 검색 노출 | 0 |
| 클릭 | 0 |
| 사이트맵 | 제출됨 (에러 0) |
| 색인 상태 | 크롤링 대기 중 |

사이트가 신규이므로 데이터 없음. 사이트맵 제출 후 인덱싱까지 1~2주 소요 예상.

---

## 개선 필요

| 우선순위 | 항목 | 현재 상태 | 권장 사항 | 영향도 |
|---------|------|----------|----------|--------|
| 1 | 섹션 _index.md 메타 비어있음 | power, factory 등 8개 섹션 `_index.md`에 `summary:` 없음 → 사이트 전체 description 폴백 | 각 섹션 _index.md에 고유 `summary:` 추가 | **높음** |
| 2 | 아티클 고유 OG 이미지 없음 | 9개 글 모두 `image:` 필드 없음 → 전부 `/og-image.webp` 공유 | 글별 대표 이미지 생성 후 `image:` 필드 추가 | **높음** |
| 3 | 콘텐츠 이미지 0개 | 전체 글에 `![alt]` 참조 0건 → 이미지 검색 유입 불가 | 핵심 다이어그램/인포그래픽 추가 (WebP, alt 키워드 포함) | **높음** |
| 4 | 내부 링크 부재 | why/ 글 9개가 서로 링크 안 함 → 크롤링 깊이/PageRank 분산 불리 | 관련 글 간 2~3개씩 내부 링크 추가 | **중간** |
| 5 | /about/ 페이지 미존재 | `about.html` 레이아웃 존재하지만 `about.md` 없음 → 프로젝트 소개 페이지 없음 | about.md 생성 (E-E-A-T 신호 강화) | **중간** |
| 6 | Overview 섹션 콘텐츠 미비 | power/, factory/ 등 8개 섹션이 빈 _index.md만 존재 → 얇은 콘텐츠 | 섹션별 개요 콘텐츠 작성 | **중간** |
| 7 | 로고 alt 비어있음 | `<img alt="" width="28" height="28">` | `alt="DABEL5"` 추가 (접근성+SEO) | **낮음** |

---

## 키워드 전략

**주요 타겟 키워드:**
- `Dyson swarm` / `Dyson swarm engineering`
- `self-replicating Dyson swarm`
- `asteroid mining Dyson swarm`
- `Lagrange L5`
- `space solar power`

**추천 LSI 키워드:**
- `Kardashev scale`, `megastructure`, `space manufacturing`
- `1986 DA asteroid`, `nickel-iron asteroid`
- `solar thermal turbine`, `space habitat`, `O'Neill cylinder`
- `climate engineering`, `Sun-Earth L1 shade`

**검색 의도 분석:**
- 정보 탐색형 (Informational): "how to build a Dyson sphere", "Dyson swarm vs Dyson sphere"
- 니치 커뮤니티: r/IsaacArthur, r/SpaceEngineers, r/Futurology 유저가 핵심 타겟
- 한국어: "다이슨 스웜", "소행성 채굴", "우주 태양광" 등 경쟁이 거의 없는 블루오션

---

## 구조화 데이터 현황

| 페이지 타입 | 스키마 | 상태 |
|-----------|--------|------|
| 홈 | `WebSite` | OK |
| 글 (why/*) | `Article` + `BreadcrumbList` | OK (`publisher` 포함) |
| About | `ProfilePage` | N/A (페이지 미존재) |

현재 구조화 데이터는 적절하게 구현되어 있음. 추가 제안:

```json
// FAQ 구조화 데이터 (why/ 글에 추가 가능)
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Why not start a Dyson swarm at Mercury?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "At Mercury's orbit (0.39 AU), mirrors experience thermal runaway..."
    }
  }]
}
```

---

## 즉시 적용 가능한 수정사항

### 1. 섹션 _index.md에 summary 추가 (8개 파일)

각 섹션 `_index.md`에 `summary:` 필드 추가. 예시:

`content/en/power/_index.md`:
```yaml
---
title: "Power"
summary: "How a Dyson module generates 370 MW from a 1 km² mirror — solar thermal turbines, heat cascade, and local consumption at L5."
---
```

`content/en/why/_index.md`:
```yaml
---
title: "Why?"
summary: "First-principles arguments for building a Dyson swarm at L5 from asteroid resources — not Mercury."
---
```

### 2. 로고 alt 텍스트 추가

`layouts/partials/header.html:3`:
```html
<!-- 현재 -->
<img class="site-logo-icon" src="/images/logo.webp" alt="" width="28" height="28">
<!-- 권장 -->
<img class="site-logo-icon" src="/images/logo.webp" alt="DABEL5" width="28" height="28">
```

### 3. 내부 링크 전략 (글 수정 시 점진적 적용)

각 why/ 글 하단에 관련 글 링크 추가:
```markdown
---
**Related:**
- [Why not Mercury?](/why/mirror-thermal-runaway/)
- [Where do you get the metal?](/why/1986da/)
```

---

## 완료된 수정사항 (1차 분석 후 적용)

- [x] `layouts/robots.txt` 커스텀 템플릿 생성 (Sitemap 디렉티브 + /languages/ Disallow)
- [x] `static/og-image.webp` 대표 이미지 생성 (1200x630)
- [x] `static/favicon.ico` + `static/apple-touch-icon.png` 생성
- [x] GSC 사이트맵 제출 (`https://dabel5.org/sitemap.xml`)
- [x] 홈 `_index.md` summary 12개 언어 개선
- [x] 홈 랜딩 페이지 4섹션 스토리텔링 구조로 리디자인 (12개 언어)
- [x] 언어 자동 리다이렉트 CloudFront Function 적용

## 다음 액션

- [ ] 8개 섹션 `_index.md`에 고유 `summary:` 추가 (12개 언어)
- [ ] 아티클별 고유 OG 이미지 생성 + `image:` front matter 추가
- [ ] 콘텐츠에 다이어그램/인포그래픽 이미지 추가 (WebP)
- [ ] why/ 글 간 내부 링크 추가
- [ ] `/about/` 페이지 생성 (12개 언어)
- [ ] Overview 섹션(power, factory 등) 개요 콘텐츠 작성
- [ ] 로고 `alt="DABEL5"` 추가
