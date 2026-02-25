---
title: "Por qué la transmisión inalámbrica de energía es impracticable"
date: 2026-02-24T12:00:06+09:00
lastmod: 2026-02-24T12:00:06+09:00
tags: ["transmisión-energía", "energía-inalámbrica", "consumo-local"]
summary: "El enjambre de Dyson estándar recolecta energía donde nadie vive y debe enviarla donde están las personas, perdiendo el 75-90% en transmisión. En L5, se colocan las fábricas junto a los espejos y se conectan directamente."
image: "/images/power-transmission-local.webp"
author: "PARK JUN WOO"
imageCaption: "Radiotelescopio de Arecibo (305 m de diametro). Recibir transmision inalambrica de energia por laser requeriria un receptor de esta escala. Foto: Mariordo / Wikimedia Commons / CC BY-SA 4.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## Recolectar es fácil — pero ¿dónde se usa?

Escenario estándar del enjambre de Dyson: desmantelar Mercurio, colocar espejos/paneles cerca del Sol. Recolección de energía — resuelto. Pero, **¿dónde se consume esa energía?** Cerca del Sol no hay nada.

Si hay que enviarla a la Tierra — revisemos la física de la transmisión inalámbrica de energía (WPT).

---

## Haz de microondas: el límite de difracción

Frecuencia 2.45 GHz (λ = 0.122 m), órbita de Mercurio → Tierra (promedio ~1 AU = 1.5×10¹¹ m):

**Diámetro del spot ≈ 2.44 × λ × distancia / diámetro de antena transmisora**

| Diámetro de antena transmisora | Diámetro del spot en la Tierra | Viabilidad |
|---|---|---|
| 1 km | 44,600 km | 3.5× el diámetro de la Tierra |
| 10 km | 4,460 km | Escala del radio terrestre |
| 100 km | 446 km | Rectenna del tamaño de la península coreana |

A la inversa — para recibir con una rectenna de 10 km en la Tierra:

```
Antena transmisora requerida = 2.44 × 0.122 × 1.5×10¹¹ / 10,000
                             = 4,460 km de diámetro
```

**El diámetro de Mercurio es 4,880 km. Se necesita una antena del tamaño de Mercurio.**

---

## ¿Y con láser?

Con λ = 1 μm, el problema de difracción se reduce enormemente:

| Diámetro del espejo transmisor | Diámetro del spot en la Tierra |
|---|---|
| 10 m | 36.6 km |
| 100 m | 3.7 km |

El tamaño del spot es realista. **Pero la cadena de eficiencia de conversión es letal:**

| Etapa | Eficiencia |
|---|---|
| Electricidad → Láser | ~40–50% |
| Transmisión atmosférica (dependiente del clima) | ~50–80% |
| Receptor PV → Electricidad | ~50–60% |
| **Total** | **~10–24%** |

Se pierde el 75–90% de la electricidad generada durante la transmisión. La ventaja de flujo de 6.6× queda más que anulada aquí.

---

## Problema adicional en la órbita de Mercurio: ocultación solar

El período orbital de Mercurio es de 88 días. Durante una parte significativa de la órbita, **el Sol se interpone entre Mercurio y la Tierra** — haciendo imposible la transmisión por haz en esos intervalos. Sin satélites de relevo, la transmisión continua no es factible.

---

## L5: producción local, consumo local

En L5, el problema de transmisión simplemente no existe.

| | Transmisión Mercurio → Tierra | Consumo local en L5 |
|---|---|---|
| Distancia de transmisión | 0.5–1.5 AU | **Unos km a decenas de km** |
| Método de transmisión | Microondas/Láser (inalámbrico) | **Cable con conexión física** |
| Eficiencia total | 10–24% (láser) | **~95%+** |
| Ocultación solar | Sí (ciclo de 88 días) | **No** |
| Infraestructura de recepción | Rectenna de miles de km o antena del tamaño de Mercurio | **No necesaria** |
| Consumidor | Tierra (a 150 millones de km) | **Cilindros O'Neill adyacentes + centros de datos** |

Nota: en el vacío espacial, los cables superconductores se enfrían prácticamente gratis. La radiación cósmica de fondo a 2.7 K actúa como refrigerante.

---

## La verdadera pregunta: ¿hay razón para enviar electricidad a la Tierra?

Si L5 tiene instalaciones industriales, hábitats y centros de datos:

- **Resultados de cómputo** (inferencia de IA, simulaciones) se transmiten por comunicación óptica — los bits son ligeros
- **Productos manufacturados** se transportan físicamente
- **No hay necesidad de enviar electricidad en sí misma a la Tierra**

No se transmite energía — **se transmiten los productos de la energía.** Este es el núcleo del modelo de consumo local en L5.

---

## Resumen en una línea

El concepto estándar del enjambre de Dyson tiene una contradicción fundamental: "recolectar energía donde nadie vive y enviarla donde están las personas." En L5, se colocan las fábricas y los hábitats junto a los espejos y se conectan directamente.
