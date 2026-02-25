---
title: "Pourquoi des batteries nickel-fer et pas du lithium"
date: 2026-02-25T12:00:01+09:00
lastmod: 2026-02-25T12:00:01+09:00
tags: ["batterie-nickel-fer", "batterie-edison", "battolyser", "ESS", "autoreplication"]
image: "/images/why-iron-nickel-battery.webp"
summary: "Il n'y a pas de lithium sur les asteroides, on ne peut pas remplacer tous les 10 ans dans l'espace et on ne peut pas eteindre un incendie dans le vide. Les batteries nickel-fer sont fabriquees a partir de sous-produits de la fonte d'asteroides, durent 30-50 ans et, une fois chargees, produisent de l'hydrogene et de l'oxygene."
author: "Park Jun Woo"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Batteries nickel-fer developpees par Edison en 1901. Thomas Edison National Historical Park. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0"
---

## "Le stockage d'energie, c'est evidemment le lithium-ion, non?"

Le module Dyson concentre la chaleur solaire avec des miroirs pour entrainer des turbines. L'ideal serait que le soleil brille 24 heures sur 24, 365 jours par an, mais la realite est autre.

- **Eclipse :** La base a EML5 entre dans l'ombre de la Terre ou de la Lune 2 a 3 fois par an, pour un total de 3 a 12 heures
- **Fluctuation de charge :** Les turbines reagissent lentement aux changements brusques de charge. Sans ESS, la tension oscille face aux variations instantanees de demande
- **Arret d'urgence :** Lors de la maintenance des miroirs ou de pannes de turbines, les systemes critiques — support vital, IA, communications — ne peuvent pas s'arreter
- **Puissance de manoeuvre :** Une haute puissance instantanee est necessaire pour les manoeuvres d'arrimage et d'evitement des remorqueurs

Sans batteries, un module Dyson ne fonctionne pas. Alors, quel type de batterie?

Sur Terre, la reponse est evidente. Lithium-ion. Densite energetique, efficacite de charge/decharge, legerete — la meilleure sur tous les indicateurs. Mais, pour la meme raison que les turbines ont surpasse les panneaux solaires dans l'article precedent, **dans l'espace, les criteres sont differents.**

Le lithium-ion doit etre remplace tous les 10 ans, et la mine de lithium la plus proche est sur Terre. Sur les asteroides, le fer et le nickel se trouvent a chaque pas.

---

## Criteres terrestres vs criteres spatiaux

| Aspect | Nickel-fer (Edison) | Lithium-ion | Ce qui compte dans l'espace |
|--------|---------------------|-------------|----------------------------|
| Densite energetique volumetrique | 30~60 Wh/L | 250~700 Wh/L | A l'echelle de 1 km², le volume est sans importance |
| Densite energetique gravimetrique | 30~50 Wh/kg | 150~270 Wh/kg | Structure fixe sans transport → sans importance |
| Duree de vie | **30~50 ans** | 5~15 ans | Le cout de remplacement dans l'espace est **astronomique** |
| Tolerance a la surcharge | **Extremement elevee** | Faible (emballement thermique/incendie) | Dans le vide, incendie = perte totale du module |
| Tolerance a la surdecharge | **Elevee** | Dommage irreversible | Possibilite de decharge totale pendant un eclipse |
| Approvisionnement local en materiaux | **Possible** (Fe, Ni, KOH) | **Impossible** (Li, Co, electrolyte organique) | La survie de la boucle d'autoreplication |
| Electrolyte | Solution aqueuse d'hydroxyde de potassium (base eau) | Solvant organique (inflammable) | Stabilite aux radiations, securite incendie |
| Autodecharge | Elevee (~1%/jour) | Faible (~0.1%/jour) | Sans importance en environnement de charge continue |

**Ce qui compte sur Terre : leger, compact, haute densite energetique.**
**Ce qui compte dans l'espace : fabricable localement, sans danger mortel, durable.**

Si les criteres changent, la reponse change.

---

## Materiaux — il n'y a pas de lithium sur les asteroides

Pour fabriquer une batterie lithium-ion, il faut :

| Materiau | Usage | Disponibilite sur les asteroides |
|----------|-------|----------------------------------|
| Lithium (Li) | Materiau actif de la cathode | **N'existe pas** — element de la nucleosynthese du Big Bang, quantites infimes dans les asteroides rocheux |
| Cobalt (Co) | Stabilisateur de la cathode | Quantites infimes — extraction economiquement inviable |
| Graphite (C) | Anode | Existe dans les asteroides carbones, mais n'est pas du graphite cristallin |
| Electrolyte organique | Conduction ionique | **Necessite une synthese** — chimie organique complexe comme le carbonate d'ethylene |
| Separateur (PE/PP) | Prevention des courts-circuits | **Necessite une synthese** — fabrication precise de polymeres |

Il n'y a pas de lithium. Cela seul suffit a clore le debat. S'il faut recevoir des approvisionnements continus de la Terre, **ce n'est pas de l'autoreplication mais de la dependance logistique**.

"Et le sodium-ion?" Le Na existe sur les asteroides. Mais il n'a pas une duree de vie verifiee de 30-50 ans, n'a pas de fonction battolyser et necessite un electrolyte organique. Le probleme du rayonnement cosmique degradant l'electrolyte organique est identique avec le sodium-ion.

"Les batteries a l'etat solide arrivent bientot, non?" Si elles ne peuvent pas etre fabriquees sur un asteroide, aussi bonnes soient-elles, elles n'ont aucun sens. La cle n'est pas la densite energetique mais la **capacite de fabrication locale**.

Pour fabriquer une batterie nickel-fer, il faut :

| Materiau | Usage | Origine |
|----------|-------|---------|
| Fer (Fe) | Anode | Composant principal de 1986 DA — **on en trouve a chaque pas** |
| Nickel (Ni) | Cathode | Composant principal de 1986 DA — **on en trouve a chaque pas** |
| Hydroxyde de potassium (KOH) | Electrolyte | K present dans les silicates d'asteroides, eau extraite des asteroides carbones |
| Tole d'acier | Boitier | Mise en forme de l'alliage Fe-Ni |

**Tous les composants de la batterie sont des sous-produits du processus de fonte.** On peut fabriquer des batteries tout en fabriquant des cadres de miroirs. Zero importation de matieres premieres supplementaires.

---

## Duree de vie — le cout de remplacement decide de tout

Sur Terre, la duree de vie de 10-15 ans du lithium-ion est suffisante. Le cout de remplacement se resume au prix de la batterie.

Dans l'espace, le cout de remplacement comprend :
1. Fabriquer une nouvelle batterie (si possible)
2. Transport (si la fabrication est impossible, depuis la Terre — **des milliers de dollars par kg**)
3. Travail de remplacement par EVA ou robot
4. Temps d'arret du systeme pendant le remplacement

**Duree de vie de la batterie nickel-fer : 30-50 ans.** Il existe **des cas de batteries nickel-fer fabriquees par Edison en 1901 qui fonctionnent encore**. Il suffit de renouveler l'electrolyte (solution aqueuse de KOH) tous les 10-15 ans ; les electrodes sont pratiquement permanentes.

La seule chimie de batterie permettant **zero remplacement** pendant toute la duree de vie de conception du module.

---

## Securite — dans le vide, un incendie signifie la mort

L'electrolyte organique des batteries lithium-ion est inflammable. En cas de surcharge, dommage physique ou court-circuit interne :

```
Augmentation de la temperature interne → retrecissement du separateur → extension du court-circuit → decomposition de l'electrolyte
→ emission de gaz inflammable → ignition → emballement thermique en cascade vers les cellules adjacentes
```

Sur Terre : les pompiers arrivent.
Dans l'espace : **dans le vide, il n'y a pas de pompiers.** Un incendie dans un module scelle = perte du support vital + remplissage de gaz toxique + impossibilite de secours.

Meme sur l'ISS, un incendie de lithium-ion est l'un des scenarios les plus redoutes. Si du lithium-ion est installe dans des milliers de modules Dyson, **statistiquement, un incendie est une certitude**.

Securite intrinseque du nickel-fer :

- Electrolyte : **solution aqueuse** d'hydroxyde de potassium — base eau. Ne brule pas
- En surcharge : l'eau s'electrolyse en produisant H₂ + O₂ — ce n'est pas un emballement thermique
- En surdecharge : pas de dommage irreversible aux electrodes — recuperation par recharge
- En cas de dommage physique : fuite de KOH — corrosif mais **pas d'explosion ni d'incendie**

**"Une batterie qui ne prend pas feu" n'est pas un luxe dans l'espace, c'est une necessite.**

---

## Battolyser — une batterie qui fait aussi de l'electrolyse

C'est ici que le nickel-fer depasse la categorie de "second choix" et offre un **avantage unique**.

### Principe

Concept de Battolyser developpe par l'Universite technique de Delft (TU Delft). Il exploite activement la tolerance a la surcharge des batteries nickel-fer :

```
[En charge]          Energie electrique → stockage chimique dans les electrodes Fe/Ni
[Charge complete]    Courant supplementaire → electrolyse de l'eau dans la solution aqueuse de KOH
                     Cathode : 2H₂O + 2e⁻ → H₂↑ + 2OH⁻
                     Anode : 2OH⁻ → ½O₂↑ + H₂O + 2e⁻
```

**Un seul dispositif fonctionne comme batterie + electrolyseur.** Pas besoin d'equipement d'electrolyse separe. Reduction de masse, de volume et de complexite.

Avec le lithium-ion, surcharge = incendie. Avec le nickel-fer, surcharge = **production d'hydrogene**.

### Cycle operationnel dans le module Dyson

```
[Fonctionnement normal] Turbine 370 MW en marche
  ├→ Consommation de charge (~320 MW)
  └→ Excedent de puissance (~50 MW) → mode Battolyser
       └→ Accumulation de H₂ ~890 kg/h + O₂ ~7 100 kg/h (en supposant ~70% d'efficacite d'electrolyse)

[Eclipse] 3-12 heures/an
  ├→ Decharge de la batterie (mode ESS)
  └→ H₂ accumule → generation par pile a combustible (en parallele)
       → Energie disponible 2x+ par rapport a la batterie seule

[Arret d'urgence]
  └→ Double stockage H₂/O₂ → prolongation du support vital
```

### Au-dela du stockage d'energie

Le H₂ et l'O₂ produits par le Battolyser depassent le simple stockage d'energie et s'integrent dans le **cycle materiel complet du module** :

| Produit | Application | Notes |
|---------|-------------|-------|
| H₂ | Reapprovisionnement en propergol pour remorqueurs NTP | Fluide de travail de la propulsion thermique nucleaire |
| H₂ | Agent reducteur dans le processus de fonte | Oxyde metallique → metal pur (FeO + H₂ → Fe + H₂O) |
| H₂ | Generation d'urgence par pile a combustible | Energie de secours pendant eclipse/maintenance |
| H₂ | Haber-Bosch → NH₃ → engrais | Agriculture du module d'habitat |
| O₂ | Support vital (respiration) | Essentiel pour le module d'habitat |
| O₂ | Oxydant (soudure, medecine) | Processus de fabrication locale |

Une batterie qui stocke de l'energie tout en produisant du propergol, un agent reducteur et de l'oxygene pour respirer. Le lithium-ion ne stocke que de l'electricite.

---

## "Si la densite energetique est 1/10, ce n'est pas trop volumineux?"

C'est vrai. Pour stocker la meme energie, le nickel-fer necessite **5 a 10 fois le volume** du lithium-ion.

Mais :

```
Echelle du module Dyson :
  Miroir : 1 km × 1 km = 1 000 000 m²
  Structure : s'etend sur plusieurs km derriere le miroir
  Volume total : des millions de m³

Capacite ESS necessaire (12 heures × 370 MW) :
  4 440 MWh = 4 440 000 kWh

Nickel-fer (base 40 Wh/L) :
  111 000 m³ = 111 m × 111 m × 9 m

→ <1% du volume total de la structure
```

Dans une structure de millions de m³ derriere un miroir de 1 km², 111 000 m³ representent **un recoin**. De plus, la masse elevee du nickel-fer peut etre utilisee comme **contrepoids pour les structures rotatives**. L'inconvenient se transforme en avantage.

La forte autodecharge de ~1% par jour n'est egalement un probleme que sur Terre. Avec la turbine en fonctionnement 24h/24, 365j/an, la batterie est toujours en etat de charge. L'autodecharge est **sans importance**.

"Si on augmente simplement la puissance de la turbine, on n'a plus besoin d'ESS?" L'eclipse et l'arret d'urgence sont des situations ou la turbine **s'arrete completement**. Generation et stockage sont des problemes distincts.

---

## Conception adaptee a l'environnement spatial

On ne peut pas emmener telle quelle une batterie nickel-fer terrestre dans l'espace. Trois adaptations sont necessaires.

### 1. Prevention de l'evaporation de l'electrolyte

La solution aqueuse de KOH perd son humidite lorsqu'elle est exposee au vide. Une **structure de cellules scellees** est indispensable. Heureusement, les cellules de batterie ont deja une conception scellees. Pour l'usage spatial, il suffit de renforcer le niveau d'etancheite.

### 2. Separation des gaz en microgravite

En mode Battolyser, les bulles de H₂/O₂ adherent a la surface des electrodes. Sur Terre, la poussee d'Archimede separe les bulles, mais en microgravite, cela ne fonctionne pas.

**Solution :** Revetement hydrophobe sur la surface des electrodes + force centrifuge generee par la rotation du module lui-meme pour la separation des gaz. Une acceleration centrifuge de seulement ~0,01G suffit pour separer les bulles.

### 3. Resistance aux radiations

La solution aqueuse de KOH est **extremement stable aux radiations**, contrairement aux electrolytes organiques. Les electrolytes organiques se degradent lorsque le rayonnement rompt les chaines moleculaires. Dans la solution aqueuse, la radiolyse de l'eau produit de faibles quantites de decomposition, mais se regenere naturellement par recombinaison. En environnement de radiation, le nickel-fer est **intrinsequement superieur** au lithium-ion.

---

## Resume en une ligne

Le lithium-ion est la meilleure batterie sur Terre. Mais il n'y a pas de lithium sur les asteroides, on ne peut pas le remplacer tous les 10 ans dans l'espace et on ne peut pas eteindre un incendie dans le vide. Les batteries nickel-fer peuvent etre fabriquees a partir de sous-produits de la fonte d'asteroides, durent 30-50 ans sans remplacement, ne prennent pas feu et, une fois completement chargees, se transforment en electrolyseurs qui produisent du propergol et de l'oxygene pour respirer. Que la densite energetique soit 1/10 n'a aucun sens a l'echelle de 1 km².

Pour les applications terrestres des batteries nickel-fer, voir [Batteries nickel-fer comme ESS hors reseau](https://www.parkjunwoo.com/1/tech/iron-nickel-ess-rural-energy/).

![Batteries nickel-fer developpees par Edison en 1901. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0](/images/why-iron-nickel-battery.webp)
