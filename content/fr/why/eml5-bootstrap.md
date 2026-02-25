---
title: "Pourquoi le premier pas est L5 Terre-Lune, pas Mercure"
date: 2026-02-24T12:00:01+09:00
lastmod: 2026-02-24T12:00:01+09:00
tags: ["essaim-dyson", "EML5", "amorçage", "point-lagrange"]
image: "/images/eml5-bootstrap.webp"
imageCaption: "Points de Lagrange du systeme Terre-Lune. Credit : NASA/WMAP Science Team. Domaine public."
summary: "Le premier miroir d'un essaim de Dyson devrait etre place au point L5 Terre-Lune, pas sur Mercure. Avec 1,3 seconde de delai de communication, des ressources lunaires directes et un ravitaillement depuis la Terre — EML5 est le site optimal pour le bootstrap."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Par ou commencer un essaim de Dyson ?

Les discussions sur les essaims de Dyson partent toujours de la forme finale. Demantelement de Mercure, deploiement pres du Soleil, puissances de plusieurs TW a PW. C'est le cadre etabli par la serie d'Isaac Arthur, et la plupart des gens le tiennent pour acquis.

Mais avant de debattre de la civilisation K2 achevee, il y a une question bien plus importante : **ou placer le tout premier miroir ?**

L'humanite se situe actuellement a K 0,73. Voici les calculs sur l'endroit ou poser ce premier pas.

---

## Pourquoi EML5 (L5 Terre-Lune)

### Feuille de route en 3 phases

| Phase | Emplacement | Distance de la Terre | Delai de communication | Role |
|-------|-------------|---------------------|----------------------|------|
| **1. Bootstrap** | **EML5** | **~380 000 km** | **~1,3 s** | **Premiere base industrielle** |
| 2. Scale-up | SEL5 (L5 Soleil-Terre) | 150 millions km | ~8 min 20 s | Essaim de Dyson a grande echelle |
| 3. Full-scale | Mercure | Variable | Variable | Demantelement planetaire K2+ |

La plupart des discussions commencent a la Phase 2 ou 3. **Mais il n'y a pas de Phase 2 sans Phase 1.**

### Les avantages decisifs d'EML5

**1. Delai de communication de 1,3 seconde — pratiquement du temps reel**

Mercure impose des delais aller de plusieurs a plus de dix minutes, plus des periodes d'occultation par conjonction solaire. EML5 est a 1,3 seconde — assez proche pour le telecontrole. **On peut demarrer sans IA entierement autonome.** Ce n'est pas un luxe ; c'est decisif pour le bootstrap. Confier tout a une IA de fabrication autonome jamais validee dans l'espace versus superviser en temps reel depuis la Terre — ce sont des propositions radicalement differentes.

**2. Approvisionnement direct en ressources lunaires**

| Ressource | Source | Usage | Methode de transport |
|-----------|--------|-------|---------------------|
| Aluminium (Al) | Regolithe Al₂O₃ (~15%) | Revetement reflectif du miroir | Mass driver |
| Titane (Ti) | Ilmenite FeTiO₃ | Materiau structurel (leger) | Delta-V ~2,5 km/s |
| Oxygene (O₂) | Sous-produit de reduction | Support de vie | Pas de fusee chimique necessaire |
| Silicates | Regolithe | Blindage anti-radiation | — |

Sans l'enorme prerequis d'une flotte de minage d'asteroides, **on peut lancer des ressources directement depuis la Lune via mass driver.** Le delta-V Lune-EML5 est ~2,5 km/s — atteignable avec des fusees chimiques, et un mass driver electromagnetique ne consomme aucun carburant.

**3. Ravitaillement facile depuis la Terre**

Le delta-V de LEO a EML5 est bien inferieur a celui vers l'espace lointain. Les equipements initiaux, l'electronique et les materiaux haute performance qui ne peuvent pas encore etre fabriques dans l'espace peuvent etre fournis par la Terre. La phase de bootstrap n'a pas besoin d'exiger 100 % d'autosuffisance.

**4. Point de stabilite gravitationnelle**

EML5 est un point de Lagrange du systeme Terre-Lune. Le cout de maintien en orbite est quasi nul.

---

## Que fait-on a EML5

### Premier objectif : capacite de fabrication in situ de miroirs germes

1. Deployer depuis la Terre le premier miroir germe + equipement de fonderie a EML5
2. Transporter Al, Ti et silicates depuis la Lune par mass driver
3. Utiliser l'energie thermique solaire concentree du miroir germe pour fondre sous vide les materiaux lunaires
4. Utiliser la production pour **fabriquer un second miroir sur place** — le point de depart de la boucle d'autoreplication

### Environnement solaire

EML5 se trouve a la meme distance de 1 AU que l'orbite terrestre. Flux solaire de 1 361 W/m². Il n'atteint pas le flux 6,6 fois superieur pres de Mercure (0,39 AU), mais la duree de vie du miroir et les conditions d'exploitation sont incomparablement meilleures.

### Phase de validation

EML5 sert egalement de terrain de validation technologique :
- La fonderie sous vide fonctionne-t-elle reellement ?
- La periode de doublement de la boucle d'autoreplication correspond-elle aux calculs ?
- La duree de vie du revetement du miroir repond-elle aux previsions ?

Tout cela peut etre valide **sous supervision a 1,3 seconde de distance.** Debuguer avec des delais de minutes a dizaines de minutes dans l'espace lointain est une tout autre histoire.

---

## Pourquoi commencer par EML5

| Approche | Prerequis pour le premier miroir | Risque |
|----------|--------------------------------|--------|
| Demantelement de Mercure | Atterrissage sur Mercure, minage, evasion, deploiement orbital | Extremement eleve |
| Espace lointain direct | Flotte de minage d'asteroides, IA entierement autonome | Eleve |
| **EML5** | **Mass driver lunaire, supervision en temps reel depuis la Terre** | **Le plus faible** |

La difference cle : **si EML5 echoue, on peut reparer.** A 1,3 seconde, un joystick est encore a portee.

---

## Mais EML5 n'est pas eternel

EML5 n'est pas une solution universelle. C'est optimal comme site de bootstrap, mais ses limites sont claires.

### 1. L'ombre de la Terre

EML5 orbite dans le meme plan que la Lune (inclinaison 5,14°), passant du cote oppose de la Terre tous les ~27,3 jours. Lorsqu'il est pres du plan de l'ecliptique, il entre dans l'ombre (umbra) de la Terre et l'energie solaire est completement bloquee.

```
Diametre de l'umbra terrestre a 384 400 km :
  r = R_earth - d × (R_sun - R_earth) / d_sun
  = 6 371 - 384 400 × 689 629 / 149 600 000
  = 6 371 - 1 772 = 4 599 km (rayon)
  → Diametre ~9 200 km

Condition d'entree : latitude ecliptique < arctan(4 599 / 384 400) ≈ 0,69°
Inclinaison orbitale lunaire 5,14° → ne se produit qu'aux noeuds ascendant/descendant ±7,7°
```

La geometrie est identique a celle d'une eclipse lunaire (decalee de 60°, elle se produit donc a des moments differents) :

| Parametre | Valeur |
|-----------|--------|
| Frequence | 2–3 fois par an |
| Duree maximale par evenement | ~2,5 heures (transit central par l'umbra) |
| Penombre incluse | ~4,3 heures |
| **Temps d'arret annuel total** | **3–12 heures** |
| **Disponibilite annuelle** | **99,86–99,97 %** |

Quelques heures de stockage thermique permettent une operation ininterrompue. Pas fatal, mais **la simple existence d'une ombre est une limitation.**

### 2. Petite region stable

En raison du rapport de masse Terre-Lune (81:1), la region stable d'EML5 ne s'etend que sur des dizaines de milliers de km. Des centaines a des milliers de modules y tiennent, mais **au-dela, ca sature.**

### 3. Les ressources lunaires seules ne suffisent pas

La Lune n'a pas de ressources Fe-Ni en volume. L'alliage fer-nickel — le principal materiau structurel des cadres de miroirs — ne peut etre obtenu en quantite qu'a partir d'asteroides.

| Ressource | Lune | Asteroide (1986 DA) |
|-----------|------|-------------------|
| Al, Ti, O₂ | Abondant | Nul / traces |
| Alliage Fe-Ni | **Quasi nul** | **90 %+** |
| Silicates | Abondant | Sous-produit de scories |

Les premiers miroirs peuvent utiliser des cadres en Ti + revetement en Al, mais **depasser quelques milliers d'unites est impossible sans Fe-Ni d'asteroides.**

### 4. Perturbation solaire

La perturbation gravitationnelle solaire rend EML5 quasi-stable plutot que parfaitement stable. Un maintien en orbite a long terme est necessaire.

### Resume des contraintes

| Contrainte | Gravite |
|------------|---------|
| Ombre de la Terre (3–12 h/an) | Faible — attenuable par stockage thermique |
| Region stable (sature a quelques milliers de modules) | **Moyenne** |
| Pas de Fe-Ni | **Elevee** |
| Perturbation solaire | Faible |

---

## Alors, quelle est la suite ?

EML5 est le premier pas optimal vers un essaim de Dyson. Delai de communication de 1,3 seconde, approvisionnement direct en ressources lunaires, capacite de ravitaillement depuis la Terre — il n'existe pas de meilleures conditions pour le bootstrap.

Mais les limites sont tout aussi claires :
- 3–12 heures/an d'indisponibilite due a l'ombre terrestre
- Region stable de dizaines de milliers de km — sature a quelques milliers de modules
- **La Lune n'a pas de Fe-Ni** — le mur pour monter en echelle

A EML5, on valide la boucle d'autoreplication et on fait croitre des centaines a des milliers de modules. La technologie fonctionne. **Mais on ne peut plus grandir ici.**

Alors, ou se trouve la prochaine etape ?
