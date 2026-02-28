# 왜 리튬전지가 아니라 철-니켈 전지인가

---

## "에너지 저장은 당연히 리튬이온이지?"

다이슨 모듈은 거울로 태양열을 모아 터빈을 돌린다. 24시간 365일 태양이 비치면 좋겠지만, 현실은 아니다.

- **식(eclipse):** EML5 거점은 연 2~3회, 총 3~12시간 지구·달 그림자에 들어간다
- **부하 변동:** 터빈은 부하 급변에 느리게 반응한다. 순간 수요 변동에 ESS 없으면 전압이 흔들린다
- **비상 정지:** 거울 유지보수, 터빈 고장 시 핵심 시스템 — 생명유지, AI, 통신 — 은 멈출 수 없다
- **기동 전력:** 예인선 도킹·회피 기동 시 순간 대전력이 필요하다

배터리 없이는 다이슨 모듈이 돌아가지 않는다. 그럼 어떤 배터리?

지구에서라면 답은 자명하다. 리튬이온. 에너지 밀도, 충방전 효율, 경량화 — 모든 지표에서 최고. 하지만 이전 글에서 터빈이 태양광 패널을 이긴 것과 같은 이유로, **우주에서는 기준이 다르다.**

리튬이온은 10년마다 교체해야 하는데, 가장 가까운 리튬 광산이 지구에 있다. 소행성에서 철과 니켈은 발에 채인다.

---

## 지구 기준 vs 우주 기준

| 항목 | 철-니켈 (에디슨) | 리튬이온 | 우주에서 뭐가 중요한가 |
|------|----------------|---------|---------------------|
| 체적 에너지 밀도 | 30~60 Wh/L | 250~700 Wh/L | 1 km² 스케일에서 부피는 무의미 |
| 중량 에너지 밀도 | 30~50 Wh/kg | 150~270 Wh/kg | 이동 불필요한 구조물 → 무관 |
| 수명 | **30~50년** | 5~15년 | 교체 비용이 우주에서는 **천문학적** |
| 과충전 내성 | **극히 강함** | 약함 (열폭주·화재) | 진공에서 화재 = 모듈 전손 |
| 과방전 내성 | **강함** | 비가역 손상 | eclipse 시 완전 방전 가능성 |
| 소재 현지 조달 | **가능** (Fe, Ni, KOH) | **불가** (Li, Co, 유기 전해질) | 자기복제 루프의 존폐 |
| 전해질 | 수산화칼륨 수용액 (물 기반) | 유기 용매 (인화성) | 방사선 안정성, 화재 안전 |
| 자가 방전 | 높음 (~1%/일) | 낮음 (~0.1%/일) | 상시 충전 환경에서 무의미 |

**지구에서 중요한 것: 가볍고, 작고, 에너지 밀도 높을 것.**
**우주에서 중요한 것: 현지에서 만들 수 있고, 안 죽고, 오래 갈 것.**

기준이 다르면 답이 달라진다.

---

## 소재 — 소행성에 리튬은 없다

리튬이온 배터리를 만들려면:

| 소재 | 용도 | 소행성 존재 여부 |
|------|------|----------------|
| 리튬 (Li) | 양극 활물질 | **없음** — 빅뱅 핵합성 원소, 암석형 소행성에 극미량 |
| 코발트 (Co) | 양극 안정화 | 극미량 — 경제적 추출 불가 |
| 흑연 (C) | 음극 | 탄소질 소행성에 존재하나 결정질 흑연 아님 |
| 유기 전해질 | 이온 전도 | **합성 필요** — 에틸렌 카보네이트 등 복잡한 유기화학 |
| 분리막 (PE/PP) | 단락 방지 | **합성 필요** — 고분자 정밀 제조 |

리튬이 없다. 이것만으로 게임 오버. 지구에서 계속 보급받아야 한다면 **자기복제가 아니라 보급선 의존**이다.

"나트륨이온은?" Na는 소행성에 존재한다. 하지만 30~50년 수명이 검증되지 않았고, 바톨라이저 기능이 없으며, 유기 전해질이 필요하다. 우주 방사선이 유기 전해질을 열화시키는 문제는 나트륨이온에서도 똑같다.

"고체 배터리가 곧 나오지 않나?" 소행성에서 만들 수 없으면 아무리 좋아도 의미 없다. 핵심은 에너지 밀도가 아니라 **현지 제조 가능성**이다.

철-니켈 배터리를 만들려면:

| 소재 | 용도 | 출처 |
|------|------|------|
| 철 (Fe) | 음극 | 1986 DA 주성분 — **발에 채인다** |
| 니켈 (Ni) | 양극 | 1986 DA 주성분 — **발에 채인다** |
| 수산화칼륨 (KOH) | 전해질 | K는 소행성 규산염에 포함, 물은 탄소질 소행성에서 추출 |
| 강판 | 케이싱 | Fe-Ni 합금 가공 |

**배터리의 모든 구성 요소가 제련 공정의 부산물이다.** 거울 프레임을 만들면서 배터리도 만들 수 있다. 추가 원료 수입 제로.

---

## 수명 — 교체 비용이 전부를 결정한다

지구에서 리튬이온의 10~15년 수명은 충분하다. 교체 비용은 배터리 가격뿐.

우주에서 교체 비용은:
1. 새 배터리 제조 (만들 수 있다면)
2. 수송 (만들 수 없으면 지구에서 — **kg당 수천 달러**)
3. EVA 또는 로봇 교체 작업
4. 교체 중 시스템 다운타임

**철-니켈 배터리 수명: 30~50년.** 에디슨이 1901년에 만든 철-니켈 전지가 **아직 작동하는 사례**가 있다. 전해질(KOH 수용액)만 10~15년에 한 번 보충하면 전극은 반영구적.

모듈 설계 수명 내내 **교체 제로**가 가능한 유일한 배터리 화학.

---

## 안전 — 진공에서 화재는 곧 죽음

리튬이온 배터리의 유기 전해질은 인화성이다. 과충전, 물리적 손상, 내부 단락 시:

```
내부 온도 상승 → 분리막 수축 → 단락 확대 → 전해질 분해
→ 가연성 가스 방출 → 발화 → 인접 셀 연쇄 열폭주
```

지구: 소방차가 온다.
우주: **진공에서 소방차는 없다.** 밀폐 모듈 내 화재 = 생명유지 손실 + 유독 가스 충만 + 구조 불가.

ISS에서도 리튬이온 화재는 가장 두려운 시나리오 중 하나다. 수천 기 다이슨 모듈에 리튬이온을 탑재하면 **통계적으로 화재는 확정적**이다.

철-니켈의 본질적 안전성:

- 전해질: 수산화칼륨 **수용액** — 물 기반. 불에 타지 않는다
- 과충전 시: 물이 전기분해되어 H₂ + O₂ 발생 — 열폭주가 아니다
- 과방전 시: 전극 비가역 손상 없음 — 재충전으로 복구
- 물리적 손상 시: KOH 누출 — 부식성이지만 **폭발·화재 없음**

**"불이 안 나는 배터리"는 우주에서 사치가 아니라 필수.**

---

## 바톨라이저 — 배터리인데 수전해도 한다

여기서 철-니켈이 단순한 "차선책"을 넘어 **독보적 이점**을 갖는다.

### 원리

델프트 공대(TU Delft)가 개발한 바톨라이저(Battolyser) 개념. 철-니켈 배터리의 과충전 내성을 적극 활용한다:

```
[충전 중]     전기 에너지 → Fe/Ni 전극에 화학 에너지 저장
[완충 후]     추가 전류 → KOH 수용액의 물이 전기분해
              음극: 2H₂O + 2e⁻ → H₂↑ + 2OH⁻
              양극: 2OH⁻ → ½O₂↑ + H₂O + 2e⁻
```

**하나의 장치가 배터리 + 수전해조를 겸한다.** 별도 전해 설비가 필요 없다. 질량·부피·복잡도 절감.

리튬이온에서는 과충전 = 화재. 철-니켈에서는 과충전 = **수소 생산**.

### 다이슨 모듈에서의 운용 사이클

```
[평상시] 터빈 370 MW 가동
  ├→ 부하 소비 (~320 MW)
  └→ 과잉 전력 (~50 MW) → 바톨라이저 모드
       └→ H₂ ~620 kg/h + O₂ ~4,960 kg/h 축적

[식(eclipse)] 3~12시간/년
  ├→ 배터리 방전 (ESS 모드)
  └→ 축적 H₂ → 연료전지 발전 (병행)
       → 배터리 단독 대비 가용 에너지 2배+

[비상 정지]
  └→ H₂/O₂ 이중 저장 → 생명유지 연장
```

### 에너지 저장을 넘어서

바톨라이저가 만드는 H₂와 O₂는 단순 에너지 저장을 넘어 **모듈 전체 물질 순환**에 통합된다:

| 산출물 | 활용처 | 비고 |
|--------|--------|------|
| H₂ | NTP 예인선 추진제 보충 | 핵열추진의 작동 유체 |
| H₂ | 제련 공정 환원제 | 금속 산화물 → 순금속 (FeO + H₂ → Fe + H₂O) |
| H₂ | 연료전지 비상 발전 | eclipse/정비 시 백업 전력 |
| H₂ | 하버-보슈 → NH₃ → 비료 | 거주 모듈 농업 |
| O₂ | 생명유지 (호흡) | 거주 모듈 필수 |
| O₂ | 산화제 (용접·의료) | 현지 제조 공정 |

에너지를 저장하면서 동시에 추진제, 환원제, 호흡용 산소를 만드는 배터리. 리튬이온은 전기만 저장한다.

---

## "에너지 밀도 1/10이면 너무 크지 않나?"

맞다. 같은 에너지를 저장하려면 철-니켈은 리튬이온의 **5~10배 부피**가 필요하다.

하지만:

```
다이슨 모듈 스케일:
  거울: 1 km × 1 km = 1,000,000 m²
  구조물: 거울 뒤로 수 km 연장
  총 체적: 수백만 m³

필요 ESS 용량 (12시간 × 370 MW):
  4,440 MWh = 4,440,000 kWh

철-니켈 (40 Wh/L 기준):
  111,000 m³ = 111 m × 111 m × 9 m

→ 전체 구조물 대비 <1%
```

1 km² 거울 뒤의 수백만 m³ 구조물에서 111,000 m³는 **구석 한 칸**이다. 게다가 철-니켈의 무거운 질량은 **회전 구조물의 균형추(counterweight)**로 활용 가능하다. 단점이 장점으로 뒤집힌다.

자가 방전이 하루 ~1%로 높다는 것도 지상에서나 문제다. 터빈이 24시간 365일 가동 중이므로 배터리는 항상 충전 상태. 자가 방전은 **무의미**하다.

"그냥 터빈 출력을 늘리면 ESS가 필요 없지 않나?" 식(eclipse)과 비상 정지는 터빈이 **아예 멈추는** 상황이다. 발전과 저장은 별개 문제다.

---

## 우주 환경 적응 설계

지상 철-니켈 배터리를 그대로 우주에 가져갈 수는 없다. 세 가지 적응이 필요하다.

### 1. 전해질 증발 방지

KOH 수용액은 진공 노출 시 수분이 증발한다. **밀폐 셀 구조** 필수. 다행히 배터리 셀은 원래 밀폐 설계다. 우주용은 밀봉 수준만 강화하면 된다.

### 2. 무중력 가스 분리

바톨라이저 모드에서 H₂/O₂ 기포가 전극 표면에 달라붙는 문제. 지구에서는 부력이 기포를 떼어내지만, 무중력에서는 안 된다.

**해결:** 전극 표면 소수성 코팅 + 모듈 자체 회전에 의한 원심력으로 가스 분리. 원심력 가속도 ~0.01G만 있어도 기포 분리에 충분하다.

### 3. 방사선 내성

KOH 수용액은 유기 전해질과 달리 **방사선에 극히 안정**하다. 유기 전해질은 방사선이 분자 사슬을 끊어 열화시킨다. 수용액은 방사선에 의한 물 분해가 소량 발생하지만, 재결합으로 자연 복원된다. 방사선 환경에서 철-니켈이 리튬이온보다 **본질적으로 유리**하다.

---

## 한 줄 요약

리튬이온은 지구 최고의 배터리다. 하지만 소행성에 리튬은 없고, 우주에서 10년마다 교체할 수도 없고, 진공에서 화재를 끌 수도 없다. 철-니켈 배터리는 소행성 제련 부산물로 만들 수 있고, 30~50년 교체 없이 버티며, 불이 나지 않고, 완충 후에는 수전해 장치로 변신해서 추진제와 호흡용 산소를 만든다. 에너지 밀도가 1/10이라는 건 1 km² 스케일에서 의미 없다.

---

## Discussion

Everyone assumes a Dyson swarm would use lithium-ion batteries. Best energy density, best efficiency, industry standard.

But lithium doesn't exist on asteroids. And in space, you can't order replacements from Earth every 10 years.

Iron-nickel (Edison) batteries flip every disadvantage:

- **Materials:** Fe and Ni are the primary output of asteroid smelting. The battery is literally a byproduct of making everything else.
- **Lifespan:** 30–50 years vs. 10–15 for Li-ion. Some Edison cells from the early 1900s still work today.
- **Safety:** Aqueous KOH electrolyte. Zero fire risk. Li-ion thermal runaway inside a sealed module in vacuum is catastrophic — and with thousands of modules, statistically inevitable.
- **Battolyser mode:** This is where iron-nickel goes from "acceptable alternative" to "uniquely superior." When fully charged, excess current electrolyzes the water in the KOH electrolyte → H₂ + O₂. One device = battery + electrolyzer, no separate equipment. The hydrogen feeds fuel cells during eclipses, serves as rocket propellant for tug vehicles, reduces metal oxides in the smelting process, and synthesizes ammonia for agriculture. The oxygen keeps people breathing. Li-ion stores electricity. Iron-nickel stores electricity AND produces the gases that keep the entire module running.

"But the energy density is 1/10th of Li-ion!" Yes. And the battery bank fits in less than 1% of the module structure. When your mirror is 1 km² and the structure behind it stretches for kilometers, volume is not a constraint. The heavy mass even serves as a counterweight for rotating habitats.

This is the same pattern as turbines vs. solar panels: the "inferior" Earth technology turns out to be the only viable option when "can you make it from asteroid metal?" is the deciding question. Except this time, the inferior technology has a trick Li-ion can't match — it makes hydrogen and oxygen as a side effect of being fully charged.

What's your take on the battolyser concept for space applications? And are there other battery chemistries that could work with asteroid-sourced materials?
