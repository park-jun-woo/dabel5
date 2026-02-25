---
title: "Por qué L5, no cerca del Sol"
date: 2026-02-24T12:00:05+09:00
lastmod: 2026-02-24T12:00:05+09:00
tags: ["enjambre-dyson", "SEL5", "autorreplicación", "escalado"]
image: "/images/post005.webp"
summary: "El escenario estándar del enjambre de Dyson asume desmantelar Mercurio cerca del Sol. Pero, ¿qué pasa si usas recursos asteroidales y construyes en el punto Sol-Tierra L5? Aquí están los cálculos."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Cuestionando la sabiduría convencional

El escenario estándar que todos imaginan al hablar de un enjambre de Dyson: desmantelar Mercurio y colocar paneles/espejos cerca del Sol. Es el marco establecido por la serie de Isaac Arthur, y la mayoría lo acepta como algo evidente.

Pero calculé un enfoque diferente: ¿qué pasa si usas recursos asteroidales y construyes en el punto Sol-Tierra L5?

---

## ¿Por qué L5?

### Flujo solar
- L5 (1 AU): ~1.361 W/m² — igual que la órbita terrestre
- Órbita de Mercurio (0,39 AU): ~8.942 W/m² — unas 6,6 veces más intenso
- "¿No es mejor Mercurio?" — Sí, por unidad de área. Pero eso no es todo

### Ventajas ocultas de L5
1. **Punto de estabilidad gravitacional** — Coste de mantenimiento orbital casi nulo. Cerca de Mercurio, el gradiente gravitacional solar es pronunciado y requiere correcciones constantes
2. **Luz solar ininterrumpida 24/7/365** — La sombra de la Tierra no puede alcanzarlo (150 millones de km). Sin eclipses
3. **Región estable de millones de km** — Se pueden desplegar cientos de miles de módulos sin interferencia mutua
4. **Distancia fija a la Tierra** — Simplifica la planificación logística. El retardo de comunicación es de ~8 min 20 s en un sentido (no es tiempo real, pero se resuelve con operaciones autónomas de IA)
5. **Habitable** — Cerca de Mercurio, el entorno térmico es extremo. L5 hace que el diseño de hábitats humanos sea mucho más realista

---

## Recursos: desmantelamiento de Mercurio vs asteroides

### Costes ocultos del enfoque de Mercurio
- Velocidad de escape de Mercurio: 4,25 km/s — un pozo gravitatorio considerable
- Temperatura superficial de Mercurio: 430 °C durante el día — gestión térmica extrema para equipos de minería
- Mercurio → despliegue en órbita solar: se requiere delta-V adicional
- **El mayor problema: Mercurio es un planeta** — La minería a gran escala con 0,38g de gravedad superficial es esencialmente una variante de la minería terrestre

### Enfoque asteroidal (1986 DA)
- Asteroide metálico tipo M: **90%+ aleación Fe-Ni** — prácticamente metal puro
- Recursos estimados: más de 20.000 millones de toneladas (diámetro ~2,3 km, densidad aparente de asteroide tipo M)
- Microgravedad → energía de minería mínima, velocidad de escape despreciable
- Incluso los subproductos se aprovechan: escoria de silicatos → blindaje contra radiación + materia prima para lingotes de silicio

| Comparación | Desmantelamiento de Mercurio | Asteroide (1986 DA) |
|------|----------|----------------|
| Escape del pozo gravitatorio | 4,25 km/s | ~unos pocos m/s |
| Temperatura superficial | 430 °C (diurna) | Criogénica (fácil de gestionar) |
| Composición de recursos | Mayormente silicatos, requiere separación de metales | 90%+ aleación Fe-Ni (casi lista para usar) |
| Complejidad del equipo minero | Alta (gravedad, calor) | Baja (microgravedad) |
| Volumen total de recursos | Abrumador (un planeta entero) | Suficiente para el bootstrap de K1 |

Mercurio gana de forma abrumadora en volumen total de recursos, pero **para la primera etapa (bootstrap phase), los asteroides son mucho más prácticos.**

---

## La clave: el bucle de autorreplicación

El verdadero diferenciador de este diseño no es simplemente "dónde minar y dónde colocar".

**Mineral asteroidal → fundición al vacío con calor solar de espejos Dyson en L5 → el producto construye nuevos espejos → el área de captación crece → la velocidad de fundición aumenta → crecimiento exponencial**

1. Los espejos semilla concentran la luz solar
2. El calor concentrado eleva el mineral a ~1.500 °C → producción de aleación Fe-Ni
3. La aleación fabrica nuevos marcos de espejos
4. Se añaden nuevos espejos → el área de captación crece → **comienza el crecimiento exponencial**

### Escalado

| Escala | Potencia | vs Tierra | Población | Computación IA |
|------|------|----------|------|---------|
| 1 módulo | 370 MW | 1 central nuclear pequeña | 2.500 | 32 EF |
| 10 módulos | 3,7 GW | 3 centrales nucleares grandes | 25.000 | 320 EF |
| 1.000 módulos | 370 GW | 2% de la Tierra | 2,5M | 32 ZF |
| 10.000 módulos | 3,7 TW | 20% de la Tierra | 25M | 320 ZF |
| 200.000 módulos | 74 TW | **4 veces la Tierra** | 500M | 6.400 ZF |

El periodo de duplicación depende del presupuesto de masa por módulo y la madurez del proceso. Suponiendo un rango de 2 a 5 años, alcanzar la escala K1.0 desde 1 módulo requiere entre 50 y 125 años.

---

## No estamos diciendo que Mercurio sea incorrecto

Seamos honestos sobre un punto. La humanidad se encuentra actualmente en K 0,73. Incluso hasta K1.0 (10¹⁶ W) hay una brecha de ~550 veces respecto a donde estamos ahora. **Antes de hablar de K2, hay que alcanzar K1 primero.**

La escala necesaria para K1.0 — ~27 millones de módulos, ~10 PW — es perfectamente alcanzable con recursos asteroidales. No hace falta tocar Mercurio. El desmantelamiento de Mercurio solo se vuelve necesario en términos de volumen total de recursos a partir de K1.5+ (10²¹ W).

Mercurio es la autopista hacia K2. Pero lo que necesitamos ahora es la rampa de acceso a esa autopista. **No necesitas una autopista para construir una autopista.**

En la fase de bootstrap:
- Los asteroides tienen costes de acceso más bajos
- L5 tiene costes operativos más bajos
- El bucle de autorreplicación se inicia antes

¿Y si alcanzar K1 en L5 primero, y luego usar esa capacidad industrial para desmantelar Mercurio, es en realidad el camino más rápido?
