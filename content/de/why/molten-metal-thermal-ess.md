---
title: "Warum geschmolzenes Metall statt Batterien"
date: 2026-02-25T12:00:02+09:00
lastmod: 2026-02-25T12:00:02+09:00
tags: ["schmelzmetall-waermespeicher", "ESS", "elektromagnetische-levitation", "waermespeicherung", "selbstreplikation"]
image: "/images/molten-metal-thermal-ess.webp"
summary: "Ein Dyson-Modul ist ein solarthermisches Kraftwerk — Waerme direkt als geschmolzenes Fe-Ni in Schwerelosigkeit speichern. ~145 Wh/kg mit latenter Waerme, unendliche Zyklen, alles aus Asteroidenerz."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Geschmolzene Fe-Ni-Masse in elektromagnetischer Levitation im Vakuum bei Schwerelosigkeit — durch Oberflaechenspannung bleibt sie kugelfoermig. Bild: Gemini"
---

## Was der vorherige Artikel vergessen hat

[Der vorherige Artikel](/de/why/why-iron-nickel-battery/) hat gezeigt, warum Eisen-Nickel-Batterien Lithium-Ionen schlagen. In Asteroiden gibt es kein Lithium, im Vakuum kann man kein Feuer loeschen, Eisen-Nickel haelt 30 bis 50 Jahre, und Ueberladung erzeugt Wasserstoff.

Alles richtig. **Aber ein Punkt wurde vergessen.**

Ein Dyson-Modul ist ein solarthermisches Kraftwerk. Spiegel buendeln Licht, Waerme treibt Turbinen an. Wenn Energie fuer Eklipsen gespeichert werden muss, sieht das aktuelle Design so aus:

```
Solarwaerme (1.600°C) -> Turbine -> Strom (370 MW)
                                  -> Ueberschuss (~50 MW)
                                       -> Batterie (chemische Energie)    <- 2 Umwandlungen
                                       -> Eklipse -> zurueck zu Strom     <- 3 Umwandlungen
```

Waerme -> Strom -> Chemie -> Strom. **3 Umwandlungen.** 20-30 % Verlust bei jedem Schritt.

Was, wenn man die Waerme direkt speichert?

```
Solarwaerme (1.600°C) -> Teil direkt im Waermespeicher gelagert     <- 0 Umwandlungen
                       -> Eklipse -> Speicher -> Turbine -> Strom    <- 1 Umwandlung
```

**1 Umwandlung.** Der Effizienzunterschied ist erdrueckend.

Den Energieueberschuss eines solarthermischen Kraftwerks in Strom umzuwandeln, dann in Chemie, dann zurueck in Strom — das ist wie Wasser zu Dampf zu machen, in Wasserstoff und Sauerstoff zu zerlegen und dann wieder zu Wasser zusammenzufuegen. **Es funktioniert, aber warum?**

Waermespeicherung ist die Antwort. Aber warum macht man das auf der Erde nicht?

---

## Warum es auf der Erde nicht funktioniert, warum es im Weltraum funktioniert

Waerme in geschmolzenem Metall auf der Erde zu speichern ist ein Forschungsthema, keine industrielle Realitaet. Dafuer gibt es Gruende:

| Problem | Erde | Weltraum (Schwerelosigkeit, Vakuum) |
|---------|------|-------------------------------------|
| Behaelter | Muss das Gewicht von Tausenden Tonnen Schmelze tragen -> massiv und teuer | **Kein Eigengewicht** — duenne Waende oder sogar kontaktfrei |
| Isolierung | Konvektion + Leitung + Strahlung muessen blockiert werden | **Nur Strahlung blockieren** — einige Dutzend Schichten MLI genuegen |
| Waermeverluste | Hoch — Luftkonvektion ist der Hauptverursacher | **Extrem niedrig** — null Konvektion im Vakuum |
| Korrosion | 1.500°C Schmelze greift Waende an | **Elektromagnetische Levitation kontaktfrei** -> null Korrosion |
| Sicherheit | Leckage = Grossunfall | Kein Feuer im Vakuum, kein Ausbreitungsmedium |

**Die Schwaechen der Erde verschwinden oder kehren sich im Weltraum um.** Dasselbe Muster, das sich in frueheren Artikeln wiederholt hat — [Turbinen vs PV](/de/why/why-turbines/), Eisen-Nickel vs Lithium-Ionen — exakt dieselbe Struktur.

---

## Waermespeicherung durch elektromagnetische Levitation

Geschmolzenes Fe-Ni ist auch bei 1.500°C ein elektrischer Leiter (es verliert seinen Magnetismus oberhalb der Curie-Temperatur von Nickel, behaelt aber seine Leitfaehigkeit). Ein magnetisches Wechselfeld induziert Wirbelstroeme (eddy currents), und die Abstossung zwischen Wirbelstroemen und Magnetfeld ermoeglicht **kontaktfreie Levitation**.

Das ist eine Technik, die auch auf der Erde im Labor eingesetzt wird. Man nennt sie [EML-Schmelzen (Electromagnetic Levitation)](https://en.wikipedia.org/wiki/Electromagnetic_levitation). Metallproben von wenigen Gramm bis einigen Kilogramm werden in der Luft schwebend geschmolzen. Der Grund, warum es auf der Erde nicht groesser geht, ist genau einer — **Schwerkraft**. Die Schwerkraft zu ueberwinden erfordert starke Magnetfelder, und starke Felder brauchen Energie. Einige Kilogramm sind die Grenze.

In Schwerelosigkeit? **Es gibt keine Schwerkraft zu ueberwinden.** Nur das minimale Magnetfeld zur Positionsstabilisierung ist noetig. Einige Tonnen, Hunderte Tonnen, Zehntausende Tonnen.

```
[Querschnitt einer Waermespeichereinheit]

        +--- MLI-Reflexionswand (Mehrschicht-Reflexionsisolierung) ---+
        |                                                              |
        |    +-- Elektromagnetische Spulen (gekuehlt) --+             |
        |    |                                          |             |
        |    |   @@@@@@@@@@@@@@@@@@                     |             |
        |    |   @ Geschmolzene Fe-Ni-Masse @           |             |
        |    |   @ (1.200~1.500°C)          @           |             |
        |    |   @@@@@@@@@@@@@@@@@@                     |             |
        |    |                                          |             |
        |    +------------------------------------------+             |
        |                                                              |
        +--------------------------------------------------------------+
```

In Schwerelosigkeit nimmt geschmolzenes Metall durch Oberflaechenspannung **natuerlich eine Kugelform** an. Die Kugel hat das kleinste Verhaeltnis von Oberflaeche zu Volumen — Strahlungswaermeverluste sind minimal. Die MLI-Reflexionswand haelt Strahlungswaerme zurueck, das elektromagnetische Feld haelt die Position, und da kein Wandkontakt besteht, gibt es null Korrosion.

**Man schmilzt aus Asteroiden gewonnenes Fe-Ni und laesst es einfach schweben — das ist ein Waermespeicher.**

---

## Laden und Entladen

```
[Laden — Normalbetrieb]
Solarkonzentration -> Strahlungsklappe oeffnen -> Metallmasse erwaermen -> 1.200°C -> 1.500°C

[Entladen — Eklipse]
Strahlungsklappe oeffnen -> Strahlungswaerme der Masse erwaermt Waermetauscher -> Arbeitsfluid -> Turbine
1.500°C -> 1.200°C (DeltaT=300°C genutzt)
```

Laden: Ein Teil der von Spiegeln gesammelten Solarwaerme wird zum Speicher geleitet. Klappe oeffnen und Licht erwaermt die Metallmasse.

Entladen: Bei einer Eklipse wird die Klappe geoeffnet, damit die Strahlungswaerme der Masse vom Waermetauscher aufgenommen wird. Der Waermetauscher erwaermt das Arbeitsfluid und treibt die Turbine an. Dieselben Turbinen werden verwendet — normalerweise sind die Spiegel die Waermequelle, bei Eklipse ist es der Waermespeicher. **Aus Sicht der Turbine aendert sich nur die Waermequelle, alles andere bleibt gleich.**

Der Waermeaustausch erfolgt durch Strahlung. Man kann kein Rohr in eine kontaktfrei schwebende Schmelze stecken, daher ist der Waermetransfer ueber Strahlungsklappen der grundlegende Mechanismus. Die Strahlungsenergie von 1.500°C geschmolzenem Metall ist nach dem Stefan-Boltzmann-Gesetz proportional zu T⁴ — mehr als ausreichend.

---

## Energiedichte: Fuehlbare + latente Waerme

Spezifische Waerme der Fe-Ni-Legierung: ~0,5 kJ/(kg·K) = ~0,14 Wh/(kg·K). Berechnet man nur die **fuehlbare Waerme (sensible heat)**, proportional zur Temperaturaenderung (DeltaT):

| Temperaturbereich (DeltaT) | Fuehlbare Waerme | Anmerkung |
|-----------------------------|------------------|-----------|
| 300°C (1.200->1.500°C) | ~42 Wh/kg | Konservativ |
| 500°C (1.000->1.500°C) | ~70 Wh/kg | Mittel |
| 1.000°C (500->1.500°C) | ~140 Wh/kg | Aggressiv |

Aber das ist nicht alles.

### Latente-Waerme-Bonus

Der Schmelzpunkt der Fe-Ni-Legierung liegt bei ~1.430-1.450°C. Der Betriebsbereich von 1.000-1.500°C **durchquert diesen Schmelzpunkt.** Beim Laden schmilzt das Metall, beim Entladen erstarrt es — Phasenuebergang.

Wenn ein Stoff schmilzt, steigt die Temperatur nicht, waehrend er enorme Waerme aufnimmt. Das ist die **Schmelzwaerme (latente Waerme der Fusion).**

```
Schmelzwaerme von Eisen (Fe): ~270 kJ/kg = 75 Wh/kg
Fe-Ni-Legierung: aehnlicher Bereich
```

Fuehlbare und latente Waerme zusammen:

| Temperaturbereich | Fuehlbar | Latent | **Gesamt** |
|-------------------|----------|--------|------------|
| 300°C (1.200->1.500°C) | ~42 | ~75 | **~117 Wh/kg** |
| 500°C (1.000->1.500°C) | ~70 | ~75 | **~145 Wh/kg** |
| 1.000°C (500->1.500°C) | ~140 | ~75 | **~215 Wh/kg** |

**Allein die latente Waerme verdoppelt die Energiedichte.** Ein Metallblock, der einfach schmilzt und erstarrt, erreicht den unteren Bereich von Lithium-Ionen-Batterien (150-270 Wh/kg).

### ESS-Vergleich (latente Waerme eingeschlossen)

| Methode | Energiedichte | Zyklenlebensdauer | Materialbeschaffung |
|---------|---------------|-------------------|---------------------|
| Lithium-Ionen | 150-270 Wh/kg | 3.000-10.000 Zyklen | Unmoeglich (kein Li in Asteroiden) |
| Eisen-Nickel-Batterie | 30-50 Wh/kg | Praktisch unbegrenzt | Asteroiden-Fe-Ni |
| **Geschmolzenes Fe-Ni Waermespeicher** | **117-215 Wh/kg** | **Praktisch unbegrenzt** | **Asteroiden-Fe-Ni** |

Dieselbe Energiedichte wie Lithium-Ionen, unbegrenzte Zyklen, und der Rohstoff liegt in Asteroiden ueberall herum. Und nur 1 Umwandlung Waerme -> Strom, sodass die Systemeffizienz erdrueckend ist.

Warum die Zyklen unbegrenzt sind: Man erwaermt und kuehlt einen Metallblock. Keine chemische Reaktion. Keine Elektroden. Kein Elektrolyt. Es gibt nichts, was degradieren koennte.

---

## Dimensionierung: Warum 60 kleine Einheiten statt einer riesigen Kugel

Maximale Eklipse 12 Stunden, Turbinenleistung 370 MW. Der Waermespeicher muss nicht alles abdecken — Wasserstoff-Brennstoffzellen und Batterien uebernehmen ihren Anteil.

### Hybridberechnung

```
Von 12 Stunden Eklipse:
  Waermespeicher: 6 Stunden
  H2-Brennstoffzelle: 4 Stunden (Jaehrl. Batholyzer-Vorrat)
  Eisen-Nickel-Batterie: 2 Stunden (Sofortlastfolge + Backup)
```

Waermespeicher fuer 6 Stunden (latente Waerme eingeschlossen):

```
370 MW / 0,30 (Turbinenwirkungsgrad) = ~1.233 MW(th) x 6h = ~7.400 MWh(th)

DeltaT=500°C + latente Waerme (145 Wh/kg):
  Benoetigte Masse = 7.400.000 kWh / 0,145 kWh/kg = ~51.000 Tonnen

(Ohne latente Waerme: 105.000 Tonnen -> Latent-Bonus halbiert die Masse)
```

51.000 Tonnen in einer einzigen Kugel ergeben einen Radius von ~12 m. Intuitiv einfach. **Aber das funktioniert nicht.** Drei ingenieurwissenschaftliche Gruende.

### Grund 1: Unzureichende Oberflaeche fuer die Entladung

Waehrend einer Eklipse uebertraegt der Waermespeicher Waerme an den Waermetauscher **ausschliesslich durch Strahlung**. Die Strahlungsleistung ist proportional zur Oberflaeche (P = epsilon sigma A T^4).

Die Kugel hat das kleinste Verhaeltnis Oberflaeche zu Volumen. Ideal zum **Bewahren** von Waerme, aber ein Engpass beim **schnellen Abgeben**.

```
Benoetigte thermische Leistung: ~1.233 MW(th)

Strahlungsleistung bei 1.500°C (1.773 K) (epsilon=0,5):
  P/A = epsilon x sigma x T^4 = 0,5 x 5,67e-8 x 1.773^4 = 280 kW/m2

Benoetigte Oberflaeche: 1.233.000 kW / 280 kW/m2 = 4.400 m2

Oberflaeche einer einzelnen Kugel mit Radius 12 m: 4pi(12)^2 = 1.810 m2 -> Unzureichend (41 % des Bedarfs)
```

**Eine einzelne Kugel kann physisch nicht die benoetigte Waerme abstrahlen.** Die Oberflaeche ist weniger als die Haelfte.

Aufgeteilt in ~58 Einheiten mit Radius 3 m:

```
Oberflaeche pro Einheit: 4pi(3)^2 = 113 m2
Gesamtoberflaeche von 58 Einheiten: 113 x 58 = 6.560 m2 -> 149 % des Bedarfs (mit Reserve)
Masse pro Einheit: (4/3)pi(3)^3 x 7.800 = 880 Tonnen
```

**Beim Speichern behaelt jede Einheit ihre Kugelform, um Verluste zu minimieren; beim Entladen liefert die Gesamtoberflaeche mehrerer Einheiten die benoetigte Waermeleistung.** Der Nachteil der Kugel wird durch die Anzahl der Einheiten geloest.

### Grund 2: Sloshing — eine 100.000-Tonnen-Lava-Abrissbirne

Wenn 51.000 Tonnen fluessiges Metall als einzelne Kugel schweben und das Modul fuer die Lageregelung auch nur geringfuegig rotiert oder vibriert, entstehen im Inneren **riesige Wellen (Sloshing)**. Wenn magnetohydrodynamische (MHD) Instabilitaeten hinzukommen, besteht die Gefahr, dass diese Lavamasse schwappt und den elektromagnetischen Einschluss durchbricht.

Einheiten mit 3 m Radius und 880 Tonnen? Die Sloshing-Energie skaliert mit der dritten Potenz der Einheitsgroesse, sodass **die Sloshing-Energie jeder Einheit weniger als 1/10.000 der einer einzelnen Kugel betraegt**. Das Risiko eines Einschlussbruchs ist praktisch beseitigt.

### Grund 3: Volumenausdehnung beim Phasenuebergang

Beim Wechsel zwischen 1.200°C (fest) und 1.500°C (fluessig) durchlaeuft Fe-Ni wiederholt Ausdehnung und Schrumpfung. Wenn eine Kugel mit 12 m Radius von aussen abkuehlt, bildet sich eine feste Kruste, und die schrumpfende Fluessigkeit im Inneren kann **die Kruste aufbrechen und Fragmente ins Vakuum schleudern**. Kleine Einheiten ermoeglichen einen gleichmaessigen Temperaturgradienten von innen nach aussen und beseitigen dieses Problem.

### Designergebnis

```
Spezifikationen der Waermespeichereinheiten:
  Form: kugelfoermig (natuerliche Bildung durch Oberflaechenspannung)
  Radius: ~3 m
  Masse: ~880 Tonnen/Einheit
  Anzahl Einheiten: ~58 (pro Modul)
  Gesamtmasse: ~51.000 Tonnen
  Anordnung: verteilt in der Struktur hinter den Spiegeln (dient auch als Gegengewicht)

Entladeleistung:
  Gesamtoberflaeche: ~6.560 m2 (149 % des Bedarfs von 4.400 m2)
  1.233 MW(th) Leistungsreserve gesichert
```

Die 51.000 Tonnen werden nicht separat beschafft. Aus Asteroiden raffiniertes Fe-Ni, **geschmolzen belassen ohne es erstarren zu lassen, bildet die Waermespeichereinheiten**. Verteilt in der Modulstruktur dienen sie zugleich als **Gegengewichte**.

---

## 3-Ebenen-ESS: Rollentrennung

Batterien muessen nicht mehr den Massenspeicher uebernehmen. Jede Ebene erhaelt die optimale Technologie:

```
Ebene 1 — Massenspeicher (Stundenskala)
  +-> Geschmolzenes-Metall-Waermespeicher
       Laden: Direkte Solarwaerme
       Entladen: Speicher -> Turbine -> Strom
       Rolle: Eklipsen-Antwort, minimale Umwandlungsverluste

Ebene 2 — Puffer (Sekunden- bis Minutenskala)
  +-> Eisen-Nickel-Batterie
       Laden: Ueberschussstrom
       Entladen: Elektrochemisch (ms-Antwort)
       Rolle: Sofortlastfolge, Startleistung

Ebene 3 — Notfall + chemische Produktion
  +-> H2/O2 (Batholyzer-Produkte)
       Notfall-Brennstoffzelle
       Treibstoff, Reduktionsmittel, Atemsauerstoff
       Sekundaer-Backup bei verlaengerter Eklipse
```

### Was diese Architektur bringt

**Der Batteriespeicher schrumpft drastisch.** Im vorherigen Design brauchte man 111.000 m3, um 12 Stunden Eklipse nur mit Batterien abzudecken. Wenn der Waermespeicher den Massenspeicher uebernimmt, decken Batterien 2 Stunden — reduziert auf einige Tausend m3.

**Die Rolle des Batholyzers wird klar.** Der vorherige Artikel beschrieb den Batholyzer (Elektrolyse durch Ueberladung) als Kombination aus ESS-Speicherung und chemischer Produktion. Wenn der Waermespeicher den Massenspeicher uebernimmt, wird der Batholyzer als **Chemiefabrik** positioniert — Wasserstofftreibstoff-, Sauerstoff- und Reduktionsmittelproduktion als Haupttaetigkeit, Notfallstromerzeugung als Nebentaetigkeit.

**Die Materialien sind identisch.** Waermespeicher = geschmolzenes Fe-Ni. Batterien = Fe-Ni-Elektroden. Batholyzer = dieselben Batterien bei Ueberladung. Alle 3 Ebenen kommen aus Asteroiden-Fe-Ni. Der Selbstreplikationsschleife werden keine neuen Rohstoffe hinzugefuegt.

---

## Beziehung zum vorherigen Artikel (Eisen-Nickel-Batterie)

Die Kernargumente des vorherigen Artikels bleiben **alle gueltig:**

- Kein Lithium in Asteroiden -> unveraendert
- 30-50 Jahre Lebensdauer der Eisen-Nickel-Batterie -> unveraendert
- Brandgefahr im Vakuum -> unveraendert
- H2/O2-Produktion des Batholyzers -> unveraendert
- Lokale Fertigung moeglich -> unveraendert

**Was ergaenzt wird:** Der vorherige Artikel konnte den Eindruck erwecken, dass die Eisen-Nickel-Batterie allein den Massenspeicher (12 Stunden Eklipse) uebernimmt. In Wirklichkeit ist Waermespeicherung fuer die Massenenergiespeicherung weit ueberlegen, und die Batterie glaenzt in ihrer eigenen Domaene: der Sofortantwort.

**Jeder macht das, was er am besten kann.** Der Hochofen fuer Waermespeicherung auf Stundenskala. Die Batterie fuer Millisekunden-Leistungsantwort. Die Brennstoffzelle fuer Notfall + chemische Produktion. Keiner muss alles allein uebernehmen.

---

## Zusammenfassung in einem Satz

Ein Dyson-Modul ist ein solarthermisches Kraftwerk — Waerme in Strom, dann in Chemie, dann zurueck in Strom umzuwandeln ist dreifacher Umwandlungsverlust. Asteroiden-Fe-Ni schmelzen und in Schwerelosigkeit schweben lassen ergibt einen Waermespeicher mit 0 Umwandlungen beim Laden und 1 beim Entladen. Mit der latenten Waerme des Phasenuebergangs erreicht die Energiedichte ~145 Wh/kg — gleichwertig mit Lithium-Ionen. 58 Einheiten mit 3 m Radius in verteilter Anordnung loesen den Oberflaechen-Engpass bei der Entladung, Sloshing und Phasenuebergangs-Ausdehnung. Die Materialien sind alle dasselbe Asteroiden-Fe-Ni.

![Geschmolzene Fe-Ni-Masse in elektromagnetischer Levitation im Vakuum bei Schwerelosigkeit. Bild: Gemini](/images/molten-metal-thermal-ess.webp)
