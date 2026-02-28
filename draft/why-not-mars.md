# 왜 인간의 거주는 화성이 아니라 L5인가

---

## "다이슨 스웜이 있으면, 사람은 어디서 사나?"

기후를 제어하고, 소행성을 캐고, 거울이 거울을 만드는 설계를 보여줬다. 자연스럽게 따라오는 질문이 있다: **그래서 사람은 어디서 사는가?**

대부분의 사람은 "화성"이라고 답한다. 수십 년간 SF가 그려온 이미지. 스페이스X가 로켓을 만들고 있다. 화성은 인류의 두 번째 고향 — 이건 거의 상식처럼 굳어져 있다.

하지만 공학적으로 따져보면, 화성은 인류 거주지로서 **치명적인 결함**이 있다. 그리고 그 결함은 기술로 해결할 수 없다.

---

## 0.38G — 아무도 모르는 숫자

화성의 표면 중력은 0.38G. 지구의 38%. "중력이 있으니까 괜찮지 않나?"라고 생각하기 쉽지만, 문제는 **얼마나 있느냐**다.

인간의 뼈, 근육, 심혈관계, 내이(평형감각기관)는 1G에 최적화되어 진화했다. ISS에서 0G에 6개월 체류한 우주인은 골밀도 감소, 근위축, 시력 저하를 겪는다. 0G가 나쁘다는 건 안다.

**0.38G는?**

솔직한 답: **아무도 모른다.**

- NASA와 ESA의 우주의학 데이터는 0G(ISS)와 1G(지구) 두 점뿐이다
- 0.38G에서 포유류의 임신, 태아 골격 형성, 내이 발달, 심혈관 형성이 정상적으로 진행되는지 **단 한 번도 실험된 적이 없다**
- 0.38G에서 태어나 자란 아이의 뼈와 근육이 1G를 견딜 수 있는지 알 수 없다
- 견딜 수 없다면, 화성에서 태어난 인간은 **지구에 올 수 없다**

이건 기술 문제가 아니다. 화성의 질량을 바꿀 수는 없다. 0.38G는 화성이라는 행성의 **물리적 상수**다.

### 오닐 실린더: 원하는 중력을 고른다

회전하는 원통형 구조물 — 오닐 실린더(O'Neill cylinder). 회전 반경과 각속도를 조절하면 내부에 원심력으로 **정확히 원하는 중력**을 만들 수 있다.

| | 화성 | 오닐 실린더 |
|---|---|---|
| 중력 | 0.38G (고정) | **0.5~1.5G (선택 가능)** |
| 1G 보장 | 불가 | 회전 속도 조절로 보장 |
| 세대 간 건강 | **미지수** | 지구와 동일 조건 |
| 지구 귀환 가능성 | 불확실 | 보장 |

화성은 "중력이 있다"가 장점이 아니라 **"중력이 애매하다"**가 문제다. 오닐 실린더는 중력을 **설계 변수**로 만든다.

---

## 에너지: 다이슨 모듈 바로 옆

화성에 도시를 세우면 에너지를 어디서 구하는가?

| | 화성 | L5 (다이슨 모듈 옆) |
|---|---|---|
| 태양광 플럭스 | 589 W/m² (지구의 43%) | 1,361 W/m² (100%) |
| 가용 시간 | 낮만 (모래폭풍 시 수개월 차단) | **365일 24시간 무중단** |
| 에너지 인프라 | 자체 발전소를 **처음부터** 건설 | 다이슨 모듈에서 **직접 수급** |

L5에서 거주 모듈은 다이슨 모듈 클러스터의 일부다:

```
다이슨 모듈 (370 MW 전기)
    ├→ 전기 → 생명유지, 농업 조명, 생활 전력
    └→ 열 캐스케이드
         ├→ 100~200°C → 거주구 난방·온수 (공짜)
         └→ 30~60°C → 데이터센터 환경열
```

모듈 1기당 370 MW 전기, 3,000명 거주. **1인당 ~120 kW.** 지구 선진국 평균 소비 전력의 10배 이상. 거주구의 에너지는 다이슨 모듈의 일부 기능일 뿐, 별도 발전소가 필요 없다.

화성에서 같은 수준의 에너지를 공급하려면? 거대한 태양광 어레이를 먼지 폭풍 속에서 건설해야 한다. 그리고 밤이면 멈춘다.

---

## 산업: 공장이 이미 있다

화성에 도시를 세우려면 **공장을 먼저 세워야 한다.** 건설 자재, 생활용품, 전자부품, 의료기기 — 전부 지구에서 보내거나, 화성에서 처음부터 산업 기반을 구축해야 한다.

화성의 산업 환경:
- 대기: CO₂ 95%, 기압 지구의 0.6% → **우주복 없이 야외 활동 불가**
- 물: 극지 빙관에 존재하나 추출·정제 인프라 필요
- 원자재: 있지만, 중력우물 바닥에서 채굴 → 궤도로 올리는 비용 막대

L5의 산업 환경:
- 다이슨 모듈 클러스터 **자체가 산업단지**
- 제련 모듈 → 구조재, 파이프, 배터리
- 팹 모듈 → 전자부품, 센서, AI 칩
- 구조재 모듈 → 거주구 확장 부재
- 생필품(의복, 도구, 의료기기)을 **현지에서 제조 가능**

화성에 도시를 세우려면 공장을 먼저 지어야 한다. L5에는 **공장이 이미 돌아가고 있다.** 거주 모듈은 기존 생산 라인에 방 하나 추가하는 것에 가깝다.

---

## 통신: 화성의 고립

여기서부터는 기술적 불가능이 아니라 **삶의 질** 문제다. 하지만 문명의 거주지를 논하는 데 삶의 질을 빼놓을 수 없다.

| | 화성 | L5 (SEL5) |
|---|---|---|
| 지구까지 통신 지연 | **4분~24분** (편도, 위치에 따라) | **~8분 20초** (편도, 일정) |
| 통신 두절 | 합(conjunction) 시 **~2주간** 완전 두절 | **없음** |
| 실시간 대화 | 불가 (왕복 8~48분) | 불가 (왕복 ~17분) |

둘 다 실시간 통화는 안 된다. 하지만 화성은 2주간 지구와 **완전히** 단절되는 기간이 있다. L5는 없다.

그리고 결정적 차이: L5의 거주 허브는 SEL5가 아니라 **EML4/5**에 둘 수 있다.

```
EML4/5 거주 허브
  ├→ 지구까지 통신: 왕복 ~2.6초 (실시간 화상통화 가능!)
  ├→ SEL5 산업단지와 교대 근무 셔틀
  └→ 달까지 2~3일 (물류·관광)
```

EML4/5에서 지구까지 왕복 2.6초면 **전화가 된다.** 화성과는 비교 자체가 안 된다.

---

## 귀환: 화성은 사실상 편도

화성에서 지구로 돌아오려면:

- 화성 표면 → 화성 궤도: 델타-v ~3.8 km/s
- 화성 궤도 → 지구 궤도: 델타-v ~2 km/s 이상
- **총 Δv ~5.7 km/s + 비행 시간 9개월**
- 발사 창: 26개월에 한 번

경제적으로, 심리적으로, 화성 이주는 **편도**다. "언제든 돌아갈 수 있다"는 말은 이론적으로만 맞고, 현실적으로는 거의 불가능하다.

L5 → 지구:
- EML 거주 허브에서 지구 궤도까지 Δv ~1 km/s 미만
- 물류 인프라(예인선, 셔틀)가 이미 존재
- **정기 셔틀 운용 가능**

화성에 간다는 건 "이민"이다. L5에 간다는 건 "출장" 또는 "이사"다. 돌아올 수 있느냐 없느냐는 거주지 선택에서 근본적인 차이.

---

## 테라포밍이라는 환상

"화성을 테라포밍하면 되지 않나?"

테라포밍 현실:

- **시간**: 수백~수천 년. 낙관적 추정치도 최소 수백 년
- **대기 유지**: 화성에는 지구형 자기장이 없다. 태양풍이 대기를 지속적으로 벗겨낸다. 대기를 만들어도 **유지할 방법이 불확실**
- **중력**: 대기를 만들어도 0.38G는 바뀌지 않는다. 대기가 지구만큼 두꺼워져도 중력 문제는 그대로

오닐 실린더는:
- 건설 **즉시** 1 atm, 1G
- 내부에 산, 강, 하늘을 만들 수 있다 (실린더 내부 풍경 설계)
- 원하는 생태계를 즉시 구현
- 테라포밍을 기다릴 필요가 없다

테라포밍이 완성되기를 수백 년 기다리는 동안, 오닐 실린더에서는 **이미 사람이 살고 있다.**

---

## "그래도 행성에 살고 싶다"

공학적 논증만으로는 설득이 안 되는 부분이 있다. 발밑에 행성이 있다는 심리적 안정감. 창밖으로 보이는 하늘과 수평선. 이건 인정한다.

하지만 몇 가지 짚자:

**"화성은 자원이 풍부하다"** — 자원은 소행성이 접근성이 더 좋다. 화성은 중력우물 바닥이라, 채굴한 자원을 궤도로 올리는 데 막대한 에너지가 든다. 소행성은 중력이 거의 없으니 가져다 쓰기만 하면 된다.

**"오닐 실린더는 너무 작다"** — 모듈 수를 늘리면 된다. 모듈 10,000기면 인구 3,000만 명. 자기복제는 지수적으로 확장되니까, 화성 테라포밍이 완료되기 한참 전에 L5 인구가 화성을 넘는다.

**"심리적으로 행성이 필요하다"** — 오닐 실린더 내부에 산과 강과 구름을 만들 수 있다. 반경 수 km의 실린더라면 하늘도 있다. 창밖 풍경이 화성의 붉은 사막인 것과 오닐 실린더의 설계된 자연인 것 — 취향 문제일 수는 있지만, 공학적 우열은 명확하다.

**"스페이스X가 이미 투자하고 있다"** — 화성 탐사와 화성 거주는 다른 문제다. 탐사 기지는 남극 세종기지와 같다. 거기서 문명을 세우자는 건 아니다. 탐사 기지 ≠ 문명의 거주지.

---

## 한 줄 요약

화성의 0.38G에서는 아이가 정상적으로 자랄 수 있을지 아무도 모른다. 오닐 실린더에서는 1G를 보장한다. 에너지는 다이슨 모듈에서 직접 받고, 공장은 이미 돌아가고 있고, 지구에 전화도 된다. 화성은 로맨틱하고, L5는 공학적이다.

---

## Discussion

Mars is everyone's default answer for "where does humanity live next?" But it has a flaw that no technology can fix.

Mars surface gravity is 0.38G. We have zero data on whether mammalian pregnancy, fetal bone formation, inner ear development, or cardiovascular growth proceed normally at 0.38G. NASA's medical data covers 0G (ISS) and 1G (Earth). Nothing in between. A child born on Mars might never be able to return to Earth.

O'Neill cylinders solve this by making gravity a design variable — spin to any G you want. 1G guaranteed.

But it goes further:
- **Energy:** An O'Neill habitat at L5 sits next to Dyson modules producing 370 MW each. Free heat from the thermal cascade. Mars gets 43% of Earth's solar flux, interrupted by months-long dust storms.
- **Industry:** At L5, the smelting and fabrication modules are already running. Structural materials, electronics, batteries — all produced on-site. Mars requires building industrial infrastructure from scratch, in 0.6% atmospheric pressure.
- **Communication:** From an EML4/5 habitat hub, Earth is 2.6 seconds round-trip — you can make a phone call. Mars is 8–48 minutes round-trip, with 2-week blackouts during conjunction.
- **Return:** Mars → Earth requires Δv ~5.7 km/s and 9 months. It's effectively one-way. EML → Earth is a shuttle ride.
- **Terraforming:** Even optimistic estimates say centuries, and Mars lacks a magnetosphere to retain an atmosphere long-term. An O'Neill cylinder provides 1 atm and 1G from day one.

Mars exploration is valuable — like Antarctic research stations. But a research station isn't a civilization's home. When you're choosing where billions of humans will live for generations, the engineering points to L5.

What's your take — is the 0.38G uncertainty a dealbreaker for Mars colonization, or am I overweighting it?
