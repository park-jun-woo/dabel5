---
title: "Why Iron-Nickel Batteries, Not Lithium-Ion"
date: 2026-02-25T12:00:01+09:00
lastmod: 2026-02-25T12:00:01+09:00
tags: ["iron-nickel-battery", "edison-battery", "battolyser", "ESS", "self-replication"]
image: "/images/why-iron-nickel-battery.webp"
summary: "There's no lithium on asteroids, you can't swap batteries every 10 years in space, and you can't put out a fire in vacuum. Iron-nickel batteries are made from asteroid smelting byproducts, last 30-50 years, and after full charge they produce hydrogen and oxygen."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Nickel-iron batteries originally developed by Edison in 1901. Thomas Edison National Historical Park. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0"
---

## "Energy storage obviously means lithium-ion, right?"

A Dyson module collects solar heat with mirrors to spin turbines. It would be nice if the Sun shone 24/7/365, but reality disagrees.

- **Eclipse:** The EML5 base enters Earth/Moon shadow 2-3 times per year, totaling 3-12 hours
- **Load fluctuation:** Turbines respond slowly to sudden load changes. Without ESS, voltage wobbles on instantaneous demand swings
- **Emergency shutdown:** During mirror maintenance or turbine failure, critical systems -- life support, AI, communications -- cannot stop
- **Maneuvering power:** Tug docking and evasive maneuvers demand high burst power

A Dyson module cannot function without batteries. So which battery?

On Earth, the answer is obvious. Lithium-ion. Energy density, charge/discharge efficiency, lightweight -- best on every metric. But for the same reason turbines beat solar panels in a previous article, **the criteria are different in space.**

Lithium-ion needs replacement every 10 years, and the nearest lithium mine is on Earth. On asteroids, iron and nickel are literally everywhere underfoot.

---

## Earth Criteria vs Space Criteria

| Parameter | Iron-Nickel (Edison) | Lithium-Ion | What matters in space |
|-----------|---------------------|-------------|----------------------|
| Volumetric energy density | 30-60 Wh/L | 250-700 Wh/L | At 1 km² scale, volume is irrelevant |
| Gravimetric energy density | 30-50 Wh/kg | 150-270 Wh/kg | Stationary structure -- doesn't matter |
| Lifespan | **30-50 years** | 5-15 years | Replacement cost in space is **astronomical** |
| Overcharge tolerance | **Extremely high** | Poor (thermal runaway/fire) | Fire in vacuum = total module loss |
| Over-discharge tolerance | **High** | Irreversible damage | Full discharge possible during eclipse |
| Local material sourcing | **Possible** (Fe, Ni, KOH) | **Impossible** (Li, Co, organic electrolyte) | Existence of the self-replication loop |
| Electrolyte | Potassium hydroxide aqueous solution (water-based) | Organic solvent (flammable) | Radiation stability, fire safety |
| Self-discharge | High (~1%/day) | Low (~0.1%/day) | Irrelevant in always-charging environment |

**What matters on Earth: light, compact, high energy density.**
**What matters in space: can be made locally, doesn't kill you, lasts long.**

When the criteria change, the answer changes.

---

## Materials -- There Is No Lithium on Asteroids

To build a lithium-ion battery:

| Material | Purpose | Asteroid availability |
|----------|---------|----------------------|
| Lithium (Li) | Cathode active material | **None** -- Big Bang nucleosynthesis element, trace amounts in rocky asteroids |
| Cobalt (Co) | Cathode stabilizer | Trace amounts -- economically unextractable |
| Graphite (C) | Anode | Present in carbonaceous asteroids but not crystalline graphite |
| Organic electrolyte | Ion conduction | **Synthesis required** -- complex organic chemistry like ethylene carbonate |
| Separator (PE/PP) | Short-circuit prevention | **Synthesis required** -- precision polymer manufacturing |

There is no lithium. Game over right there. If you need continuous resupply from Earth, **that's not self-replication -- that's supply-line dependency.**

"What about sodium-ion?" Na exists on asteroids. But 30-50 year lifespan is unproven, it has no battolyser capability, and it requires organic electrolyte. The problem of space radiation degrading organic electrolyte is identical for sodium-ion.

"Aren't solid-state batteries coming soon?" If you can't make them on an asteroid, it doesn't matter how good they are. The key is not energy density but **local manufacturability.**

To build an iron-nickel battery:

| Material | Purpose | Source |
|----------|---------|--------|
| Iron (Fe) | Anode | Main component of 1986 DA -- **literally everywhere** |
| Nickel (Ni) | Cathode | Main component of 1986 DA -- **literally everywhere** |
| Potassium hydroxide (KOH) | Electrolyte | K found in asteroid silicates, water extracted from carbonaceous asteroids |
| Steel plate | Casing | Fe-Ni alloy fabrication |

**Every component of the battery is a byproduct of the smelting process.** You can make batteries while building mirror frames. Zero additional raw material imports.

---

## Lifespan -- Replacement Cost Decides Everything

On Earth, lithium-ion's 10-15 year lifespan is sufficient. Replacement cost is just the battery price.

In space, replacement cost includes:
1. Manufacturing new batteries (if you can make them)
2. Transport (if you can't -- from Earth at **thousands of dollars per kg**)
3. EVA or robotic replacement work
4. System downtime during replacement

**Iron-nickel battery lifespan: 30-50 years.** There are **documented cases** of iron-nickel cells Edison built in 1901 that **still work today**. Just top off the electrolyte (KOH aqueous solution) every 10-15 years, and the electrodes are virtually permanent.

The only battery chemistry that enables **zero replacements** within a module's design life.

---

## Safety -- Fire in Vacuum Means Death

The organic electrolyte in lithium-ion batteries is flammable. On overcharge, physical damage, or internal short:

```
Internal temperature rise -> separator shrinkage -> short-circuit expansion -> electrolyte decomposition
-> flammable gas release -> ignition -> cascading thermal runaway to adjacent cells
```

Earth: fire trucks arrive.
Space: **there are no fire trucks in vacuum.** Fire in a sealed module = life support loss + toxic gas filling + no rescue.

Even on the ISS, lithium-ion fire is one of the most feared scenarios. Install lithium-ion across thousands of Dyson modules, and **fire becomes a statistical certainty.**

Intrinsic safety of iron-nickel:

- Electrolyte: potassium hydroxide **aqueous solution** -- water-based. It does not burn
- On overcharge: water electrolyzes into H₂ + O₂ -- not thermal runaway
- On over-discharge: no irreversible electrode damage -- recoverable by recharging
- On physical damage: KOH leaks -- corrosive but **no explosion or fire**

**"A battery that doesn't catch fire" is not a luxury in space -- it's a necessity.**

---

## Battolyser -- A Battery That Also Does Electrolysis

This is where iron-nickel goes beyond being a mere "second choice" to having a **unique advantage.**

### Principle

The Battolyser concept developed by TU Delft. It actively exploits iron-nickel batteries' overcharge tolerance:

```
[Charging]        Electrical energy -> stored as chemical energy in Fe/Ni electrodes
[After full charge] Additional current -> electrolyzes water in KOH aqueous solution
                    Cathode: 2H₂O + 2e⁻ -> H₂↑ + 2OH⁻
                    Anode: 2OH⁻ -> ½O₂↑ + H₂O + 2e⁻
```

**One device serves as both battery + electrolyzer.** No separate electrolysis equipment needed. Mass, volume, and complexity savings.

In lithium-ion, overcharge = fire. In iron-nickel, overcharge = **hydrogen production.**

### Operational Cycle in a Dyson Module

```
[Normal operation] Turbine running at 370 MW
  |-> Load consumption (~320 MW)
  |-> Surplus power (~50 MW) -> Battolyser mode
       |-> H₂ ~890 kg/h + O₂ ~7,100 kg/h accumulation (assuming ~70% electrolysis efficiency)

[Eclipse] 3-12 hours/year
  |-> Battery discharge (ESS mode)
  |-> Stored H₂ -> fuel cell generation (parallel)
       -> 2x+ available energy vs battery alone

[Emergency shutdown]
  |-> H₂/O₂ dual storage -> extended life support
```

### Beyond Energy Storage

The H₂ and O₂ produced by the battolyser go beyond simple energy storage to integrate into the **entire module's material cycle:**

| Output | Application | Notes |
|--------|-------------|-------|
| H₂ | NTP tug propellant replenishment | Working fluid for nuclear thermal propulsion |
| H₂ | Smelting process reducing agent | Metal oxide -> pure metal (FeO + H₂ -> Fe + H₂O) |
| H₂ | Fuel cell emergency power | Backup power during eclipse/maintenance |
| H₂ | Haber-Bosch -> NH₃ -> fertilizer | Habitat module agriculture |
| O₂ | Life support (breathing) | Essential for habitat modules |
| O₂ | Oxidizer (welding, medical) | Local manufacturing processes |

A battery that stores energy while simultaneously producing propellant, reducing agent, and breathable oxygen. Lithium-ion only stores electricity.

---

## "Isn't 1/10 the Energy Density Way Too Bulky?"

Yes. To store the same energy, iron-nickel needs **5-10x the volume** of lithium-ion.

But:

```
Dyson module scale:
  Mirror: 1 km x 1 km = 1,000,000 m²
  Structure: extends several km behind the mirror
  Total volume: millions of m³

Required ESS capacity (12 hours x 370 MW):
  4,440 MWh = 4,440,000 kWh

Iron-nickel (at 40 Wh/L):
  111,000 m³ = 111 m x 111 m x 9 m

-> Less than 1% of total structure
```

In the millions of m³ of structure behind a 1 km² mirror, 111,000 m³ is **one small corner.** Moreover, the heavy mass of iron-nickel can serve as a **counterweight for rotating structures.** The disadvantage flips into an advantage.

The high self-discharge rate of ~1% per day is only a problem on the ground. With turbines running 24/7/365, the battery is always charging. Self-discharge is **meaningless.**

"Can't you just increase turbine output and skip ESS?" Eclipse and emergency shutdowns are situations where turbines **stop entirely.** Generation and storage are separate problems.

---

## Space Environment Adaptation Design

You cannot simply bring a terrestrial iron-nickel battery to space. Three adaptations are needed.

### 1. Electrolyte Evaporation Prevention

KOH aqueous solution loses water through evaporation in vacuum. **Sealed cell structure** is mandatory. Fortunately, battery cells are designed to be sealed by default. For space use, only the sealing level needs reinforcement.

### 2. Zero-Gravity Gas Separation

In battolyser mode, H₂/O₂ bubbles cling to electrode surfaces. On Earth, buoyancy lifts bubbles away, but in zero gravity this doesn't work.

**Solution:** Hydrophobic coating on electrode surfaces + centrifugal force from module rotation for gas separation. A centrifugal acceleration of just ~0.01G is sufficient for bubble separation.

### 3. Radiation Tolerance

KOH aqueous solution is **extremely stable against radiation** unlike organic electrolytes. Organic electrolytes degrade as radiation breaks molecular chains. Aqueous solution experiences minor water radiolysis from radiation, but natural recombination restores it. In a radiation environment, iron-nickel is **inherently superior** to lithium-ion.

---

## One-Line Summary

Lithium-ion is Earth's best battery. But there is no lithium on asteroids, you can't swap batteries every 10 years in space, and you can't extinguish fires in vacuum. Iron-nickel batteries can be made from asteroid smelting byproducts, last 30-50 years without replacement, don't catch fire, and after full charge transform into an electrolyzer that produces propellant and breathable oxygen. The 1/10 energy density is meaningless at the 1 km² scale.

For terrestrial applications of iron-nickel batteries, see [Iron-Nickel Batteries as Off-Grid ESS](https://www.parkjunwoo.com/1/tech/iron-nickel-ess-rural-energy/).

![Nickel-iron batteries developed by Edison in 1901. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0](/images/why-iron-nickel-battery.webp)
