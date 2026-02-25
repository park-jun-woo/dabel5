---
title: "Warum nicht vor Ort schmelzen"
date: 2026-02-24T12:00:04+09:00
lastmod: 2026-02-24T12:00:04+09:00
tags: ["asteroidenbergbau", "transport", "SMR", "NTP"]
image: "/images/1986da-orbit.webp"
summary: "Ein vollstandiges technisches Design fur den Abbau des metallischen Asteroiden 1986 DA mit einem SMR-betriebenen Bergbauschiff, Verpackung von Erz in Fe-Ni-Drahtnetzen und Transport von 200.000 Tonnen pro Transferfenster."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

*Orbital visualization: [SpaceReference.org](https://www.spacereference.org/asteroid/6178-1986-da), built with [SpaceKit](https://typpo.github.io/spacekit/). Data: JPL Small Body Database.*

## Abbau klingt gut, aber wie?

Im vorherigen Artikel haben wir 1986 DA als Rohstoffquelle fur einen Dyson-Schwarm vorgeschlagen. Uber 90 % Fe-Ni, Mikrogravitation, null Abfall. In jeder Hinsicht besser als Merkur fur das Bootstrapping.

Aber eine Frage bleibt: **Wie baut man tatsachlich einen Metallklumpen in Mikrogravitation ab, und wie transportiert man ihn?**

Zuerst das Grundprinzip: **"Vor Ort wird nur gegraben, zerkleinert und verpackt. Die schwere Arbeit findet dort statt, wo Energie im Uberfluss vorhanden ist."**

---

## Rollenverteilung: Vor Ort vs Basis

| Aufgabe | Ort | Grund |
|---------|-----|-------|
| Abbau und Zerkleinerung | 1986 DA vor Ort | Wo das Erz ist |
| Verpackung (Drahtnetz) | 1986 DA vor Ort | Aus lokalem Fe-Ni gefertigt |
| Sortierung | **Entfallt** | Jede Komponente hat eine Verwendung |
| Verhuttung | **Basis (Dyson-Spiegel)** | Spiegel-Solarwarme GW-Klasse >> vor Ort SMR kW-Klasse |
| Fertigung und Montage | **Basis** | Spezialisierte Cluster |

Warum nicht vor Ort verhutten? Die Verhuttung erfordert 1.600°C. Der SMR vor Ort produziert 50~100 kW. Die Dyson-Spiegel der Basis liefern ca. 600 MW (thermisch). **Der Energieunterschied betragt das Tausendfache.** Eine Schmelzhutte auf dem Asteroiden zu bauen ist wie ein Stahlwerk auf einem Berggipfel -- es ist sinnvoller, das Erz zu verschiffen.

---

![mining-transport](/images/post004.webp)

## Das Bergbauschiff: Eine Maschine, die grabt, zerkleinert und verpackt

### Energie: SMR + Solarboost

Die stark elliptische Umlaufbahn von 1986 DA (Exzentrizitat 0,58) lasst den Solarfluss je nach Bahnposition um mehr als das 14-fache schwanken.

| Bahnposition | Entfernung | Solarfluss | vs Erde |
|-------------|------------|------------|---------|
| Perihel | 1,17 AU | ~995 W/m² | 73 % |
| Halbachse | 2,81 AU | ~172 W/m² | 13 % |
| Aphel | 4,46 AU | ~68 W/m² | 5 % |

**Solarenergie allein kann keinen kontinuierlichen Abbau aufrechterhalten.** Ein SMR (kleiner modularer Reaktor, 50~100 kW) ist die primare Energiequelle. In Perihelnahe liefern Solarpanels zusatzlichen Boost.

| Bahnabschnitt | SMR | Solar | Gesamt | Modus |
|--------------|-----|-------|--------|-------|
| Perihelnahe (~1,2 AU) | 50~100 kW | 50~100 kW | **100~200 kW** | Boost |
| Mittlere Bahn (~2,8 AU) | 50~100 kW | ~15 kW | ~65~115 kW | Normal |
| Aphelnahe (~4,5 AU) | 50~100 kW | ~5 kW | ~55~105 kW | Langsam |

Selbst am Aphel halt der SMR den Abbau aufrecht. Er wird nur langsamer.

### Ausrustung

| Ausrustung | Funktion | Leistungsaufnahme |
|------------|----------|-------------------|
| Bagger | Oberfachen-/Untertagebau | ~20~50 kW |
| Brecher | Zerkleinerung auf Transportgrosse | ~10~30 kW |
| Kleiner Elektroofen | Fe-Ni → Drahtrohmaterial | ~10~20 kW |
| Drahtziehmaschine | Draht → Maschennetz | ~5~10 kW |
| Steuerung und Kommunikation | KI-autonome Steuerung | ~5 kW |
| **Gesamt** | | **~50~115 kW** |

Ein einziger SMR betreibt die gesamte Ausrustung. Das Bergbauschiff ist **dauerhaft stationiert** -- es umkreist 1986 DA und baut ohne Pause ab.

### Produktivitat

Konservative Annahme: durchschnittlich 50 kW Einsatz, ca. 100 kg Erz pro kWh verarbeitet (mechanische Zerkleinerung in Mikrogravitation ist vergleichbar mit den terrestrischen 10-25 Wh/kg; die Verhüttung erfolgt separat an der Basis).

| Posten | Wert |
|--------|------|
| Tagliche Forderung | ~120 Tonnen |
| Jahrliche Forderung | ~43.800 Tonnen |
| **Pro Umlaufperiode (4,71 Jahre)** | **~200.000 Tonnen** |

---

## Container: Netze, keine Kisten

Was braucht ein Frachtcontainer im Weltraum?
- Druckdichtung -- Vakuum, unnotig
- Eigengewichtsstutzung -- Mikrogravitation, unnotig
- Luftwiderstand -- Vakuum, unnotig
- **Das Erz darf sich wahrend des Transports nicht verstreuen**

Das ist die einzige Anforderung. Keine starre Kiste -- **ein Netz genugt.**

### Herstellungsprozess

```
Gefodertes Erz
  ├─ 99,5 % → Fracht (Erzbundel)
  └─ 0,5 % → Kleiner Elektroofen → Drahtziehen → Netzweben
                                                 → Erzbundel verpacken
```

| Methode | Masse-Verhaltnis Container:Fracht |
|---------|----------------------------------|
| Metallcontainer von der Erde | Extremer Transportabfall |
| Vor Ort gegossene Fe-Ni-Kisten | ~2~3 % (uberdimensioniert) |
| **Vor Ort gefertigtes Fe-Ni-Drahtnetz** | **~0,1~0,5 %** |

**Das Netz selbst wird bei Ankunft als Schmelzrohstoff eingesetzt.** Sogar die Verpackung wird zu 100 % genutzt.

---

## Transport: Transferfenster und Antrieb

### Bahnmechanik

Umlaufperiode von 1986 DA: 4,71 Jahre. Das optimale Transferfenster zum Erdraum offnet sich einmal pro Umlaufperiode.

| Posten | Wert |
|--------|------|
| LEO → 1986 DA Rendezvous | delta-V ~7,1 km/s |
| Optimaler Abflug | Perihelnahe (1,17 AU) |
| Nachste Annaherung | **2038 (0,21 AU)** |

### Antriebsoptionen

| Methode | Spezifischer Impuls (Isp) | Eigenschaften | Eignung |
|---------|--------------------------|---------------|---------|
| Chemisch (LH2/LOX) | ~450 s | Extrem niedriger Nutzlastanteil | ❌ |
| **Nuklearthermischer Antrieb (NTP)** | **~900 s** | Hoher Schub, schnell | ✅ |
| **Nuklearelektrischer Antrieb (NEP)** | **~3.000 s+** | Minimaler Treibstoff, langsam | ✅ Massentransport |
| Solarelektrischer Antrieb (SEP) | ~3.000 s | Effizienz bricht am Aphel ein | ⚠️ Begrenzt |

**Ein NTP + NEP-Hybrid konnte optimal sein:** Ein einziger Reaktor dient als NTP-Warmequelle (hoher Schub fur den Perihel-Abflug) und als NEP-Stromquelle (niedriger Schub, hohe Effizienz im Reiseflug).

### Logistikzyklus

```
[Jahr 0]  Bergbauschiff erreicht 1986 DA, Abbau beginnt
             │ 4,71 Jahre Abbau, Verpackung, Lagerung (~200.000 Tonnen)
[Jahr ~5] Transferfenster → Transportschiff wird beladen und startet
             │ Hohmann-Transfer (~2-3 Jahre)
[Jahr ~7] Transportschiff kommt an, Erz wird entladen
             │ Wartung und Nachschub
[Jahr ~8] Transportschiff startet Ruckflug
             │
[Jahr ~10] Zweite Beladung ... Zyklus wiederholt sich
```

Das Bergbauschiff bleibt; das Transportschiff pendelt. Abbau und Transport laufen **asynchron parallel.**

---

## 2038: Verpassen heisst Jahrzehnte warten

| Zeitpunkt | Ereignis |
|-----------|----------|
| 2030er | Starship kommerzialisiert, Weltraum-SMR-Technologie ausgereift |
| **2038** | **1986 DA Annaherung (0,21 AU) -- optimales Fenster fur Bergbauschiff-Einsatz** |
| 2038~2042 | Bergbauschiff erreicht den Standort, Abbau beginnt |
| ~2043 | Erstes Transportschiff beladen und gestartet |
| **~2046** | **Erste Erzlieferung** |

Nach 2038 liegt die nachste Annaherung dieser Grossenordnung Jahrzehnte entfernt. **Dieses Fenster zu verpassen verschiebt den Zeitplan erheblich.**

### Status der benotigten Technologien

| Technologie | Aktuell (2026) | Ausblick 2038 |
|-------------|---------------|---------------|
| Starship (Schwerlasttrager) | Testfluge laufen | ✅ Kommerzialisierung erwartet |
| Weltraum-SMR | NASA FSP 40-kW-Klasse in Entwicklung | ✅ Monddemonstration erwartet |
| NTP-Antrieb | DARPA DRACO in Entwicklung | ⚠️ Testflug erwartet |
| Asteroidenbergbau | OSIRIS-REx Probenruckfuhrung erfolgreich | ⚠️ Grossmassstab unbewiesen |
| KI-autonomer Weltraumbetrieb | Mars-Rover-Niveau | ✅ Ausreichende Reife erwartet |

Keine dieser Technologien ist unmoglich. Alle sind **in Entwicklung oder werden voraussichtlich innerhalb eines Jahrzehnts ausgereift sein.**

---

## Nach der Ankunft: Die Sonne schmilzt

Wenn das Erz ankommt, erhitzen Dyson-Spiegel es direkt auf 1.600°C. Das Weltraumvakuum ist "kostenlose Raffinierungsausrustung":

1. **Optisches Schmelzen** -- Konzentrierte Spiegelwarme schmilzt Roherz zu flussigem Metall
2. **Vakuumentgasung** -- Schwefel und Phosphor verdampfen naturlich im Vakuum (aufgefangen in Kaltefallen)
3. **Zentrifugaltrennung** -- Aussenschicht: Fe-Ni + Platingruppenmetalle / Innenschicht: Silikatschlacke

```
Erzbundel kommt an
  ├→ Fe-Ni-Drahtnetz → in Schmelze eingefuhrt (Verpackung wird Rohstoff)
  └→ Erz → Spiegelerhitzung auf 1.600°C
       ├→ Fe-Ni-Legierung (90 %+) → Strukturteile, Spiegelrahmen, Rohre
       ├→ Silikatschlacke → Abschirmung + Siliziumbarren-Rohstoff
       ├→ Platingruppenmetalle → Beschichtungen, Katalysatoren
       └→ S, P → Chemierohstoffe, Halbleiterdotierung
```

Was irdische Stahlwerke mit enormem Energie- und Chemikalieneinsatz erreichen, **liefern Weltraumvakuum und Solarwarme kostenlos.**

---

## Zusammenfassung in einem Satz

Das Bergbauschiff grabt, zerkleinert und verpackt mit einem einzigen SMR. Container sind lokale Fe-Ni-Drahtnetze -- sogar die Verpackung ist Rohstoff. Das Transportschiff befordert 200.000 Tonnen pro Transferfenster. 2038 ist das erste Gelegenheitsfenster. Das ankommende Erz wird von der Sonne geschmolzen. Nichts wird verschwendet.
