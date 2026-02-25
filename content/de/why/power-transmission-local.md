---
title: "Warum drahtlose Energieübertragung unpraktisch ist"
date: 2026-02-24T12:00:06+09:00
lastmod: 2026-02-24T12:00:06+09:00
tags: ["energieübertragung", "drahtlose-energie", "lokalverbrauch"]
summary: "Der Standard-Dyson-Schwarm sammelt Energie, wo niemand lebt, und muss sie dorthin übertragen, wo Menschen sind — mit 75-90 % Übertragungsverlust. Bei L5 stellt man die Fabriken neben die Spiegel und steckt den Stecker ein."
image: "/images/power-transmission-local.webp"
author: "PARK JUN WOO"
imageCaption: "Arecibo-Radioteleskop (305 m Durchmesser). Der Empfang drahtloser Laser-Energieübertragung würde einen Empfänger dieser Größenordnung erfordern. Foto: Mariordo / Wikimedia Commons / CC BY-SA 4.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## Sammeln ist einfach — aber wo wird die Energie genutzt?

Standard-Szenario des Dyson-Schwarms: Merkur zerlegen, Spiegel/Panels in Sonnennähe platzieren. Energiesammlung — gelöst. Aber **wo wird diese Energie verbraucht?** In Sonnennähe gibt es nichts.

Wenn man sie zur Erde senden muss — prüfen wir die Physik der drahtlosen Energieübertragung (WPT).

---

## Mikrowellenstrahl: die Beugungsgrenze

Frequenz 2,45 GHz (λ = 0,122 m), Merkur-Umlaufbahn → Erde (durchschnittlich ~1 AU = 1,5×10¹¹ m):

**Spot-Durchmesser ≈ 2,44 × λ × Entfernung / Sendeantennendurchmesser**

| Sendeantennendurchmesser | Spot-Durchmesser auf der Erde | Realisierbarkeit |
|---|---|---|
| 1 km | 44.600 km | 3,5× Erddurchmesser |
| 10 km | 4.460 km | Erdradius-Größenordnung |
| 100 km | 446 km | Rectenna in der Größe der koreanischen Halbinsel |

Umgekehrt — um mit einer 10-km-Rectenna auf der Erde zu empfangen:

```
Erforderliche Sendeantenne = 2,44 × 0,122 × 1,5×10¹¹ / 10.000
                           = 4.460 km Durchmesser
```

**Merkurs Durchmesser beträgt 4.880 km. Man braucht eine Antenne so groß wie Merkur.**

---

## Und mit Laser?

Bei λ = 1 μm wird das Beugungsproblem erheblich reduziert:

| Sendespiegel-Durchmesser | Spot-Durchmesser auf der Erde |
|---|---|
| 10 m | 36,6 km |
| 100 m | 3,7 km |

Die Spot-Größe ist realistisch. **Aber die Konversionseffizienzkette ist fatal:**

| Stufe | Effizienz |
|---|---|
| Elektrizität → Laser | ~40–50 % |
| Atmosphärische Transmission (wetterabhängig) | ~50–80 % |
| PV-Empfänger → Elektrizität | ~50–60 % |
| **Gesamt** | **~10–24 %** |

75–90 % der erzeugten Elektrizität gehen bei der Übertragung verloren. Der 6,6-fache Flussvorteil wird hier mehr als aufgehoben.

---

## Zusätzliches Problem in der Merkur-Umlaufbahn: Sonnenverdeckung

Merkurs Umlaufzeit beträgt 88 Tage. Während eines erheblichen Teils der Umlaufbahn **steht die Sonne zwischen Merkur und der Erde** — was die Strahlübertragung in diesen Abschnitten physisch unmöglich macht. Ohne Relaissatelliten ist eine kontinuierliche Übertragung nicht realisierbar.

---

## L5: Lokale Produktion, lokaler Verbrauch

Bei L5 existiert das Übertragungsproblem schlicht nicht.

| | Übertragung Merkur → Erde | Lokaler Verbrauch bei L5 |
|---|---|---|
| Übertragungsentfernung | 0,5–1,5 AU | **Einige km bis Dutzende km** |
| Übertragungsmethode | Mikrowelle/Laser (drahtlos) | **Kabelgebunden** |
| Gesamteffizienz | 10–24 % (Laser) | **~95 %+** |
| Sonnenverdeckung | Ja (88-Tage-Zyklus) | **Nein** |
| Empfangsinfrastruktur | Tausende km Rectenna oder Merkur-große Antenne | **Nicht erforderlich** |
| Verbraucher | Erde (150 Millionen km entfernt) | **Benachbarte O'Neill-Zylinder + Rechenzentren** |

Hinweis: Im Weltraumvakuum ist die Kühlung supraleitender Kabel praktisch kostenlos. Die kosmische Hintergrundstrahlung bei 2,7 K dient als Kühlmittel.

---

## Die eigentliche Frage: Gibt es einen Grund, Elektrizität zur Erde zu senden?

Wenn L5 über Industrieanlagen, Habitate und Rechenzentren verfügt:

- **Berechnungsergebnisse** (KI-Inferenz, Simulationen) werden per optischer Kommunikation übertragen — Bits sind leicht
- **Fertigprodukte** werden physisch transportiert
- **Es besteht keine Notwendigkeit, Elektrizität selbst zur Erde zu senden**

Man überträgt nicht Energie — **man überträgt die Erzeugnisse der Energie.** Das ist der Kern des lokalen Verbrauchsmodells bei L5.

---

## Zusammenfassung in einem Satz

Das Standard-Konzept des Dyson-Schwarms hat einen grundlegenden Widerspruch: „Energie dort sammeln, wo niemand lebt, und sie dorthin senden, wo Menschen sind." Bei L5 stellt man die Fabriken und Habitate neben die Spiegel und steckt den Stecker ein.
