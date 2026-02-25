---
title: "Por que os espelhos de Dyson morrem na órbita de Mercúrio"
date: 2026-02-24T12:00:02+09:00
lastmod: 2026-02-24T12:00:02+09:00
tags: ["enxame-dyson", "mercúrio", "fuga-térmica", "espelho"]
image: "/images/post002.webp"
summary: "Na órbita de Mercúrio (0,39 AU), uma queda de 5% na refletividade não apenas reduz a produção — ela desencadeia um ciclo de retroalimentação de fuga térmica que destrói o espelho. Em L5 (1 AU), a mesma degradação é erro de arredondamento."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## A vantagem de 6,6x não é de graça

A órbita de Mercúrio (0,39 AU) recebe um fluxo solar 6,6 vezes maior que a 1 AU. A eficiência por unidade de área é esmagadora. Mas espelhos não têm 100% de refletividade — a energia absorvida é o que os mata.

---

## Calor absorvido e temperatura de equilíbrio

Energia absorvida e temperatura de equilíbrio para um espelho com refletividade de 90% (Stefan-Boltzmann, emissividade do lado posterior ε=0,5 — para a superfície do radiador sem revestimento, não a face refletiva revestida de Al. Se a emissividade do radiador for menor, a temperatura será ainda maior):

| | L5 (1 AU) | Órbita de Mercúrio (0,39 AU) |
|---|---|---|
| Fluxo incidente | 1.361 W/m² | 8.940 W/m² |
| Absorvido (10%) | 136 W/m² | **894 W/m²** |
| Temp. de equilíbrio | ~−10°C | **~150°C** |

90–150°C é uma temperatura que metais conseguem suportar por si só. **Mas o problema está no que acontece em seguida.**

---

## Ciclo de retroalimentação positiva (Thermal Runaway)

A 150°C, a degradação do revestimento se acelera. A interdifusão Al-substrato segue a lei de Arrhenius — escala exponencialmente com a temperatura.

```
Refletividade 90% → 894 W/m² absorvidos → 150°C
  ↓ Degradação do revestimento
Refletividade 85% → 1.341 W/m² absorvidos → ~190°C
  ↓ Degradação acelerada
Refletividade 80% → 1.788 W/m² absorvidos → ~230°C
  ↓ Limiar de interdifusão Al-substrato ultrapassado
Refletividade despenca → Morte do espelho
```

**E se a mesma queda de 5% acontecer em L5?** Absorção adicional: 68 W/m². Variação de temperatura insignificante. O ciclo de retroalimentação nunca se ativa.

---

## CME puxa o gatilho

A densidade do vento solar escala com o inverso do quadrado da distância. A 0,39 AU, é ~6,6 vezes a densidade a 1 AU.

A ameaça maior são as CMEs (ejeções de massa coronal). A 0,39 AU, uma CME ainda não teve tempo de se expandir — atinge o espelho com densidade de energia concentrada. Uma única CME poderosa pode pulverizar a superfície do revestimento → refletividade cai → fuga térmica começa.

Para referência: a sonda MESSENGER não sobreviveria na órbita de Mercúrio sem um protetor solar cerâmico.

---

## Comparação da realidade operacional

| | L5 (1 AU) | Órbita de Mercúrio (0,39 AU) |
|---|---|---|
| Temp. de equilíbrio | −10°C (seguro) | 150°C (zona de degradação) |
| Efeito de 5% de perda de refletividade | +68 W/m² (desprezível) | **+447 W/m² (início da fuga térmica)** |
| Tolerância a CME | Alta | Baixa (6,6x densidade) |
| Ciclo de substituição estimado | Décadas+ | Anos a ~uma década |
| Logística de manutenção | Ao lado do cluster industrial L5 | Requer infraestrutura de serviço separada |

---

## Resumo em uma linha

Na órbita de Mercúrio, uma perda de 5% na refletividade não é uma redução de 5% na produção — é o sinal de que o espelho está começando a morrer. Em L5, é erro de arredondamento.
