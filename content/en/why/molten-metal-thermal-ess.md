---
title: "Why Molten Metal, Not Batteries"
date: 2026-02-25T12:00:02+09:00
lastmod: 2026-02-25T12:00:02+09:00
tags: ["molten-metal-thermal-storage", "ESS", "electromagnetic-levitation", "thermal-storage", "self-replication"]
image: "/images/molten-metal-thermal-ess.webp"
summary: "A Dyson module is a solar thermal power plant — store heat directly as molten Fe-Ni in zero-g. ~145 Wh/kg with latent heat, infinite cycles, all from asteroid ore."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Electromagnetically levitated molten Fe-Ni thermal storage mass in zero-gravity vacuum — surface tension holds it in a perfect sphere. Image: Gemini"
---

## What the previous post missed

The [previous post](/why/why-iron-nickel-battery/) showed why iron-nickel batteries beat lithium-ion. No lithium in asteroids, no way to fight fires in vacuum, iron-nickel lasts 30-50 years, and overcharging produces hydrogen.

All true. **But I missed one thing.**

A Dyson module is a solar thermal power plant. Mirrors concentrate sunlight, heat spins turbines. When you need to store energy for eclipse coverage, the current design does this:

```
Solar heat (1,600 C) -> Turbine -> Electricity (370 MW)
                                -> Surplus power (~50 MW)
                                     -> Battery (chemical energy)       <- 2 conversions
                                     -> During eclipse -> Back to electricity  <- 3 conversions
```

Heat -> electricity -> chemistry -> electricity. **Three conversions.** Each step loses 20-30%.

What if you store the heat directly?

```
Solar heat (1,600 C) -> Store part directly in thermal reservoir  <- 0 conversions
                      -> During eclipse -> Reservoir -> Turbine -> Electricity  <- 1 conversion
```

**One conversion.** The efficiency difference is overwhelming.

Converting a solar thermal plant's surplus energy to electricity, then to chemistry, then back to electricity is like turning water into steam, splitting it into hydrogen and oxygen, then recombining them back into water. **It works, but why?**

Thermal storage is the answer. So why doesn't Earth do it?

---

## Why it fails on Earth, why it works in space

Storing heat in molten metal on Earth is an academic research topic, not an industrial reality. There are good reasons:

| Problem | Earth | Space (zero-g vacuum) |
|---------|-------|----------------------|
| Container | Must support the weight of thousands of tons of melt -> massive and expensive | **No self-weight** -- thin walls, or contactless entirely |
| Insulation | Must block convection + conduction + radiation simultaneously | **Block radiation only** -- a few dozen layers of MLI |
| Heat loss | High -- air convection is the main culprit | **Extremely low** -- zero convection in vacuum |
| Corrosion | 1,500 C melt erodes container walls | **Electromagnetic levitation = contactless** -> zero corrosion |
| Safety | Leak means catastrophe | No fire in vacuum, no medium for leaks to spread |

**Every weakness on Earth vanishes or reverses in space.** The same pattern seen in previous posts -- [turbines vs PV](/why/why-turbines/), [iron-nickel vs lithium-ion](/why/why-iron-nickel-battery/) -- exactly the same structure.

---

## Electromagnetic levitation thermal storage

Molten Fe-Ni remains electrically conductive at 1,500 C (nickel loses ferromagnetism above its Curie point, but conductivity persists). Apply an AC electromagnetic field and eddy currents are induced; the repulsion between eddy currents and the field enables **contactless levitation**.

This is a proven laboratory technique on Earth. It's called [EML (Electromagnetic Levitation)](https://en.wikipedia.org/wiki/Electromagnetic_levitation) melting. Metal samples from a few grams to a few kilograms are floated and melted in midair. The reason it can't scale larger on Earth is exactly one thing -- **gravity**. Overcoming gravity demands stronger fields, and stronger fields consume energy. A few kilograms is the practical limit.

In zero gravity? **There is no gravity to overcome.** Only the minimal field needed for positional stabilization. Tons, hundreds of tons, tens of thousands of tons.

```
[Thermal storage unit cross-section]

        +--- MLI reflective wall (multi-layer insulation) ---+
        |                                                     |
        |    +-- EM coils (cooled) --+                        |
        |    |                       |                        |
        |    |   @@@@@@@@@@@@@@@@    |                        |
        |    |   @ Molten Fe-Ni  @   |                        |
        |    |   @ (1,200~1,500 C) @ |                        |
        |    |   @@@@@@@@@@@@@@@@    |                        |
        |    |                       |                        |
        |    +-----------------------+                        |
        |                                                     |
        +-----------------------------------------------------+
```

In zero gravity, molten metal **naturally forms a sphere** due to surface tension. A sphere has the minimum surface area for a given volume -- minimizing radiative heat loss. MLI reflective walls trap radiated heat, electromagnetic fields hold the position, and wall contact is zero -- meaning zero corrosion.

**Melt asteroid Fe-Ni and let it float. That's a thermal reservoir.**

---

## Charging and discharging

```
[Charging -- normal operation]
Solar concentration -> Open radiative shutter -> Heat the metal mass -> 1,200 C -> 1,500 C

[Discharging -- during eclipse]
Open radiative shutter -> Metal mass radiates heat to heat exchanger -> Working fluid -> Turbine
1,500 C -> 1,200 C (utilizing DT=300 C)
```

Charging: direct a portion of the mirror-concentrated solar heat toward the thermal reservoir. Open the shutter and light heats the metal mass.

Discharging: when eclipse arrives, open the shutter so the metal mass's radiated heat reaches the heat exchanger. The heat exchanger heats the working fluid and spins the turbine. The existing turbine is used as-is -- during normal operation the mirror is the heat source, during eclipse the thermal reservoir is the heat source. **From the turbine's perspective, only the heat source changes; everything else stays the same.**

The heat transfer medium is radiation. You can't insert pipes into a contactless melt, so radiative heat transfer through a shutter is the fundamental mechanism. The radiative energy from 1,500 C molten metal scales as T^4 per the Stefan-Boltzmann law -- more than sufficient.

---

## Energy density: sensible heat + latent heat

Fe-Ni alloy specific heat: ~0.5 kJ/(kg*K) = ~0.14 Wh/(kg*K). Calculating only **sensible heat** proportional to temperature change (DT):

| Temperature range (DT) | Sensible heat | Note |
|------------------------|---------------|------|
| 300 C (1,200 -> 1,500 C) | ~42 Wh/kg | Conservative |
| 500 C (1,000 -> 1,500 C) | ~70 Wh/kg | Moderate |
| 1,000 C (500 -> 1,500 C) | ~140 Wh/kg | Aggressive |

But that's not the whole story.

### Latent heat bonus

The Fe-Ni alloy melting point is ~1,430-1,450 C. The operating range 1,000-1,500 C **crosses right through it.** During charging the metal melts; during discharging it solidifies -- a phase change.

When a material melts, it absorbs enormous heat without any temperature rise. This is the **latent heat of fusion.**

```
Iron (Fe) latent heat of fusion: ~270 kJ/kg = 75 Wh/kg
Fe-Ni alloy: similar range
```

Combining sensible and latent heat:

| Temperature range | Sensible | Latent | **Total** |
|-------------------|----------|--------|-----------|
| 300 C (1,200 -> 1,500 C) | ~42 | ~75 | **~117 Wh/kg** |
| 500 C (1,000 -> 1,500 C) | ~70 | ~75 | **~145 Wh/kg** |
| 1,000 C (500 -> 1,500 C) | ~140 | ~75 | **~215 Wh/kg** |

**Latent heat alone doubles the energy density.** A lump of metal melting and solidifying matches the low end of lithium-ion batteries (150-270 Wh/kg).

### ESS comparison (including latent heat)

| Type | Energy density | Cycle life | Material sourcing |
|------|---------------|------------|-------------------|
| Lithium-ion | 150-270 Wh/kg | 3,000-10,000 cycles | Impossible (no Li in asteroids) |
| Iron-nickel battery | 30-50 Wh/kg | Effectively infinite | Asteroid Fe-Ni |
| **Molten Fe-Ni thermal** | **117-215 Wh/kg** | **Effectively infinite** | **Asteroid Fe-Ni** |

Energy density matching lithium-ion, infinite cycle life, and the material is underfoot on any asteroid. Plus heat-to-electricity is only one conversion, so system efficiency is overwhelmingly better.

Why infinite cycle life? You're heating a lump of metal and letting it cool. No chemical reaction. No electrodes. No electrolyte. There is nothing to degrade.

---

## Scale: why 60 small units, not one giant sphere

Maximum eclipse duration 12 hours, turbine output 370 MW. There is no need to cover the entire eclipse with thermal storage alone -- H2 fuel cells and batteries share the load.

### Hybrid allocation

```
During 12-hour eclipse:
  Thermal storage: 6 hours
  H2 fuel cells: 4 hours (battolyser annual accumulation)
  Iron-nickel batteries: 2 hours (instant load-following + backup)
```

Thermal storage for 6 hours (including latent heat):

```
370 MW / 0.30 (turbine efficiency) = ~1,233 MW(th) x 6h = ~7,400 MWh(th)

DT=500 C + latent heat basis (145 Wh/kg):
  Required mass = 7,400,000 kWh / 0.145 kWh/kg = ~51,000 tons

(Without latent heat: 105,000 tons -> latent heat bonus cuts mass in half)
```

Putting 51,000 tons in a single sphere gives a radius of ~12 m. Intuitively simple. **But this doesn't work.** Three engineering reasons.

### Reason 1: insufficient surface area for discharge

During eclipse, the thermal mass transfers heat to the heat exchanger **by radiation only**. Radiative output is proportional to surface area (P = e * sigma * A * T^4).

A sphere has the minimum surface-area-to-volume ratio. Ideal for **retaining** heat, but a bottleneck when you need to **emit heat rapidly**.

```
Required thermal output: ~1,233 MW(th)

1,500 C (1,773 K) radiative output (e=0.5):
  P/A = e x sigma x T^4 = 0.5 x 5.67e-8 x 1,773^4 = 280 kW/m2

Required surface area: 1,233,000 kW / 280 kW/m2 = 4,400 m2

Single sphere r=12m surface area: 4*pi*(12)^2 = 1,810 m2 -> insufficient (41% of requirement)
```

**A single sphere physically cannot emit the required heat.** The surface area is less than half of what's needed.

Split into ~58 units of radius 3 m:

```
Per-unit surface area: 4*pi*(3)^2 = 113 m2
58 units total surface area: 113 x 58 = 6,560 m2 -> 149% of requirement (margin secured)
Per-unit mass: (4/3)*pi*(3)^3 x 7,800 = ~880 tons
```

**During storage, each unit maintains its spherical shape to minimize losses. During discharge, the combined surface area of multiple units provides sufficient thermal output.** The sphere's weakness is overcome by unit count.

### Reason 2: sloshing -- a 100,000-ton lava wrecking ball

When 51,000 tons of liquid metal float as a single sphere, any rotation or vibration from attitude control generates **massive internal waves (sloshing)**. Add magnetohydrodynamic (MHD) instabilities and this molten mass can slosh its way through electromagnetic containment.

With 3 m radius, 880-ton units? Fluid kinetic energy scales with the cube of unit size, so **individual unit sloshing energy drops by 10,000x or more** compared to the single sphere. Containment breach risk is effectively eliminated.

### Reason 3: volumetric expansion during phase change

Cycling between 1,200 C (solid) and 1,500 C (liquid), Fe-Ni repeatedly expands and contracts. When a 12 m radius sphere cools from the outside, a solid shell forms first while the liquid interior contracts -- **the shell cracks and fragments are ejected into vacuum**. Small units maintain uniform internal-external temperature gradients, eliminating this problem.

### Design conclusion

```
Thermal storage unit specs:
  Shape: Spherical (naturally formed by surface tension)
  Radius: ~3 m
  Mass: ~880 tons/unit
  Unit count: ~58 (per module)
  Total mass: ~51,000 tons
  Placement: Distributed throughout structure behind mirrors (doubles as counterweight)

Discharge performance:
  Total surface area: ~6,560 m2 (149% of 4,400 m2 requirement)
  1,233 MW(th) output margin secured
```

The 51,000 tons are not sourced separately. Smelt asteroid Fe-Ni and **keep it molten instead of letting it solidify -- that's a thermal storage unit**. Distribute them across the module structure and they **double as counterweights**.

---

## Three-tier ESS: role separation

Batteries no longer need to handle bulk ESS. The optimal technology is assigned to each tier:

```
Tier 1 -- Bulk (hours)
  -> Molten metal thermal reservoir
       Charging: direct solar heat
       Discharging: thermal -> turbine -> electricity
       Role: eclipse coverage, minimum conversion loss

Tier 2 -- Buffer (seconds to minutes)
  -> Iron-nickel batteries
       Charging: surplus electricity
       Discharging: electrochemical (ms response)
       Role: instant load-following, startup power

Tier 3 -- Emergency + chemical production
  -> H2/O2 (battolyser output)
       Fuel cell emergency power
       Propellant, reducing agent, breathable oxygen
       Extended eclipse secondary backup
```

### What this architecture delivers

**Battery banks shrink dramatically.** In the previous design, covering a 12-hour eclipse with batteries alone required 111,000 m3. With thermal storage handling bulk duty, batteries cover only 2 hours -- shrinking to a few thousand m3.

**The battolyser's role becomes clear.** The previous post described the battolyser (water electrolysis via overcharging) as combining ESS function with chemical production. With thermal storage carrying the bulk ESS load, the battolyser is repositioned as a **chemical plant** -- hydrogen propellant, oxygen, and reducing agent production is the main job; emergency power generation is a side function.

**Same material throughout.** Thermal reservoir = molten Fe-Ni. Batteries = Fe-Ni electrodes. Battolyser = same batteries overcharged. All three tiers come from asteroid Fe-Ni. No new feedstock enters the self-replication loop.

---

## Relationship to the previous post (iron-nickel batteries)

The previous post's core arguments **all remain valid:**

- No lithium in asteroids -> unchanged
- Iron-nickel battery 30-50 year lifespan -> unchanged
- Fire risk in vacuum -> unchanged
- Battolyser H2/O2 production -> unchanged
- Local manufacturability -> unchanged

**What this post adds:** The previous post could be read as if iron-nickel batteries alone handle bulk ESS (12-hour eclipse coverage). In reality, bulk energy storage overwhelmingly favors thermal storage, while batteries excel in their own domain -- instant response.

**Each technology does what it's best at.** The furnace stores hours of heat. The battery delivers milliseconds of power. The fuel cell handles emergencies and makes chemicals. No single system needs to do everything.

---

## One-line summary

A Dyson module is a solar thermal power plant -- converting heat to electricity to chemistry and back is triple-conversion waste. Melt asteroid Fe-Ni and float it in zero-g and you get a thermal reservoir with 0 conversion charges and 1 conversion discharges. With phase-change latent heat, energy density reaches ~145 Wh/kg -- matching lithium-ion. 58 distributed units of radius 3 m solve discharge surface area bottleneck, sloshing, and phase-change expansion. All from the same asteroid Fe-Ni.

![Electromagnetically levitated molten Fe-Ni thermal storage mass in zero-gravity vacuum. Image: Gemini](/images/molten-metal-thermal-ess.webp)
