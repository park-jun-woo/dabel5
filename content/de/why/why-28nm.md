---
title: "Warum 28nm"
date: 2026-02-25T12:00:03+09:00
lastmod: 2026-02-25T12:00:03+09:00
tags: ["28nm", "halbleiter", "TPU", "selbstreplikation", "ArF-lithographie"]
image: "/images/why-28nm.webp"
summary: "Modernste 3nm-Chips sind ohne ASMLs exklusives EUV nicht herstellbar — im Weltraum unmoeglich. 28nm ist allein mit ArF realisierbar, und Googles TPU v1 hat 92 TOPS im Praxisbetrieb bewiesen. Silizium kommt aus der Schlacke, und der Weltraum selbst ist ein Reinraum."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Die-Foto eines TTL-4-Eingang-NAND-Gatter-Chips — 7 Transistoren, minimale Strukturbreite 20 um (1968). Foto: Dgarte / Wikimedia Commons / CC BY-SA 3.0"
---

## „Selbstreplikation — und woher kommen die Chips?"

Fruehere Artikel haben gezeigt, dass Spiegel, Strukturen, [Turbinen](/de/why/why-turbines/), [Batterien](/de/why/why-iron-nickel-battery/) und [Waermemanagement](/de/why/heat-flow/) alle aus Asteroiden-Fe-Ni hergestellt werden koennen. Die Selbstreplikationsschleife ist fast geschlossen.

Fast.

**KI-Chips werden immer noch von der Erde importiert.** Der autonome Betrieb eines Dyson-Moduls — Steuerung von Bergbaurobotern, Orbitalanpassung, Raffinerieprozess-Management, Lebenserhaltung — wird komplett von KI uebernommen. Ohne Chips ist das Modul blind.

So wie „es gibt kein Lithium in Asteroiden" das Game Over fuer Lithium-Ionen-Batterien war, **ist „man kann im Weltraum kein EUV herstellen" das Game Over fuer modernstes 3nm.**

Welcher Prozess also fuer die Chipfertigung?

---

## Warum nicht modernste 3nm

Der Kern der Halbleiterfertigung ist Lithographie — mit Licht Schaltkreismuster auf einen Wafer zu schreiben.

| Element | 28nm | 3-5nm (modernste) |
|---------|------|--------------------|
| Lithographie | **ArF-Immersion** (Nikon, Canon, ASML) | **EUV** (ASML-Monopol, Tausende Milliarden pro Einheit) |
| Geraeteverfuegbarkeit | Reifer Markt, Gebrauchtgeraete reichlich vorhanden | Extrem begrenzt, Exportkontrolle |
| Designkomplexitaet | Single-Patterning | Multi-Patterning (extrem komplex) |
| Fab-Baukosten | ~3-5 Mrd. $ | ~20-30 Mrd. $ |
| Ausbeute | Hoch (10+ Jahre bewaehrt) | Anfangs niedrig |

Der EUV-Scanner (extreme Ultraviolett) wird **von nur einer einzigen Firma weltweit hergestellt: ASML.** Eine einzige Fabrik in Veldhoven, Niederlande. Exportkontrolliert. Die Anlage, deren Verkauf an China die Allianz USA-Japan-Niederlande verhindert. Das im Weltraum nachbauen? Unmoeglich.

Der leistungsfaehigste Prozess ohne EUV. Das ist **28nm**.

„Ist 7nm nicht auch mit ArF moeglich?" — Moeglich. Multi-Patterning erlaubt es, ArF-Licht mehrfach zu belichten, um feinere Muster zu erzeugen. Aber die Designkomplexitaet explodiert und die Ausbeute bricht ein. Bevor Personal und Infrastruktur fuer Ausbeutemanagement im Weltraum verfuegbar sind, ist das unrealistisch.

„Waere 65nm nicht einfacher herzustellen?" — Ja. Aber die Leistung pro Chip ist zu niedrig. Fuer dieselbe Arbeitslast explodiert die Chipanzahl, und mehr Chips bedeuten proportional mehr Verdrahtung, Packaging und Kuehlung. Einfach herzustellen, aber das Gesamtsystem wird schwieriger.

**28nm = die optimale Integrationsdichte ohne EUV.**

---

## Das ist keine Theorie — Google TPU v1

„Kann 28nm wirklich KI ausfuehren?"

Google hat 2015 die Antwort geliefert. **[TPU v1](https://arxiv.org/abs/1704.04760).** In 28nm gefertigt, ueber 100.000 Stueck in eigenen Rechenzentren eingesetzt. Ein KI-Beschleuniger im Produktionseinsatz.

| Element | Google TPU v1 (gemessen) |
|---------|--------------------------|
| Prozess | 28nm |
| Architektur | 256 x 256 systolisches Array |
| Rechenleistung | 92 TOPS (INT8) = 23 TFLOPS (FP16) |
| Leistungsaufnahme | ~75 W im Betrieb |
| Siliziumnutzung | **90 %+** |

Die systolische Array-Architektur ist der Schluessel. Ein GPU ist ein Universalchip — 70 % des Siliziums entfallen auf Steuerlogik, Cache und Scheduler. Nur 30 % fuehren tatsaechlich Matrixmultiplikationen aus. Ein systolisches Array ist so konstruiert, dass es nur Matrixmultiplikationen ausfuehrt — **ueber 90 % des Siliziums werden fuer tatsaechliche Berechnungen genutzt.**

Wenn man nur KI ausfuehrt, ist der Universalitaets-Overhead des GPU reine Verschwendung. Der TPU ist der Chip, der diese Verschwendung beseitigt.

Und das ist kein theoretischer Vorschlag. **Das ist der Chip, auf dem AlphaGo lief.** Hardware, die ueber Jahre im Produktionsbetrieb in Google-Rechenzentren eingesetzt wurde.

---

## „4,6-mal mehr Strom?"

Der derzeit leistungsfaehigste KI-Chip der Erde, NVIDIA H100. 4nm-Prozess, 990 TFLOPS, 700 W Leistungsaufnahme.

Ein TPU v1 leistet 23 TFLOPS. Wie viele fuer dieselbe Rechenleistung wie ein H100?

```
990 TFLOPS / 23 TFLOPS = 43 Karten

43 Karten x 75 W = 3.225 W = 3,2 kW
```

| | TPU v1 x 43 Karten | H100 x 1 Karte |
|---|---|---|
| FP16 gesamt | ~990 TFLOPS | ~990 TFLOPS |
| Gesamtleistung | **3,2 kW** | 700 W |
| Leistungsverhaeltnis | **4,6x** | Referenz |

4,6-fach. Auf der Erde ist das ein fataler Unterschied. Wenn Stromkosten 30-40 % der Betriebskosten eines Rechenzentrums ausmachen, bedeutet 4,6-fache Leistung Insolvenz.

**Im Weltraum?**

1 Dyson-Modul = 370 MW. 3,2 kW sind **0,00086 %** von 370 MW. In Spiegelflaeche ausgedrueckt sind das 2,4 m2 — ein Pixel auf 1 km2 Dyson-Spiegel.

Auf der Erde ist Strom Geld. **Im Weltraum ist Strom Spiegelflaeche.** Spiegel werden aus Asteroiden-Fe-Ni gewalzt.

Dieselbe logische Struktur wie im [vorherigen Artikel, wo Turbinen Solarpanels geschlagen haben](/de/why/why-turbines/). Eine nach irdischen Masstaeben unterlegene Wahl wird nach Weltraummasstaeben zur einzigen Wahl. **Wenn sich die Masstaebe aendern, aendert sich die Antwort.**

---

## 1 Modul = ein Rechenzentrum mit 30.000 H100

Werden 30 % der 370 MW des Moduls fuer KI-Berechnungen zugeteilt:

```
111 MW / 75 W/Chip = ~1.480.000 Karten (1,48 Millionen TPU v1)

1,48 Millionen / 43 Karten pro H100-Aequivalent = ~34.000 H100

Interconnect-/Kuehlungs-Overhead 20-30 % -> konservativ ~25.000-30.000 H100
```

Gleichwertig mit den groessten KI-Clustern der Erde im Jahr 2026. **Ein einzelnes Modul.**

Wenn sich 270.000 Module selbst repliziert haben? Das Aequivalent von Dutzenden Milliarden H100. Eine Rechenkapazitaet, die die gesamte aktuelle Kapazitaet der Menschheit uebersteigt, aus einem einzigen Asteroiden.

---

## Rohstoff: KI-Chips aus Schlacke

Hier liegt die Meisterleistung dieses Designs. Keine separate Halbleitermine noetig.

Beim Raffinieren von Asteroidenerz ist Fe-Ni (90 %+) das Hauptprodukt, und **der Rest ist Schlacke**. Der Hauptbestandteil der Schlacke ist SiO2 — Silikat. Das wird nicht weggeworfen.

```
Asteroidenerz -> Vakuumraffination
  +-> Fe-Ni (90 %+) -> Spiegel, Strukturen, Batterien, Turbinen
  +-> Schlacke (hauptsaechlich SiO2)
       +-> Grossteil -> Strahlungsabschirmung
       +-> Ein Teil -> Kohlenstoffreduktion (SiO2 + 2C -> Si + 2CO)
            -> metallisches Silizium
            -> Zonenraffination (Solarwaerme + Vakuum + Mikrogravitation)
            -> Halbleiterqualitaet Einkristall-Barren (Reinheit 9N+)
            -> 300-mm-Wafer
            -> 28nm-TPU
```

**Aus Raffinerieabfaellen werden KI-Chips.**

[Zonenraffination (zone refining)](https://en.wikipedia.org/wiki/Zone_melting) ist im Weltraum vorteilhaft. Es ist ein Reinigungsverfahren, bei dem eine schmale Schmelzzone durch einen Siliziumbarren wandert und Verunreinigungen herausdrueckt:

- **Energie:** Direkte Solarwaerme. Null Kosten
- **Vakuum:** Der Weltraum ist Vakuum. Verunreinigungen verdampfen automatisch
- **Mikrogravitation:** Die Schmelzzone fliesst nicht herunter. Auf der Erde ist das FZ-Verfahren (Float Zone) auf Barrendurchmesser von 200 mm begrenzt — darueber bricht geschmolzenes Silizium unter der Schwerkraft zusammen. **In Schwerelosigkeit sind 300 mm und mehr moeglich**
- **Wiederholung:** Spiegelwinkel anpassen fuer unbegrenzte Reinigungspaesse. Null Zusatzkosten

Auf der Erde ist Zonenraffination ein teurer Premium-Prozess im kleinen Massstab. Im Weltraum wird er zum **Standardprozess**.

---

## Die Fab: Der Weltraum ist ein Reinraum

Einer der groessten Kostenposten einer 28nm-Fab auf der Erde: der Reinraum Klasse 1-10. Weniger als 10 Partikel mit 0,5 um Durchmesser oder groesser pro Kubikfuss Luft. Das aufrechtzuerhalten erfordert riesige HEPA-Filtersysteme, Luftbehandlungsanlagen und Ueberdruckmanagement. Ein erheblicher Teil der Fab-Baukosten fliesst hier ein.

Im Weltraum gibt es **keine Luft.** Die Partikelkontaminationsquelle fehlt schlicht. Vakuum ist ein **perfekter Reinraum.**

Weltraumtauglichkeit nach Fertigungsstufe (7 Stufen):

| Stufe | Weltraumtauglichkeit | Grund |
|-------|---------------------|-------|
| Barrenwachstum | **Weltraumvorteil** | FZ bei Mikrogravitation, grosse Barrendurchmesser |
| Wafer-Zuschnitt | Moeglich | Mechanischer Prozess, umgebungsunabhaengig |
| Oxidation/Abscheidung (CVD, PVD) | **Vakuumvorteil** | Auf der Erde muss die Kammer evakuiert werden — Weltraum ist schon Vakuum |
| Photolithographie | Engpass | ArF-Scanner und Photoresist erdabhaengig |
| Aetzen | **Vakuumvorteil** | Plasmaaeatz-Kammervereinfachung |
| Ionenimplantation | **Vakuumvorteil** | Weniger Strahlstreuung, keine Hochvakuumpumpe noetig |
| Verdrahtung/Packaging | Moeglich | Cu von Asteroiden/Mond beschaffbar |

**6 von 7 Stufen sind im Weltraum vorteilhaft oder gleichwertig.** Der einzige Engpass ist Photolithographie — den ArF-Scanner selbst kann man im Weltraum nicht bauen. Aber einmal hochgebracht, haelt er Jahrzehnte.

---

## Fab-Waermemanagement: „Halbleiter im Weltraum fertigen?"

„Die sonnenzugewandte Seite hat Hunderte Grad, die abgewandte -100°C, und +-0,01°C Kontrolle soll moeglich sein?"

Ja. Und **einfacher als auf der Erde.**

### Der Kern des Problems

Das Projektionslinsensystem des ArF-Lithographiescanners ist extrem empfindlich gegenueber thermischer Ausdehnung. 0,01°C Temperaturschwankung aendert die Linsenkruemmung, erzeugt Overlay-Fehler und senkt die Ausbeute. Die Overlay-Toleranz des 28nm-Prozesses betraegt wenige nm.

Wie irdische Fabs das loesen:
- Gesamter Reinraum bei 23,00 +- 0,1°C temperiert
- Scanner-intern +-0,01°C Kontrolle ueber dedizierten Kuehlkreislauf
- **Problem:** Externe Stoerungen kommen staendig — Aussentemperaturschwankungen, Jahreszeiten, Tag/Nacht, Wetter, Erdbeben, Strassenvibrationen, Waerme benachbarter Geraete

### Thermisches Design der Weltraum-Fab

```
[Querschnitt des Fab-Moduls]

Aussen: Weltraumvakuum (Leitung null, Konvektion null)
  |
  +- MLI-Reflexionswand (Mehrschicht-Reflexionsisolierung, Dutzende Schichten)
  |    -> Blockierung der solaren Strahlungswaerme zu 99,5 %+
  |    -> Blockiert auch Strahlungsverluste innen->aussen
  |
  +- Strukturelle Aussenwand (Fe-Ni)
  |
  +- Aktive Fluessigkeitszirkulationsschicht
  |    -> Feine Zirkulation von Reinstwasser (UPW)
  |    -> Aktive Steuerung durch Pumpe + Heizer + Ablassventil
  |    -> Innenwand gleichmaessig bei 23,00 +- 0,05°C
  |
  +- Fab-Innenraum (1 atm N2-Atmosphaere)
       -> Geraetewaerme -> aufgenommen vom zirkulierenden Kuehlmittel
       -> Scanner-intern: dedizierter Kuehlkreislauf +-0,01°C
```

### Warum einfacher als auf der Erde

| Element | Irdische Fab | Weltraum-Fab-Modul |
|---------|-------------|-------------------|
| Externe Waermestoerungen | Staendig (Wetter, Jahreszeiten, Tag/Nacht) | **Keine** — Vakuumisolierung |
| Externe Vibrationen | Strassen, Erdbeben, Nachbarfabriken | **Keine** — Schwerelosigkeit ohne Vibration |
| Isolierungskosten | HVAC verbraucht 30-40 % der Fab-Leistung | **Vakuum ist kostenlose Isolierung** |
| Vorhersagbarkeit der Waermequellen | Externe Stoerungen + interne Geraete | **Nur interne Geraete** (vollstaendig vorhersagbar) |
| Waermeabfuhr | Kuehltuerme, Chiller (massiver Wasser- und Stromverbrauch) | **Radiatoren** (Vakuumstrahlung) |

Das zentrale Paradox: Die extreme Waermeumgebung des Weltraums (Hunderte Grad vs -100°C) **erreicht das Fab-Innere nicht.** Vakuum ist der beste Isolator, und sobald MLI die Strahlung blockiert, ist das Fab-Innere thermisch komplett vom Aussen isoliert. Danach muss nur noch die Waerme interner Geraete gemanagt werden — und das ist einfacher als auf der Erde, weil externe Stoerungen null sind.

Irdische Fabs geben 30-40 % ihrer Gesamtleistung fuer HVAC aus, weil sie **staendig gegen die Umgebung kaempfen**. Die Weltraum-Fab hat diesen Kampf nicht.

### UPW — kommt vom Batholyzer

Das Reinstwasser (UPW) fuer die thermostatische Zirkulation der Fab stammt aus Batholyzer-Produkten:

```
Batholyzer: H2O -> H2 + O2 (Elektrolyse)
Umkehrreaktion: H2 + O2 -> H2O (Brennstoffzelle)

Nebenprodukt H2O -> Reinigung -> UPW
  +-> Thermostatisches Zirkulationskuehlmittel der Fab
  +-> Wafer-Reinigung
  +-> Immersionslithographie-Fluessigkeit
```

### Kuenstliche-Schwerkraft-Abteilung

Die Immersionslithographie erfordert einen Duennfilm aus Reinstwasser auf dem Wafer — dafuer wird Schwerkraft benoetigt. Das Fab-Modul wird in zwei Abteilungen unterteilt:

```
Vakuum-Abteilung (0G):
  +-> CVD/PVD-Abscheidung (Vakuum erforderlich)
  +-> Ionenimplantation (Vakuum erforderlich)
  +-> Plasmaaetzen (Vakuum erforderlich)

Kuenstliche-Schwerkraft-Abteilung (~1G Rotation):
  +-> ArF-Immersionslithographie (Schwerkraft fuer Fluessigkeitsmanagement noetig)
  +-> Nassreinigung (Schwerkraft fuer UPW-Reinigung noetig)
  +-> Wafer-Handling (Robotertransfer)
```

Wafer wechseln ueber Schleusen zwischen Vakuum- und Kuenstliche-Schwerkraft-Abteilung. Die Rotationsabteilung hat keine externe Vibrationsquelle, sodass **nur die Gleichmaessigkeit der Rotation selbst gemanagt werden muss** — weit einfacher als auf der Erde Erdbeben und Strassenvibrationen abzuwehren.

---

## Externe Abhaengigkeit: 5 %

| Kategorie | Beschaffung | Anmerkung |
|-----------|-------------|-----------|
| Silizium | Lokal (Schlacke -> Si) | |
| Energie | Lokal (Solarwaerme) | |
| Reinraum | Lokal (Weltraumvakuum) | |
| Reinstwasser | Lokal (Batholyzer H2O -> Reinigung) | |
| Kupferverdrahtung | Lokal (Asteroiden/Mond) | |
| ArF-Scanner | **Erde, einmalig** | Jahrzehnte Lebensdauer |
| Photoresist | **Erde, 1x/Jahr** | Einige Hundert kg/Jahr |
| Aetzgas | **Erde, 1x/Jahr** | Recycelbar, geringe Menge |
| Dotierelemente (B, As) | **Erde, 1x/Jahr** | Einige Dutzend kg |

95 % werden im Weltraum beschafft. Die restlichen 5 % — ArF-Scanner (einmalig) + Verbrauchsmaterial (einige Tonnen/Jahr) — koennen mit einem einzigen Starship-Start fuer Jahrzehnte mitgenommen werden.

„Photoresist ist praezise organische Chemie, oder?" — Ja. Lokale Herstellung ist schwierig. Aber der Jahresverbrauch liegt bei einigen Hundert Kilogramm. Ein Starship-Start kann Jahrzehnte-Vorraete mitfuehren. Keine vollstaendige Autarkie, aber eine **faktische Autarkie**.

---

## Die Selbstreplikationsschleife schliesst sich

```
Vorher:
  Asteroidenerz -> Raffination -> Fe-Ni -> Spiegel, Strukturen, Batterien -> Selbstreplikation
                                                                             ^
                                                                  KI-Chips von der Erde importiert

Jetzt:
  Asteroidenerz -> Raffination -> Fe-Ni -> Spiegel, Strukturen, Batterien, Turbinen
                               -> Schlacke -> Si-Barren -> 28nm-TPU -> KI-Autonomsteuerung
                                                                       |
                                                            Selbstreplikationsschleife geschlossen
```

Spiegel bauen Spiegel. Batterien erzeugen Treibstoff. **Schlacke erzeugt KI-Chips.** Nichts wird verschwendet.

---

## Zusammenfassung in einem Satz

Modernste 3nm-Chips sind ohne ASMLs exklusives EUV nicht herstellbar — im Weltraum unmoeglich. 28nm ist allein mit ArF realisierbar, und Googles TPU v1 hat 92 TOPS im Praxisbetrieb bewiesen. Der 4,6-fache Leistungsnachteil entspricht 2,4 m2 Spiegelflaeche bei einem 370-MW-Modul. Silizium kommt aus der Schlacke, der Weltraum selbst ist ein Reinraum, und Vakuumisolierung macht +-0,01°C Waermemanagement einfacher als auf der Erde. Das letzte Glied der Selbstreplikationsschleife.

![Die-Foto eines TTL-4-Eingang-NAND-Gatter-Chips. Foto: Dgarte / Wikimedia Commons / CC BY-SA 3.0](/images/why-28nm.webp)
