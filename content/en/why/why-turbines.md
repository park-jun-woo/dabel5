---
title: "Why Turbines, Not Solar Panels"
date: 2026-02-24T12:00:07+09:00
lastmod: 2026-02-24T12:00:07+09:00
tags: ["solar-thermal", "turbine", "self-replication", "photovoltaic"]
summary: "Solar panels and turbines both convert sunlight to electricity at ~30% efficiency in space. But turbines cascade the remaining 70% as useful heat, can be built from asteroid materials, and are field-serviceable — making them the only option for a self-replicating Dyson swarm."
image: "/images/why-turbines.webp"
author: "PARK JUN WOO"
imageCaption: "Steam turbine rotor blade installation at a Siemens factory. Photo: Siemens Pressebild / Wikimedia Commons / CC BY-SA 3.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## "Why turbines again?"

When people think about Dyson swarm power, solar panels (PV) are the obvious choice. They are the standard for space power. The ISS runs on PV. Most deep-space probes run on PV.

Yet this design uses turbines. Why go back to 19th-century technology in the 21st century?

The answer is simple: **you can't make solar panels from asteroids, but you can make turbines.**

---

## The efficiency is the same — 30%

Let's address this first. "Isn't PV more efficient?"

| | Solar Panel (GaAs multi-junction) | Solar Thermal Turbine |
|---|---|---|
| Conversion efficiency | ~30% (space-grade) | ~30% (hot side 1,500 K / cold side 500 K) |
| Carnot limit | N/A | 66.7% (realized ~45%) |
| Electrical output | **Same** | **Same** |

Collect 1,225 MW(thermal) with a 1 km² mirror, and whether you use PV or a turbine, **the electrical output is ~370 MW either way.**

If efficiency is the same, the differences lie elsewhere.

---

## Difference 1: The other 70%

Both PV and turbines fail to convert 70% of incoming energy into electricity. But where that 70% goes is very different.

### PV: 70% vanishes as low-grade waste heat

```
Solar input 1,225 MW
  ├→ 30% → 370 MW (electricity)
  └→ 70% → 855 MW → panel surface at 60–80°C waste heat
                     → no use. Radiated to space via heat sinks.
```

At 60–80°C, you can't smelt metal, run a factory, or heat a habitat. **70% of the energy simply disappears.**

### Turbine: 70% cascades from high to low temperature

```
Solar thermal 1,225 MW
  ├→ 30% → 370 MW (electricity)
  └→ 70% → 855 MW (heat) → staged utilization by temperature:
       ├→ 800–1,000°C: ~400 MW → smelting (Fe-Ni melting)
       ├→ 400–600°C:   ~250 MW → coating, heat treatment, forming
       ├→ 100–200°C:   ~120 MW → habitat heating
       └→ 30–60°C:      ~85 MW → data center environmental heat
```

**The same 70% passes sequentially through smelter → factory → habitat → data center, and all of it gets used.** The turbine's "waste heat" isn't waste — it's the energy source for the next process.

Effective utilization of incoming energy:
- PV: ~30% (electricity only)
- **Turbine: ~30% + thermal cascade → effectively 85%+**

---

## Difference 2: Self-replication loop compatibility

This is the decisive factor.

### Making PV in space

Manufacturing solar panels (GaAs multi-junction) requires:
1. Gallium (Ga) + arsenic (As) feedstock — **not found in asteroids**
2. Single-crystal growth (MOCVD, MBE) — **extreme precision equipment**
3. Multi-layer epitaxial deposition — **cleanroom required**
4. Anti-reflective coating, wiring, module assembly — **dedicated fab line**

Asteroids have neither Ga nor As. Even with the equipment, there is no feedstock. **PV cannot enter the self-replication loop.** It must be continuously resupplied from Earth.

What about silicon (Si) PV? This design actually already includes a process to produce semiconductor-grade Si ingots from silicate slag (zone refining, for AI chips). So Si feedstock is available. However:
- Si PV space efficiency ~20% — lower than GaAs (30%) and below turbines (30%)
- PV cell manufacturing line (diffusion, anti-reflective coating, electrode patterning) is **separate from the chip fab**
- Efficiency degrades from space radiation → shorter replacement cycle
- The same Si wafer is **far more valuable as an AI chip**

Even with Si available, making PV from it is wasteful. **If you have silicon, you make chips.**

### Making turbines in space

| Component | Material | Source | Fabrication |
|-----------|----------|--------|-------------|
| Hot blades & nozzles | Ni superalloy | Asteroid Fe-Ni | Precision casting |
| Cold compressor & shaft | Ti alloy | Lunar ilmenite | Machining |
| Casing | Fe-Ni | Asteroid | Sheet metal & welding |

**Everything can be built from materials already in the self-replication loop (Fe-Ni, Ti).** No additional feedstock required, no additional fab lines required. Turbines come off the same production line that makes mirror frames.

---

## Difference 3: Lifespan and maintenance

### PV's radiation problem

Space PV is damaged by high-energy particles (protons, heavy ions) that disrupt the crystal lattice. Efficiency degrades by ~1–3% per year.

- After 10 years: efficiency drops to 70–80%
- Replacement needed → **can't be manufactured, must be resupplied from Earth**
- If resupply is unavailable: accept reduced output

### Turbine wear

Turbines don't last forever either. High-temperature blade creep and bearing wear are the main degradation mechanisms.

But:
- Blades can be **recast locally from Ni superalloy**
- Bearings → **magnetic bearings for contactless** operation: zero wear
- Modular design: only replace degraded components, not the whole unit

**Turbine parts can be manufactured and replaced on-site. PV parts cannot.** In a self-replicating system, this difference is decisive.

---

## Real limitations of turbines — and solutions

Let's be honest about the downsides.

### Limitation 1: Working fluid is required

Turbines need a fluid that expands when heated to spin the rotor. Where do you get this fluid in space?

| Candidate | Advantages | Disadvantages | Procurement |
|-----------|-----------|---------------|-------------|
| Helium (He) | Inert, high-temp stable | Hard to replenish if leaked | Captured from asteroid outgassing |
| Supercritical CO₂ | High density, compact turbine | Corrosion management needed | Asteroid outgassing |
| Sodium/Potassium (liquid metal) | Ultra-high temp capable, excellent heat transfer | Reactive (safe in vacuum) | Trace amounts from asteroids |

The system runs a closed cycle, so there is no fluid consumption. Only the initial charge needs to be secured. Gas can be captured during asteroid smelting outgassing, or a small amount can be supplied from Earth initially.

### Limitation 2: Moving parts — failure risk in space

The fundamental weakness of turbines: high-speed rotating components. Even on Earth, turbine maintenance is demanding work.

**Solutions:**
- **Magnetic bearings** — contactless rotational support. Zero wear. Already commercialized in high-speed turbomachinery on Earth
- **Modular blade cartridges** — replace blade sets as a unit. No individual blade servicing needed
- **Local manufacturing** — cast replacement parts on demand. No waiting for Earth resupply
- **Redundancy** — multiple turbines per module. Output maintained even during single-unit maintenance

### Limitation 3: Vibration

High-speed rotation generates vibration. This is a problem if semiconductor fabs or precision optical equipment share the same module.

**Solutions:**
- **Specialized clusters** — physically separate turbine modules from fab modules (distinct structures)
- **Vibration-damping mounts** — install turbines on flexible structural joints
- On Earth, you don't put a power plant and a semiconductor fab in the same building either

### Limitation 4: Heat rejection

The turbine's cold-side heat must be radiated to space. There's no atmosphere in space, so convective cooling is impossible — only radiative cooling works.

**This is a large independent topic. It will be covered in detail in the next post.**

---

## One-line summary

Solar panels and turbines have the same electrical efficiency (30%). But PV throws away the other 70%, while turbines use it. PV can't be made in space; turbines can. When PV breaks, you wait for Earth; when a turbine blade wears out, you recast it on-site. In a self-replicating system, the answer is clear.
