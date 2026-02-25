---
title: "Why You Can't Pipe Heat"
date: 2026-02-24T12:00:08+09:00
lastmod: 2026-02-24T12:00:08+09:00
tags: ["thermal-management", "radiator", "heat-cascade"]
summary: "No fluid survives 1,600°C in a closed loop. Each facility gets its own mirror, dumps waste heat at the highest possible temperature, and only sub-100°C leftovers reach the habitat."
image: "/images/post008.webp"
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Homework from the Previous Post

The previous post argued that turbines beat PV for self-replication. Efficiency 30 %, electrical output 370 MW, the remaining 855 MW is heat.

And it said this:

> "The same 70 % passes sequentially through the smelter, factory, habitat, and data center — all of it gets used."

Conceptually correct. Turbine waste heat is far more useful than PV's 60 °C low-grade reject heat. **But "sequential pass-through" is not a real design.** This post traces the actual heat flow.

---

## First, a Correction: Why "Sequential Pass-Through" Doesn't Work

### Problem 1 — Temperature of turbine waste heat

Thermodynamics of the turbine (Brayton cycle):
- Hot side: ~1,200 °C (working fluid heated by concentrated sunlight)
- Cold side: ~227 °C (heat is rejected here)
- 30 % efficiency → 370 MW electricity, **855 MW rejected at ~227 °C**

Key point: **All turbine waste heat exits at ~227 °C.** Smelting requires 1,600 °C. You cannot run a 1,600 °C process with 227 °C heat — second law of thermodynamics. Heat flows only from hot to cold.

The "800–1,000 °C → smelting" arrow in the previous diagram was not turbine waste heat. The smelter's heat comes **directly from the mirror**.

### Problem 2 — No medium can carry 1,000 °C

Even if 1,600 °C heat existed somewhere, could you pipe it to another facility?

| Heat-transfer medium | Max operating temp | Limit |
|---|---|---|
| Pressurized water | ~340 °C | Critical point |
| Molten salt | ~565 °C | Decomposition |
| Liquid sodium | ~800 °C | Vapor pressure |
| High-pressure helium | ~950 °C | Piping material limit |
| **Above 1,000 °C** | **N/A** | **No medium exists** |

No fluid can carry 1,600 °C heat. The only way to deliver energy at this temperature is **light.** Direct irradiation by mirrors.

### Problem 3 — Distance between modules

In a specialized cluster, smelting modules and data-center modules are **50–100 km apart.** This is deliberate separation for vibration, contamination, and thermal isolation. Heat piping over this distance is impractical.

**Conclusion: Piping turbine waste heat to high-temperature processes is physically impossible.**

---

## The Real Design: Each Facility Gets Its Own Mirror

The true principles of heat flow:

1. **Input heat is delivered directly from each module's own mirror** — transmitted as light, no medium needed
2. **Cascading works only inside each module** — process waste heat is reused at progressively lower temperatures
3. **No heat transfer between modules** — distance and medium limitations
4. **Only sub-100 °C waste heat is supplied to the habitat** — piping is feasible, and the temperature matches habitat demand

### Mirror Allocation (10-module cluster)

| Module type | Qty | Mirror split (heat : power) | High-temp source |
|---|---|---|---|
| Smelting module | 3 | 90 : 10 | Mirror → direct 1,600 °C |
| Ingot module | 1 | 70 : 30 | Mirror → direct 1,400 °C |
| Structural module | 2 | 60 : 40 | Mirror → direct 800–1,200 °C |
| Fab module | 1 | 20 : 80 | Mirror → direct 900 °C |
| Data center | 2 | 5 : 95 | Mirror → turbine → electricity |
| Habitat / logistics | 1 | 30 : 70 | Mirror → turbine → electricity |

**Above 1,000 °C, light delivers the heat directly.** Turbines run only in modules that primarily need electricity (data centers, habitats).

---

## Radiator Physics: The T⁴ Law

The only way to dump heat in space is **infrared radiation.** No convection, no conduction.

Stefan-Boltzmann law:

**Radiated power = ε × σ × A × T⁴**

(ε: emissivity, σ: Stefan-Boltzmann constant, A: area, T: absolute temperature)

The key is **T⁴**. Double the temperature, 16× the radiated power. Conversely, the area needed for the same heat load shrinks to 1/16.

| Radiator temp | Area per MW | Analogy |
|---|---|---|
| 800 °C (1,073 K) | **8 m²** | One parking space |
| 400 °C (673 K) | **50 m²** | One apartment |
| 227 °C (500 K) | **166 m²** | A tennis court |
| 100 °C (373 K) | **535 m²** | Three basketball courts |
| 60 °C (333 K) | **844 m²** | 1/8 of a soccer field |

(Double-sided radiation, emissivity ε = 0.85, uncoated Fe-Ni sheet)

**Lesson: Heat that takes 8 m² to reject at 800 °C needs 844 m² at 60 °C. Over 100× more.**

Therefore the core principle of thermal management: **"Dump unusable heat at the highest possible temperature, immediately."**

### Radiator Material

Radiators sit inside the self-replication loop:
- **Material:** Asteroid-sourced Fe-Ni thin sheet
- **Surface:** No aluminum coating (opposite of a mirror) — uncoated Fe-Ni has high infrared emissivity, ideal for radiation
- **Fabrication:** Same sheet-metal line as the mirror frames. Only the coating step is skipped
- **Extra resources:** Zero. Same material, same process, different product

---

## Heat Flow by Facility

### Smelting Module — Heat Is the Star (90 % heat, 10 % power)

The smelting module receives 90 % of its mirror energy as direct heat. A small turbine (10 %) generates electricity for motors and robots.

```
☀️ Dedicated mirror (90 % → direct irradiation, 10 % → small turbine)
 │
 ▼
Smelting furnace (1,600 °C) ← Heated directly by mirror light, no medium
 │
 │ Waste heat ~800 °C ← From here, a medium (He / liquid metal) can carry it
 ├→ Alloy heat-treatment, annealing (uses 800 °C)
 ├→ Surplus → ★ Radiator A (800 °C) — 8 m²/MW, compact
 │
 │ Waste heat ~400 °C
 ├→ Preheating, auxiliary heating (uses 400 °C)
 ├→ Surplus → ★ Radiator B (400 °C) — 50 m²/MW, medium
 │
 │ Waste heat ~200 °C
 ├→ ★ Radiator C (200 °C) — most heat disposed here
 │
 │ Residual < 100 °C
 └→ Can be piped to the habitat

Small-turbine waste heat (~227 °C) → ★ Radiator D
```

The smelting module uses heat top-down, **radiating the surplus at each stage.** High-temperature radiators are small, so the penalty is low. Only the sub-100 °C residual is sent to the habitat.

### Data-Center Module — Electricity Is the Star (5 % heat, 95 % power)

The data center is the hardest module to cool. 95 % of its mirror energy passes through turbine → electricity → chips → heat, all emerging at ~60 °C.

```
☀️ Dedicated mirror (95 % → large turbine, 5 % → auxiliary heat)
 │
 ▼
Large turbine → ~370 MW-class electricity
 │
 │ Turbine waste heat ~227 °C (~855 MW)
 └→ ★ Radiator A (227 °C) — 166 m²/MW
     Most turbine waste heat disposed here

Chip operation → all electricity becomes heat
 │
 │ Chip waste heat ~60 °C
 │  Direct radiation at 60 °C: 844 m²/MW → 111 MW needs ~94,000 m²
 │
 ├→ [Heat pump] 60 °C → 200 °C (COP ~3, power ~37 MW)
 │   └→ ★ Radiator B (200 °C) — area reduced to ~1/4
 │
 └→ Residual < 100 °C → can be supplied to the habitat
```

**The heat pump is a key technology.** Lifting 60 °C heat to 200 °C slashes radiator area. The heat-pump power (~37 MW) comes from the turbine's own output. Both the turbine and the heat pump can be built on-site from Fe-Ni + Ti.

### Structural Module (60 % heat, 40 % power)

```
☀️ Dedicated mirror (60 % → direct heating, 40 % → turbine)
 │
 ▼
Welding / heat-treatment (800–1,200 °C) ← Direct mirror heating
 │ Waste heat ~400 °C
 ├→ Forming / bending preheat (uses 400 °C)
 ├→ Surplus → ★ Radiator (400 °C)
 │ Waste heat ~200 °C
 ├→ ★ Radiator (200 °C)
 │ Residual < 100 °C
 └→ Can be supplied to the habitat

Turbine (40 %) → electricity (robots, CNC, welders)
 └→ Turbine waste heat → ★ Radiator (227 °C)
```

### Habitat / Logistics Module — Consumer of Sub-100 °C Waste Heat

The habitat is the final heat sink. Its own turbine produces electricity for life support, lighting, and agriculture, while **receiving sub-100 °C waste heat from nearby modules.**

```
☀️ Dedicated mirror (30 % → heat, 70 % → turbine)
 │
 ├→ Turbine → electricity (life support, lighting, agricultural LEDs)
 │   Waste heat (~227 °C) → ★ Radiator
 │
 └→ Heat → hot water, supplemental heating
     └→ Residual → ★ Radiator

Sub-100 °C waste heat from nearby modules (smelting, structural)
 │
 └→ Habitat heating, hot water, agricultural soil warming
     └→ Residual → radiated from habitat outer hull (the structure itself acts as a radiator)
```

Habitat heat demand (heating, hot water) is modest compared to industrial waste-heat volumes. The sub-100 °C residual from nearby modules is more than enough. **The habitat receives free heating — industrial modules do not generate heat for the habitat's sake.**

---

## Distributed Radiation: The Big Picture

Summary of cluster-wide heat flow:

```
☀️ Sunlight → Mirrors → Distributed directly to each module
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
[Smelting]     [Structural]    [Data center]
 Mirror→1,600°C Mirror→1,200°C  Mirror→Turbine→Elec.
    │               │               │
    ▼               ▼               ▼
 ★Rad.(800°C)   ★Rad.(400°C)   ★Rad.(227°C) ← turbine waste
 ★Rad.(400°C)   ★Rad.(200°C)   ★Rad.(200°C) ← after heat pump
 ★Rad.(200°C)       │               │
    │               ▼               ▼
    └──── <100°C ──→ [Habitat] ←── <100°C
                      Heating & hot water
                         │
                    ★Rad.(hull, ~30°C)
```

**Not "sequential pass-through" but "parallel distribution + individual radiation + low-temp sharing only."** Each module receives heat from its own mirror, dumps it via its own radiators, and passes only the dregs to the habitat.

### Why This Is Better

1. **High-temp radiators are tiny** — 8 m² to dump 1 MW at 800 °C. Just a small fin next to the process
2. **No inter-module piping** — avoids the nightmare of 50 km high-temperature plumbing
3. **Each module is thermally independent** — maintenance on one module doesn't affect the others
4. **The habitat stays safe** — no 1,600 °C heat pipes passing through living quarters

---

## Correcting the Previous Post: Where Does the 70 % Actually Go?

The previous post said "PV wastes 70 %, turbines use it." Is that still correct?

**Yes.** But the mechanism differs:

| | PV | Turbine system |
|---|---|---|
| 30 % | Electricity | Electricity |
| Remaining 70 % | 60–80 °C low-grade waste → **no use** | Distributed to each process as direct mirror heating → **used for smelting, forming, heat-treatment** |
| Radiation burden | All 70 % radiated at low temperature (enormous radiator) | Staged radiation at high temperature (small distributed radiators) |

PV's 70 % is all 60–80 °C — the worst temperature for both industry and radiation. In the turbine system, that 70 % is delivered via mirrors to each process at the exact temperature needed, and waste heat is radiated at the highest temperature possible.

**What "using the remaining 70 %" really means: not turbine waste heat, but mirror thermal energy consumed directly by each process.**

---

## One-Line Summary

No medium can carry 1,600 °C. So each facility receives its own mirror. Heat cascades inside each process, and surplus is radiated at the highest achievable temperature. Only sub-100 °C residual waste reaches the habitat. The radiator panels are the same Fe-Ni sheet as the mirror frames — skip the coating and you have a radiator.
