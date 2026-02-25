---
title: "Pourquoi les miroirs de Dyson meurent sur l'orbite de Mercure"
date: 2026-02-24T12:00:02+09:00
lastmod: 2026-02-24T12:00:02+09:00
tags: ["essaim-dyson", "mercure", "emballement-thermique", "miroir"]
image: "/images/post002.webp"
summary: "Sur l'orbite de Mercure (0,39 AU), une baisse de 5% de réflectivité ne réduit pas seulement la production — elle déclenche une boucle de rétroaction d'emballement thermique qui détruit le miroir. À L5 (1 AU), la même dégradation n'est qu'une erreur d'arrondi."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## L'avantage de 6,6x n'est pas gratuit

L'orbite de Mercure (0,39 AU) reçoit un flux solaire 6,6 fois supérieur à celui de 1 AU. L'efficacité par unité de surface est écrasante. Mais les miroirs n'ont pas une réflectivité de 100% — c'est l'énergie absorbée qui les tue.

---

## Chaleur absorbée et température d'équilibre

Énergie absorbée et température d'équilibre pour un miroir à 90% de réflectivité (Stefan-Boltzmann, émissivité côté arrière ε=0,5 — pour la surface du radiateur non revêtue, pas la face réfléchissante revêtue d'Al. Si l'émissivité du radiateur est plus basse, la température est encore plus élevée) :

| | L5 (1 AU) | Orbite de Mercure (0,39 AU) |
|---|---|---|
| Flux incident | 1 361 W/m² | 8 940 W/m² |
| Absorbé (10%) | 136 W/m² | **894 W/m²** |
| Temp. d'équilibre | ~−10°C | **~150°C** |

90–150°C est une température que les métaux peuvent supporter en soi. **Mais le problème réside dans ce qui se passe ensuite.**

---

## Boucle de rétroaction positive (Thermal Runaway)

À 150°C, la dégradation du revêtement s'accélère. L'interdiffusion Al-substrat suit la loi d'Arrhenius — elle croît exponentiellement avec la température.

```
Réflectivité 90% → 894 W/m² absorbés → 150°C
  ↓ Dégradation du revêtement
Réflectivité 85% → 1 341 W/m² absorbés → ~190°C
  ↓ Dégradation accélérée
Réflectivité 80% → 1 788 W/m² absorbés → ~230°C
  ↓ Seuil d'interdiffusion Al-substrat franchi
Réflectivité s'effondre → Mort du miroir
```

**Que se passe-t-il si la même baisse de 5% survient à L5 ?** Absorption supplémentaire : 68 W/m². Variation de température négligeable. La boucle de rétroaction ne s'active jamais.

---

## Les CME appuient sur la gâchette

La densité du vent solaire est inversement proportionnelle au carré de la distance. À 0,39 AU, elle est ~6,6 fois celle à 1 AU.

La menace la plus grave, ce sont les CME (éjections de masse coronale). À 0,39 AU, une CME n'a pas encore eu le temps de se disperser — elle frappe le miroir avec une densité d'énergie concentrée. Une seule CME puissante peut pulvériser la surface du revêtement → la réflectivité chute → l'emballement thermique commence.

Pour référence : la sonde MESSENGER n'aurait pas survécu sur l'orbite de Mercure sans un pare-soleil en céramique.

---

## Comparaison de la réalité opérationnelle

| | L5 (1 AU) | Orbite de Mercure (0,39 AU) |
|---|---|---|
| Temp. d'équilibre | −10°C (sûr) | 150°C (zone de dégradation) |
| Effet d'une perte de 5% de réflectivité | +68 W/m² (négligeable) | **+447 W/m² (début de l'emballement thermique)** |
| Tolérance aux CME | Élevée | Faible (6,6x densité) |
| Cycle de remplacement estimé | Décennies+ | Années à ~une décennie |
| Logistique de maintenance | Juste à côté du cluster industriel L5 | Nécessite une infrastructure de service dédiée |

---

## Résumé en une ligne

Sur l'orbite de Mercure, une perte de 5% de réflectivité n'est pas une réduction de 5% de la production — c'est le signal que le miroir commence à mourir. À L5, c'est une erreur d'arrondi.
