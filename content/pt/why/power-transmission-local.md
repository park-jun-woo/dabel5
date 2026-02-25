---
title: "Por que a transmissão sem fio de energia é impraticável"
date: 2026-02-24T12:00:06+09:00
lastmod: 2026-02-24T12:00:06+09:00
tags: ["transmissão-energia", "energia-sem-fio", "consumo-local"]
summary: "O enxame de Dyson padrão coleta energia onde ninguém vive e precisa transmiti-la para onde as pessoas estão — perdendo 75-90% na transmissão. Em L5, colocam-se as fábricas ao lado dos espelhos e conecta-se diretamente."
image: "/images/power-transmission-local.webp"
author: "PARK JUN WOO"
imageCaption: "Radiotelescópio de Arecibo (305 m de diâmetro). Receber transmissão sem fio de energia por laser exigiria um receptor desta escala. Foto: Mariordo / Wikimedia Commons / CC BY-SA 4.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## Coletar é fácil — mas onde usar?

Cenário padrão do enxame de Dyson: desmontar Mercúrio, posicionar espelhos/painéis perto do Sol. Coleta de energia — resolvido. Mas **onde essa energia é consumida?** Perto do Sol não há nada.

Se for necessário enviá-la à Terra — vamos verificar a física da transmissão sem fio de energia (WPT).

---

## Feixe de micro-ondas: o limite de difração

Frequência 2.45 GHz (λ = 0.122 m), órbita de Mercúrio → Terra (média ~1 AU = 1.5×10¹¹ m):

**Diâmetro do spot ≈ 2.44 × λ × distância / diâmetro da antena transmissora**

| Diâmetro da antena transmissora | Diâmetro do spot na Terra | Viabilidade |
|---|---|---|
| 1 km | 44,600 km | 3,5× o diâmetro da Terra |
| 10 km | 4,460 km | Escala do raio terrestre |
| 100 km | 446 km | Rectenna do tamanho da península coreana |

Inversamente — para receber com uma rectenna de 10 km na Terra:

```
Antena transmissora necessária = 2.44 × 0.122 × 1.5×10¹¹ / 10,000
                               = 4,460 km de diâmetro
```

**O diâmetro de Mercúrio é 4,880 km. É necessária uma antena do tamanho de Mercúrio.**

---

## E com laser?

Com λ = 1 μm, o problema de difração é bastante reduzido:

| Diâmetro do espelho transmissor | Diâmetro do spot na Terra |
|---|---|
| 10 m | 36.6 km |
| 100 m | 3.7 km |

O tamanho do spot é realista. **Mas a cadeia de eficiência de conversão é fatal:**

| Etapa | Eficiência |
|---|---|
| Eletricidade → Laser | ~40–50% |
| Transmissão atmosférica (dependente do clima) | ~50–80% |
| Receptor PV → Eletricidade | ~50–60% |
| **Total** | **~10–24%** |

Perde-se 75–90% da eletricidade gerada durante a transmissão. A vantagem de fluxo de 6,6× é mais do que anulada aqui.

---

## Problema adicional na órbita de Mercúrio: ocultação solar

O período orbital de Mercúrio é de 88 dias. Durante uma parte significativa da órbita, **o Sol se posiciona entre Mercúrio e a Terra** — tornando a transmissão por feixe fisicamente impossível nesses intervalos. Sem satélites de retransmissão, a transmissão contínua é inviável.

---

## L5: produção local, consumo local

Em L5, o problema de transmissão simplesmente não existe.

| | Transmissão Mercúrio → Terra | Consumo local em L5 |
|---|---|---|
| Distância de transmissão | 0.5–1.5 AU | **Alguns km a dezenas de km** |
| Método de transmissão | Micro-ondas/Laser (sem fio) | **Cabo com fio** |
| Eficiência total | 10–24% (laser) | **~95%+** |
| Ocultação solar | Sim (ciclo de 88 dias) | **Não** |
| Infraestrutura de recepção | Rectenna de milhares de km ou antena do tamanho de Mercúrio | **Desnecessária** |
| Consumidor | Terra (a 150 milhões de km) | **Cilindros O'Neill adjacentes + data centers** |

Nota: no vácuo espacial, cabos supercondutores têm resfriamento praticamente gratuito. A radiação cósmica de fundo a 2.7 K funciona como refrigerante.

---

## A verdadeira questão: há razão para enviar eletricidade à Terra?

Se L5 possui instalações industriais, habitats e data centers:

- **Resultados computacionais** (inferência de IA, simulações) são transmitidos por comunicação óptica — bits são leves
- **Produtos manufaturados** são transportados fisicamente
- **Não há necessidade de enviar eletricidade em si à Terra**

Não se transmite energia — **transmitem-se os produtos da energia.** Este é o cerne do modelo de consumo local em L5.

---

## Resumo em uma linha

O conceito padrão do enxame de Dyson tem uma contradição fundamental: "coletar energia onde ninguém vive e enviá-la para onde as pessoas estão." Em L5, colocam-se as fábricas e os habitats ao lado dos espelhos e conecta-se diretamente.
