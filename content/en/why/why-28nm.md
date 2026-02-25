---
title: "Why 28nm"
date: 2026-02-25T12:00:03+09:00
lastmod: 2026-02-25T12:00:03+09:00
tags: ["28nm", "semiconductor", "TPU", "self-replication", "ArF-lithography"]
image: "/images/why-28nm.webp"
summary: "Cutting-edge 3nm can't be made without ASML's monopoly EUV — impossible in space. 28nm needs only ArF, and Google TPU v1 proved 92 TOPS at that node. Silicon comes from smelting slag, and space itself is the cleanroom."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Die photo of a TTL 4-input NAND gate chip — 7 transistors, minimum feature size 20 um (1968). Photo: Dgarte / Wikimedia Commons / CC BY-SA 3.0"
---

## "Self-replicating, you say — so where do the chips come from?"

[Previous posts](/why/dyson-swarm-at-l5/) showed that mirrors, structural frames, [turbines](/why/why-turbines/), [batteries](/why/why-iron-nickel-battery/), and [thermal management](/why/heat-flow/) can all be built from asteroid Fe-Ni. The self-replication loop is nearly closed.

Nearly.

**AI chips still come from Earth.** Autonomous operation of a Dyson module -- mining robot control, orbit adjustment, smelting process management, habitat life support -- is all done by AI. Without chips, the module is blind.

"No lithium in asteroids" was game over for lithium-ion batteries. **"You can't make EUV in space" is game over for cutting-edge 3nm.**

So what process node do you fabricate chips at?

---

## Why not cutting-edge 3nm

The core of semiconductor manufacturing is lithography -- using light to etch circuit patterns onto a wafer.

| Item | 28nm | 3-5nm (cutting edge) |
|------|------|---------------------|
| Lithography | **ArF immersion** (Nikon, Canon, ASML) | **EUV** (ASML monopoly, >$100M per unit) |
| Equipment availability | Mature market, abundant secondhand | Extremely limited, export-controlled |
| Design complexity | Single patterning | Multi-patterning (extremely complex) |
| Fab construction cost | ~$3-5B | ~$20-30B |
| Yield | High (10+ years of validation) | Initially poor |

EUV (extreme ultraviolet) scanners are **made by exactly one company on Earth.** ASML. A single factory in Veldhoven, Netherlands. Subject to export controls. The equipment that the US-Japan-Netherlands alliance blocks China from buying. Reproduce this in space? Impossible.

The most powerful process node that doesn't need EUV. That's **28nm**.

"Can't 7nm be done with ArF?" -- It can. A technique called multi-patterning exposes the ArF light multiple times to create finer patterns. But design complexity explodes and yield plummets. Before you have the workforce and infrastructure for yield management in space, it's unrealistic.

"65nm would be easier to make, though?" -- True. But per-chip performance is too low. To get the same work done you need far more chips, and more chips means proportionally more complex wiring, packaging, and cooling. Easy to fabricate, but the overall system becomes harder.

**28nm = the optimal density achievable without EUV.**

---

## This isn't theoretical -- Google TPU v1

"Can 28nm actually run AI?"

Google answered that in 2015. **[TPU v1.](https://arxiv.org/abs/1704.04760)** Fabricated at 28nm, deployed to 100,000+ units across Google's own datacenters. A production AI accelerator.

| Item | Google TPU v1 (measured) |
|------|------------------------|
| Process | 28nm |
| Architecture | 256 x 256 systolic array |
| Compute | 92 TOPS (INT8) = 23 TFLOPS (FP16) |
| Power consumption | ~75W in real operation |
| Silicon utilization | **90%+** |

The systolic array architecture is key. A GPU is a general-purpose chip -- 70% of its silicon goes to control logic, caches, and schedulers. Only 30% does actual matrix math. A systolic array is designed solely for matrix multiplication, so **90%+ of the silicon performs actual computation.**

If all you need is AI, every bit of GPU general-purpose overhead is waste. The TPU eliminates that waste.

And this isn't a paper proposal. **It's the chip that ran AlphaGo.** Hardware deployed in production at Google datacenters for years.

---

## "4.6x the power draw?"

The current top-performing AI chip on Earth: NVIDIA H100. 4nm process, 990 TFLOPS, 700W power draw.

One TPU v1 delivers 23 TFLOPS. To match a single H100:

```
990 TFLOPS / 23 TFLOPS = 43 chips

43 chips x 75W = 3,225W = 3.2 kW
```

| | TPU v1 x 43 | H100 x 1 |
|---|---|---|
| FP16 total | ~990 TFLOPS | ~990 TFLOPS |
| Total power | **3.2 kW** | 700W |
| Power ratio | **4.6x** | Baseline |

4.6x. On Earth, that's a fatal gap. In a world where electricity is 30-40% of datacenter operating costs, a 4.6x power penalty means bankruptcy.

**In space?**

One Dyson module = 370 MW. 3.2 kW is **0.00086%** of 370 MW. In mirror area, that's 2.4 m2 -- a single pixel on a 1 km2 Dyson mirror.

On Earth, power is money. **In space, power is mirror area.** Mirrors are made by flattening asteroid Fe-Ni.

Same logical structure as the [previous post where turbines beat solar panels](/why/why-turbines/). An inferior choice by Earth's standards flips to the only viable choice by space standards. **Different baseline, different answer.**

---

## One module = a 30,000 H100-class datacenter

Allocate 30% of a module's 370 MW to AI compute:

```
111 MW / 75W per chip = ~1,480,000 chips (1.48 million TPU v1)

1.48 million / 43 chips per H100-equivalent = ~34,000 H100s

Interconnect and cooling overhead 20-30% -> conservatively ~25,000-30,000 H100-class
```

Equivalent to the largest AI clusters on Earth as of 2026. **One module.**

When 270,000 modules self-replicate? Billions of H100-equivalents. Computational capacity exceeding all of humanity's current capability -- from a single asteroid.

---

## Feedstock: AI chips from slag

This is the most elegant part of the design. No dedicated semiconductor mine needed.

Smelting asteroid ore yields Fe-Ni (90%+) as the primary product, and **the remainder is slag**. The main component of slag is SiO2 -- silicate. Don't throw it away.

```
Asteroid ore -> Vacuum smelting
  +-> Fe-Ni (90%+) -> Mirrors, structural frames, batteries, turbines
  +-> Slag (mostly SiO2)
       +-> Bulk -> Radiation shielding
       +-> Fraction -> Carbon reduction (SiO2 + 2C -> Si + 2CO)
            -> Metallic silicon
            -> Zone refining (solar heat + vacuum + microgravity)
            -> Semiconductor-grade single-crystal ingot (9N+ purity)
            -> 300mm wafer
            -> 28nm TPU
```

**AI chips come from smelting waste.**

[Zone refining](https://en.wikipedia.org/wiki/Zone_melting) has specific advantages in space. It's a purification technique where a narrow molten zone is passed through a silicon ingot to push impurities to one end:

- **Energy:** Direct solar heating. Zero cost
- **Vacuum:** Space is vacuum. Impurities auto-evaporate
- **Microgravity:** The molten zone doesn't sag. Earth's FZ (Float Zone) method is limited to 200mm ingot diameter -- any larger and the molten silicon collapses under gravity. **In zero-g, 300mm+ is feasible**
- **Repetition:** Adjust mirror angle and repeat refining passes indefinitely. Zero marginal cost

On Earth, zone refining is an expensive, small-scale premium process. In space, it becomes the **default process**.

---

## The fab: space is the cleanroom

One of the biggest cost items for a terrestrial 28nm fab: Class 1-10 cleanrooms. Fewer than 10 particles of diameter 0.5 um or larger per cubic foot of air. Maintaining this requires massive HEPA filter systems, air handling units, and positive pressure management. A significant fraction of fab construction cost goes here.

Space has **no air.** The particle contamination source simply doesn't exist. Vacuum is the **perfect cleanroom.**

Space suitability by major fab process step:

| Process | Space suitability | Reason |
|---------|-------------------|--------|
| Ingot growth | **Space advantage** | Microgravity FZ method, large-diameter ingots |
| Wafer slicing | Feasible | Mechanical process, environment-independent |
| Oxidation/Deposition (CVD, PVD) | **Vacuum advantage** | Earth fabs must pump chambers to vacuum -- space is already vacuum |
| Photolithography | Bottleneck | ArF scanner and photoresist are Earth-dependent |
| Etching | **Vacuum advantage** | Plasma etch chamber simplified |
| Ion implantation | **Vacuum advantage** | Reduced beam scattering, no high-vacuum pumps needed |
| Metallization/Packaging | Feasible | Cu sourced from asteroids/Moon |

**Six of seven steps are advantaged or equivalent in space.** The sole bottleneck is photolithography -- the ArF scanner itself can't be made in space. But once launched, it lasts decades.

---

## Fab thermal management: "You want to make semiconductors in space?"

"The sun-facing side is hundreds of degrees, the shaded side is minus 100 C, and you claim plus-or-minus 0.01 C control is possible?"

Yes. And **it's easier than on Earth.**

### The core problem

The ArF lithography scanner's projection lens system is extremely sensitive to thermal expansion. A 0.01 C temperature fluctuation changes lens curvature, creates overlay error, and kills yield. The overlay tolerance for 28nm is a few nanometers.

How terrestrial fabs solve this:
- Maintain the entire cleanroom at 23.00 +/- 0.1 C
- Scanner internals get a dedicated cooling loop at +/- 0.01 C
- **Problem:** External disturbances constantly intrude -- ambient temperature swings, seasons, day/night cycles, weather, earthquakes, road vibration, adjacent equipment heat

### Space fab thermal design

```
[Fab module cross-section]

Exterior: space vacuum (zero conduction, zero convection)
  |
  +- MLI reflective wall (multi-layer insulation, dozens of layers)
  |    -> Solar radiation rejection 99.5%+
  |    -> Internal-to-external radiative loss also blocked
  |
  +- Structural outer wall (Fe-Ni)
  |
  +- Active liquid circulation layer
  |    -> Ultra-pure water (UPW) micro-circulation
  |    -> Pump + heater + radiator valve for active control
  |    -> Entire inner wall at 23.00 +/- 0.05 C uniformly
  |
  +- Fab interior (1 atm N2 atmosphere)
       -> Equipment heat -> absorbed by circulating coolant
       -> Scanner internals: dedicated cooling loop +/- 0.01 C
```

### Why it's easier than on Earth

| Item | Terrestrial fab | Space fab module |
|------|----------------|-----------------|
| External temperature disturbance | Constant (weather, seasons, day/night) | **None** -- vacuum insulation |
| External vibration | Roads, earthquakes, adjacent factories | **None** -- zero vibration in space |
| Insulation cost | HVAC consumes 30-40% of fab power | **Vacuum is free insulation** |
| Heat source predictability | External disturbance + internal equipment | **Internal equipment only** (fully predictable) |
| Heat rejection | Cooling towers, chillers (massive water and power) | **Radiator panels** (vacuum radiation) |

The key paradox: space's extreme thermal environment (hundreds of degrees vs minus 100 C) **never reaches the fab interior**. Vacuum is the best insulator, and once MLI blocks radiation, the fab interior is completely thermally isolated from the exterior. From that point, you only manage internal equipment heat -- and that's easier than on Earth because external disturbance is zero.

Terrestrial fabs spend 30-40% of their total power on HVAC because **they are constantly fighting the outside environment**. The space fab doesn't have that fight at all.

### UPW -- from the battolyser

The ultra-pure water (UPW) for fab thermal circulation doesn't require a separate water treatment plant. It comes from battolyser output:

```
Battolyser: H2O -> H2 + O2 (electrolysis)
Reverse:    H2 + O2 -> H2O (fuel cell)

Byproduct H2O -> Purification -> UPW
  +-> Fab thermal circulation coolant
  +-> Wafer cleaning
  +-> Immersion lithography fluid
```

### Artificial gravity compartment

Immersion lithography requires a thin film of ultra-pure water on the wafer surface -- gravity is needed. The fab module is divided into two compartments:

```
Vacuum compartment (0G):
  +-> CVD/PVD deposition (vacuum required)
  +-> Ion implantation (vacuum required)
  +-> Plasma etching (vacuum required)

Artificial gravity compartment (~1G rotation):
  +-> ArF immersion lithography (liquid management needs gravity)
  +-> Wet cleaning (UPW rinse needs gravity)
  +-> Wafer handling (robotic transfer)
```

Wafers move between vacuum and artificial-gravity compartments through airlocks. The rotating compartment has no external vibration sources, so **only the uniformity of rotation itself needs management** -- far simpler than defending against earthquakes and road vibration on Earth.

---

## External dependency: 5%

| Item | Source | Note |
|------|--------|------|
| Silicon | Local (slag -> Si) | |
| Energy | Local (solar thermal) | |
| Cleanroom | Local (space vacuum) | |
| Ultra-pure water | Local (battolyser H2O -> purification) | |
| Copper wiring | Local (asteroid/Moon) | |
| ArF scanner | **Earth, once** | Decades of service life |
| Photoresist | **Earth, annual** | A few hundred kg/year |
| Etch gases | **Earth, annual** | Recycled, small volume |
| Dopant elements (B, As) | **Earth, annual** | Tens of kg |

95% sourced in space. The remaining 5% -- one ArF scanner (initial launch) + consumables (a few tons per year) -- fits on a single Starship launch covering decades of operation.

"Photoresist is precision organic chemistry, isn't it?" -- Yes. Local manufacturing is difficult. But annual consumption is on the order of a few hundred kilograms. A single Starship can carry decades' worth. Not complete self-sufficiency, but **effective self-sufficiency**.

---

## The self-replication loop closes

```
Previously:
  Asteroid ore -> Smelting -> Fe-Ni -> Mirrors, structures, batteries -> Self-replication
                                                                      ^
                                                              AI chips imported from Earth X

Now:
  Asteroid ore -> Smelting -> Fe-Ni -> Mirrors, structures, batteries, turbines
                           -> Slag -> Si ingot -> 28nm TPU -> AI autonomous control
                                                            |
                                                  Self-replication loop fully closed
```

Mirrors make mirrors. Batteries make propellant. **Slag makes AI chips.** Nothing is wasted.

---

## One-line summary

Cutting-edge 3nm can't be made without ASML's monopoly EUV -- impossible in space. 28nm needs only ArF, and Google TPU v1 proved 92 TOPS at that node. The 4.6x power penalty is 2.4 m2 of mirror on a 370 MW module. Silicon comes from smelting slag, space itself is the cleanroom, and vacuum insulation makes +/-0.01 C thermal control easier than on Earth. The last link in the self-replication loop.

![Die photo of a TTL 4-input NAND gate chip. Photo: Dgarte / Wikimedia Commons / CC BY-SA 3.0](/images/why-28nm.webp)
