---
title: "Warum L5, nicht nahe der Sonne"
date: 2026-02-24T12:00:05+09:00
lastmod: 2026-02-24T12:00:05+09:00
tags: ["dyson-schwarm", "SEL5", "selbstreplikation", "skalierung"]
image: "/images/post005.webp"
summary: "Das Standardszenario für einen Dyson-Schwarm setzt den Abbau von Merkur nahe der Sonne voraus. Doch was, wenn man Asteroidenressourcen nutzt und am Sonne-Erde-Punkt L5 baut? Hier sind die Berechnungen."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Die gängige Annahme hinterfragen

Das Standardszenario, das jedem bei einem Dyson-Schwarm einfällt: Merkur zerlegen und Paneele/Spiegel nahe der Sonne platzieren. Das ist der von der Isaac-Arthur-Serie etablierte Rahmen, und die meisten akzeptieren es als selbstverständlich.

Aber ich habe einen anderen Ansatz durchgerechnet — was, wenn man Asteroidenressourcen nutzt und am Sonne-Erde-Punkt L5 baut?

---

## Warum L5?

### Solare Flussdichte
- L5 (1 AU): ~1.361 W/m² — identisch mit der Erdumlaufbahn
- Merkur-Umlaufbahn (0,39 AU): ~8.942 W/m² — etwa 6,6-mal stärker
- „Ist Merkur nicht besser?" — Ja, pro Flächeneinheit. Aber das ist nicht alles

### Versteckte Vorteile von L5
1. **Gravitationsstabiler Punkt** — Bahnhaltungskosten nahezu null. In der Nähe von Merkur ist der solare Gravitationsgradient steil, was kontinuierliche Bahnkorrekturen erfordert
2. **Ununterbrochenes Sonnenlicht rund um die Uhr, 365 Tage im Jahr** — Der Erdschatten kann ihn nicht erreichen (150 Millionen km). Keine Finsternisse
3. **Stabiler Bereich über Millionen von km** — Hunderttausende Module können ohne gegenseitige Störung platziert werden
4. **Fester Abstand zur Erde** — Vereinfacht die Logistikplanung. Die Kommunikationsverzögerung beträgt ~8 min 20 s pro Richtung (nicht in Echtzeit, aber durch autonome KI-Operationen lösbar)
5. **Bewohnbar** — In der Nähe von Merkur ist die thermische Umgebung extrem. L5 macht die Gestaltung menschlicher Habitate deutlich realistischer

---

## Ressourcen: Merkur-Zerlegung vs Asteroiden

### Versteckte Kosten des Merkur-Ansatzes
- Fluchtgeschwindigkeit von Merkur: 4,25 km/s — ein erheblicher Gravitationsschacht
- Oberflächentemperatur von Merkur: 430 °C tagsüber — extremes Wärmemanagement für Bergbauausrüstung
- Merkur → Einsatz in Sonnenumlaufbahn: zusätzliches Delta-V erforderlich
- **Das größte Problem: Merkur ist ein Planet** — Großflächiger Bergbau bei 0,38g Oberflächengravitation ist im Grunde eine Variante des irdischen Bergbaus

### Asteroiden-Ansatz (1986 DA)
- Metallischer M-Typ-Asteroid: **90%+ Fe-Ni-Legierung** — nahezu reines Metall
- Geschätzte Ressourcen: 20+ Milliarden Tonnen (Durchmesser ~2,3 km, Schüttdichte eines M-Typ-Asteroiden)
- Mikrogravitation → minimaler Energieaufwand für den Abbau, Fluchtgeschwindigkeit vernachlässigbar
- Selbst Nebenprodukte werden vollständig genutzt: Silikatschlacke → Strahlungsabschirmung + Rohstoff für Siliziumbarren

| Vergleich | Merkur-Zerlegung | Asteroid (1986 DA) |
|------|----------|----------------|
| Flucht aus dem Gravitationsschacht | 4,25 km/s | ~einige m/s |
| Oberflächentemperatur | 430 °C (tagsüber) | Kryogen (leicht zu handhaben) |
| Ressourcenzusammensetzung | Überwiegend Silikate, Metalltrennung erforderlich | 90%+ Fe-Ni-Legierung (nahezu einsatzbereit) |
| Komplexität der Bergbauausrüstung | Hoch (Gravitation, Hitze) | Niedrig (Mikrogravitation) |
| Gesamtressourcenvolumen | Überwältigend (ein ganzer Planet) | Ausreichend für K1-Bootstrap |

Merkur gewinnt beim Gesamtressourcenvolumen überwältigend, aber **für die erste Phase (Bootstrap Phase) sind Asteroiden weitaus praktischer.**

---

## Der Kern: die Selbstreplikationsschleife

Das eigentliche Unterscheidungsmerkmal dieses Designs ist nicht einfach „wo abbauen und wo platzieren".

**Asteroidenerz → Vakuumschmelze mit Dyson-Spiegel-Solarwärme bei L5 → Produkt baut neue Spiegel → Sammelfläche wächst → Schmelzgeschwindigkeit steigt → exponentielles Wachstum**

1. Anfangsspiegel konzentrieren Sonnenlicht
2. Konzentrierte Hitze erhitzt das Erz auf ~1.500 °C → Fe-Ni-Legierung als Produkt
3. Die Legierung fertigt neue Spiegelrahmen
4. Neue Spiegel werden hinzugefügt → Sammelfläche wächst → **exponentielles Wachstum beginnt**

### Skalierung

| Maßstab | Leistung | vs Erde | Bevölkerung | KI-Rechenleistung |
|------|------|----------|------|---------|
| 1 Modul | 370 MW | 1 kleines Kernkraftwerk | 2.500 | 32 EF |
| 10 Module | 3,7 GW | 3 große Kernkraftwerke | 25.000 | 320 EF |
| 1.000 Module | 370 GW | 2% der Erde | 2,5M | 32 ZF |
| 10.000 Module | 3,7 TW | 20% der Erde | 25M | 320 ZF |
| 200.000 Module | 74 TW | **4-mal die Erde** | 500M | 6.400 ZF |

Die Verdopplungsperiode hängt vom Massenbudget pro Modul und der Prozessreife ab. Bei einer angenommenen Spanne von 2 bis 5 Jahren dauert es 50 bis 125 Jahre, um von 1 Modul die K1.0-Skala zu erreichen.

---

## Das heißt nicht, dass Merkur falsch ist

Seien wir ehrlich über einen Punkt. Die Menschheit befindet sich derzeit bei K 0,73. Selbst bis K1.0 (10¹⁶ W) klafft eine Lücke von ~550-fach gegenüber dem heutigen Stand. **Bevor man über K2 spricht, muss man erst K1 erreichen.**

Der für K1.0 erforderliche Maßstab — ~27 Millionen Module, ~10 PW — ist mit Asteroidenressourcen vollständig abdeckbar. Merkur muss nicht angetastet werden. Die Zerlegung von Merkur wird erst bei K1.5+ (10²¹ W) in Bezug auf das Gesamtressourcenvolumen notwendig.

Merkur ist die Autobahn zu K2. Aber was wir jetzt brauchen, ist die Auffahrt zu dieser Autobahn. **Man braucht keine Autobahn, um eine Autobahn zu bauen.**

In der Bootstrap-Phase:
- Asteroiden haben niedrigere Zugangskosten
- L5 hat niedrigere Betriebskosten
- Die Selbstreplikationsschleife startet früher

Was, wenn es tatsächlich der schnellere Weg ist, zuerst K1 bei L5 zu erreichen und dann diese Industriekapazität für die Zerlegung von Merkur zu nutzen?
