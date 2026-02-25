---
title: "Pourquoi ne pas fondre sur place"
date: 2026-02-24T12:00:04+09:00
lastmod: 2026-02-24T12:00:04+09:00
tags: ["exploitation-astéroïde", "transport", "SMR", "NTP"]
image: "/images/1986da-orbit.webp"
summary: "Conception technique complète pour exploiter l'astéroïde métallique 1986 DA avec un vaisseau minier propulsé par SMR, emballer le minerai dans des filets en fil de Fe-Ni et expédier 200 000 tonnes par fenêtre de transfert."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

*Orbital visualization: [SpaceReference.org](https://www.spacereference.org/asteroid/6178-1986-da), built with [SpaceKit](https://typpo.github.io/spacekit/). Data: JPL Small Body Database.*

## L'exploitation minière, d'accord, mais comment ?

Dans l'article précédent, nous avons proposé 1986 DA comme source de matières premières pour un essaim de Dyson. Plus de 90 % de Fe-Ni, microgravité, zéro déchet. Supérieur à Mercure à tous égards pour l'amorçage.

Mais une question demeure : **Comment exploiter réellement un bloc métallique en microgravité, et comment le transporter ?**

Le principe fondamental d'abord : **« Sur place, on ne fait que creuser, broyer et emballer. Le travail lourd se fait là où l'énergie abonde. »**

---

## Répartition des rôles : site vs base

| Tâche | Lieu | Raison |
|-------|------|--------|
| Excavation et broyage | 1986 DA sur site | Là où se trouve le minerai |
| Emballage (filet métallique) | 1986 DA sur site | Fabriqué en Fe-Ni local |
| Tri | **Non effectué** | Chaque composant a une utilité |
| Fonderie | **Base (miroirs Dyson)** | Thermique solaire miroirs GW >> SMR sur site kW |
| Fabrication et assemblage | **Base** | Clusters spécialisés |

Pourquoi ne pas fondre sur place ? La fonderie nécessite 1 600°C. Le SMR sur site produit 50~100 kW. Les miroirs Dyson de la base fournissent environ 600 MW (thermiques). **L'écart énergétique est de plusieurs milliers de fois.** Construire une fonderie sur l'astéroïde, c'est comme installer une aciérie au sommet d'une montagne — il est plus rationnel d'expédier le minerai.

---

![mining-transport](/images/post004.webp)

## Le vaisseau minier : une machine qui creuse, broie et emballe

### Énergie : SMR + appoint solaire

L'orbite très elliptique de 1986 DA (excentricité 0,58) fait varier le flux solaire de plus de 14 fois selon la position orbitale.

| Position orbitale | Distance | Flux solaire | vs Terre |
|------------------|----------|-------------|----------|
| Périhélie | 1,17 AU | ~995 W/m² | 73 % |
| Demi-grand axe | 2,81 AU | ~172 W/m² | 13 % |
| Aphélie | 4,46 AU | ~68 W/m² | 5 % |

**L'énergie solaire seule ne peut pas soutenir une exploitation continue.** Un SMR (petit réacteur modulaire, 50~100 kW) est la source d'énergie principale. Près du périhélie, les panneaux solaires s'ajoutent en appoint.

| Segment orbital | SMR | Solaire | Combiné | Mode |
|----------------|-----|---------|---------|------|
| Proche du périhélie (~1,2 AU) | 50~100 kW | 50~100 kW | **100~200 kW** | Appoint |
| Mi-orbite (~2,8 AU) | 50~100 kW | ~15 kW | ~65~115 kW | Normal |
| Proche de l'aphélie (~4,5 AU) | 50~100 kW | ~5 kW | ~55~105 kW | Vitesse réduite |

Même à l'aphélie, le SMR maintient l'exploitation. Elle ralentit simplement.

### Équipement

| Équipement | Fonction | Consommation |
|------------|----------|-------------|
| Excavatrice | Exploitation de surface/souterraine | ~20~50 kW |
| Broyeur | Concassage à taille de transport | ~10~30 kW |
| Petit four électrique | Fe-Ni → matière première de fil | ~10~20 kW |
| Tréfileuse | Fil → filet maillé | ~5~10 kW |
| Contrôle et communications | Contrôle autonome IA | ~5 kW |
| **Total** | | **~50~115 kW** |

Un seul SMR alimente tout l'équipement. Le vaisseau minier est **stationné en permanence** — il orbite avec 1986 DA et exploite sans interruption.

### Productivité

Hypothèse conservatrice : 50 kW moyens, environ 100 kg de minerai traités par kWh (le concassage mécanique en microgravité est comparable aux 10-25 Wh/kg terrestres ; la fonderie est séparée, à la base).

| Élément | Valeur |
|---------|--------|
| Production journalière | ~120 tonnes |
| Production annuelle | ~43 800 tonnes |
| **Par période orbitale (4,71 ans)** | **~200 000 tonnes** |

---

## Conteneurs : des filets, pas des caisses

De quoi a besoin un conteneur de fret dans l'espace ?
- Maintien de pression — vide, inutile
- Support du poids propre — microgravité, inutile
- Résistance de l'air — vide, inutile
- **Empêcher le minerai de se disperser pendant le transport**

C'est la seule exigence. Pas une caisse rigide — **un filet suffit.**

### Procédé de fabrication

```
Minerai extrait
  ├─ 99,5 % → Cargaison (paquets de minerai)
  └─ 0,5 % → Petit four électrique → Tréfilage → Tissage de filet
                                                 → Emballage des paquets
```

| Méthode | Ratio masse conteneur:cargaison |
|---------|-------------------------------|
| Conteneurs métalliques depuis la Terre | Gaspillage de transport extrême |
| Caisses Fe-Ni coulées sur site | ~2~3 % (excessif) |
| **Filet en fil Fe-Ni sur site** | **~0,1~0,5 %** |

**Le filet lui-même devient matière première de fonderie à l'arrivée.** Même l'emballage est utilisé à 100 %.

---

## Transport : fenêtres de transfert et propulsion

### Mécanique orbitale

Période orbitale de 1986 DA : 4,71 ans. La fenêtre de transfert optimale vers l'espace terrestre s'ouvre une fois par période orbitale.

| Élément | Valeur |
|---------|--------|
| LEO → rendez-vous avec 1986 DA | delta-V ~7,1 km/s |
| Départ optimal | Près du périhélie (1,17 AU) |
| Prochain rapprochement | **2038 (0,21 AU)** |

### Options de propulsion

| Méthode | Impulsion spécifique (Isp) | Caractéristiques | Adéquation |
|---------|--------------------------|-----------------|------------|
| Chimique (LH2/LOX) | ~450 s | Fraction de charge utile extrêmement basse | ❌ |
| **Propulsion Nucléaire Thermique (NTP)** | **~900 s** | Forte poussée, rapide | ✅ |
| **Propulsion Nucléaire Électrique (NEP)** | **~3 000 s+** | Ergol minimal, lent | ✅ Transport en masse |
| Propulsion Solaire Électrique (SEP) | ~3 000 s | Efficacité chute à l'aphélie | ⚠️ Limité |

**Un hybride NTP + NEP pourrait être optimal :** un seul réacteur sert à la fois de source thermique NTP (forte poussée pour le départ au périhélie) et de source électrique NEP (faible poussée, haute efficacité en croisière).

### Cycle logistique

```
[Année 0]  Le vaisseau minier arrive sur 1986 DA, exploitation commence
             │ 4,71 ans d'exploitation, emballage, stockage (~200 000 tonnes)
[Année ~5] Fenêtre de transfert → vaisseau de transport charge et part
             │ Transfert de Hohmann (~2-3 ans)
[Année ~7] Vaisseau de transport arrive, minerai déchargé
             │ Maintenance et ravitaillement
[Année ~8] Vaisseau de transport repart
             │
[Année ~10] Deuxième chargement ... le cycle se répète
```

Le vaisseau minier reste ; le vaisseau de transport fait la navette. Exploitation et transport fonctionnent **de manière asynchrone et parallèle.**

---

## 2038 : ratez-la et attendez des décennies

| Date | Événement |
|------|-----------|
| Années 2030 | Starship commercialisé, technologie SMR spatiale mature |
| **2038** | **Rapprochement de 1986 DA (0,21 AU) — fenêtre optimale pour déployer le vaisseau minier** |
| 2038~2042 | Le vaisseau minier arrive sur site, exploitation commence |
| ~2043 | Premier vaisseau de transport chargé et parti |
| **~2046** | **Première livraison de minerai** |

Après 2038, le prochain rapprochement de cette ampleur est à des décennies. **Rater cette fenêtre retarde considérablement le calendrier.**

### État des technologies requises

| Technologie | Actuel (2026) | Perspectives 2038 |
|-------------|--------------|-------------------|
| Starship (lanceur lourd) | Vols d'essai en cours | ✅ Commercialisation attendue |
| SMR spatial | NASA FSP classe 40 kW en développement | ✅ Démonstration lunaire attendue |
| Propulsion NTP | DARPA DRACO en développement | ⚠️ Vol d'essai attendu |
| Exploitation d'astéroïdes | OSIRIS-REx retour d'échantillon réussi | ⚠️ Grande échelle non prouvée |
| IA autonome spatiale | Niveau rover martien | ✅ Maturité suffisante attendue |

Aucune de ces technologies n'est impossible. Toutes sont **en développement ou devraient atteindre leur maturité d'ici une décennie.**

---

## Après l'arrivée : le Soleil fond le minerai

Quand le minerai arrive, les miroirs Dyson le chauffent directement à 1 600°C. Le vide spatial est un « équipement de raffinage gratuit » :

1. **Fusion optique** — La chaleur concentrée des miroirs fond le minerai brut en métal liquide
2. **Dégazage sous vide** — Le soufre et le phosphore se vaporisent naturellement dans le vide (capturés par des pièges froids)
3. **Séparation centrifuge** — Couche extérieure : Fe-Ni + métaux du groupe platine / Couche intérieure : laitier de silicate

```
Paquet de minerai arrive
  ├→ Filet en fil Fe-Ni → Alimenté en fonderie (l'emballage devient matière première)
  └→ Minerai → Chauffage par miroir à 1 600°C
       ├→ Alliage Fe-Ni (90 %+) → Éléments structurels, cadres de miroir, tuyaux
       ├→ Laitier de silicate → Blindage + matière première pour lingots de silicium
       ├→ Métaux du groupe platine → Revêtements, catalyseurs
       └→ S, P → Matières premières chimiques, dopage des semi-conducteurs
```

Ce que les aciéries terrestres accomplissent avec d'énormes quantités d'énergie et de produits chimiques, **le vide spatial et la chaleur solaire le fournissent gratuitement.**

---

## Résumé en une ligne

Le vaisseau minier creuse, broie et emballe avec un seul SMR. Les conteneurs sont des filets en Fe-Ni local — même l'emballage est une matière première. Le vaisseau de transport achemine 200 000 tonnes par fenêtre de transfert. 2038 est la première fenêtre d'opportunité. Le minerai arrivé est fondu par le Soleil. Rien n'est gaspillé.
