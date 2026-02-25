---
title: "Pourquoi du metal fondu, pas des batteries"
date: 2026-02-25T12:00:02+09:00
lastmod: 2026-02-25T12:00:02+09:00
tags: ["stockage-thermique-metal-fondu", "ESS", "levitation-electromagnetique", "stockage-thermique", "autoreplication"]
image: "/images/molten-metal-thermal-ess.webp"
summary: "Un module Dyson est une centrale solaire thermique — stocker la chaleur directement sous forme de Fe-Ni fondu en apesanteur. ~145 Wh/kg avec chaleur latente, cycles infinis, le tout a partir de minerai d'asteroide."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Masse de Fe-Ni fondu en levitation electromagnetique dans le vide en apesanteur — elle maintient une forme spherique par tension de surface. Image : Gemini"
---

## Ce que l'article precedent a oublie

[L'article precedent](/fr/why/why-iron-nickel-battery/) a montre pourquoi les batteries fer-nickel battent le lithium-ion. Il n'y a pas de lithium dans les asteroides, on ne peut pas eteindre un feu dans le vide, le fer-nickel dure 30 a 50 ans, et la surcharge produit de l'hydrogene.

Tout cela est vrai. **Mais un point a ete oublie.**

Un module Dyson est une centrale solaire thermique. Les miroirs concentrent la lumiere, la chaleur fait tourner des turbines. Quand il faut stocker de l'energie pour les eclipses, la conception actuelle fonctionne ainsi :

```
Chaleur solaire (1 600°C) -> Turbine -> Electricite (370 MW)
                                     -> Surplus (~50 MW)
                                          -> Batterie (energie chimique)    <- 2 conversions
                                          -> Eclipse -> retour electricite  <- 3 conversions
```

Chaleur -> electricite -> chimie -> electricite. **3 conversions.** 20 a 30 % de pertes a chaque etape.

Et si on stockait la chaleur directement ?

```
Chaleur solaire (1 600°C) -> une partie stockee directement           <- 0 conversion
                          -> Eclipse -> stockage -> turbine -> electricite  <- 1 conversion
```

**1 conversion.** La difference d'efficacite est ecrasante.

Convertir le surplus energetique d'une centrale solaire thermique en electricite, puis en chimie, puis a nouveau en electricite, c'est comme transformer de l'eau en vapeur, la separer en hydrogene et oxygene, puis les recombiner en eau. **Ca fonctionne, mais pourquoi ?**

Le stockage thermique est la reponse. Mais pourquoi ne le fait-on pas sur Terre ?

---

## Pourquoi ca ne marche pas sur Terre, pourquoi ca marche dans l'espace

Stocker de la chaleur dans du metal fondu sur Terre est un sujet de recherche, pas une realite industrielle. Il y a des raisons :

| Probleme | Terre | Espace (apesanteur, vide) |
|----------|-------|--------------------------|
| Contenant | Doit supporter le poids de milliers de tonnes de metal fondu -> massif et couteux | **Pas de poids propre** — parois fines, ou meme sans contact |
| Isolation | Doit bloquer convection + conduction + rayonnement | **Bloquer le rayonnement seulement** — quelques dizaines de couches MLI suffisent |
| Pertes thermiques | Elevees — la convection de l'air est le principal coupable | **Extremement faibles** — zero convection dans le vide |
| Corrosion | Le metal fondu a 1 500°C attaque les parois | **Levitation electromagnetique sans contact** -> zero corrosion |
| Securite | Fuite = accident majeur | Pas de feu dans le vide, pas de milieu de propagation |

**Les faiblesses terrestres disparaissent ou s'inversent dans l'espace.** Le meme schema repete dans les articles precedents — [turbines vs PV](/fr/why/why-turbines/), fer-nickel vs lithium-ion — exactement la meme structure.

---

## Stockage thermique par levitation electromagnetique

Le Fe-Ni fondu est un conducteur electrique meme a 1 500°C (il perd son magnetisme au-dessus du point de Curie du nickel, mais conserve sa conductivite). Un champ electromagnetique alternatif induit des courants de Foucault (eddy currents), et la repulsion entre les courants de Foucault et le champ magnetique permet une **levitation sans contact**.

C'est une technique utilisee en laboratoire meme sur Terre. On l'appelle fusion [EML (Electromagnetic Levitation)](https://en.wikipedia.org/wiki/Electromagnetic_levitation). On fait leviter et fondre des echantillons metalliques de quelques grammes a quelques kilogrammes. La raison pour laquelle on ne peut pas faire plus grand sur Terre tient en un mot — **la gravite**. Vaincre la gravite necessite un champ magnetique puissant, et un champ puissant consomme de l'energie. Quelques kilogrammes, c'est la limite.

En apesanteur ? **Il n'y a pas de gravite a vaincre.** Seul le champ magnetique minimal pour la stabilisation de position est necessaire. Quelques tonnes, centaines de tonnes, dizaines de milliers de tonnes.

```
[Coupe d'une unite de stockage thermique]

        +--- Paroi reflective MLI (isolation multicouche) ---+
        |                                                     |
        |    +-- Bobines electromagnetiques (refroidies) --+  |
        |    |                                             |  |
        |    |   @@@@@@@@@@@@@@@@@@                        |  |
        |    |   @ Masse de Fe-Ni fondu @                  |  |
        |    |   @ (1 200~1 500°C)      @                  |  |
        |    |   @@@@@@@@@@@@@@@@@@                        |  |
        |    |                                             |  |
        |    +---------------------------------------------+  |
        |                                                     |
        +-----------------------------------------------------+
```

En apesanteur, le metal fondu prend **naturellement une forme spherique** sous l'effet de la tension de surface. La sphere a le plus petit rapport surface/volume — les pertes thermiques par rayonnement sont minimales. La paroi MLI confine la chaleur rayonnee, le champ electromagnetique maintient la position, et l'absence de contact avec les parois signifie zero corrosion.

**On fond le Fe-Ni extrait des asteroides et on le laisse flotter — c'est un reservoir de stockage thermique.**

---

## Charge et decharge

```
[Charge — mode normal]
Concentration solaire -> volet radiatif ouvert -> chauffage de la masse metallique -> 1 200°C -> 1 500°C

[Decharge — eclipse]
Volet radiatif ouvert -> la chaleur rayonnee de la masse chauffe l'echangeur -> fluide de travail -> turbine
1 500°C -> 1 200°C (DeltaT=300°C utilise)
```

Charge : une partie de la chaleur solaire captee par les miroirs est dirigee vers le stockage. On ouvre le volet et la lumiere chauffe la masse metallique.

Decharge : lors d'une eclipse, on ouvre le volet pour que la chaleur rayonnee par la masse soit captee par l'echangeur thermique. L'echangeur chauffe le fluide de travail et fait tourner la turbine. On utilise les memes turbines — normalement les miroirs sont la source de chaleur, pendant l'eclipse c'est le stockage thermique. **Du point de vue de la turbine, seule la source de chaleur change, le reste est identique.**

Le vecteur d'echange thermique est le rayonnement. On ne peut pas planter un tuyau dans une masse fondue en levitation, donc le transfert thermique par volet radiatif est le mecanisme fondamental. L'energie rayonnee par du metal fondu a 1 500°C est proportionnelle a T⁴ selon la loi de Stefan-Boltzmann — largement suffisante.

---

## Densite energetique : chaleur sensible + latente

Chaleur specifique de l'alliage Fe-Ni : ~0,5 kJ/(kg-K) = ~0,14 Wh/(kg-K). En ne calculant que la **chaleur sensible**, proportionnelle a la variation de temperature (DeltaT) :

| Plage de temperature (DeltaT) | Chaleur sensible | Note |
|-------------------------------|-----------------|------|
| 300°C (1 200->1 500°C) | ~42 Wh/kg | Conservateur |
| 500°C (1 000->1 500°C) | ~70 Wh/kg | Intermediaire |
| 1 000°C (500->1 500°C) | ~140 Wh/kg | Agressif |

Mais ce n'est pas tout.

### Le bonus de la chaleur latente

Le point de fusion de l'alliage Fe-Ni est ~1 430-1 450°C. La plage de fonctionnement 1 000-1 500°C **traverse ce point de fusion.** Le metal fond lors de la charge et se solidifie lors de la decharge — changement de phase.

Quand une substance fond, sa temperature n'augmente pas alors qu'elle absorbe une enorme quantite de chaleur. C'est la **chaleur latente de fusion.**

```
Chaleur latente de fusion du fer (Fe) : ~270 kJ/kg = 75 Wh/kg
Alliage Fe-Ni : dans la meme gamme
```

Chaleur sensible + latente combinees :

| Plage de temperature | Sensible | Latente | **Total** |
|---------------------|----------|---------|-----------|
| 300°C (1 200->1 500°C) | ~42 | ~75 | **~117 Wh/kg** |
| 500°C (1 000->1 500°C) | ~70 | ~75 | **~145 Wh/kg** |
| 1 000°C (500->1 500°C) | ~140 | ~75 | **~215 Wh/kg** |

**La chaleur latente seule double la densite energetique.** Un simple bloc de metal qui fond et se solidifie atteint la gamme basse du lithium-ion (150-270 Wh/kg).

### Comparaison ESS (chaleur latente incluse)

| Methode | Densite energetique | Duree de vie en cycles | Approvisionnement |
|---------|--------------------|-----------------------|-------------------|
| Lithium-ion | 150-270 Wh/kg | 3 000-10 000 cycles | Impossible (pas de Li dans les asteroides) |
| Batterie fer-nickel | 30-50 Wh/kg | Pratiquement infinie | Fe-Ni d'asteroide |
| **Stockage thermique Fe-Ni fondu** | **117-215 Wh/kg** | **Pratiquement infinie** | **Fe-Ni d'asteroide** |

La meme densite energetique que le lithium-ion, des cycles infinis, et la matiere premiere jonche les asteroides. Et seulement 1 conversion chaleur -> electricite, donc l'efficacite systeme est ecrasante.

Pourquoi les cycles sont infinis : on chauffe et on refroidit un bloc de metal. Pas de reaction chimique. Pas d'electrodes. Pas d'electrolyte. Il n'y a rien a degrader.

---

## Dimensionnement : pourquoi 60 petites unites, pas une seule sphere geante

Eclipse maximale 12 heures, puissance turbine 370 MW. Il n'est pas necessaire de tout couvrir par stockage thermique — les piles a hydrogene et les batteries prennent leur part.

### Estimation hybride

```
Sur 12 heures d'eclipse :
  Stockage thermique : 6 heures
  Pile a combustible H2 : 4 heures (stock annuel du batholyseur)
  Batterie fer-nickel : 2 heures (suivi de charge instantane + secours)
```

Stockage thermique pour 6 heures (chaleur latente incluse) :

```
370 MW / 0,30 (rendement turbine) = ~1 233 MW(th) x 6h = ~7 400 MWh(th)

DeltaT=500°C + chaleur latente (145 Wh/kg) :
  Masse necessaire = 7 400 000 kWh / 0,145 kWh/kg = ~51 000 tonnes

(Sans chaleur latente : 105 000 tonnes -> le bonus latent divise la masse par deux)
```

51 000 tonnes dans une seule sphere donnent un rayon de ~12 m. Intuitivement simple. **Mais ca ne marche pas.** Trois raisons d'ingenierie.

### Raison 1 : Surface insuffisante pour la decharge

Pendant l'eclipse, le stockage thermique transfere la chaleur a l'echangeur **uniquement par rayonnement**. La puissance rayonnee est proportionnelle a la surface (P = epsilon sigma A T^4).

La sphere a le plus petit rapport surface/volume. Ideal pour **conserver** la chaleur, mais goulot d'etranglement pour la **decharger** rapidement.

```
Puissance thermique necessaire : ~1 233 MW(th)

Puissance rayonnee a 1 500°C (1 773 K) (epsilon=0,5) :
  P/A = epsilon x sigma x T^4 = 0,5 x 5,67e-8 x 1 773^4 = 280 kW/m2

Surface necessaire : 1 233 000 kW / 280 kW/m2 = 4 400 m2

Surface d'une sphere unique de rayon 12 m : 4pi(12)^2 = 1 810 m2 -> Insuffisant (41 % du besoin)
```

**Une sphere unique ne peut physiquement pas emettre la chaleur necessaire.** La surface est inferieure a la moitie.

En divisant en ~58 unites de rayon 3 m :

```
Surface par unite : 4pi(3)^2 = 113 m2
Surface totale de 58 unites : 113 x 58 = 6 560 m2 -> 149 % du besoin (avec marge)
Masse par unite : (4/3)pi(3)^3 x 7 800 = 880 tonnes
```

**Lors du stockage, chaque unite maintient sa forme spherique pour minimiser les pertes ; lors de la decharge, la surface totale de multiples unites fournit la puissance thermique necessaire.** L'inconvenient de la sphere est resolu par le nombre d'unites.

### Raison 2 : Ballottement — une boule de demolition de 100 000 tonnes de lave

Quand 51 000 tonnes de metal liquide flottent en une seule sphere et que le module effectue la moindre rotation ou vibration pour le controle d'attitude, d'**enormes vagues (sloshing)** se forment a l'interieur. Avec l'instabilite magnetohydrodynamique (MHD) en plus, cette masse de lave risque d'osciller et de s'echapper du confinement electromagnetique.

Des unites de rayon 3 m et 880 tonnes ? L'energie de sloshing est proportionnelle au cube de la taille de l'unite, donc **l'energie de ballottement de chaque unite est moins de 1/10 000 de celle d'une sphere unique**. Le risque d'evasion du confinement est pratiquement elimine.

### Raison 3 : Expansion volumique lors du changement de phase

En alternant entre 1 200°C (solide) et 1 500°C (liquide), le Fe-Ni subit des cycles d'expansion et contraction. Si une sphere de rayon 12 m se refroidit par l'exterieur, une croute solide se forme, et le liquide interieur qui se contracte peut **casser la croute et projeter des fragments dans le vide**. Les petites unites permettent un gradient de temperature interne-externe uniforme, eliminant ce probleme.

### Conclusion de conception

```
Specifications des unites de stockage thermique :
  Forme : spherique (formation naturelle par tension de surface)
  Rayon : ~3 m
  Masse : ~880 tonnes/unite
  Nombre d'unites : ~58 (par module)
  Masse totale : ~51 000 tonnes
  Disposition : distribuees dans la structure derriere les miroirs (servant aussi de contrepoids)

Performance de decharge :
  Surface totale : ~6 560 m2 (149 % du besoin de 4 400 m2)
  Marge assuree pour 1 233 MW(th)
```

Les 51 000 tonnes ne sont pas un approvisionnement supplementaire. Du Fe-Ni raffine a partir d'asteroides, **laisse fondu sans le solidifier, constitue les unites de stockage**. Distribuees dans la structure du module, elles servent aussi de **contrepoids**.

---

## ESS a 3 niveaux : separation des roles

Les batteries n'ont plus a assurer le stockage en vrac. La technologie optimale est affectee a chaque niveau :

```
Niveau 1 — Vrac (echelle horaire)
  +-> Stockage thermique en metal fondu
       Charge : chaleur solaire directe
       Decharge : stockage -> turbine -> electricite
       Role : reponse aux eclipses, pertes de conversion minimales

Niveau 2 — Tampon (echelle seconde~minute)
  +-> Batterie fer-nickel
       Charge : surplus electrique
       Decharge : electrochimique (reponse ms)
       Role : suivi de charge instantane, alimentation de demarrage

Niveau 3 — Urgence + production chimique
  +-> H2/O2 (produits du batholyseur)
       Pile a combustible d'urgence
       Propergol, reducteur, oxygene respirable
       Secours secondaire en cas d'eclipse prolongee
```

### Ce que cette architecture apporte

**Le parc de batteries est considerablement reduit.** Dans la conception precedente, couvrir 12 heures d'eclipse avec les seules batteries necessitait 111 000 m3. Avec le stockage thermique pour le vrac, les batteries couvrent 2 heures — reduites a quelques milliers de m3.

**Le role du batholyseur est clarifie.** L'article precedent decrivait le batholyseur (electrolyse par surcharge) comme combinant stockage ESS et production chimique. Avec le stockage thermique pour le vrac, le batholyseur est positionne comme **usine chimique** — production de propergol hydrogene, oxygene et reducteur en activite principale, generation d'urgence en activite secondaire.

**Les materiaux sont identiques.** Stockage thermique = Fe-Ni fondu. Batteries = electrodes Fe-Ni. Batholyseur = memes batteries en surcharge. Les 3 niveaux proviennent tous du Fe-Ni d'asteroide. Aucune matiere premiere supplementaire n'est ajoutee a la boucle d'autoreplication.

---

## Relation avec l'article precedent (batterie fer-nickel)

Les arguments principaux de l'article precedent restent **tous valides** :

- Pas de lithium dans les asteroides -> inchange
- Duree de vie 30-50 ans des batteries fer-nickel -> inchange
- Risque d'incendie dans le vide -> inchange
- Production H2/O2 du batholyseur -> inchange
- Fabrication locale possible -> inchange

**Ce qui est complete :** l'article precedent pouvait laisser entendre que la batterie fer-nickel assurait seule le stockage en vrac (12 heures d'eclipse). En realite, le stockage thermique est nettement superieur pour le stockage d'energie en masse, et la batterie excelle dans son domaine propre : la reponse instantanee.

**Chacun fait ce qu'il fait le mieux.** Le haut-fourneau pour le stockage thermique a l'echelle horaire. La batterie pour la reponse electrique a la milliseconde. La pile a combustible pour l'urgence + la production chimique. Aucun n'a besoin de tout faire seul.

---

## Resume en une ligne

Un module Dyson est une centrale solaire thermique — convertir la chaleur en electricite, puis en chimie, puis a nouveau en electricite, c'est une triple perte de conversion. Fondre du Fe-Ni d'asteroide et le laisser flotter en apesanteur donne un stockage thermique a 0 conversion en charge et 1 en decharge. Avec la chaleur latente de changement de phase, la densite energetique atteint ~145 Wh/kg — equivalent au lithium-ion. 58 unites de rayon 3 m en configuration distribuee resolvent le goulot de surface en decharge, le ballottement et l'expansion de changement de phase. Les materiaux sont tous le meme Fe-Ni d'asteroide.

![Masse de Fe-Ni fondu en levitation electromagnetique dans le vide en apesanteur. Image : Gemini](/images/molten-metal-thermal-ess.webp)
