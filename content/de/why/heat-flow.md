---
title: "Warum man Wärme nicht durch Rohre leiten kann"
date: 2026-02-24T12:00:08+09:00
lastmod: 2026-02-24T12:00:08+09:00
tags: ["wärmemanagement", "radiator", "wärme-kaskade"]
summary: "Kein Fluid übersteht 1.600 °C im geschlossenen Kreislauf. Jede Anlage erhält ihren eigenen Spiegel, gibt Abwärme bei der höchstmöglichen Temperatur ab und nur der Rest unter 100 °C erreicht das Habitat."
image: "/images/post008.webp"
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Hausaufgabe aus dem letzten Artikel

Der vorherige Artikel argumentierte, dass Turbinen der Photovoltaik bei der Selbstreplikation überlegen sind. Wirkungsgrad 30 %, elektrische Leistung 370 MW, die verbleibenden 855 MW sind Wärme.

Dort stand:

> „Dieselben 70 % durchlaufen nacheinander Schmelze, Fabrik, Habitat und Rechenzentrum — alles wird genutzt."

Konzeptionell korrekt. Die Abwärme der Turbine ist weit nützlicher als die 60 °C-Abwärme der Photovoltaik. **Aber „sequenzieller Durchlauf" ist kein realer Entwurf.** Dieser Artikel verfolgt den tatsächlichen Wärmefluss.

---

## Zunächst eine Korrektur: Warum der „sequenzielle Durchlauf" nicht funktioniert

### Problem 1: Temperatur der Turbinenabwärme

Thermodynamik der Turbine (Brayton-Kreisprozess):
- Heißseite: ~1.200 °C (Arbeitsmedium durch konzentriertes Sonnenlicht erhitzt)
- Kaltseite: ~227 °C (hier wird Wärme abgegeben)
- Wirkungsgrad 30 % → 370 MW Strom, **855 MW bei ~227 °C abgegeben**

Kernpunkt: **Die gesamte Turbinenabwärme liegt bei ~227 °C.** Schmelzen erfordert 1.600 °C. Ein 1.600 °C-Prozess lässt sich nicht mit 227 °C-Wärme betreiben — zweiter Hauptsatz der Thermodynamik. Wärme fließt nur von heiß nach kalt.

Der Pfeil „800–1.000 °C → Schmelze" im vorherigen Diagramm war keine Turbinenabwärme. Die Wärme für die Schmelze kommt **direkt vom Spiegel**.

### Problem 2: Kein Medium für 1.000 °C

Selbst wenn irgendwo 1.600 °C-Wärme existierte — ließe sie sich durch Rohre transportieren?

| Wärmeträger | Max. Betriebstemp. | Grenze |
|---|---|---|
| Druckwasser | ~340 °C | Kritischer Punkt |
| Flüssigsalz | ~565 °C | Zersetzung |
| Flüssiges Natrium | ~800 °C | Dampfdruck |
| Hochdruck-Helium | ~950 °C | Rohrmaterial-Grenze |
| **Über 1.000 °C** | **Entfällt** | **Kein Medium vorhanden** |

Kein Fluid kann Wärme bei 1.600 °C transportieren. Die einzige Methode, Energie bei dieser Temperatur zu übertragen, ist **Licht.** Direkte Bestrahlung durch Spiegel.

### Problem 3: Entfernung zwischen Modulen

In einem spezialisierten Cluster liegen Schmelzmodule und Rechenzentren **50–100 km auseinander.** Absichtliche Trennung gegen Vibrationen, Kontamination und thermische Wechselwirkung. Auf diese Distanz sind Wärmeleitungen unrealistisch.

**Fazit: Turbinenabwärme zu Hochtemperaturprozessen zu leiten ist physikalisch unmöglich.**

---

## Der reale Entwurf: Jede Anlage bekommt ihren eigenen Spiegel

Die wahren Prinzipien des Wärmeflusses:

1. **Die Eingangswärme wird direkt vom eigenen Spiegel jedes Moduls empfangen** — als Licht übertragen, kein Medium nötig
2. **Die Kaskade funktioniert nur innerhalb jedes Moduls** — Prozessabwärme wird bei stufenweise sinkenden Temperaturen wiederverwendet
3. **Kein Wärmeaustausch zwischen Modulen** — Einschränkungen durch Distanz und Medium
4. **Nur Abwärme unter 100 °C wird dem Habitat zugeführt** — Rohrleitungen sind machbar, Temperatur passt zum Bedarf

### Spiegelzuteilung (Cluster mit 10 Modulen)

| Modultyp | Anz. | Spiegelaufteilung (Wärme : Strom) | Hochtemp.-Quelle |
|---|---|---|---|
| Schmelzmodul | 3 | 90 : 10 | Spiegel → direkt 1.600 °C |
| Barrenmodul | 1 | 70 : 30 | Spiegel → direkt 1.400 °C |
| Strukturmodul | 2 | 60 : 40 | Spiegel → direkt 800–1.200 °C |
| Fab-Modul | 1 | 20 : 80 | Spiegel → direkt 900 °C |
| Rechenzentrum | 2 | 5 : 95 | Spiegel → Turbine → Strom |
| Habitat / Logistik | 1 | 30 : 70 | Spiegel → Turbine → Strom |

**Über 1.000 °C liefert Licht die Wärme direkt.** Turbinen laufen nur in Modulen, die hauptsächlich Strom brauchen (Rechenzentren, Habitate).

---

## Radiator-Physik: Das T⁴-Gesetz

Die einzige Möglichkeit, Wärme im Weltraum abzuführen, ist **Infrarotstrahlung.** Keine Konvektion, keine Wärmeleitung.

Stefan-Boltzmann-Gesetz:

**Abstrahlleistung = ε × σ × A × T⁴**

(ε: Emissionsgrad, σ: Stefan-Boltzmann-Konstante, A: Fläche, T: absolute Temperatur)

Der Schlüssel ist **T⁴**. Doppelte Temperatur ergibt 16-fache Abstrahlleistung. Umgekehrt schrumpft die benötigte Fläche für dieselbe Wärmelast auf 1/16.

| Radiator-Temp. | Fläche pro MW | Vergleich |
|---|---|---|
| 800 °C (1.073 K) | **8 m²** | Ein Parkplatz |
| 400 °C (673 K) | **50 m²** | Eine Wohnung |
| 227 °C (500 K) | **166 m²** | Ein Tennisplatz |
| 100 °C (373 K) | **535 m²** | Drei Basketballfelder |
| 60 °C (333 K) | **844 m²** | 1/8 eines Fußballfeldes |

(Beidseitige Abstrahlung, Emissionsgrad ε = 0,85, unbeschichtetes Fe-Ni-Blech)

**Lektion: Wärme, die bei 800 °C 8 m² braucht, benötigt bei 60 °C 844 m². Über 100× mehr.**

Daher das Kernprinzip des Wärmemanagements: **„Nicht nutzbare Wärme bei der höchstmöglichen Temperatur sofort abstrahlen."**

### Radiator-Material

Die Radiatoren sind Teil der Selbstreplikationsschleife:
- **Material:** Dünnes Fe-Ni-Blech aus Asteroidenressourcen
- **Oberfläche:** Keine Aluminiumbeschichtung (Gegenteil des Spiegels) — unbeschichtetes Fe-Ni hat einen hohen Infrarot-Emissionsgrad, ideal für Abstrahlung
- **Fertigung:** Dieselbe Blechlinie wie die Spiegelrahmen. Nur der Beschichtungsschritt entfällt
- **Zusätzliche Ressourcen:** Null. Gleiches Material, gleicher Prozess, anderes Produkt

---

## Wärmefluss nach Anlage

### Schmelzmodul — Wärme als Hauptakteur (90 % Wärme, 10 % Strom)

Das Schmelzmodul empfängt 90 % seiner Spiegelenergie als direkte Wärme. Eine kleine Turbine (10 %) erzeugt Strom für Motoren und Roboter.

```
☀️ Eigener Spiegel (90 % → direkte Bestrahlung, 10 % → kleine Turbine)
 │
 ▼
Schmelzofen (1.600 °C) ← Direkt durch Spiegellicht erhitzt, kein Medium
 │
 │ Abwärme ~800 °C ← Ab hier kann ein Medium (He / Flüssigmetall) transportieren
 ├→ Legierungs-Wärmebehandlung, Glühen (nutzt 800 °C)
 ├→ Überschuss → ★ Radiator A (800 °C) — 8 m²/MW, kompakt
 │
 │ Abwärme ~400 °C
 ├→ Vorwärmung, Hilfsheizung (nutzt 400 °C)
 ├→ Überschuss → ★ Radiator B (400 °C) — 50 m²/MW, mittel
 │
 │ Abwärme ~200 °C
 ├→ ★ Radiator C (200 °C) — Großteil wird hier abgeführt
 │
 │ Rest < 100 °C
 └→ Kann per Rohrleitung zum Habitat geleitet werden

Abwärme der kleinen Turbine (~227 °C) → ★ Radiator D
```

Das Schmelzmodul nutzt Wärme von oben nach unten und **strahlt den Überschuss auf jeder Stufe ab.** Hochtemperatur-Radiatoren sind klein, der Aufwand gering. Nur der Rest unter 100 °C geht ans Habitat.

### Rechenzentrum-Modul — Strom als Hauptakteur (5 % Wärme, 95 % Strom)

Das Rechenzentrum ist das am schwersten zu kühlende Modul. 95 % der Spiegelenergie durchlaufen Turbine → Strom → Chips → Wärme, alles bei ~60 °C.

```
☀️ Eigener Spiegel (95 % → große Turbine, 5 % → Hilfswärme)
 │
 ▼
Große Turbine → ~370 MW-Klasse Strom
 │
 │ Turbinenabwärme ~227 °C (~855 MW)
 └→ ★ Radiator A (227 °C) — 166 m²/MW
     Großteil der Turbinenabwärme wird hier abgeführt

Chip-Betrieb → gesamter Strom wird zu Wärme
 │
 │ Chip-Abwärme ~60 °C
 │  Direkte Abstrahlung bei 60 °C: 844 m²/MW → 111 MW brauchen ~94.000 m²
 │
 ├→ [Wärmepumpe] 60 °C → 200 °C (COP ~3, Leistung ~37 MW)
 │   └→ ★ Radiator B (200 °C) — Fläche auf ~1/4 reduziert
 │
 └→ Rest < 100 °C → kann dem Habitat zugeführt werden
```

**Die Wärmepumpe ist die Schlüsseltechnologie.** Wärme von 60 °C auf 200 °C zu heben, reduziert die Radiatorfläche drastisch. Die Pumpenleistung (~37 MW) kommt aus der Turbine selbst. Sowohl Turbine als auch Wärmepumpe können vor Ort aus Fe-Ni + Ti gefertigt werden.

### Strukturmodul (60 % Wärme, 40 % Strom)

```
☀️ Eigener Spiegel (60 % → direkte Erwärmung, 40 % → Turbine)
 │
 ▼
Schweißen / Wärmebehandlung (800–1.200 °C) ← Direkte Spiegelerwärmung
 │ Abwärme ~400 °C
 ├→ Vorwärmung zum Formen / Biegen (nutzt 400 °C)
 ├→ Überschuss → ★ Radiator (400 °C)
 │ Abwärme ~200 °C
 ├→ ★ Radiator (200 °C)
 │ Rest < 100 °C
 └→ Kann dem Habitat zugeführt werden

Turbine (40 %) → Strom (Roboter, CNC, Schweißgeräte)
 └→ Turbinenabwärme → ★ Radiator (227 °C)
```

### Habitat- / Logistikmodul — Verbraucher von Abwärme unter 100 °C

Das Habitat ist die letzte Wärmesenke. Seine eigene Turbine erzeugt Strom für Lebenserhaltung, Beleuchtung und Landwirtschaft, während es **Abwärme unter 100 °C von benachbarten Modulen empfängt.**

```
☀️ Eigener Spiegel (30 % → Wärme, 70 % → Turbine)
 │
 ├→ Turbine → Strom (Lebenserhaltung, Beleuchtung, Agrar-LEDs)
 │   Abwärme (~227 °C) → ★ Radiator
 │
 └→ Wärme → Warmwasser, Zusatzheizung
     └→ Rest → ★ Radiator

Abwärme <100 °C von Nachbarmodulen (Schmelze, Struktur)
 │
 └→ Habitat-Heizung, Warmwasser, Bodenerwärmung für Landwirtschaft
     └→ Rest → Abstrahlung über die Außenhülle des Habitats (die Struktur selbst dient als Radiator)
```

Der Wärmebedarf des Habitats (Heizung, Warmwasser) ist bescheiden im Vergleich zu den industriellen Abwärmemengen. Der Rest unter 100 °C aus Nachbarmodulen reicht mehr als aus. **Das Habitat erhält kostenlose Heizung — die Industriemodule erzeugen nicht Wärme für das Habitat.**

---

## Verteilte Abstrahlung: Das Gesamtbild

Zusammenfassung des Wärmeflusses im gesamten Cluster:

```
☀️ Sonnenlicht → Spiegel → Direkt an jedes Modul verteilt
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
[Schmelze]     [Struktur]      [Rechenzentrum]
 Spiegel→1.600°C Spiegel→1.200°C Spiegel→Turbine→Strom
    │               │               │
    ▼               ▼               ▼
 ★Rad.(800°C)   ★Rad.(400°C)   ★Rad.(227°C) ← Turbinenabwärme
 ★Rad.(400°C)   ★Rad.(200°C)   ★Rad.(200°C) ← nach Wärmepumpe
 ★Rad.(200°C)       │               │
    │               ▼               ▼
    └──── <100°C ──→ [Habitat] ←── <100°C
                      Heizung & Warmwasser
                         │
                    ★Rad.(Hülle, ~30°C)
```

**Kein „sequenzieller Durchlauf", sondern „parallele Verteilung + individuelle Abstrahlung + nur Niedertemperatur wird geteilt".** Jedes Modul empfängt Wärme von seinem eigenen Spiegel, strahlt sie über eigene Radiatoren ab und gibt nur den Rest ans Habitat weiter.

### Warum das besser ist

1. **Hochtemperatur-Radiatoren sind winzig** — 8 m² zum Abführen von 1 MW bei 800 °C. Eine kleine Rippe neben dem Prozess genügt
2. **Keine Rohrleitungen zwischen Modulen** — der Albtraum von 50 km Hochtemperaturrohren entfällt
3. **Jedes Modul ist thermisch unabhängig** — Wartung an einem Modul beeinflusst die anderen nicht
4. **Das Habitat bleibt sicher** — keine 1.600 °C-Rohre durch Wohnbereiche

---

## Korrektur zum vorherigen Artikel: Wohin gehen die 70 % tatsächlich?

Der vorherige Artikel sagte: „PV verschwendet 70 %, Turbinen nutzen sie." Stimmt das noch?

**Ja.** Aber der Mechanismus ist anders:

| | PV | Turbinensystem |
|---|---|---|
| 30 % | Strom | Strom |
| Verbleibende 70 % | 60–80 °C Niedertemperatur-Abwärme → **nicht nutzbar** | Als direkte Spiegelerwärmung an jeden Prozess verteilt → **genutzt für Schmelzen, Formen, Wärmebehandlung** |
| Abstrahlungslast | Gesamte 70 % bei niedriger Temperatur abgestrahlt (riesiger Radiator) | Stufenweise Abstrahlung bei hoher Temperatur (kleine verteilte Radiatoren) |

Die 70 % der PV liegen komplett bei 60–80 °C — die schlechteste Temperatur sowohl für Industrie als auch für Abstrahlung. Im Turbinensystem werden diese 70 % über Spiegel bei der exakt benötigten Temperatur an jeden Prozess geliefert, und die Abwärme wird bei der höchstmöglichen Temperatur abgestrahlt.

**Was „die verbleibenden 70 % nutzen" wirklich bedeutet: nicht Turbinenabwärme, sondern Wärmeenergie des Spiegels, die von jedem Prozess direkt verbraucht wird.**

---

## Zusammenfassung in einem Satz

Kein Medium kann 1.600 °C transportieren. Daher empfängt jede Anlage ihren eigenen Spiegel. Wärme kaskadiert innerhalb jedes Prozesses, und der Überschuss wird bei der höchsten erreichbaren Temperatur sofort abgestrahlt. Nur der Rest unter 100 °C erreicht das Habitat. Die Radiatorplatten bestehen aus demselben Fe-Ni-Blech wie die Spiegelrahmen — einfach die Beschichtung weglassen, und man hat einen Radiator.
