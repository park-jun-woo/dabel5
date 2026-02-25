---
title: "Pourquoi on ne peut pas transporter la chaleur par tuyaux"
date: 2026-02-24T12:00:08+09:00
lastmod: 2026-02-24T12:00:08+09:00
tags: ["gestion-thermique", "radiateur", "cascade-thermique"]
summary: "Aucun fluide ne survit à 1 600 °C en circuit fermé. Chaque installation reçoit son propre miroir, évacue la chaleur résiduelle à la température la plus élevée possible, et seul le résidu en dessous de 100 °C atteint l'habitat."
image: "/images/post008.webp"
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Devoir du précédent article

L'article précédent affirmait que les turbines surpassent le photovoltaïque pour l'autoréplication. Rendement 30 %, production électrique 370 MW, les 855 MW restants sont de la chaleur.

Et il disait :

> « Les mêmes 70 % passent séquentiellement par la fonderie, l'usine, l'habitat et le centre de données — tout est utilisé. »

Conceptuellement correct. La chaleur résiduelle de la turbine est bien plus utile que le rejet à 60 °C du photovoltaïque. **Mais le « passage séquentiel » n'est pas une conception réelle.** Cet article retrace le flux thermique véritable.

---

## D'abord une correction : pourquoi le « passage séquentiel » ne fonctionne pas

### Problème 1 : température de la chaleur résiduelle de la turbine

Thermodynamique de la turbine (cycle Brayton) :
- Côté chaud : ~1 200 °C (fluide de travail chauffé par lumière solaire concentrée)
- Côté froid : ~227 °C (chaleur rejetée ici)
- Rendement 30 % → 370 MW électriques, **855 MW rejetés à ~227 °C**

Point clé : **Toute la chaleur résiduelle de la turbine sort à ~227 °C.** La fusion exige 1 600 °C. Impossible de faire tourner un procédé à 1 600 °C avec de la chaleur à 227 °C — deuxième loi de la thermodynamique. La chaleur ne circule que du chaud vers le froid.

La flèche « 800–1 000 °C → fusion » du diagramme précédent n'était pas de la chaleur de turbine. La chaleur de fusion provient **directement du miroir**.

### Problème 2 : aucun fluide ne supporte 1 000 °C

Même s'il existait de la chaleur à 1 600 °C quelque part, pourrait-on la transporter par tuyauterie ?

| Fluide caloporteur | Temp. max. d'exploitation | Limite |
|---|---|---|
| Eau pressurisée | ~340 °C | Point critique |
| Sels fondus | ~565 °C | Décomposition |
| Sodium liquide | ~800 °C | Pression de vapeur |
| Hélium haute pression | ~950 °C | Limite du matériau de tuyauterie |
| **Au-dessus de 1 000 °C** | **N/A** | **Aucun fluide disponible** |

Aucun fluide ne peut transporter de la chaleur à 1 600 °C. La seule façon de livrer de l'énergie à cette température est **la lumière.** Irradiation directe par des miroirs.

### Problème 3 : distance entre modules

Dans un cluster spécialisé, les modules de fusion et les centres de données sont **séparés de 50 à 100 km.** Séparation délibérée contre vibrations, contamination et interférence thermique. À cette distance, la tuyauterie thermique est irréaliste.

**Conclusion : acheminer la chaleur résiduelle de turbine vers des procédés haute température est physiquement impossible.**

---

## La vraie conception : chaque installation reçoit son propre miroir

Les véritables principes du flux thermique :

1. **La chaleur d'entrée est reçue directement du miroir propre à chaque module** — transmise sous forme de lumière, sans fluide
2. **La cascade ne fonctionne qu'à l'intérieur de chaque module** — la chaleur résiduelle du procédé est réutilisée à des températures progressivement décroissantes
3. **Pas de transfert de chaleur entre modules** — limitations de distance et de fluide
4. **Seule la chaleur résiduelle inférieure à 100 °C est fournie à l'habitat** — tuyauterie possible, température adaptée à la demande

### Répartition des miroirs (cluster de 10 modules)

| Type de module | Qté | Répartition du miroir (chaleur : puissance) | Source haute temp. |
|---|---|---|---|
| Module de fusion | 3 | 90 : 10 | Miroir → direct 1 600 °C |
| Module de lingots | 1 | 70 : 30 | Miroir → direct 1 400 °C |
| Module structural | 2 | 60 : 40 | Miroir → direct 800–1 200 °C |
| Module de fabrication | 1 | 20 : 80 | Miroir → direct 900 °C |
| Centre de données | 2 | 5 : 95 | Miroir → turbine → électricité |
| Habitat / logistique | 1 | 30 : 70 | Miroir → turbine → électricité |

**Au-dessus de 1 000 °C, la lumière livre la chaleur directement.** Les turbines ne fonctionnent que dans les modules nécessitant principalement de l'électricité (centres de données, habitats).

---

## Physique du radiateur : la loi T⁴

La seule façon d'évacuer la chaleur dans l'espace est **le rayonnement infrarouge.** Ni convection ni conduction.

Loi de Stefan-Boltzmann :

**Puissance rayonnée = ε × σ × A × T⁴**

(ε : émissivité, σ : constante de Stefan-Boltzmann, A : surface, T : température absolue)

L'élément clé est **T⁴**. Doubler la température multiplie la puissance rayonnée par 16. Inversement, la surface nécessaire pour la même charge thermique est divisée par 16.

| Temp. du radiateur | Surface par MW | Analogie |
|---|---|---|
| 800 °C (1 073 K) | **8 m²** | Une place de parking |
| 400 °C (673 K) | **50 m²** | Un appartement |
| 227 °C (500 K) | **166 m²** | Un court de tennis |
| 100 °C (373 K) | **535 m²** | Trois terrains de basket |
| 60 °C (333 K) | **844 m²** | 1/8 d'un terrain de football |

(Rayonnement bilatéral, émissivité ε = 0,85, tôle Fe-Ni sans revêtement)

**Leçon : ce qui se dissipe en 8 m² à 800 °C nécessite 844 m² à 60 °C. Plus de 100×.**

D'où le principe fondamental de la gestion thermique : **« Évacuez la chaleur inutilisable à la température la plus élevée possible, immédiatement. »**

### Matériau du radiateur

Les radiateurs font partie de la boucle d'autoréplication :
- **Matériau :** tôle fine Fe-Ni d'origine astéroïdale
- **Surface :** sans revêtement aluminium (l'inverse du miroir) — le Fe-Ni non revêtu possède une forte émissivité infrarouge, idéale pour le rayonnement
- **Fabrication :** même ligne de tôlerie que les cadres des miroirs. Seule l'étape de revêtement est omise
- **Ressources supplémentaires :** zéro. Même matériau, même procédé, produit différent

---

## Flux thermique par installation

### Module de fusion — la chaleur est au premier plan (90 % chaleur, 10 % puissance)

Le module de fusion reçoit 90 % de l'énergie de son miroir sous forme de chaleur directe. Une petite turbine (10 %) produit l'électricité pour moteurs et robots.

```
☀️ Miroir dédié (90 % → irradiation directe, 10 % → petite turbine)
 │
 ▼
Four de fusion (1 600 °C) ← Chauffé directement par la lumière du miroir, sans fluide
 │
 │ Chaleur résiduelle ~800 °C ← À partir d'ici un fluide (He / métal liquide) peut la transporter
 ├→ Traitement thermique d'alliages, recuit (utilise 800 °C)
 ├→ Excédent → ★ Radiateur A (800 °C) — 8 m²/MW, compact
 │
 │ Chaleur résiduelle ~400 °C
 ├→ Préchauffage, chauffage auxiliaire (utilise 400 °C)
 ├→ Excédent → ★ Radiateur B (400 °C) — 50 m²/MW, moyen
 │
 │ Chaleur résiduelle ~200 °C
 ├→ ★ Radiateur C (200 °C) — l'essentiel est dissipé ici
 │
 │ Résidu < 100 °C
 └→ Peut être acheminé vers l'habitat par tuyauterie

Chaleur résiduelle de la petite turbine (~227 °C) → ★ Radiateur D
```

Le module de fusion utilise la chaleur du haut vers le bas, **rayonnant l'excédent à chaque étape.** Les radiateurs haute température sont petits, donc la pénalité est faible. Seul le résidu en dessous de 100 °C est envoyé à l'habitat.

### Module centre de données — l'électricité est au premier plan (5 % chaleur, 95 % puissance)

Le centre de données est le module le plus difficile à refroidir. 95 % de l'énergie du miroir passe par turbine → électricité → puces → chaleur, le tout sortant à ~60 °C.

```
☀️ Miroir dédié (95 % → grande turbine, 5 % → chaleur auxiliaire)
 │
 ▼
Grande turbine → ~370 MW d'électricité
 │
 │ Chaleur résiduelle de turbine ~227 °C (~855 MW)
 └→ ★ Radiateur A (227 °C) — 166 m²/MW
     L'essentiel de la chaleur de turbine est dissipé ici

Fonctionnement des puces → toute l'électricité devient chaleur
 │
 │ Chaleur des puces ~60 °C
 │  Rayonnement direct à 60 °C : 844 m²/MW → 111 MW nécessitent ~94 000 m²
 │
 ├→ [Pompe à chaleur] 60 °C → 200 °C (COP ~3, puissance ~37 MW)
 │   └→ ★ Radiateur B (200 °C) — surface réduite à ~1/4
 │
 └→ Résidu < 100 °C → peut être fourni à l'habitat
```

**La pompe à chaleur est la technologie clé.** Remonter la chaleur de 60 °C à 200 °C réduit considérablement la surface du radiateur. La puissance de la pompe (~37 MW) provient de la turbine elle-même. Turbine et pompe à chaleur peuvent être fabriquées sur place en Fe-Ni + Ti.

### Module structural (60 % chaleur, 40 % puissance)

```
☀️ Miroir dédié (60 % → chauffage direct, 40 % → turbine)
 │
 ▼
Soudure / traitement thermique (800–1 200 °C) ← Chauffage direct par miroir
 │ Chaleur résiduelle ~400 °C
 ├→ Préchauffage pour formage / pliage (utilise 400 °C)
 ├→ Excédent → ★ Radiateur (400 °C)
 │ Chaleur résiduelle ~200 °C
 ├→ ★ Radiateur (200 °C)
 │ Résidu < 100 °C
 └→ Peut être fourni à l'habitat

Turbine (40 %) → électricité (robots, CNC, postes de soudure)
 └→ Chaleur résiduelle de turbine → ★ Radiateur (227 °C)
```

### Module habitat / logistique — consommateur de chaleur résiduelle sous 100 °C

L'habitat est le puits thermique final. Sa propre turbine produit l'électricité pour le support de vie, l'éclairage et l'agriculture, tout en **recevant la chaleur résiduelle inférieure à 100 °C des modules voisins.**

```
☀️ Miroir dédié (30 % → chaleur, 70 % → turbine)
 │
 ├→ Turbine → électricité (support de vie, éclairage, LED agricoles)
 │   Chaleur résiduelle (~227 °C) → ★ Radiateur
 │
 └→ Chaleur → eau chaude, chauffage d'appoint
     └→ Résidu → ★ Radiateur

Chaleur résiduelle <100 °C des modules voisins (fusion, structural)
 │
 └→ Chauffage de l'habitat, eau chaude, chauffage du sol agricole
     └→ Résidu → rayonné par la coque extérieure de l'habitat (la structure elle-même fait office de radiateur)
```

Les besoins thermiques de l'habitat (chauffage, eau chaude) sont modestes par rapport aux volumes de chaleur industrielle résiduelle. Le résidu sous 100 °C des modules voisins suffit largement. **L'habitat reçoit du chauffage gratuit — les modules industriels ne produisent pas de chaleur pour lui.**

---

## Rayonnement distribué : la vue d'ensemble

Synthèse du flux thermique du cluster :

```
☀️ Lumière solaire → Miroirs → Distribuée directement à chaque module
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
[Fusion]       [Structural]    [Centre de données]
 Miroir→1 600°C Miroir→1 200°C  Miroir→Turbine→Élec.
    │               │               │
    ▼               ▼               ▼
 ★Rad.(800°C)   ★Rad.(400°C)   ★Rad.(227°C) ← résidu turbine
 ★Rad.(400°C)   ★Rad.(200°C)   ★Rad.(200°C) ← après pompe à chaleur
 ★Rad.(200°C)       │               │
    │               ▼               ▼
    └──── <100°C ──→ [Habitat] ←── <100°C
                      Chauffage et eau chaude
                         │
                    ★Rad.(coque, ~30°C)
```

**Non pas un « passage séquentiel » mais une « distribution parallèle + rayonnement individuel + partage de la basse température uniquement ».** Chaque module reçoit la chaleur de son propre miroir, l'évacue par ses propres radiateurs et ne transmet que les résidus à l'habitat.

### Pourquoi c'est mieux

1. **Les radiateurs haute température sont minuscules** — 8 m² pour dissiper 1 MW à 800 °C. Une petite ailette à côté du procédé suffit
2. **Pas de tuyauterie entre modules** — on évite le cauchemar de 50 km de tuyaux haute température
3. **Chaque module est thermiquement indépendant** — la maintenance d'un module n'affecte pas les autres
4. **L'habitat est en sécurité** — aucun tuyau à 1 600 °C ne traverse les zones habitées

---

## Correction de l'article précédent : où vont réellement les 70 % ?

L'article précédent disait « le PV gaspille 70 %, les turbines les utilisent ». Est-ce toujours vrai ?

**Oui.** Mais le mécanisme diffère :

| | PV | Système à turbines |
|---|---|---|
| 30 % | Électricité | Électricité |
| 70 % restants | Chaleur résiduelle 60–80 °C → **inutilisable** | Distribuée comme chauffage direct par miroir à chaque procédé → **utilisée pour la fusion, le formage, le traitement thermique** |
| Charge de rayonnement | La totalité des 70 % rayonnée à basse température (radiateur géant) | Rayonnement étagé à haute température (petits radiateurs distribués) |

Les 70 % du PV sont entièrement à 60–80 °C — la pire température tant pour l'industrie que pour le rayonnement. Dans le système à turbines, ces 70 % sont livrés par les miroirs à chaque procédé à la température exacte requise, et la chaleur résiduelle est rayonnée à la température la plus élevée possible.

**Ce que signifie vraiment « utiliser les 70 % restants » : pas la chaleur résiduelle de la turbine, mais l'énergie thermique du miroir consommée directement par chaque procédé.**

---

## Résumé en une ligne

Aucun fluide ne peut transporter 1 600 °C. Chaque installation reçoit donc son propre miroir. La chaleur est utilisée en cascade à l'intérieur de chaque procédé et l'excédent est rayonné à la température la plus élevée atteignable. Seul le résidu sous 100 °C parvient à l'habitat. Les panneaux radiateurs sont la même tôle Fe-Ni que les cadres des miroirs — il suffit de ne pas appliquer le revêtement pour obtenir un radiateur.
