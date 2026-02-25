---
title: "Pourquoi le 28nm"
date: 2026-02-25T12:00:03+09:00
lastmod: 2026-02-25T12:00:03+09:00
tags: ["28nm", "semi-conducteur", "TPU", "autoreplication", "lithographie-ArF"]
image: "/images/why-28nm.webp"
summary: "Le 3nm de pointe est impossible sans l'EUV exclusif d'ASML — irrealisable dans l'espace. Le 28nm ne necessite que l'ArF, et le Google TPU v1 a demontre 92 TOPS en conditions reelles. Le silicium sort des scories, et l'espace lui-meme est une salle blanche."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Photo du die d'une puce NAND a 4 entrees en logique TTL — 7 transistors, largeur de ligne minimale 20 um (1968). Photo : Dgarte / Wikimedia Commons / CC BY-SA 3.0"
---

## « Vous dites autoreplication, mais d'ou viennent les puces ? »

Les articles precedents ont montre que miroirs, structures, [turbines](/fr/why/why-turbines/), [batteries](/fr/why/why-iron-nickel-battery/) et [gestion thermique](/fr/why/heat-flow/) peuvent tous etre fabriques a partir de Fe-Ni d'asteroide. La boucle d'autoreplication est presque fermee.

Presque.

**Les puces d'IA sont encore importees de la Terre.** Le fonctionnement autonome d'un module Dyson — controle des robots miniers, ajustement orbital, gestion des procedes de raffinage, maintien des systemes de survie — tout est gere par l'IA. Sans puces, le module est aveugle.

Tout comme « il n'y a pas de lithium dans les asteroides » etait le game over pour les batteries lithium-ion, **« on ne peut pas fabriquer d'EUV dans l'espace » est le game over pour le 3nm de pointe.**

Alors, quel procede pour fabriquer des puces ?

---

## Pourquoi pas le 3nm de pointe

Le coeur de la fabrication de semi-conducteurs est la lithographie — graver des motifs de circuits sur un wafer avec de la lumiere.

| Element | 28nm | 3-5nm (pointe) |
|---------|------|----------------|
| Lithographie | **ArF immersion** (Nikon, Canon, ASML) | **EUV** (monopole ASML, milliers de milliards par unite) |
| Disponibilite des equipements | Marche mature, occasion abondante | Extremement limitee, soumise au controle des exportations |
| Complexite de conception | Patterning simple | Multi-patterning (extremement complexe) |
| Cout de construction de la fab | ~3-5 Md$ | ~20-30 Md$ |
| Rendement | Eleve (10+ ans de validation) | Initialement faible |

Le scanner EUV (extreme ultraviolet) n'est fabrique que par **une seule entreprise dans le monde entier : ASML.** Une seule usine a Veldhoven, Pays-Bas. Soumis au controle des exportations. L'equipement que l'alliance Etats-Unis-Japon-Pays-Bas empeche de vendre a la Chine. Reproduire ca dans l'espace ? Impossible.

Le procede le plus puissant qui n'a pas besoin d'EUV. C'est le **28nm**.

« Le 7nm est faisable en ArF, non ? » — C'est possible. Le multi-patterning permet de tirer l'ArF plusieurs fois pour creer des motifs plus fins. Mais la complexite de conception explose et le rendement chute. Avant d'avoir le personnel et l'infrastructure pour gerer le rendement dans l'espace, c'est irrealiste.

« Le 65nm ne serait pas plus facile a fabriquer ? » — Si. Mais la performance par puce est trop faible. Pour la meme charge de travail, le volume de puces explose, et plus de puces signifie plus de cablage, packaging et refroidissement proportionnellement complexes. Facile a fabriquer ne veut pas dire facile en systeme.

**28nm = l'integration optimale realisable sans EUV.**

---

## Ce n'est pas de la theorie — Google TPU v1

« Le 28nm peut-il vraiment faire tourner de l'IA ? »

Google a repondu en 2015. **[TPU v1](https://arxiv.org/abs/1704.04760).** Fabrique en 28nm, deploye a plus de 100 000 exemplaires dans ses propres datacenters. Un accelerateur IA de production.

| Element | Google TPU v1 (mesure reelle) |
|---------|-------------------------------|
| Procede | 28nm |
| Architecture | Matrice systolique 256 x 256 |
| Calcul | 92 TOPS (INT8) = 23 TFLOPS (FP16) |
| Consommation | ~75 W en exploitation |
| Utilisation du silicium | **90 %+** |

L'architecture systolique est la cle. Un GPU est une puce generaliste — 70 % du silicium est consacre a la logique de controle, au cache et aux ordonnanceurs. Seulement 30 % effectue reellement des multiplications matricielles. Une matrice systolique est concue pour ne faire que des multiplications matricielles — **plus de 90 % du silicium effectue du calcul reel.**

Si tout ce qu'on fait c'est de l'IA, le surcharge generaliste du GPU est du pur gaspillage. Le TPU est la puce qui elimine ce gaspillage.

Et ce n'est pas une proposition theorique. **C'est la puce qui a fait tourner AlphaGo.** Du materiel deploye en production dans les datacenters Google pendant des annees.

---

## « 4,6 fois plus d'electricite ? »

La meilleure puce IA actuelle sur Terre, le NVIDIA H100. Procede 4nm, 990 TFLOPS, 700 W.

Un TPU v1 fait 23 TFLOPS. Combien pour egaler un H100 ?

```
990 TFLOPS / 23 TFLOPS = 43 cartes

43 cartes x 75 W = 3 225 W = 3,2 kW
```

| | TPU v1 x 43 cartes | H100 x 1 carte |
|---|---|---|
| FP16 cumule | ~990 TFLOPS | ~990 TFLOPS |
| Puissance totale | **3,2 kW** | 700 W |
| Ratio de puissance | **4,6x** | Reference |

4,6 fois. Sur Terre, c'est un ecart fatal. Quand l'electricite represente 30-40 % des couts d'exploitation d'un datacenter, 4,6 fois la puissance egale la faillite.

**Dans l'espace ?**

1 module Dyson = 370 MW. 3,2 kW represente **0,00086 %** de 370 MW. En surface de miroir, c'est 2,4 m2 — un pixel sur 1 km2 de miroir Dyson.

Sur Terre, l'electricite c'est de l'argent. **Dans l'espace, l'electricite c'est de la surface de miroir.** Les miroirs se fabriquent en aplatissant du Fe-Ni d'asteroide.

La meme structure logique que [l'article precedent ou les turbines battaient les panneaux solaires](/fr/why/why-turbines/). Un choix inferieur selon les criteres terrestres se transforme en choix unique selon les criteres spatiaux. **Si les criteres changent, la reponse change.**

---

## 1 module = un datacenter de 30 000 H100

Si 30 % des 370 MW du module sont alloues au calcul IA :

```
111 MW / 75 W/puce = ~1 480 000 cartes (1,48 million de TPU v1)

1,48 million / 43 cartes par equivalent H100 = ~34 000 H100

Surcharge interconnexion/refroidissement 20-30 % -> estimation conservatrice ~25 000-30 000 H100
```

Equivalent aux plus grands clusters IA de la planete en 2026. **Un seul module.**

Quand 270 000 modules se sont autorepliques ? L'equivalent de dizaines de milliards de H100. Une puissance de calcul depassant la capacite actuelle de toute l'humanite, a partir d'un seul asteroide.

---

## Matieres premieres : des puces IA sortent des scories

C'est la piece maitresse de cette conception. Pas besoin de mine de semi-conducteurs separee.

Le raffinage du minerai d'asteroide produit du Fe-Ni (90 %+) comme produit principal, et **le reste est du laitier**. Le composant principal du laitier est SiO2 — du silicate. On ne le jette pas.

```
Minerai d'asteroide -> Raffinage sous vide
  +-> Fe-Ni (90 %+) -> miroirs, structures, batteries, turbines
  +-> Laitier (principalement SiO2)
       +-> Majorite -> blindage anti-radiation
       +-> Une partie -> reduction au carbone (SiO2 + 2C -> Si + 2CO)
            -> silicium metallique
            -> zone refining (chaleur solaire + vide + microgravite)
            -> lingot monocristallin qualite semi-conducteur (purete 9N+)
            -> wafers 300 mm
            -> TPU 28nm
```

**Des puces IA sortent des dechets de raffinage.**

Le [zone refining](https://en.wikipedia.org/wiki/Zone_melting) est avantageux dans l'espace. C'est un procede de purification qui fait passer une zone fondue etroite le long d'un lingot de silicium pour repousser les impuretes :

- **Energie :** chauffage solaire direct. Cout zero
- **Vide :** l'espace est deja le vide. Les impuretes s'evaporent spontanement
- **Microgravite :** la zone fondue ne s'effondre pas. Sur Terre, le procede FZ (Float Zone) est limite a des lingots de 200 mm — au-dela, le silicium fondu s'effondre sous la gravite. **En apesanteur, 300 mm et plus sont possibles**
- **Repetition :** ajuster l'angle du miroir pour des passes de purification infinies. Cout supplementaire zero

Sur Terre, le zone refining est un procede premium couteux et a petite echelle. Dans l'espace, il devient le **procede standard**.

---

## La fab : l'espace est une salle blanche

L'un des postes de cout les plus importants d'une fab 28nm terrestre : la salle blanche classe 1-10. Moins de 10 particules de diametre 0,5 um ou plus par pied cube d'air. Maintenir cela necessite un enorme systeme de filtres HEPA, des unites de traitement d'air et un controle de pression positive. Une part significative du cout de construction de la fab y est consacree.

L'espace n'a **pas d'air.** La source de contamination par particules est tout simplement absente. Le vide est une **salle blanche parfaite.**

Aptitude spatiale par etape de fabrication (7 etapes) :

| Etape | Aptitude spatiale | Raison |
|-------|-------------------|--------|
| Croissance du lingot | **Avantage spatial** | FZ en microgravite, lingots de grand diametre |
| Decoupe du wafer | Possible | Procede mecanique, independant de l'environnement |
| Oxydation/depot (CVD, PVD) | **Vide avantageux** | Sur Terre, la chambre doit etre mise sous vide — l'espace est deja le vide |
| Photolithographie | Goulot | Scanner ArF et photoresist dependent de la Terre |
| Gravure | **Vide avantageux** | Simplification de la chambre de gravure plasma |
| Implantation ionique | **Vide avantageux** | Moins de diffusion du faisceau, pas de pompe a vide poussee necessaire |
| Cablage/packaging | Possible | Cu approvisionne depuis asteroides/Lune |

**6 des 7 etapes sont avantageuses ou equivalentes dans l'espace.** Le seul goulot est la photolithographie — on ne peut pas fabriquer le scanner ArF lui-meme dans l'espace. Mais une fois envoye, il dure des decennies.

---

## Gestion thermique de la fab : « Fabriquer des semi-conducteurs dans l'espace ? »

« Le cote face au soleil est a des centaines de degres, le cote oppose a -100°C, et vous pretendez controler a +-0,01°C ? »

Oui. Et **c'est plus facile que sur Terre.**

### Le coeur du probleme

Le systeme de lentilles de projection du scanner ArF est extremement sensible a la dilatation thermique. Une variation de 0,01°C modifie la courbure de la lentille, cree une erreur d'overlay et reduit le rendement. La tolerance d'overlay du procede 28nm est de quelques nm.

Comment les fabs terrestres resolvent cela :
- Maintien de l'ensemble de la salle blanche a 23,00 +- 0,1°C
- Controle interne du scanner a +-0,01°C par circuit de refroidissement dedie
- **Probleme :** les perturbations externes sont incessantes — variations de temperature exterieure, saisons, jour/nuit, meteo, seismes, vibrations routieres, chaleur des equipements voisins

### Conception thermique de la fab spatiale

```
[Coupe du module fab]

Exterieur : vide spatial (conduction zero, convection zero)
  |
  +- Paroi reflective MLI (isolation multicouche, dizaines de couches)
  |    -> Blocage de la chaleur solaire radiative a 99,5 %+
  |    -> Blocage aussi des pertes radiatives interieur->exterieur
  |
  +- Coque structurelle (Fe-Ni)
  |
  +- Couche de circulation liquide active
  |    -> Circulation fine d'eau ultrapure (UPW)
  |    -> Controle actif par pompe + rechauffeur + vanne de dissipation
  |    -> Paroi interieure uniforme a 23,00 +- 0,05°C
  |
  +- Interieur de la fab (atmosphere N2 a 1 atm)
       -> Chaleur des equipements -> absorbee par le refrigerant en circulation
       -> Interieur du scanner : boucle de refroidissement dediee +-0,01°C
```

### Pourquoi c'est plus facile que sur Terre

| Element | Fab terrestre | Module fab spatial |
|---------|--------------|-------------------|
| Perturbations thermiques externes | Incessantes (meteo, saisons, jour/nuit) | **Aucune** — isolation par le vide |
| Vibrations externes | Routes, seismes, usines voisines | **Aucune** — apesanteur sans vibration |
| Cout d'isolation | HVAC consomme 30-40 % de la puissance de la fab | **Le vide est un isolant gratuit** |
| Previsibilite des sources de chaleur | Perturbations externes + equipements internes | **Equipements internes uniquement** (entierement previsible) |
| Evacuation de chaleur | Tours de refroidissement, chillers (consommation massive d'eau et d'electricite) | **Radiateurs** (rayonnement dans le vide) |

Le paradoxe cle : l'environnement thermique extreme de l'espace (centaines de degres vs -100°C) **n'atteint pas l'interieur de la fab.** Le vide est le meilleur isolant, et une fois que le MLI bloque le rayonnement, l'interieur de la fab est thermiquement isole de l'exterieur. Ensuite, il ne reste qu'a gerer la chaleur des equipements internes — ce qui est plus facile que sur Terre, car les perturbations externes sont a zero.

Les fabs terrestres depensent 30-40 % de leur puissance totale en HVAC parce qu'elles **combattent sans cesse l'exterieur**. La fab spatiale n'a pas ce combat.

### UPW — vient du batholyseur

L'eau ultrapure (UPW) utilisee pour la circulation thermostatique de la fab provient des produits du batholyseur :

```
Batholyseur : H2O -> H2 + O2 (electrolyse)
Reaction inverse : H2 + O2 -> H2O (pile a combustible)

Sous-produit H2O -> purification -> UPW
  +-> Refrigerant de circulation thermostatique de la fab
  +-> Nettoyage des wafers
  +-> Liquide de lithographie par immersion
```

### Compartiment en gravite artificielle

La lithographie par immersion necessite un film mince d'eau ultrapure sur le wafer — il faut de la gravite. Le module fab est divise en deux compartiments :

```
Compartiment vide (0G) :
  +-> Depot CVD/PVD (vide requis)
  +-> Implantation ionique (vide requis)
  +-> Gravure plasma (vide requis)

Compartiment en gravite artificielle (~1G en rotation) :
  +-> Lithographie par immersion ArF (gravite necessaire pour gerer le liquide)
  +-> Nettoyage humide (gravite necessaire pour le nettoyage UPW)
  +-> Manutention des wafers (transfert robotise)
```

Les wafers circulent entre les compartiments vide et gravite artificielle via des sas. Le compartiment en rotation n'a aucune source de vibration externe, donc **seule l'uniformite de la rotation elle-meme doit etre geree** — bien plus simple que de se defendre contre les seismes et les vibrations routieres sur Terre.

---

## Dependance exterieure : 5 %

| Categorie | Approvisionnement | Note |
|-----------|-------------------|------|
| Silicium | Local (laitier -> Si) | |
| Energie | Local (chaleur solaire) | |
| Salle blanche | Local (vide spatial) | |
| Eau ultrapure | Local (H2O du batholyseur -> purification) | |
| Cablage en cuivre | Local (asteroides/Lune) | |
| Scanner ArF | **Terre, 1 fois** | Duree de vie de plusieurs decennies |
| Photoresist | **Terre, 1 fois/an** | Quelques centaines de kg/an |
| Gaz de gravure | **Terre, 1 fois/an** | Recyclable, faible quantite |
| Elements de dopage (B, As) | **Terre, 1 fois/an** | Quelques dizaines de kg |

95 % est approvisionne dans l'espace. Les 5 % restants — scanner ArF (1 fois) + consommables (quelques tonnes/an) — peuvent etre charges pour des decennies sur un seul lancement Starship.

« Le photoresist est de la chimie organique de precision, non ? » — Oui. La production locale est difficile. Mais la consommation annuelle est de l'ordre de quelques centaines de kg. Un seul Starship peut emporter des decennies de stock. Ce n'est pas l'autosuffisance totale, mais une **autosuffisance de facto**.

---

## La boucle d'autoreplication se ferme

```
Avant :
  Minerai d'asteroide -> raffinage -> Fe-Ni -> miroirs, structures, batteries -> autoreplication
                                                                               ^
                                                                    Puces IA importees de la Terre

Maintenant :
  Minerai d'asteroide -> raffinage -> Fe-Ni -> miroirs, structures, batteries, turbines
                                  -> laitier -> lingot Si -> TPU 28nm -> controle autonome IA
                                                                        |
                                                             Boucle d'autoreplication fermee
```

Les miroirs fabriquent des miroirs. Les batteries fabriquent du propergol. **Les scories fabriquent des puces IA.** Rien n'est gaspille.

---

## Resume en une ligne

Le 3nm de pointe est impossible sans l'EUV exclusif d'ASML — irrealisable dans l'espace. Le 28nm ne necessite que l'ArF, et le Google TPU v1 a demontre 92 TOPS en conditions reelles. L'ecart de 4,6x en puissance se traduit par 2,4 m2 de miroir sur un module de 370 MW. Le silicium sort des scories, l'espace lui-meme est une salle blanche, et l'isolation sous vide rend le controle thermique a +-0,01°C plus facile que sur Terre. Le dernier maillon de la boucle d'autoreplication.

![Photo du die d'une puce NAND a 4 entrees en logique TTL. Photo : Dgarte / Wikimedia Commons / CC BY-SA 3.0](/images/why-28nm.webp)
