---
title: "Warum Turbinen, nicht Solarpanels"
date: 2026-02-24T12:00:07+09:00
lastmod: 2026-02-24T12:00:07+09:00
tags: ["solarthermie", "turbine", "selbstreplikation", "photovoltaik"]
summary: "Solarpanels und Turbinen wandeln Sonnenlicht im Weltraum mit je ~30 % Wirkungsgrad in Strom um. Aber Turbinen nutzen die restlichen 70 % als Waerme kaskadenartig, koennen aus Asteroidenmaterial gefertigt und vor Ort gewartet werden — die einzige Option fuer einen selbstreplizierenden Dyson-Schwarm."
image: "/images/why-turbines.webp"
author: "PARK JUN WOO"
imageCaption: "Einbau einer Dampfturbinen-Rotorschaufel in einer Siemens-Fabrik. Foto: Siemens Pressebild / Wikimedia Commons / CC BY-SA 3.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## „Warum schon wieder Turbinen?"

Wenn man an die Stromerzeugung eines Dyson-Schwarms denkt, sind Solarpanels (PV) die naheliegende Wahl. Der Standard fuer Weltraumenergie. Die ISS nutzt PV. Die meisten Raumsonden nutzen PV.

Doch dieses Design verwendet Turbinen. Warum im 21. Jahrhundert auf Technik des 19. Jahrhunderts zurueckgreifen?

Die Antwort ist einfach: **Aus Asteroiden kann man keine Solarpanels herstellen, aber Turbinen schon.**

---

## Der Wirkungsgrad ist gleich — 30 %

Klaeren wir das zuerst. „Ist PV nicht effizienter?"

| | Solarpanel (GaAs-Mehrfachuebergang) | Solarthermische Turbine |
|---|---|---|
| Umwandlungswirkungsgrad | ~30 % (Weltraumqualitaet) | ~30 % (Heissseite 1.500 K / Kaltseite 500 K) |
| Carnot-Grenze | Nicht zutreffend | 66,7 % (realisiert ~45 %) |
| Elektrische Leistung | **Gleich** | **Gleich** |

Sammelt man 1.225 MW(thermisch) mit einem 1-km²-Spiegel, betraegt die **elektrische Leistung ~370 MW — egal ob PV oder Turbine.**

Wenn der Wirkungsgrad gleich ist, liegen die Unterschiede woanders.

---

## Unterschied 1: Die anderen 70 %

Sowohl PV als auch Turbinen koennen 70 % der einfallenden Energie nicht in Strom umwandeln. Aber wohin diese 70 % gehen, ist voellig unterschiedlich.

### PV: 70 % verschwinden als Niedertemperatur-Abwaerme

```
Solareintrag 1.225 MW
  ├→ 30 % → 370 MW (Strom)
  └→ 70 % → 855 MW → Paneloberflaeche bei 60–80°C Abwaerme
                      → kein Nutzen. Ueber Kuehlkoerper ins All abgestrahlt.
```

Bei 60–80°C kann man kein Metall schmelzen, keine Fabrik betreiben und keinen Lebensraum heizen. **70 % der Energie verschwinden einfach.**

### Turbine: 70 % kaskadieren von hoher zu niedriger Temperatur

```
Solarthermischer Eintrag 1.225 MW
  ├→ 30 % → 370 MW (Strom)
  └→ 70 % → 855 MW (Waerme) → stufenweise Nutzung nach Temperatur:
       ├→ 800–1.000°C: ~400 MW → Verhuettung (Fe-Ni-Schmelze)
       ├→ 400–600°C:   ~250 MW → Beschichtung, Waermebehandlung, Umformung
       ├→ 100–200°C:   ~120 MW → Habitatheizung
       └→ 30–60°C:      ~85 MW → Rechenzentrum-Umgebungswaerme
```

**Dieselben 70 % durchlaufen nacheinander Huette → Fabrik → Habitat → Rechenzentrum, und alles wird genutzt.** Die „Abwaerme" der Turbine ist kein Abfall — sie ist die Energiequelle fuer den naechsten Prozess.

Effektive Nutzung der einfallenden Energie:
- PV: ~30 % (nur Strom)
- **Turbine: ~30 % + Waermekaskade → effektiv 85 %+**

---

## Unterschied 2: Kompatibilitaet mit der Selbstreplikationsschleife

Das ist der entscheidende Faktor.

### PV im Weltraum herstellen

Die Herstellung von Solarpanels (GaAs-Mehrfachuebergang) erfordert:
1. Gallium (Ga) + Arsen (As) als Rohstoffe — **in Asteroiden nicht vorhanden**
2. Einkristallzuechtung (MOCVD, MBE) — **extreme Praezisionsanlagen**
3. Mehrschichtige Epitaxie-Abscheidung — **Reinraum erforderlich**
4. Antireflexbeschichtung, Verdrahtung, Modulassemblierung — **dedizierte Fertigungslinie**

Asteroiden haben weder Ga noch As. Selbst mit der Ausruestung fehlt der Rohstoff. **PV kann nicht in die Selbstreplikationsschleife eintreten.** Es muss kontinuierlich von der Erde nachgeliefert werden.

Was ist mit Silizium-(Si)-PV? Tatsaechlich enthaelt dieses Design bereits einen Prozess zur Herstellung von Halbleiter-Si-Bloecken aus Silikatschlacke (Zonenraffination, fuer KI-Chips). Si-Rohstoff ist also verfuegbar. Allerdings:
- Si-PV-Weltraumwirkungsgrad ~20 % — niedriger als GaAs (30 %) und unter Turbinen (30 %)
- Die PV-Zellfertigung (Diffusion, Antireflexbeschichtung, Elektrodenmuster) ist **separat von der Chipfertigung noetig**
- Wirkungsgrad sinkt durch Weltraumstrahlung → kuerzerer Austauschzyklus
- Derselbe Si-Wafer ist **als KI-Chip weit wertvoller**

Selbst wenn Si verfuegbar ist, ist PV daraus Verschwendung. **Wenn man Silizium hat, baut man Chips.**

### Turbinen im Weltraum herstellen

| Komponente | Material | Quelle | Fertigung |
|------------|----------|--------|-----------|
| Hochtemperatur-Schaufeln & -Duesen | Ni-Superlegierung | Asteroiden-Fe-Ni | Praezisionsguss |
| Niedertemperatur-Verdichter & -Welle | Ti-Legierung | Lunarer Ilmenit | Zerspanung |
| Gehaeuse | Fe-Ni | Asteroide | Blechbearbeitung & Schweissen |

**Alles kann aus Materialien hergestellt werden, die bereits in der Selbstreplikationsschleife vorhanden sind (Fe-Ni, Ti).** Kein zusaetzlicher Rohstoff, keine zusaetzliche Fertigungslinie noetig. Turbinen kommen von derselben Produktionslinie wie die Spiegelrahmen.

---

## Unterschied 3: Lebensdauer und Wartung

### Das Strahlungsproblem von Weltraum-PV

Weltraum-PV wird durch hochenergetische Teilchen (Protonen, schwere Ionen) geschaedigt, die das Kristallgitter stoeren. Der Wirkungsgrad sinkt um ~1–3 % pro Jahr.

- Nach 10 Jahren: Wirkungsgrad faellt auf 70–80 %
- Austausch noetig → **kann nicht hergestellt werden, muss von der Erde nachgeliefert werden**
- Wenn keine Nachlieferung moeglich: Leistungseinbussen akzeptieren

### Turbinenverschleiss

Turbinen halten auch nicht ewig. Hochtemperatur-Schaufelkriechen und Lagerverschleiss sind die Hauptursachen fuer Degradation.

Aber:
- Schaufeln koennen **vor Ort aus Ni-Superlegierung neu gegossen werden**
- Lager → **Magnetlager fuer beruehrungslosen** Betrieb: null Verschleiss
- Modulares Design: nur degradierte Komponenten werden ersetzt, nicht die ganze Einheit

**Turbinenteile koennen vor Ort gefertigt und ersetzt werden. PV-Teile nicht.** In einem selbstreplizierenden System ist dieser Unterschied entscheidend.

---

## Reale Grenzen von Turbinen — und Loesungen

Seien wir ehrlich ueber die Nachteile.

### Grenze 1: Ein Arbeitsfluid ist erforderlich

Turbinen brauchen ein Fluid, das sich bei Erwaermung ausdehnt, um den Rotor anzutreiben. Woher kommt dieses Fluid im Weltraum?

| Kandidat | Vorteile | Nachteile | Beschaffung |
|----------|----------|-----------|-------------|
| Helium (He) | Inert, hochtemperaturstabil | Schwer nachzufuellen bei Leckage | Auffangen beim Ausgasen von Asteroiden |
| Ueberkritisches CO₂ | Hohe Dichte, kompakte Turbine | Korrosionsmanagement noetig | Ausgasen von Asteroiden |
| Natrium/Kalium (Fluessigmetall) | Ultrahohe Temperatur, hervorragende Waermeuebertragung | Reaktiv (im Vakuum sicher) | Spurenmengen aus Asteroiden |

Das System laeuft im geschlossenen Kreislauf — es gibt keinen Fluidverbrauch. Nur die Erstbefuellung muss sichergestellt werden. Gas kann beim Ausgasen der Asteroidenverhuettung aufgefangen werden, oder eine kleine Menge wird anfangs von der Erde geliefert.

### Grenze 2: Bewegliche Teile — Ausfallrisiko im Weltraum

Die grundlegende Schwaeche von Turbinen: Hochgeschwindigkeits-Rotationskomponenten. Selbst auf der Erde ist die Turbinenwartung anspruchsvoll.

**Loesungen:**
- **Magnetlager** — beruehrungslose Rotationsstuetzung. Null Verschleiss. Bereits in terrestrischen Hochgeschwindigkeits-Turbomaschinen kommerziell eingesetzt
- **Modulare Schaufelkartuschen** — Schaufelsaetze als Einheit austauschen. Keine Einzelschaufel-Wartung noetig
- **Lokale Fertigung** — Ersatzteile bei Bedarf giessen. Kein Warten auf Erdnachschub
- **Redundanz** — mehrere Turbinen pro Modul. Leistung auch bei Wartung einer Einheit aufrechterhalten

### Grenze 3: Vibration

Hochgeschwindigkeitsrotation erzeugt Vibrationen. Das ist ein Problem, wenn Halbleiterfabriken oder Praezisionsoptik im selben Modul untergebracht sind.

**Loesungen:**
- **Spezialisierte Cluster** — Turbinenmodule und Fertigungsmodule physisch trennen (separate Strukturen)
- **Vibrationsdaempfende Halterungen** — Turbinen auf flexiblen Strukturverbindungen installieren
- Auf der Erde stellt man Kraftwerk und Halbleiterfabrik auch nicht in dasselbe Gebaeude

### Grenze 4: Waermeabfuhr

Die Waerme der Turbinen-Kaltseite muss ins All abgestrahlt werden. Im Weltraum gibt es keine Atmosphaere, Konvektionskuehlung ist unmoeglich — nur Strahlungskuehlung funktioniert.

**Das ist ein grosses eigenstaendiges Thema. Es wird im naechsten Beitrag ausfuehrlich behandelt.**

---

## Zusammenfassung in einem Satz

Solarpanels und Turbinen haben denselben elektrischen Wirkungsgrad (30 %). Aber PV verschwendet die anderen 70 %, waehrend Turbinen sie nutzen. PV kann im Weltraum nicht hergestellt werden; Turbinen schon. Wenn PV ausfaellt, wartet man auf die Erde; wenn eine Turbinenschaufel verschleisst, wird sie vor Ort neu gegossen. In einem selbstreplizierenden System ist die Antwort klar.
