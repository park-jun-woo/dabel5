---
title: "Por qué los espejos de Dyson mueren en la órbita de Mercurio"
date: 2026-02-24T12:00:02+09:00
lastmod: 2026-02-24T12:00:02+09:00
tags: ["enjambre-dyson", "mercurio", "desbordamiento-térmico", "espejo"]
image: "/images/post002.webp"
summary: "En la órbita de Mercurio (0,39 AU), una caída del 5% en reflectividad no solo reduce la producción: desencadena un bucle de retroalimentación de fuga térmica que destruye el espejo. En L5 (1 AU), la misma degradación es un error de redondeo."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## La ventaja de 6,6x no es gratis

La órbita de Mercurio (0,39 AU) recibe un flujo solar 6,6 veces mayor que a 1 AU. La eficiencia por unidad de área es abrumadora. Pero los espejos no tienen una reflectividad del 100% — la energía absorbida es lo que los mata.

---

## Calor absorbido y temperatura de equilibrio

Energía absorbida y temperatura de equilibrio para un espejo con reflectividad del 90% (Stefan-Boltzmann, emisividad del lado posterior ε=0,5 — para la superficie radiadora sin recubrimiento, no la cara reflectante con recubrimiento de Al. Si la emisividad del radiador es menor, la temperatura es aún mayor):

| | L5 (1 AU) | Órbita de Mercurio (0,39 AU) |
|---|---|---|
| Flujo incidente | 1.361 W/m² | 8.940 W/m² |
| Absorbido (10%) | 136 W/m² | **894 W/m²** |
| Temp. de equilibrio | ~−10°C | **~150°C** |

90–150°C es una temperatura que los metales pueden soportar por sí sola. **Pero el problema está en lo que ocurre después.**

---

## Bucle de retroalimentación positiva (Thermal Runaway)

A 150°C, la degradación del recubrimiento se acelera. La interdifusión Al-sustrato sigue la ley de Arrhenius — escala exponencialmente con la temperatura.

```
Reflectividad 90% → 894 W/m² absorbidos → 150°C
  ↓ Degradación del recubrimiento
Reflectividad 85% → 1.341 W/m² absorbidos → ~190°C
  ↓ Degradación acelerada
Reflectividad 80% → 1.788 W/m² absorbidos → ~230°C
  ↓ Umbral de interdifusión Al-sustrato superado
Reflectividad se desploma → Muerte del espejo
```

**¿Qué pasa si la misma caída del 5% ocurre en L5?** Absorción adicional: 68 W/m². Cambio de temperatura insignificante. El bucle de retroalimentación nunca se activa.

---

## Las CME aprietan el gatillo

La densidad del viento solar escala con el inverso del cuadrado de la distancia. A 0,39 AU, es ~6,6 veces la densidad a 1 AU.

La amenaza mayor son las CME (eyecciones de masa coronal). A 0,39 AU, una CME no ha tenido tiempo de expandirse — impacta el espejo con una densidad de energía concentrada. Una sola CME potente puede pulverizar la superficie del recubrimiento → baja la reflectividad → comienza la fuga térmica.

Como referencia: la sonda MESSENGER no podría haber sobrevivido en la órbita de Mercurio sin un parasol cerámico.

---

## Comparación de la realidad operativa

| | L5 (1 AU) | Órbita de Mercurio (0,39 AU) |
|---|---|---|
| Temp. de equilibrio | −10°C (seguro) | 150°C (zona de degradación) |
| Efecto de 5% de pérdida de reflectividad | +68 W/m² (despreciable) | **+447 W/m² (inicio de fuga térmica)** |
| Tolerancia a CME | Alta | Baja (6,6x densidad) |
| Ciclo de reemplazo estimado | Décadas+ | Años a ~una década |
| Logística de mantenimiento | Junto al clúster industrial de L5 | Requiere infraestructura de servicio independiente |

---

## Resumen en una línea

En la órbita de Mercurio, una pérdida de reflectividad del 5% no es una reducción del 5% en la producción — es la señal de que el espejo empieza a morir. En L5, es un error de redondeo.
