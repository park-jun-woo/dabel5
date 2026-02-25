---
title: "Why Wireless Power Transmission Is Impractical"
date: 2026-02-24T12:00:06+09:00
lastmod: 2026-02-24T12:00:06+09:00
tags: ["power-transmission", "wireless-power", "local-consumption"]
summary: "The standard Dyson swarm collects energy where nothing lives and must beam it to where people are — losing 75-90% in transmission. At L5, you put the factories next to the mirrors and plug them in."
image: "/images/power-transmission-local.webp"
author: "PARK JUN WOO"
imageCaption: "Arecibo radio telescope (305 m diameter). Receiving wireless laser power transmission would require a receiver of this scale. Photo: Mariordo / Wikimedia Commons / CC BY-SA 4.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## Collecting Is Easy — But Where Do You Use It?

Standard Dyson swarm scenario: disassemble Mercury, place mirrors/panels near the Sun. Energy collection — solved. But **where do you consume that energy?** There is nothing near the Sun.

If you have to send it to Earth — let's check the physics of wireless power transmission (WPT).

---

## Microwave Beam: The Diffraction Limit

Frequency 2.45 GHz (λ = 0.122 m), Mercury orbit → Earth (average ~1 AU = 1.5×10¹¹ m):

**Spot diameter ≈ 2.44 × λ × distance / transmit antenna diameter**

| Transmit Antenna Diameter | Spot Diameter at Earth | Feasibility |
|---|---|---|
| 1 km | 44,600 km | 3.5× Earth's diameter |
| 10 km | 4,460 km | Earth-radius scale |
| 100 km | 446 km | Korean-peninsula-sized rectenna |

Working backwards — to receive with a 10 km rectenna on Earth:

```
Required transmit antenna = 2.44 × 0.122 × 1.5×10¹¹ / 10,000
                          = 4,460 km diameter
```

**Mercury's diameter is 4,880 km. You need an antenna the size of Mercury.**

---

## What About Lasers?

With λ = 1 μm, the diffraction problem is greatly reduced:

| Transmit Mirror Diameter | Spot Diameter at Earth |
|---|---|
| 10 m | 36.6 km |
| 100 m | 3.7 km |

The spot size is realistic. **But the conversion efficiency chain is fatal:**

| Stage | Efficiency |
|---|---|
| Electricity → Laser | ~40–50% |
| Atmospheric transmission (weather-dependent) | ~50–80% |
| PV receiver → Electricity | ~50–60% |
| **End-to-end** | **~10–24%** |

You throw away 75–90% of the generated electricity during transmission. The 6.6× flux advantage is more than cancelled out here.

---

## Additional Problem at Mercury's Orbit: Solar Occultation

Mercury's orbital period is 88 days. For a significant portion of the orbit, **the Sun sits between Mercury and Earth** — making beam transmission physically impossible for those intervals. Without relay satellites, continuous transmission is not achievable.

---

## L5: Produce Locally, Consume Locally

At L5, the transmission problem simply does not exist.

| | Mercury → Earth Transmission | L5 Local Consumption |
|---|---|---|
| Transmission distance | 0.5–1.5 AU | **A few km to tens of km** |
| Transmission method | Microwave/Laser (wireless) | **Wired cable** |
| End-to-end efficiency | 10–24% (laser) | **~95%+** |
| Solar occultation | Yes (88-day cycle) | **None** |
| Receiving infrastructure | Thousands-of-km rectenna or Mercury-sized antenna | **Not needed** |
| Consumer | Earth (150 million km away) | **Adjacent O'Neill cylinders + data centers** |

Note: In the vacuum of space, superconducting cables get cooling essentially for free. The cosmic microwave background at 2.7 K serves as the coolant.

---

## The Real Question: Is There Any Reason to Send Electricity to Earth?

If L5 has industrial facilities, habitats, and data centers:

- **Computation results** (AI inference, simulations) are transmitted via optical communication — bits are light
- **Manufactured goods** are shipped physically
- **There is no need to send electricity itself to Earth**

You don't transmit energy — **you transmit the products of energy.** This is the core of the L5 local consumption model.

---

## One-Line Summary

The standard Dyson swarm concept has a fundamental contradiction: "collect energy where nobody lives, then send it to where people are." At L5, you place the factories and habitats next to the mirrors and plug them in.
