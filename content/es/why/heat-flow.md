---
title: "Por qué no se puede transportar calor por tuberías"
date: 2026-02-24T12:00:08+09:00
lastmod: 2026-02-24T12:00:08+09:00
tags: ["gestión-térmica", "radiador", "cascada-térmica"]
summary: "Ningún fluido sobrevive a 1.600 °C en un circuito cerrado. Cada instalación recibe su propio espejo, disipa el calor residual a la mayor temperatura posible y solo el remanente por debajo de 100 °C llega al hábitat."
image: "/images/post008.webp"
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## Tarea pendiente del artículo anterior

El artículo anterior argumentó que las turbinas superan a los paneles fotovoltaicos para la autorreplicación. Eficiencia del 30 %, salida eléctrica de 370 MW, los 855 MW restantes son calor.

Y se afirmó:

> "El mismo 70 % pasa secuencialmente por la fundición, la fábrica, el hábitat y el centro de datos: todo se aprovecha."

Conceptualmente correcto. El calor residual de las turbinas es mucho más útil que el rechazo a 60 °C de los paneles fotovoltaicos. **Pero el "paso secuencial" no es un diseño real.** Este artículo traza el flujo térmico verdadero.

---

## Primero una corrección: por qué el "paso secuencial" no funciona

### Problema 1: temperatura del calor residual de la turbina

Termodinámica de la turbina (ciclo Brayton):
- Lado caliente: ~1.200 °C (el fluido de trabajo se calienta con luz solar concentrada)
- Lado frío: ~227 °C (aquí se rechaza el calor)
- Eficiencia 30 % → 370 MW eléctricos, **855 MW rechazados a ~227 °C**

Punto clave: **Todo el calor residual de la turbina sale a ~227 °C.** La fundición requiere 1.600 °C. No se puede operar un proceso a 1.600 °C con calor de 227 °C: segunda ley de la termodinámica. El calor solo fluye de caliente a frío.

La flecha "800–1.000 °C → fundición" del diagrama anterior no era calor residual de la turbina. El calor de la fundición proviene **directamente del espejo**.

### Problema 2: no existe medio que soporte 1.000 °C

Incluso si existiera calor a 1.600 °C en algún lugar, ¿se podría transportar por tuberías a otra instalación?

| Medio de transferencia | Temp. máx. de operación | Límite |
|---|---|---|
| Agua presurizada | ~340 °C | Punto crítico |
| Sales fundidas | ~565 °C | Descomposición |
| Sodio líquido | ~800 °C | Presión de vapor |
| Helio a alta presión | ~950 °C | Límite del material de tuberías |
| **Por encima de 1.000 °C** | **N/A** | **No existe medio** |

No hay fluido capaz de transportar calor a 1.600 °C. La única forma de entregar energía a esta temperatura es **la luz.** Irradiación directa mediante espejos.

### Problema 3: distancia entre módulos

En un clúster especializado, los módulos de fundición y los de centros de datos están **separados 50–100 km.** Es una separación deliberada contra vibraciones, contaminación e interferencia térmica. A esta distancia las tuberías térmicas son inviables.

**Conclusión: transportar calor residual de turbinas a procesos de alta temperatura es físicamente imposible.**

---

## El diseño real: cada instalación recibe su propio espejo

Los verdaderos principios del flujo térmico:

1. **Cada módulo recibe su calor directamente de su propio espejo** — transmitido como luz, sin medio
2. **La cascada funciona solo dentro de cada módulo** — el calor residual del proceso se reutiliza a temperaturas progresivamente más bajas
3. **No hay transferencia de calor entre módulos** — limitaciones de distancia y medio
4. **Solo el calor residual por debajo de 100 °C se suministra al hábitat** — las tuberías son viables y la temperatura coincide con la demanda del hábitat

### Asignación de espejos (clúster de 10 módulos)

| Tipo de módulo | Cant. | Reparto del espejo (calor : potencia) | Fuente de alta temp. |
|---|---|---|---|
| Módulo de fundición | 3 | 90 : 10 | Espejo → directo 1.600 °C |
| Módulo de lingotes | 1 | 70 : 30 | Espejo → directo 1.400 °C |
| Módulo estructural | 2 | 60 : 40 | Espejo → directo 800–1.200 °C |
| Módulo de fabricación | 1 | 20 : 80 | Espejo → directo 900 °C |
| Centro de datos | 2 | 5 : 95 | Espejo → turbina → electricidad |
| Hábitat / logística | 1 | 30 : 70 | Espejo → turbina → electricidad |

**Por encima de 1.000 °C, la luz entrega el calor directamente.** Las turbinas operan solo en módulos que necesitan principalmente electricidad (centros de datos, hábitats).

---

## Física del radiador: la ley T⁴

La única forma de disipar calor en el espacio es **la radiación infrarroja.** Sin convección ni conducción.

Ley de Stefan-Boltzmann:

**Potencia radiada = ε × σ × A × T⁴**

(ε: emisividad, σ: constante de Stefan-Boltzmann, A: área, T: temperatura absoluta)

La clave es **T⁴**. El doble de temperatura, 16× la potencia radiada. Inversamente, el área necesaria para la misma carga térmica se reduce a 1/16.

| Temp. del radiador | Área por MW | Analogía |
|---|---|---|
| 800 °C (1.073 K) | **8 m²** | Una plaza de aparcamiento |
| 400 °C (673 K) | **50 m²** | Un apartamento |
| 227 °C (500 K) | **166 m²** | Una cancha de tenis |
| 100 °C (373 K) | **535 m²** | Tres canchas de baloncesto |
| 60 °C (333 K) | **844 m²** | 1/8 de un campo de fútbol |

(Radiación por ambas caras, emisividad ε = 0,85, chapa Fe-Ni sin recubrimiento)

**Lección: lo que se disipa con 8 m² a 800 °C necesita 844 m² a 60 °C. Más de 100×.**

Por tanto, el principio fundamental de la gestión térmica: **"El calor que no se puede usar se disipa de inmediato a la mayor temperatura posible."**

### Material del radiador

Los radiadores forman parte del bucle de autorreplicación:
- **Material:** chapa delgada de Fe-Ni de origen asteroidal
- **Superficie:** sin recubrimiento de aluminio (al contrario que los espejos) — el Fe-Ni sin recubrir tiene alta emisividad infrarroja, ideal para radiar
- **Fabricación:** misma línea de chapa que los marcos de espejos. Solo se omite el paso de recubrimiento
- **Recursos adicionales:** cero. Mismo material, mismo proceso, distinto producto

---

## Flujo térmico por instalación

### Módulo de fundición — el calor es protagonista (90 % calor, 10 % potencia)

El módulo de fundición recibe el 90 % de la energía de su espejo como calor directo. Una turbina pequeña (10 %) genera electricidad para motores y robots.

```
☀️ Espejo dedicado (90 % → irradiación directa, 10 % → turbina pequeña)
 │
 ▼
Horno de fundición (1.600 °C) ← Calentado directamente por luz del espejo, sin medio
 │
 │ Calor residual ~800 °C ← Desde aquí un medio (He / metal líquido) puede transportarlo
 ├→ Tratamiento térmico de aleaciones, recocido (usa 800 °C)
 ├→ Excedente → ★ Radiador A (800 °C) — 8 m²/MW, compacto
 │
 │ Calor residual ~400 °C
 ├→ Precalentamiento, calentamiento auxiliar (usa 400 °C)
 ├→ Excedente → ★ Radiador B (400 °C) — 50 m²/MW, mediano
 │
 │ Calor residual ~200 °C
 ├→ ★ Radiador C (200 °C) — la mayor parte se disipa aquí
 │
 │ Residual < 100 °C
 └→ Puede enviarse al hábitat por tubería

Calor residual de turbina pequeña (~227 °C) → ★ Radiador D
```

El módulo de fundición usa el calor de arriba abajo, **radiando el excedente en cada etapa.** Los radiadores de alta temperatura son pequeños, así que la penalización es baja. Solo el residuo por debajo de 100 °C se envía al hábitat.

### Módulo de centro de datos — la electricidad es protagonista (5 % calor, 95 % potencia)

El centro de datos es el módulo más difícil de refrigerar. El 95 % de la energía de su espejo pasa por turbina → electricidad → chips → calor, todo saliendo a ~60 °C.

```
☀️ Espejo dedicado (95 % → turbina grande, 5 % → calor auxiliar)
 │
 ▼
Turbina grande → electricidad de ~370 MW
 │
 │ Calor residual de turbina ~227 °C (~855 MW)
 └→ ★ Radiador A (227 °C) — 166 m²/MW
     La mayor parte del calor de turbina se disipa aquí

Operación de chips → toda la electricidad se convierte en calor
 │
 │ Calor de chips ~60 °C
 │  Radiación directa a 60 °C: 844 m²/MW → 111 MW necesitan ~94.000 m²
 │
 ├→ [Bomba de calor] 60 °C → 200 °C (COP ~3, potencia ~37 MW)
 │   └→ ★ Radiador B (200 °C) — área reducida a ~1/4
 │
 └→ Residual < 100 °C → puede suministrarse al hábitat
```

**La bomba de calor es la tecnología clave.** Elevar el calor de 60 °C a 200 °C reduce drásticamente el área del radiador. La potencia de la bomba (~37 MW) proviene de la propia turbina. Tanto la turbina como la bomba de calor se fabrican in situ con Fe-Ni + Ti.

### Módulo estructural (60 % calor, 40 % potencia)

```
☀️ Espejo dedicado (60 % → calentamiento directo, 40 % → turbina)
 │
 ▼
Soldadura / tratamiento térmico (800–1.200 °C) ← Calentamiento directo por espejo
 │ Calor residual ~400 °C
 ├→ Precalentamiento para conformado / plegado (usa 400 °C)
 ├→ Excedente → ★ Radiador (400 °C)
 │ Calor residual ~200 °C
 ├→ ★ Radiador (200 °C)
 │ Residual < 100 °C
 └→ Puede suministrarse al hábitat

Turbina (40 %) → electricidad (robots, CNC, soldadoras)
 └→ Calor residual de turbina → ★ Radiador (227 °C)
```

### Módulo de hábitat / logística — consumidor de calor residual por debajo de 100 °C

El hábitat es el sumidero térmico final. Su propia turbina produce electricidad para soporte vital, iluminación y agricultura, mientras **recibe calor residual por debajo de 100 °C de módulos cercanos.**

```
☀️ Espejo dedicado (30 % → calor, 70 % → turbina)
 │
 ├→ Turbina → electricidad (soporte vital, iluminación, LEDs agrícolas)
 │   Calor residual (~227 °C) → ★ Radiador
 │
 └→ Calor → agua caliente, calefacción auxiliar
     └→ Residual → ★ Radiador

Calor residual <100 °C de módulos cercanos (fundición, estructural)
 │
 └→ Calefacción del hábitat, agua caliente, calentamiento de suelo agrícola
     └→ Residual → radiado desde el casco exterior del hábitat (la estructura misma actúa como radiador)
```

La demanda térmica del hábitat (calefacción, agua caliente) es modesta comparada con los volúmenes de calor residual industrial. El remanente por debajo de 100 °C de módulos cercanos es más que suficiente. **El hábitat recibe calefacción gratuita — los módulos industriales no generan calor para el hábitat.**

---

## Radiación distribuida: la imagen completa

Resumen del flujo térmico de todo el clúster:

```
☀️ Luz solar → Espejos → Distribuida directamente a cada módulo
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
[Fundición]    [Estructural]   [Centro de datos]
 Espejo→1.600°C Espejo→1.200°C  Espejo→Turbina→Elec.
    │               │               │
    ▼               ▼               ▼
 ★Rad.(800°C)   ★Rad.(400°C)   ★Rad.(227°C) ← residual turbina
 ★Rad.(400°C)   ★Rad.(200°C)   ★Rad.(200°C) ← tras bomba de calor
 ★Rad.(200°C)       │               │
    │               ▼               ▼
    └──── <100°C ──→ [Hábitat] ←── <100°C
                      Calefacción y agua caliente
                         │
                    ★Rad.(casco, ~30°C)
```

**No es "paso secuencial" sino "distribución en paralelo + radiación individual + solo se comparte la baja temperatura".** Cada módulo recibe calor de su propio espejo, lo disipa desde sus propios radiadores y solo pasa los restos al hábitat.

### Por qué es mejor

1. **Los radiadores de alta temperatura son diminutos** — 8 m² para disipar 1 MW a 800 °C. Basta con una pequeña aleta junto al proceso
2. **Sin tuberías entre módulos** — evita la pesadilla de 50 km de tuberías de alta temperatura
3. **Cada módulo es térmicamente independiente** — el mantenimiento de uno no afecta a los demás
4. **El hábitat permanece seguro** — ninguna tubería de 1.600 °C atraviesa las zonas habitadas

---

## Corrección del artículo anterior: ¿adónde va realmente el 70 %?

El artículo anterior decía "los PV desperdician el 70 %, las turbinas lo usan". ¿Sigue siendo correcto?

**Sí.** Pero el mecanismo difiere:

| | PV | Sistema de turbinas |
|---|---|---|
| 30 % | Electricidad | Electricidad |
| 70 % restante | Calor residual a 60–80 °C → **sin uso** | Distribuido como calentamiento directo por espejo a cada proceso → **usado en fundición, conformado, tratamiento térmico** |
| Carga de radiación | El 70 % completo radiado a baja temperatura (radiador enorme) | Radiación escalonada a alta temperatura (radiadores pequeños distribuidos) |

El 70 % del PV es todo 60–80 °C — la peor temperatura tanto para la industria como para la radiación. En el sistema de turbinas, ese 70 % se entrega a cada proceso a la temperatura exacta que necesita, y el calor residual se radia a la mayor temperatura posible.

**Lo que realmente significa "usar el 70 % restante": no es el calor residual de la turbina, sino la energía térmica del espejo consumida directamente por cada proceso.**

---

## Resumen en una línea

Ningún medio puede transportar 1.600 °C. Por eso cada instalación recibe su propio espejo. El calor se usa en cascada dentro de cada proceso y el excedente se radia a la mayor temperatura alcanzable. Solo el residuo por debajo de 100 °C llega al hábitat. Los paneles radiadores son la misma chapa Fe-Ni que los marcos de espejo — basta con omitir el recubrimiento para tener un radiador.
