**[English](README.md)**

# DABEL5 — 다이슨 스웜 공학

**소행성 자원으로 지구-태양 L5에 자기복제 다이슨 스웜을 건설하는 오픈 엔지니어링 설계.**

웹사이트: [dabel5.org](https://dabel5.org/ko/)

---

## DABEL5란?

DABEL5(**D**yson modules, **A**steroid **B**elt & **E**arth **L5**)는 하나의 질문에 답하는 오픈 엔지니어링 설계다: *기존 기술과 소행성 자원만으로 다이슨 스웜을 만들 수 있는가?*

핵융합도, 반물질도, 아직 존재하지 않는 기술 돌파구도 필요 없다. 터빈(1884), 철-니켈 전지(1901), 존 리파이닝(1952), 28nm 반도체(2011) — 자기복제와 우주 환경이라는 제약 조건에서 최적이 되는 검증된 기술들.

## 설계 개요

| 섹션 | 내용 |
|------|------|
| [왜?](https://dabel5.org/ko/why/) | 모든 설계 선택 뒤의 제1원리 논증 |
| [발전](https://dabel5.org/ko/power/) | 1 km² 거울 → 1.2 GW 집열 → 370 MW 터빈 발전 |
| [공장](https://dabel5.org/ko/factory/) | 진공 제련, 슬래그→실리콘, 28nm TPU 제조 |
| [채광](https://dabel5.org/ko/mining/) | 소행성 1986 DA — 직경 3 km 니켈-철, 2038년 지구 접근 |
| [수송](https://dabel5.org/ko/transport/) | 궤도역학, NTP 추진, 솔라 세일, 전이 창 물류 |
| [거주](https://dabel5.org/ko/habitat/) | 오닐 실린더, 인공중력, 폐쇄 생태계 |
| [연산](https://dabel5.org/ko/computing/) | 슬래그 → Si → 28nm TPU — 모듈 1기 = H100 3만 장급 |
| [기후](https://dabel5.org/ko/climate/) | SEL1 Fe-Ni 차폐판 — 200만 km²로 2°C 냉각 |
| [설계](https://dabel5.org/ko/detail/) | 상세 스펙, 계산 근거 |

## 핵심 수치

```
모듈 거울 면적:       1 km²
태양열 입력:          1.2 GW
전기 출력:            370 MW (터빈, 효율 30%)
열 캐스케이드:        1,600°C → 600°C → 200°C → 30°C
축열:                51,000 t 용융 Fe-Ni, 반경 3m × 58유닛, ~145 Wh/kg
AI 연산:             H100 ~3만 장 환산 (28nm TPU × 148만 장)
모듈당 거주 인원:     ~3,000명
대상 소행성:          1986 DA (M형, 직경 3 km, 90%+ Fe-Ni)
부트스트랩:           지구-달 L5 → 태양-지구 L5
자기복제:             소행성 1개 → 모듈 270,000기
```

## 언어

12개 언어 지원: [English](https://dabel5.org) · [한국어](https://dabel5.org/ko/) · [中文](https://dabel5.org/zh/) · [日本語](https://dabel5.org/ja/) · [Español](https://dabel5.org/es/) · [Português](https://dabel5.org/pt/) · [Français](https://dabel5.org/fr/) · [Deutsch](https://dabel5.org/de/) · [Русский](https://dabel5.org/ru/) · [Bahasa Indonesia](https://dabel5.org/id/) · [العربية](https://dabel5.org/ar/) · [עברית](https://dabel5.org/he/)

## 기술 스택

- [Hugo](https://gohugo.io/) 정적 사이트 생성기 — 외부 테마 없이 직접 제작
- AWS S3 + CloudFront + Route53 + ACM
- Terraform 인프라 코드
- 다크 테마, 반응형, RTL 지원 (아랍어, 히브리어)

## 저장소 구조

```
content/           12개 언어 콘텐츠 (마크다운)
layouts/           Hugo 템플릿 (외부 테마 없음)
assets/css/        단일 CSS (다크 테마, RTL)
static/images/     WebP 이미지
deployments/       Terraform 인프라
hugo.toml          Hugo 설정
Makefile           빌드·배포 명령
```

## 빌드

```bash
hugo server -D          # 로컬 개발 (localhost:1313)
hugo --minify           # 프로덕션 빌드 → public/
```

## 라이선스

- 콘텐츠 (`content/`, `static/images/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 코드 (그 외 전부): [MIT](LICENSE)

## 저자

[박준우](https://parkjunwoo.com)
