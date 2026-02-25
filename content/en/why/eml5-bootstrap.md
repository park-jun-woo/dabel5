---
title: "Why the First Step Is Earth-Moon L5, Not Mercury"
date: 2026-02-24T12:00:01+09:00
lastmod: 2026-02-24T12:00:01+09:00
tags: ["dyson-swarm", "EML5", "bootstrap", "lagrange-point"]
image: "/images/eml5-bootstrap.webp"
imageCaption: "Lagrange points of the Earth-Moon system. Credit: NASA/WMAP Science Team. Public domain."
summary: "The first mirror of a Dyson swarm should be placed at Earth-Moon L5, not Mercury. With 1.3-second communication delay, direct lunar resources, and Earth resupply — EML5 is the optimal bootstrap site."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Where Do You Start a Dyson Swarm?

Dyson swarm discussions always start with the final form. Mercury disassembly, near-solar placement, multi-TW to PW output. That's the framework Isaac Arthur's series established, and most people take it for granted.

But before debating the finished K2 civilization, there's a far more important question: **where do you place the very first mirror?**

Humanity currently sits at K 0.73. Here's the math on where to take that first step.

---

## Why EML5 (Earth-Moon L5)

### 3-Phase Roadmap

| Phase | Location | Distance from Earth | Comm Delay | Role |
|-------|----------|-------------------|------------|------|
| **1. Bootstrap** | **EML5** | **~380,000 km** | **~1.3 s** | **First industrial base** |
| 2. Scale-up | SEL5 (Sun-Earth L5) | 150 million km | ~8 min 20 s | Large-scale Dyson swarm |
| 3. Full-scale | Mercury | Variable | Variable | K2+ planetary disassembly |

Most discussions start at Phase 2 or 3. **But there is no Phase 2 without Phase 1.**

### The Decisive Advantages of EML5

**1. Communication Delay of 1.3 Seconds — Effectively Real-Time**

Mercury has one-way delays of several to over ten minutes, plus solar conjunction blackout periods. EML5 is 1.3 seconds — close enough for remote control. **You can begin without fully autonomous AI.** This isn't a nice-to-have; it's decisive for bootstrap. Entrusting everything to autonomous manufacturing AI that has never been validated in space versus supervising in real-time from Earth — those are entirely different propositions.

**2. Direct Lunar Resource Supply**

| Resource | Source | Use | Transport Method |
|----------|--------|-----|-----------------|
| Aluminum (Al) | Regolith Al₂O₃ (~15%) | Mirror reflective coating | Mass driver |
| Titanium (Ti) | Ilmenite FeTiO₃ | Structural material (lightweight) | Delta-V ~2.5 km/s |
| Oxygen (O₂) | Reduction byproduct of the above | Life support | No chemical rocket needed |
| Silicates | Regolith | Radiation shielding | — |

Without the massive prerequisite of an asteroid mining fleet, **you can launch resources directly from the Moon via mass driver.** The delta-V from Moon to EML5 is ~2.5 km/s — achievable with chemical rockets, and zero propellant cost with an electromagnetic mass driver.

**3. Easy Resupply from Earth**

The delta-V from LEO to EML5 is far smaller than to deep space. Early equipment, electronics, and high-performance materials that can't yet be manufactured in space can be supplied from Earth. The bootstrap phase doesn't need to demand 100% self-sufficiency.

**4. Gravitational Stability**

EML5 is a Lagrange point of the Earth-Moon system. Station-keeping cost is near zero.

---

## What Happens at EML5

### First Goal: In-Situ Mirror Fabrication Capability

1. Deploy the first seed mirror + smelting equipment from Earth to EML5
2. Transport Al, Ti, and silicates from the Moon via mass driver
3. Use the seed mirror's concentrated solar thermal energy to vacuum-smelt lunar materials
4. Use the output to **fabricate a second mirror on-site** — the starting point of the self-replication loop

### Solar Environment

EML5 sits at the same 1 AU as Earth's orbit. Solar flux is 1,361 W/m². It can't match the 6.6x flux near Mercury (0.39 AU), but mirror lifespan and operating conditions are incomparably better.

### Validation Phase

EML5 also serves as a technology validation stage:
- Does vacuum smelting actually work?
- Does the self-replication loop's doubling period match calculations?
- Does mirror coating lifespan meet predictions?

All of this can be validated **under supervision from 1.3 seconds away.** Debugging with delays of minutes to tens of minutes in deep space is a completely different story.

---

## Why Start at EML5

| Approach | Prerequisites for First Mirror | Risk |
|----------|-------------------------------|------|
| Mercury disassembly | Mercury landing, mining, escape, orbital deployment | Extremely high |
| Direct deep space | Asteroid mining fleet, fully autonomous AI | High |
| **EML5** | **Lunar mass driver, real-time Earth supervision** | **Lowest** |

The key difference: **if EML5 fails, you can fix it.** At 1.3 seconds, a joystick still reaches.

---

## But EML5 Isn't Forever

EML5 isn't a silver bullet. It's optimal as a bootstrap site, but its limits are clear.

### 1. Earth's Shadow

EML5 orbits in the same plane as the Moon (inclination 5.14°), passing opposite the Earth every ~27.3 days. When near the ecliptic plane, it enters Earth's umbra and solar power is completely blocked.

```
Earth's umbra diameter at 384,400 km:
  r = R_earth - d × (R_sun - R_earth) / d_sun
  = 6,371 - 384,400 × 689,629 / 149,600,000
  = 6,371 - 1,772 = 4,599 km (radius)
  → Diameter ~9,200 km

Entry condition: ecliptic latitude < arctan(4,599 / 384,400) ≈ 0.69°
Lunar orbit inclination 5.14° → occurs only near ascending/descending nodes ±7.7° range
```

The geometry is identical to a lunar eclipse (offset by 60°, so it occurs at different times):

| Parameter | Value |
|-----------|-------|
| Frequency | 2–3 times per year |
| Max duration per event | ~2.5 hours (central umbra transit) |
| Including penumbra | ~4.3 hours |
| **Total annual downtime** | **3–12 hours** |
| **Annual uptime** | **99.86–99.97%** |

A few hours of thermal storage enables uninterrupted operation. Not fatal, but **the mere existence of a shadow is a limitation.**

### 2. Small Stable Region

Due to the Earth-Moon mass ratio (81:1), EML5's stable region spans only tens of thousands of km. Hundreds to thousands of modules fit, but **beyond that, it saturates.**

### 3. Lunar Resources Alone Aren't Enough

The Moon has no bulk Fe-Ni resources. Iron-nickel alloy — the primary structural material for mirror frames — can only be obtained in bulk from asteroids.

| Resource | Moon | Asteroid (1986 DA) |
|----------|------|-------------------|
| Al, Ti, O₂ | Abundant | None / trace |
| Fe-Ni alloy | **Nearly zero** | **90%+** |
| Silicates | Abundant | Slag byproduct |

Early mirrors can use Ti frames + Al coating, but **scaling beyond thousands of units is impossible without asteroid Fe-Ni.**

### 4. Solar Perturbation

Solar gravitational perturbation makes EML5 quasi-stable rather than perfectly stable. Long-term station-keeping is required.

### Constraint Summary

| Constraint | Severity |
|------------|----------|
| Earth's shadow (3–12 hrs/year) | Low — mitigated by thermal storage |
| Stable region (saturates at thousands of modules) | **Medium** |
| No Fe-Ni | **High** |
| Solar perturbation | Low |

---

## So, What's Next?

EML5 is the optimal first step for a Dyson swarm. Communication delay of 1.3 seconds, direct lunar resource supply, Earth resupply capability — no better conditions exist for bootstrap.

But the limits are equally clear:
- 3–12 hours/year of Earth shadow downtime
- Stable region of tens of thousands of km — saturates at thousands of modules
- **The Moon has no Fe-Ni** — the wall for scale-up

At EML5 you validate the self-replication loop and grow hundreds to thousands of modules. The technology works. **But you can't grow any larger here.**

So where is the next stage?
