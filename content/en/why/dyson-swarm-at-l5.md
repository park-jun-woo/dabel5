---
title: "Why L5, Not Near the Sun"
date: 2026-02-24T12:00:05+09:00
lastmod: 2026-02-24T12:00:05+09:00
tags: ["dyson-swarm", "SEL5", "self-replication", "scaling"]
image: "/images/post005.webp"
summary: "The standard Dyson swarm scenario assumes dismantling Mercury near the Sun. But what if you use asteroid resources and build at Sun-Earth L5 instead? Here are the calculations."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Questioning the Conventional Wisdom

The standard Dyson swarm scenario everyone pictures: dismantle Mercury and place panels/mirrors near the Sun. This is the framework established by the Isaac Arthur series, and most people accept it as a given.

But I ran the numbers on a different approach — what if you use asteroid resources and build at Sun–Earth L5?

---

## Why L5

### Solar Flux
- L5 (1 AU): ~1,361 W/m² — same as Earth orbit
- Mercury orbit (0.39 AU): ~8,942 W/m² — about 6.6x stronger
- "Isn't Mercury better?" — Yes, per unit area. But that's not the whole story

### Hidden Advantages of L5
1. **Gravitational stability** — Station-keeping cost is nearly zero. Near Mercury, the solar gravity gradient is steep, requiring continuous station-keeping
2. **24/7/365 uninterrupted sunlight** — Earth's shadow cannot reach it (150 million km away). No eclipses
3. **Stable region spanning millions of km** — Hundreds of thousands of modules can be deployed without mutual interference
4. **Fixed distance from Earth** — Simplifies logistics planning. Communication delay is ~8 min 20 sec one-way (not real-time, but solved by autonomous AI operations)
5. **Habitable** — Near Mercury, the thermal environment is extreme. L5 makes human habitat design far more realistic

---

## Resources: Mercury Disassembly vs Asteroids

### Hidden Costs of the Mercury Approach
- Mercury escape velocity: 4.25 km/s — a significant gravity well
- Mercury surface temperature: 430°C daytime — extreme thermal management for mining equipment
- Mercury to solar orbit deployment: additional delta-V required
- **The biggest issue: Mercury is a planet** — Large-scale mining at 0.38g surface gravity is essentially a variant of terrestrial mining

### Asteroid (1986 DA) Approach
- M-type metallic asteroid: **90%+ Fe-Ni alloy** — nearly pure metal
- Estimated mass: ~2.3 km diameter, M-type asteroid bulk density → **20+ billion tonnes**
- Microgravity — minimal mining energy, escape velocity is negligible
- Even byproducts are fully utilized: silicate slag becomes radiation shielding + silicon ingot feedstock

| Comparison | Mercury Disassembly | Asteroid (1986 DA) |
|------|----------|----------------|
| Gravity well escape | 4.25 km/s | ~a few m/s |
| Surface temperature | 430°C (daytime) | Cryogenic (easy to manage) |
| Resource composition | Mostly silicates, metal separation required | 90%+ Fe-Ni alloy (nearly ready to use) |
| Mining equipment complexity | High (gravity, heat) | Low (microgravity) |
| Total resource volume | Overwhelming (entire planet) | Sufficient for K1 bootstrap |

Mercury wins overwhelmingly in total resource volume, but **for the first stage (bootstrap phase), asteroids are far more practical.**

---

## The Key: Self-Replication Loop

The real differentiator of this design is not simply "where to mine and where to place."

**Asteroid ore → vacuum smelting with Dyson mirror solar heat at L5 → output builds new mirrors → collecting area grows → smelting rate increases → exponential growth**

1. Seed mirrors concentrate sunlight
2. Concentrated heat raises ore to ~1,500°C → Fe-Ni alloy output
3. Alloy fabricates new mirror frames
4. New mirrors added → collecting area grows → **exponential growth begins**

### Scaling

| Scale | Power | vs Earth | Population | AI Compute |
|------|------|----------|------|---------|
| 1 module | 370 MW | 1 small nuclear plant | 2,500 | 32 EF |
| 10 modules | 3.7 GW | 3 large nuclear plants | 25,000 | 320 EF |
| 1,000 modules | 370 GW | 2% of Earth | 2.5M | 32 ZF |
| 10,000 modules | 3.7 TW | 20% of Earth | 25M | 320 ZF |
| 200,000 modules | 74 TW | **4x Earth** | 500M | 6,400 ZF |

The doubling period depends on per-module mass budget and process maturity. Assuming a 2–5 year range, reaching K1.0 scale from 1 module takes 50–125 years.

---

## This Is Not Saying Mercury Is Wrong

Let's be honest about one thing. Humanity is currently at K 0.73. Even K1.0 (10^16 W) is a ~550x gap from where we are now. **Before talking about K2, we need to reach K1 first.**

The scale required for K1.0 — ~27 million modules, ~10 PW — is fully coverable with asteroid resources. No need to touch Mercury. Mercury disassembly only becomes necessary for total resource volume at K1.5+ (10^21 W) and beyond.

Mercury is the highway to K2. But what we need right now is the on-ramp to that highway. **You don't need a highway to build a highway.**

In the bootstrap phase:
- Asteroids have lower access costs
- L5 has lower operational costs
- The self-replication loop starts sooner

What if reaching K1 at L5 first, then using that industrial capacity to dismantle Mercury, is actually the faster path?
