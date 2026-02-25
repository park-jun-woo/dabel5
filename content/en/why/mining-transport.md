---
title: "Why Not Smelt On-Site"
date: 2026-02-24T12:00:04+09:00
lastmod: 2026-02-24T12:00:04+09:00
tags: ["asteroid-mining", "transport", "SMR", "NTP"]
image: "/images/1986da-orbit.webp"
summary: "A complete engineering design for mining metallic asteroid 1986 DA with an SMR-powered mining ship, packaging ore in Fe-Ni wire mesh nets, and shipping 200,000 tons per transfer window."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

*Orbital visualization: [SpaceReference.org](https://www.spacereference.org/asteroid/6178-1986-da), built with [SpaceKit](https://typpo.github.io/spacekit/). Data: JPL Small Body Database.*

## Mining Sounds Great, but How?

In the previous post, we proposed 1986 DA as the raw material source for a Dyson swarm. Over 90% Fe-Ni, microgravity, zero waste. Superior to Mercury in every way for bootstrapping.

But a question remains: **How do you actually mine a metallic lump in microgravity, and how do you move it?**

The core principle first: **"On-site, you only dig, crush, and bag. Heavy processing happens where energy is abundant."**

---

## Division of Roles: On-Site vs Base

| Task | Location | Reason |
|------|----------|--------|
| Excavation & crushing | 1986 DA on-site | Where the ore is |
| Packaging (wire mesh) | 1986 DA on-site | Made from local Fe-Ni |
| Sorting | **Not done** | Every component has a use |
| Smelting | **Base (Dyson mirrors)** | Mirror solar thermal GW-class >> on-site SMR kW-class |
| Fabrication & assembly | **Base** | Specialized clusters |

Why not smelt on-site? Smelting requires 1,600°C. The on-site SMR produces 50--100 kW. The base's Dyson mirrors deliver ~600 MW (thermal). **The energy gap is thousands of times.** Building a smelter on the asteroid is like putting a steel mill on a mountaintop -- it makes more sense to ship the ore down.

---

![mining-transport](/images/post004.webp)

## The Mining Ship: A Machine That Digs, Crushes, and Bags

### Energy: SMR + Solar Boost

1986 DA's highly elliptical orbit (eccentricity 0.58) causes solar flux to vary by more than 14x depending on orbital position.

| Orbital Position | Distance | Solar Flux | vs Earth |
|-----------------|----------|------------|----------|
| Perihelion | 1.17 AU | ~995 W/m² | 73% |
| Semi-major axis | 2.81 AU | ~172 W/m² | 13% |
| Aphelion | 4.46 AU | ~68 W/m² | 5% |

**Solar power alone cannot sustain continuous mining.** An SMR (Small Modular Reactor, 50--100 kW) is the primary energy source. Near perihelion, solar panels join in as a boost.

| Orbital Segment | SMR | Solar | Combined | Mode |
|----------------|-----|-------|----------|------|
| Near perihelion (~1.2 AU) | 50--100 kW | 50--100 kW | **100--200 kW** | Boost |
| Mid-orbit (~2.8 AU) | 50--100 kW | ~15 kW | ~65--115 kW | Normal |
| Near aphelion (~4.5 AU) | 50--100 kW | ~5 kW | ~55--105 kW | Low-speed |

Even at aphelion, the SMR keeps mining going. It just slows down.

### Equipment

| Equipment | Function | Power Draw |
|-----------|----------|------------|
| Excavator | Surface/subsurface mining | ~20--50 kW |
| Crusher | Breaking ore to transport size | ~10--30 kW |
| Small electric furnace | Fe-Ni to wire stock | ~10--20 kW |
| Wire drawing machine | Wire to mesh net | ~5--10 kW |
| Control & comms | AI autonomous control | ~5 kW |
| **Total** | | **~50--115 kW** |

A single SMR powers all equipment. The mining ship is **permanently stationed** -- it orbits with 1986 DA and mines without pause.

### Productivity

Conservative assumption: average 50 kW input, ~100 kg of ore processed per kWh (mechanical crushing and packaging in microgravity; comparable to terrestrial rock crushing at 10–25 Wh/kg; smelting is performed separately at base).

| Item | Value |
|------|-------|
| Daily mining output | ~120 tons |
| Annual mining output | ~43,800 tons |
| **Per orbital period (4.71 years)** | **~200,000 tons** |

---

## Containers: Nets, Not Boxes

What does a cargo container need in space?
- Pressure containment -- vacuum, so unnecessary
- Self-weight support -- microgravity, so unnecessary
- Air resistance -- vacuum, so unnecessary
- **Keeping ore from scattering during transport**

That is the only requirement. Not a rigid box -- **a net is enough.**

### Fabrication Process

```
Mined ore
  |-- 99.5% -> Cargo (ore bundles)
  +-- 0.5% -> Small electric furnace -> Wire drawing -> Mesh net weaving
                                                     -> Ore bundle packaging
```

| Method | Container:Cargo Mass Ratio |
|--------|---------------------------|
| Metal containers shipped from Earth | Extreme transport waste |
| On-site Fe-Ni box casting | ~2--3% (overkill) |
| **On-site Fe-Ni wire mesh** | **~0.1--0.5%** |

**The mesh itself becomes smelting feedstock upon arrival.** Even the packaging is 100% utilized.

---

## Transport: Transfer Windows and Propulsion

### Orbital Mechanics

1986 DA orbital period: 4.71 years. The optimal transfer window to Earth-space opens once per orbital period.

| Item | Value |
|------|-------|
| LEO to 1986 DA rendezvous | delta-V ~7.1 km/s |
| Optimal departure | Near perihelion (1.17 AU) |
| Next close approach | **2038 (0.21 AU)** |

### Propulsion Options

| Method | Specific Impulse (Isp) | Characteristics | Suitability |
|--------|----------------------|-----------------|-------------|
| Chemical (LH2/LOX) | ~450 s | Extremely low payload fraction | ❌ |
| **Nuclear Thermal Propulsion (NTP)** | **~900 s** | High thrust, fast | ✅ |
| **Nuclear Electric Propulsion (NEP)** | **~3,000 s+** | Minimal propellant, slow | ✅ Bulk transport |
| Solar Electric Propulsion (SEP) | ~3,000 s | Efficiency collapses at aphelion | ⚠️ Limited |

**An NTP + NEP hybrid may be optimal:** a single reactor serves as both the NTP heat source (high thrust for perihelion departure) and the NEP power source (low-thrust, high-efficiency cruise).

### Logistics Cycle

```
[Year 0]  Mining ship arrives at 1986 DA, mining begins
             | 4.71 years of mining, packaging, stockpiling (~200,000 tons)
[Year ~5] Transfer window -> Transport ship loads and departs
             | Hohmann transfer (~2-3 years)
[Year ~7] Transport ship arrives, ore offloaded
             | Maintenance & resupply
[Year ~8] Transport ship departs for return
             |
[Year ~10] Second loading ... cycle repeats
```

The mining ship stays; the transport ship shuttles. Mining and transport run **asynchronously in parallel.**

---

## 2038: Miss It and Wait Decades

| Timeframe | Event |
|-----------|-------|
| 2030s | Starship commercialized, space SMR technology matures |
| **2038** | **1986 DA close approach (0.21 AU) -- optimal window to deploy mining ship** |
| 2038--2042 | Mining ship arrives on-site, mining begins |
| ~2043 | First transport ship loads and departs |
| **~2046** | **First ore delivery** |

After 2038, the next close approach of this magnitude is decades away. **Miss this window and the timeline slips significantly.**

### Required Technology Status

| Technology | Current (2026) | 2038 Outlook |
|------------|---------------|--------------|
| Starship (heavy-lift vehicle) | Test flights underway | ✅ Commercialization expected |
| Space SMR | NASA FSP 40 kW-class in development | ✅ Lunar demonstration expected |
| NTP propulsion | DARPA DRACO in development | ⚠️ Test flight expected |
| Asteroid mining | OSIRIS-REx sample return succeeded | ⚠️ Large-scale unproven |
| AI autonomous space ops | Mars rover level | ✅ Expected to be sufficiently mature |

None of these technologies are impossible. All are **in development or expected to mature within a decade.**

---

## After Arrival: The Sun Does the Smelting

Once the ore arrives, Dyson mirrors heat it directly to 1,600°C. The vacuum of space is "free refining equipment":

1. **Optical melting** -- Concentrated mirror heat melts raw ore into molten metal
2. **Vacuum degassing** -- Sulfur and phosphorus naturally vaporize in vacuum (captured by cold traps)
3. **Centrifugal separation** -- Outer layer: Fe-Ni + platinum group metals / Inner layer: silicate slag

```
Ore bundle arrives
  |-> Fe-Ni wire mesh -> Fed into smelter (packaging becomes feedstock)
  +-> Ore -> Mirror heating to 1,600°C
       |-> Fe-Ni alloy (90%+) -> Structural members, mirror frames, pipes
       |-> Silicate slag -> Shielding + silicon ingot feedstock
       |-> Platinum group metals -> Coatings, catalysts
       +-> S, P -> Chemical feedstock, semiconductor doping
```

What terrestrial steel mills achieve with massive energy and chemicals, **space vacuum and solar heat provide for free.**

---

## One-Line Summary

The mining ship digs, crushes, and bags with a single SMR. Containers are local Fe-Ni mesh nets -- even the packaging is feedstock. The transport ship hauls 200,000 tons per transfer window. 2038 is the first window of opportunity. The arriving ore is smelted by the Sun. Nothing is wasted.
