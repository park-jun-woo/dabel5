---
title: "Pourquoi des turbines, pas des panneaux solaires"
date: 2026-02-24T12:00:07+09:00
lastmod: 2026-02-24T12:00:07+09:00
tags: ["solaire-thermique", "turbine", "autoréplication", "photovoltaïque"]
summary: "Panneaux solaires et turbines convertissent la lumiere solaire en electricite avec un rendement de 30 % dans l'espace. Mais les turbines cascadent les 70 % restants en chaleur utile, se fabriquent a partir de materiaux d'asteroides et se reparent sur place — la seule option pour un essaim de Dyson autoreplicant."
image: "/images/why-turbines.webp"
author: "PARK JUN WOO"
imageCaption: "Installation des aubes de rotor d'une turbine a vapeur dans une usine Siemens. Photo : Siemens Pressebild / Wikimedia Commons / CC BY-SA 3.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## « Pourquoi des turbines, encore ? »

Quand on pense a la production d'energie d'un essaim de Dyson, les panneaux solaires (PV) sont le choix evident. C'est le standard de l'energie spatiale. L'ISS fonctionne avec du PV. La plupart des sondes spatiales fonctionnent avec du PV.

Pourtant, cette conception utilise des turbines. Pourquoi revenir a une technologie du XIXe siecle au XXIe siecle ?

La reponse est simple : **on ne peut pas fabriquer des panneaux solaires a partir d'asteroides, mais on peut fabriquer des turbines.**

---

## L'efficacite est la meme — 30 %

Clarifions cela d'abord. « Le PV n'est-il pas plus efficace ? »

| | Panneau solaire (GaAs multijonction) | Turbine solaire thermique |
|---|---|---|
| Rendement de conversion | ~30 % (qualite spatiale) | ~30 % (cote chaud 1 500 K / cote froid 500 K) |
| Limite de Carnot | Sans objet | 66,7 % (realise ~45 %) |
| Production electrique | **Identique** | **Identique** |

En collectant 1 225 MW(thermiques) avec un miroir de 1 km², que ce soit avec du PV ou une turbine, **la production electrique est de ~370 MW dans les deux cas.**

Si l'efficacite est la meme, les differences sont ailleurs.

---

## Difference 1 : Les 70 % restants

Le PV et les turbines echouent tous deux a convertir 70 % de l'energie entrante en electricite. Mais la destination de ces 70 % est tres differente.

### PV : 70 % disparaissent en chaleur residuelle basse temperature

```
Entree solaire 1 225 MW
  ├→ 30 % → 370 MW (electricite)
  └→ 70 % → 855 MW → surface du panneau a 60–80°C chaleur residuelle
                      → aucune utilite. Rayonnee dans l'espace via des dissipateurs.
```

A 60–80°C, on ne peut ni fondre du metal, ni faire tourner une usine, ni chauffer un habitat. **70 % de l'energie disparait tout simplement.**

### Turbine : 70 % en cascade de haute a basse temperature

```
Entree solaire thermique 1 225 MW
  ├→ 30 % → 370 MW (electricite)
  └→ 70 % → 855 MW (chaleur) → utilisation etagee par temperature :
       ├→ 800–1 000°C : ~400 MW → fonderie (fusion Fe-Ni)
       ├→ 400–600°C :   ~250 MW → revetement, traitement thermique, formage
       ├→ 100–200°C :   ~120 MW → chauffage de l'habitat
       └→ 30–60°C :      ~85 MW → chaleur ambiante du datacenter
```

**Les memes 70 % passent successivement par la fonderie → l'usine → l'habitat → le datacenter, et tout est utilise.** La « chaleur residuelle » de la turbine n'est pas un dechet — c'est la source d'energie du processus suivant.

Utilisation effective de l'energie entrante :
- PV : ~30 % (electricite uniquement)
- **Turbine : ~30 % + cascade thermique → effectivement 85 %+**

---

## Difference 2 : Compatibilite avec la boucle d'autoreplication

C'est le facteur decisif.

### Fabriquer du PV dans l'espace

La fabrication de panneaux solaires (GaAs multijonction) necessite :
1. Matieres premieres gallium (Ga) + arsenic (As) — **introuvables dans les asteroides**
2. Croissance monocristalline (MOCVD, MBE) — **equipements de precision extreme**
3. Depot epitaxial multicouche — **salle blanche requise**
4. Revetement antireflet, cablage, assemblage de modules — **ligne de fabrication dediee**

Les asteroides n'ont ni Ga ni As. Meme avec l'equipement, il n'y a pas de matiere premiere. **Le PV ne peut pas entrer dans la boucle d'autoreplication.** Il doit etre continuellement reapprovisionne depuis la Terre.

Et le PV en silicium (Si) ? En fait, cette conception inclut deja un procede pour produire des lingots de Si de qualite semi-conducteur a partir de scories de silicate (raffinage par zone, pour les puces d'IA). La matiere premiere Si est donc disponible. Cependant :
- Rendement du Si PV spatial ~20 % — inferieur au GaAs (30 %) et en dessous des turbines (30 %)
- La ligne de fabrication des cellules PV (diffusion, revetement antireflet, motif d'electrodes) est **separee de la fonderie de puces**
- Le rendement se degrade sous la radiation spatiale → cycle de remplacement plus court
- La meme plaquette de Si est **bien plus precieuse en tant que puce d'IA**

Meme avec du Si disponible, en faire du PV est du gaspillage. **Si vous avez du silicium, vous fabriquez des puces.**

### Fabriquer des turbines dans l'espace

| Composant | Materiau | Source | Fabrication |
|-----------|----------|--------|-------------|
| Aubes et tuyeres haute temperature | Superalliage de Ni | Asteroide Fe-Ni | Fonderie de precision |
| Compresseur et arbre basse temperature | Alliage de Ti | Ilmenite lunaire | Usinage |
| Carter | Fe-Ni | Asteroide | Tolerie et soudage |

**Tout peut etre construit avec des materiaux deja presents dans la boucle d'autoreplication (Fe-Ni, Ti).** Aucune matiere premiere supplementaire, aucune ligne de fabrication supplementaire. Les turbines sortent de la meme ligne de production que les cadres de miroirs.

---

## Difference 3 : Duree de vie et maintenance

### Le probleme de la radiation du PV spatial

Le PV spatial est endommage par les particules de haute energie (protons, ions lourds) qui perturbent le reseau cristallin. Le rendement se degrade de ~1–3 % par an.

- Apres 10 ans : le rendement tombe a 70–80 %
- Remplacement necessaire → **ne peut pas etre fabrique, doit etre reapprovisionne depuis la Terre**
- Si le reapprovisionnement n'est pas disponible : accepter la reduction de production

### Usure des turbines

Les turbines ne durent pas eternellement non plus. Le fluage des aubes a haute temperature et l'usure des paliers sont les principaux mecanismes de degradation.

Mais :
- Les aubes peuvent etre **refondues localement en superalliage de Ni**
- Paliers → **paliers magnetiques sans contact** : zero usure
- Conception modulaire : seuls les composants degrades sont remplaces, pas l'unite entiere

**Les pieces de turbine peuvent etre fabriquees et remplacees sur place. Celles du PV ne le peuvent pas.** Dans un systeme autoreplicant, cette difference est decisive.

---

## Limites reelles des turbines — et solutions

Soyons honnetes sur les inconvenients.

### Limite 1 : Un fluide de travail est necessaire

Les turbines ont besoin d'un fluide qui se dilate a la chaleur pour faire tourner le rotor. Ou trouver ce fluide dans l'espace ?

| Candidat | Avantages | Inconvenients | Approvisionnement |
|----------|-----------|---------------|-------------------|
| Helium (He) | Inerte, stable a haute temperature | Difficile a reconstituer en cas de fuite | Capture du degazage d'asteroides |
| CO₂ supercritique | Haute densite, turbine compacte | Gestion de la corrosion necessaire | Degazage d'asteroides |
| Sodium/Potassium (metal liquide) | Ultra-haute temperature, excellent transfert thermique | Reactif (sur en vide) | Traces d'asteroides |

Le systeme fonctionne en cycle ferme, il n'y a donc pas de consommation de fluide. Seule la charge initiale doit etre assuree. Le gaz peut etre capture lors du degazage de la fonderie d'asteroides, ou une petite quantite peut etre fournie depuis la Terre au depart.

### Limite 2 : Pieces mobiles — risque de panne dans l'espace

La faiblesse fondamentale des turbines : des composants rotatifs a grande vitesse. Meme sur Terre, la maintenance des turbines est un travail exigeant.

**Solutions :**
- **Paliers magnetiques** — support rotatif sans contact. Zero usure. Deja commercialise dans les turbomachines a grande vitesse sur Terre
- **Cartouches d'aubes modulaires** — remplacement des jeux d'aubes en une seule unite. Pas de maintenance individuelle
- **Fabrication locale** — coulee de pieces de rechange a la demande. Pas d'attente de reapprovisionnement terrestre
- **Redondance** — plusieurs turbines par module. Production maintenue meme pendant la maintenance d'une unite

### Limite 3 : Vibrations

La rotation a grande vitesse genere des vibrations. C'est un probleme si des usines de semi-conducteurs ou des equipements optiques de precision partagent le meme module.

**Solutions :**
- **Clusters specialises** — separer physiquement les modules turbines des modules de fabrication (structures distinctes)
- **Supports antivibratoires** — installer les turbines sur des joints structurels flexibles
- Sur Terre non plus, on ne met pas une centrale electrique et une usine de semi-conducteurs dans le meme batiment

### Limite 4 : Rejet de chaleur

La chaleur du cote froid de la turbine doit etre rayonnee dans l'espace. Il n'y a pas d'atmosphere dans l'espace, donc le refroidissement par convection est impossible — seul le refroidissement radiatif fonctionne.

**C'est un vaste sujet independant. Il sera traite en detail dans le prochain article.**

---

## Resume en une ligne

Les panneaux solaires et les turbines ont le meme rendement electrique (30 %). Mais le PV gaspille les 70 % restants, tandis que les turbines les utilisent. Le PV ne peut pas etre fabrique dans l'espace ; les turbines si. Quand le PV tombe en panne, on attend la Terre ; quand une aube de turbine s'use, on la refond sur place. Dans un systeme autoreplicant, la reponse est evidente.
