---
title: "Warum Nickel-Eisen-Batterien statt Lithium-Ionen"
date: 2026-02-25T12:00:01+09:00
lastmod: 2026-02-25T12:00:01+09:00
tags: ["nickel-eisen-batterie", "edison-batterie", "battolyser", "ESS", "selbstreplikation"]
image: "/images/why-iron-nickel-battery.webp"
summary: "Auf Asteroiden gibt es kein Lithium, im Weltraum kann man nicht alle 10 Jahre austauschen, und im Vakuum kann man kein Feuer loeschen. Nickel-Eisen-Batterien werden aus Nebenprodukten der Asteroidenverhuettung hergestellt, halten 30-50 Jahre, und nach voller Ladung produzieren sie Wasserstoff und Sauerstoff."
author: "Park Jun Woo"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Von Edison 1901 entwickelte Nickel-Eisen-Batterien. Thomas Edison National Historical Park. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0"
---

## "Energiespeicherung ist doch selbstverstaendlich Lithium-Ionen?"

Dyson-Module buendeln Sonnenlicht mit Spiegeln und treiben Turbinen an. Es waere schoen, wenn die Sonne 24 Stunden am Tag, 365 Tage im Jahr scheinen wuerde, aber die Realitaet sieht anders aus.

- **Finsternisse (Eclipse):** Der EML5-Stuetzpunkt tritt 2-3 Mal pro Jahr fuer insgesamt 3-12 Stunden in den Schatten von Erde und Mond ein
- **Lastschwankungen:** Turbinen reagieren langsam auf abrupte Lastaenderungen. Ohne ESS schwankt die Spannung bei momentanen Bedarfsaenderungen
- **Notabschaltung:** Bei Spiegelwartung oder Turbinenausfall duerfen kritische Systeme — Lebenserhaltung, KI, Kommunikation — nicht ausfallen
- **Startstrom:** Beim Andocken und Ausweichmanoever von Schleppern wird kurzzeitig hohe Leistung benoetigt

Ohne Batterie funktioniert ein Dyson-Modul nicht. Welche Batterie also?

Auf der Erde ist die Antwort offensichtlich. Lithium-Ionen. Energiedichte, Lade-/Entladeeffizienz, Gewichtsreduktion — in allen Kennzahlen fuehrend. Aber aus demselben Grund, warum Turbinen in einem frueheren Beitrag Solarpanels ueberlegen waren, **gelten im Weltraum andere Masstaebe.**

Lithium-Ionen muessen alle 10 Jahre ausgetauscht werden, und die naechste Lithiummine befindet sich auf der Erde. Auf Asteroiden stolpert man ueber Eisen und Nickel.

---

## Irdische Masstaebe vs. Weltraum-Masstaebe

| Kriterium | Nickel-Eisen (Edison) | Lithium-Ionen | Was zaehlt im Weltraum? |
|-----------|----------------------|---------------|------------------------|
| Volumetrische Energiedichte | 30-60 Wh/L | 250-700 Wh/L | Im km²-Massstab ist Volumen bedeutungslos |
| Gravimetrische Energiedichte | 30-50 Wh/kg | 150-270 Wh/kg | Unbewegliche Strukturen → irrelevant |
| Lebensdauer | **30-50 Jahre** | 5-15 Jahre | Austauschkosten sind im Weltraum **astronomisch** |
| Ueberladungstoleranz | **Extrem hoch** | Gering (thermisches Durchgehen, Brand) | Feuer im Vakuum = Totalverlust des Moduls |
| Tiefentladungstoleranz | **Hoch** | Irreversible Schaeden | Vollstaendige Entladung bei Eclipse moeglich |
| Lokale Materialbeschaffung | **Moeglich** (Fe, Ni, KOH) | **Unmoeglich** (Li, Co, organischer Elektrolyt) | Existenzfrage der Selbstreplikationsschleife |
| Elektrolyt | Kaliumhydroxid-Loesung (wasserbasiert) | Organisches Loesungsmittel (entflammbar) | Strahlungsstabilitaet, Brandsicherheit |
| Selbstentladung | Hoch (~1%/Tag) | Niedrig (~0,1%/Tag) | Bei Dauerladeumgebung bedeutungslos |

**Was auf der Erde zaehlt: Leicht, klein, hohe Energiedichte.**
**Was im Weltraum zaehlt: Vor Ort herstellbar, sicher, langlebig.**

Andere Masstaebe, andere Antworten.

---

## Material — Auf Asteroiden gibt es kein Lithium

Um eine Lithium-Ionen-Batterie herzustellen, braucht man:

| Material | Verwendung | Vorkommen auf Asteroiden |
|----------|-----------|------------------------|
| Lithium (Li) | Kathodenaktivmaterial | **Nicht vorhanden** — Urknall-Nukleosynthese-Element, in Gesteinsasteroiden nur in Spuren |
| Kobalt (Co) | Kathodenstabilisierung | Nur in Spuren — wirtschaftliche Gewinnung unmoeglich |
| Graphit (C) | Anode | In kohlenstoffhaltigen Asteroiden vorhanden, aber nicht als kristalliner Graphit |
| Organischer Elektrolyt | Ionenleitung | **Synthese erforderlich** — Ethylencarbonat usw., komplexe organische Chemie |
| Separator (PE/PP) | Kurzschlussschutz | **Synthese erforderlich** — Praezisionspolymerfertigung |

Es gibt kein Lithium. Das allein ist Game Over. Wenn man staendig von der Erde nachliefern muss, ist das **keine Selbstreplikation, sondern Nachschubabhaengigkeit**.

"Was ist mit Natrium-Ionen?" Na kommt auf Asteroiden vor. Aber eine Lebensdauer von 30-50 Jahren ist nicht nachgewiesen, es gibt keine Battolyser-Funktion, und organischer Elektrolyt ist noetig. Das Problem, dass Weltraumstrahlung organische Elektrolyte degradiert, besteht bei Natrium-Ionen genauso.

"Kommen nicht bald Festkoerperbatterien?" Wenn man sie nicht auf Asteroiden herstellen kann, nuetzen sie nichts, egal wie gut sie sind. Der Schluesselfaktor ist nicht die Energiedichte, sondern die **lokale Herstellbarkeit**.

Um eine Nickel-Eisen-Batterie herzustellen, braucht man:

| Material | Verwendung | Herkunft |
|----------|-----------|---------|
| Eisen (Fe) | Anode | Hauptbestandteil von 1986 DA — **ueberall vorhanden** |
| Nickel (Ni) | Kathode | Hauptbestandteil von 1986 DA — **ueberall vorhanden** |
| Kaliumhydroxid (KOH) | Elektrolyt | K in Asteroidensilikaten enthalten, Wasser aus kohlenstoffhaltigen Asteroiden |
| Stahlblech | Gehaeuse | Fe-Ni-Legierungsverarbeitung |

**Alle Batteriekomponenten sind Nebenprodukte des Verhuettungsprozesses.** Beim Bau von Spiegelrahmen koennen gleichzeitig Batterien hergestellt werden. Zusaetzlicher Rohstoffimport: null.

---

## Lebensdauer — Austauschkosten bestimmen alles

Auf der Erde sind 10-15 Jahre Lithium-Ionen-Lebensdauer ausreichend. Die Austauschkosten beschraenken sich auf den Batteriepreis.

Im Weltraum umfassen die Austauschkosten:
1. Neue Batterieherstellung (falls moeglich)
2. Transport (falls nicht moeglich, von der Erde — **tausende Dollar pro kg**)
3. EVA- oder Roboteraustauscharbeiten
4. Systemausfallzeit waehrend des Austauschs

**Nickel-Eisen-Batterie-Lebensdauer: 30-50 Jahre.** Es gibt **noch funktionierende Exemplare** von Edisons Nickel-Eisen-Batterien aus dem Jahr 1901. Wenn man den Elektrolyten (KOH-Loesung) nur alle 10-15 Jahre auffuellt, halten die Elektroden praktisch ewig.

Die einzige Batteriechemie, die **null Austausch** waehrend der gesamten Modulllebensdauer ermoeglicht.

---

## Sicherheit — Feuer im Vakuum bedeutet Tod

Der organische Elektrolyt von Lithium-Ionen-Batterien ist entflammbar. Bei Ueberladung, physischer Beschaedigung oder internem Kurzschluss:

```
Interne Temperaturerhoehung → Separatorschrumpfung → Kurzschlussausweitung → Elektrolytzersetzung
→ Freisetzung brennbarer Gase → Entzuendung → Thermisches Durchgehen benachbarter Zellen
```

Auf der Erde: Die Feuerwehr kommt.
Im Weltraum: **Im Vakuum gibt es keine Feuerwehr.** Brand in einem abgedichteten Modul = Verlust der Lebenserhaltung + toxische Gasanreicherung + keine Rettung.

Selbst auf der ISS gehoeren Lithium-Ionen-Braende zu den gefuerchtetsten Szenarien. Bei tausenden Dyson-Modulen mit Lithium-Ionen-Batterien sind **Braende statistisch gesehen unvermeidlich**.

Die inhaerent Sicherheit von Nickel-Eisen:

- Elektrolyt: Kaliumhydroxid-**Wasserlosung** — wasserbasiert. Brennt nicht
- Bei Ueberladung: Wasser wird zu H₂ + O₂ elektrolysiert — kein thermisches Durchgehen
- Bei Tiefentladung: Keine irreversiblen Elektrodenschaeden — Wiederaufladung moeglich
- Bei physischer Beschaedigung: KOH-Austritt — aetzend, aber **keine Explosion, kein Brand**

**"Eine Batterie, die nicht brennt" ist im Weltraum kein Luxus, sondern eine Notwendigkeit.**

---

## Battolyser — Eine Batterie, die gleichzeitig Wasserelektrolyse betreibt

Hier geht Nickel-Eisen ueber eine blosse "zweitbeste Loesung" hinaus und bietet einen **einzigartigen Vorteil**.

### Prinzip

Das von der TU Delft entwickelte Battolyser-Konzept. Es nutzt aktiv die Ueberladungstoleranz der Nickel-Eisen-Batterie:

```
[Waehrend des Ladens]     Elektrische Energie → Chemische Energiespeicherung in Fe/Ni-Elektroden
[Nach Vollladung]          Zusaetzlicher Strom → Elektrolyse des Wassers in der KOH-Loesung
                           Kathode: 2H₂O + 2e⁻ → H₂↑ + 2OH⁻
                           Anode: 2OH⁻ → ½O₂↑ + H₂O + 2e⁻
```

**Ein einziges Geraet vereint Batterie + Elektrolyseur.** Keine separate Elektrolyseanlage erforderlich. Einsparung bei Masse, Volumen und Komplexitaet.

Bei Lithium-Ionen bedeutet Ueberladung = Brand. Bei Nickel-Eisen bedeutet Ueberladung = **Wasserstoffproduktion**.

### Betriebszyklus im Dyson-Modul

```
[Normalbetrieb] Turbine 370 MW in Betrieb
  ├→ Lastverbrauch (~320 MW)
  └→ Ueberschussleistung (~50 MW) → Battolyser-Modus
       └→ H₂ ~890 kg/h + O₂ ~7.100 kg/h Akkumulation (bei ~70% Elektrolyseeffizienz)

[Finsternis (Eclipse)] 3-12 Stunden/Jahr
  ├→ Batterieentladung (ESS-Modus)
  └→ Akkumuliertes H₂ → Brennstoffzellen-Stromerzeugung (parallel)
       → Verfuegbare Energie 2x+ gegenueber Batterie allein

[Notabschaltung]
  └→ H₂/O₂-Doppelspeicher → Verlaengerung der Lebenserhaltung
```

### Ueber Energiespeicherung hinaus

Das vom Battolyser erzeugte H₂ und O₂ geht ueber einfache Energiespeicherung hinaus und wird in den **gesamten Materialkreislauf des Moduls** integriert:

| Produkt | Verwendung | Anmerkung |
|---------|-----------|-----------|
| H₂ | NTP-Schlepper-Treibstoffnachschub | Arbeitsmedium der nuklearthermischen Antriebe |
| H₂ | Reduktionsmittel im Verhuettungsprozess | Metalloxid → Reinmetall (FeO + H₂ → Fe + H₂O) |
| H₂ | Brennstoffzellen-Notstromerzeugung | Backup-Strom bei Eclipse/Wartung |
| H₂ | Haber-Bosch → NH₃ → Duenger | Landwirtschaft im Habitatmodul |
| O₂ | Lebenserhaltung (Atmung) | Unverzichtbar im Habitatmodul |
| O₂ | Oxidationsmittel (Schweissen, Medizin) | Lokale Fertigungsprozesse |

Eine Batterie, die Energie speichert und gleichzeitig Treibstoff, Reduktionsmittel und Atemsauerstoff produziert. Lithium-Ionen speichern nur Strom.

---

## "Ist 1/10 der Energiedichte nicht zu gross?"

Richtig. Um die gleiche Energie zu speichern, braucht Nickel-Eisen das **5- bis 10-fache Volumen** von Lithium-Ionen.

Aber:

```
Dyson-Modul-Massstab:
  Spiegel: 1 km × 1 km = 1.000.000 m²
  Struktur: Mehrere km hinter dem Spiegel
  Gesamtvolumen: Mehrere Millionen m³

Benoetigte ESS-Kapazitaet (12 Stunden × 370 MW):
  4.440 MWh = 4.440.000 kWh

Nickel-Eisen (bei 40 Wh/L):
  111.000 m³ = 111 m × 111 m × 9 m

→ Weniger als 1% der Gesamtstruktur
```

In den mehreren Millionen m³ Struktur hinter einem 1 km²-Spiegel sind 111.000 m³ **eine Ecke**. Ausserdem kann die schwere Masse der Nickel-Eisen-Batterie als **Gegengewicht fuer rotierende Strukturen** genutzt werden. Der Nachteil wird zum Vorteil.

Dass die Selbstentladung mit ~1% pro Tag hoch ist, ist nur auf der Erde ein Problem. Da die Turbine rund um die Uhr, 365 Tage im Jahr laeuft, ist die Batterie immer geladen. Selbstentladung ist **bedeutungslos**.

"Kann man nicht einfach die Turbinenleistung erhoehen und braucht dann kein ESS?" Finsternisse und Notabschaltungen sind Situationen, in denen die Turbine **komplett stillsteht**. Stromerzeugung und Speicherung sind separate Probleme.

---

## Anpassung an die Weltraumumgebung

Eine terrestrische Nickel-Eisen-Batterie kann nicht einfach so ins All mitgenommen werden. Drei Anpassungen sind erforderlich.

### 1. Verhinderung der Elektrolytverdampfung

KOH-Wasserlosung verliert bei Vakuumexposition Feuchtigkeit durch Verdampfung. **Hermetisch abgedichtete Zellstruktur** ist zwingend erforderlich. Gluecklicherweise sind Batteriezellen grundsaetzlich hermetisch konstruiert. Fuer den Weltraumeinsatz muss lediglich das Dichtungsniveau erhoeht werden.

### 2. Gastrennung in Schwerelosigkeit

Im Battolyser-Modus haften H₂/O₂-Blasen an der Elektrodenoberflaeche. Auf der Erde loest der Auftrieb die Blasen ab, in der Schwerelosigkeit nicht.

**Loesung:** Hydrophobe Beschichtung der Elektrodenoberflaeche + Zentrifugalkraft durch Eigenrotation des Moduls zur Gastrennung. Eine Zentrifugalbeschleunigung von ~0,01G reicht fuer die Blasentrennung aus.

### 3. Strahlungsbestaendigkeit

KOH-Wasserlosung ist im Gegensatz zu organischen Elektrolyten **extrem stabil gegenueber Strahlung**. Organische Elektrolyte werden durch Strahlung degradiert, die Molekuelketten aufbricht. Bei waessriger Loesung tritt zwar eine geringe strahlungsinduzierte Wasserspaltung auf, die sich aber durch Rekombination natuerlich regeneriert. In Strahlungsumgebungen ist Nickel-Eisen gegenueber Lithium-Ionen **grundsaetzlich ueberlegen**.

---

## Zusammenfassung in einem Satz

Lithium-Ionen ist die beste Batterie der Erde. Aber auf Asteroiden gibt es kein Lithium, im Weltraum kann man nicht alle 10 Jahre austauschen, und im Vakuum kann man kein Feuer loeschen. Nickel-Eisen-Batterien koennen aus Nebenprodukten der Asteroidenverhuettung hergestellt werden, halten 30-50 Jahre ohne Austausch, brennen nicht, und verwandeln sich nach Vollladung in Wasserelektrolyseure, die Treibstoff und Atemsauerstoff produzieren. Dass die Energiedichte 1/10 betraegt, ist im km²-Massstab bedeutungslos.

Zu terrestrischen Anwendungen der Nickel-Eisen-Batterien siehe [Nickel-Eisen-Batterien als netzunabhaengige ESS](https://www.parkjunwoo.com/1/tech/iron-nickel-ess-rural-energy/).

![Von Edison 1901 entwickelte Nickel-Eisen-Batterien. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0](/images/why-iron-nickel-battery.webp)
