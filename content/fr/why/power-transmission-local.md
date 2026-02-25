---
title: "Pourquoi la transmission sans fil d'énergie est irréaliste"
date: 2026-02-24T12:00:06+09:00
lastmod: 2026-02-24T12:00:06+09:00
tags: ["transmission-énergie", "énergie-sans-fil", "consommation-locale"]
summary: "L'essaim de Dyson standard collecte l'énergie là où personne ne vit et doit la transmettre là où se trouvent les gens — avec 75 à 90 % de pertes. À L5, on place les usines à côté des miroirs et on branche."
image: "/images/power-transmission-local.webp"
author: "PARK JUN WOO"
imageCaption: "Radiotélescope d'Arecibo (305 m de diamètre). Recevoir une transmission d'énergie laser sans fil nécessiterait un récepteur de cette envergure. Photo : Mariordo / Wikimedia Commons / CC BY-SA 4.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## Collecter, c'est bien — mais où l'utiliser ?

Scénario standard de l'essaim de Dyson : démanteler Mercure, placer des miroirs/panneaux près du Soleil. Collecte d'énergie — réglé. Mais **où consomme-t-on cette énergie ?** Il n'y a rien près du Soleil.

S'il faut l'envoyer sur Terre — vérifions la physique de la transmission d'énergie sans fil (WPT).

---

## Faisceau micro-ondes : la limite de diffraction

Fréquence 2,45 GHz (λ = 0,122 m), orbite de Mercure → Terre (moyenne ~1 AU = 1,5×10¹¹ m) :

**Diamètre du spot ≈ 2,44 × λ × distance / diamètre de l'antenne d'émission**

| Diamètre de l'antenne d'émission | Diamètre du spot côté Terre | Faisabilité |
|---|---|---|
| 1 km | 44 600 km | 3,5× le diamètre de la Terre |
| 10 km | 4 460 km | Échelle du rayon terrestre |
| 100 km | 446 km | Rectenna de la taille de la péninsule coréenne |

En sens inverse — pour recevoir avec une rectenna de 10 km sur Terre :

```
Antenne d'émission requise = 2,44 × 0,122 × 1,5×10¹¹ / 10 000
                           = 4 460 km de diamètre
```

**Le diamètre de Mercure est de 4 880 km. Il faut une antenne de la taille de Mercure.**

---

## Et le laser ?

Avec λ = 1 μm, le problème de diffraction est considérablement réduit :

| Diamètre du miroir d'émission | Diamètre du spot côté Terre |
|---|---|
| 10 m | 36,6 km |
| 100 m | 3,7 km |

La taille du spot est réaliste. **Mais la chaîne d'efficacité de conversion est fatale :**

| Étape | Efficacité |
|---|---|
| Électricité → Laser | ~40–50 % |
| Transmission atmosphérique (dépendante de la météo) | ~50–80 % |
| Récepteur PV → Électricité | ~50–60 % |
| **Total** | **~10–24 %** |

On perd 75 à 90 % de l'électricité produite pendant la transmission. L'avantage de flux de 6,6× est plus qu'annulé ici.

---

## Problème supplémentaire en orbite de Mercure : occultation solaire

La période orbitale de Mercure est de 88 jours. Pendant une partie significative de l'orbite, **le Soleil se trouve entre Mercure et la Terre** — rendant la transmission par faisceau physiquement impossible durant ces intervalles. Sans satellites relais, la transmission continue est irréalisable.

---

## L5 : production locale, consommation locale

À L5, le problème de transmission n'existe tout simplement pas.

| | Transmission Mercure → Terre | Consommation locale à L5 |
|---|---|---|
| Distance de transmission | 0,5–1,5 AU | **Quelques km à quelques dizaines de km** |
| Méthode de transmission | Micro-ondes/Laser (sans fil) | **Câble filaire** |
| Efficacité totale | 10–24 % (laser) | **~95 %+** |
| Occultation solaire | Oui (cycle de 88 jours) | **Non** |
| Infrastructure de réception | Rectenna de milliers de km ou antenne de la taille de Mercure | **Inutile** |
| Consommateur | Terre (à 150 millions de km) | **Cylindres O'Neill adjacents + centres de données** |

Note : dans le vide spatial, les câbles supraconducteurs bénéficient d'un refroidissement quasi gratuit. Le fond diffus cosmologique à 2,7 K joue le rôle de réfrigérant.

---

## La vraie question : y a-t-il une raison d'envoyer de l'électricité sur Terre ?

Si L5 dispose d'installations industrielles, d'habitats et de centres de données :

- **Les résultats de calcul** (inférence IA, simulations) sont transmis par communication optique — les bits sont légers
- **Les produits manufacturés** sont transportés physiquement
- **Il n'y a aucune raison d'envoyer l'électricité elle-même sur Terre**

On ne transmet pas l'énergie — **on transmet les produits de l'énergie.** C'est le cœur du modèle de consommation locale à L5.

---

## Résumé en une ligne

Le concept standard de l'essaim de Dyson présente une contradiction fondamentale : « collecter l'énergie là où personne ne vit, puis l'envoyer là où se trouvent les gens. » À L5, on place les usines et les habitats à côté des miroirs et on branche.
