---
title: "Por que 28nm"
date: 2026-02-25T12:00:03+09:00
lastmod: 2026-02-25T12:00:03+09:00
tags: ["28nm", "semiconductor", "TPU", "autorreplicacion", "litografia-ArF"]
image: "/images/why-28nm.webp"
summary: "El proceso de vanguardia de 3nm no se puede fabricar sin el EUV monopolizado por ASML — imposible en el espacio. 28nm es posible solo con ArF, y el Google TPU v1 lo demostro con 92 TOPS medidos. El silicio sale de la escoria de fundicion y el espacio mismo es una sala limpia."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Foto del die de un chip NAND de 4 entradas TTL — 7 transistores, ancho minimo de linea 20μm (1968). Photo: Dgarte / Wikimedia Commons / CC BY-SA 3.0"
---

## "¿Si es autorreplicante, de donde salen los chips?"

Los articulos anteriores mostraron que espejos, estructuras, [turbinas](/es/why/why-turbines/), [baterias](/es/why/why-iron-nickel-battery/) y [gestion termica](/es/why/heat-flow/) — todo se puede fabricar con Fe-Ni de asteroides. El bucle de autorreplicacion casi se cerro.

Casi.

**Los chips de IA aun se importan de la Tierra.** La operacion autonoma del modulo Dyson — control de robots mineros, ajuste orbital, gestion de procesos de fundicion, soporte vital del habitat — todo lo hace la IA. Sin chips, el modulo esta ciego.

"No hay litio en los asteroides" fue el fin del juego para las baterias de litio-ion. Del mismo modo, **"no se puede fabricar EUV en el espacio" es el fin del juego para el proceso de vanguardia de 3nm.**

Entonces, ¿con que proceso se fabrican los chips?

---

## Por que no el proceso de vanguardia de 3nm

El nucleo del proceso semiconductor es la litografia — grabar patrones de circuitos en obleas con luz.

| Elemento | 28nm | 3~5nm (vanguardia) |
|----------|------|-------------------|
| Litografia | **ArF inmersion** (Nikon, Canon, ASML) | **EUV** (monopolio ASML, miles de millones por unidad) |
| Disponibilidad de equipos | Mercado maduro, amplio usado | Extremadamente limitado, sujeto a control de exportacion |
| Complejidad de diseno | Patron unico | Patron multiple (extremadamente complejo) |
| Coste de la fab | ~$3~5B | ~$20~30B |
| Rendimiento | Alto (10+ anos de validacion) | Bajo inicialmente |

El escaner EUV (ultravioleta extremo) lo fabrica **una sola empresa en todo el planeta: ASML.** Una unica fabrica en Eindhoven, Paises Bajos. Sujeto a control de exportacion. El equipo que la alianza EE.UU.-Japon-Paises Bajos prohibe vender a China. ¿Reproducirlo en el espacio? Imposible.

El proceso mas potente que no requiere EUV. Eso es **28nm**.

"¿7nm no es posible con ArF?" — Si. Mediante una tecnica llamada patron multiple se dispara la luz ArF varias veces para crear patrones mas finos. Pero la complejidad de diseno explota y el rendimiento cae en picado. Sin la mano de obra e infraestructura para gestionar el rendimiento en el espacio, no es realista.

"¿65nm no seria mas facil de fabricar?" — Correcto. Pero el rendimiento por chip es demasiado bajo. Para la misma tarea se necesitan muchos mas chips, y mas chips significan cableado, encapsulado y refrigeracion proporcionalmente mas complejos. Fabricar mas facil, pero el sistema completo se complica.

**28nm = la integracion optima alcanzable sin EUV.**

---

## Esto no es teoria — Google TPU v1

"¿Se puede realmente ejecutar IA con 28nm?"

Google dio la respuesta en 2015. **[TPU v1](https://arxiv.org/abs/1704.04760).** Fabricado en proceso de 28nm, mas de 100,000 unidades desplegadas en sus propios centros de datos. Un acelerador de IA probado en combate.

| Elemento | Google TPU v1 (medido) |
|----------|----------------------|
| Proceso | 28nm |
| Arquitectura | Arreglo sistolico 256 × 256 |
| Rendimiento | 92 TOPS (INT8) ≈ 23 TFLOPS (FP16) |
| Consumo | ~75W en operacion real |
| Utilizacion del silicio | **90%+** |

La clave es la arquitectura de arreglo sistolico (systolic array). Una GPU es un chip de proposito general — el 70% del silicio se destina a logica de control, cache y planificador. Solo el 30% hace realmente multiplicacion de matrices. El arreglo sistolico esta disenado exclusivamente para multiplicacion de matrices, por lo que **mas del 90% del silicio se usa en computacion real.**

Si solo vas a ejecutar IA, toda la sobrecarga de proposito general de la GPU es desperdicio. El TPU es el chip que elimina ese desperdicio.

Y esto no es una propuesta teorica. **Es el chip que ejecuto AlphaGo.** Hardware en servicio real durante anos en los centros de datos de Google.

---

## "¿4.6 veces mas consumo de energia?"

El chip de IA de mayor rendimiento actual, NVIDIA H100. Proceso de 4nm, 990 TFLOPS, consumo de 700W.

Un TPU v1 ofrece 23 TFLOPS. ¿Cuantos se necesitan para igualar un H100?

```
990 TFLOPS ÷ 23 TFLOPS = 43 unidades

43 unidades × 75W = 3,225W ≈ 3.2 kW
```

| | TPU v1 × 43 | H100 × 1 |
|---|---|---|
| FP16 total | ~990 TFLOPS | ~990 TFLOPS |
| Potencia total | **3.2 kW** | 700W |
| Ratio de potencia | **4.6x** | Referencia |

4.6 veces. En la Tierra es una diferencia mortal. En un mundo donde la electricidad es el 30~40% del coste operativo de un centro de datos, 4.6 veces mas consumo equivale a la quiebra.

**¿En el espacio?**

Un modulo Dyson = 370 MW. 3.2 kW es el **0.00086%** de 370 MW. En area de espejo, 2.4 m² — un pixel del espejo Dyson de 1 km².

En la Tierra, la electricidad es dinero. **En el espacio, la electricidad es area de espejo.** Los espejos se hacen aplanando Fe-Ni de asteroides.

La misma estructura logica de cuando [la turbina supero al panel solar](/es/why/why-turbines/) en articulos anteriores. Una eleccion inferior segun los estandares terrestres se invierte como unica opcion segun los estandares espaciales. **Si cambian los estandares, cambian las respuestas.**

---

## 1 modulo = centro de datos de 30,000 H100

Asignando el 30% de los 370 MW del modulo a computacion IA:

```
111 MW ÷ 75W/chip = ~1,480,000 unidades (1.48 millones de TPU v1)

1.48 millones ÷ 43 unidades/H100 equivalente = ~34,000 H100

Sobrecarga de interconexion y refrigeracion 20~30% → conservadoramente H100 ~25,000~30,000 equivalentes
```

Equivalente al cluster de IA mas grande del planeta en 2026. **Con un solo modulo.**

¿Cuando los modulos se autorrepliquen a 270,000? Equivalente a miles de millones de H100. Una escala que supera la capacidad computacional actual de toda la humanidad, surgida de un solo asteroide.

---

## Materia prima: chips de IA a partir de escoria

Aqui esta la pieza maestra de este diseno. No se necesita una mina de semiconductores dedicada.

Al refinar el mineral de asteroide, el Fe-Ni (90%+) es el producto principal y **el resto es escoria (slag)**. El componente principal de la escoria es SiO₂ — silicato. No se desecha.

```
Mineral de asteroide → Fundicion al vacio
  +→ Fe-Ni (90%+) → Espejos, estructuras, baterias, turbinas
  +→ Escoria (SiO₂ como componente principal)
       +→ La mayor parte → Material de blindaje contra radiacion
       +→ Una parte → Reduccion con carbono (SiO₂ + 2C → Si + 2CO)
            → Silicio metalico
            → Refinado zonal (calor solar + vacio + microgravedad)
            → Lingote monocristalino de grado semiconductor (pureza 9N+)
            → Oblea de 300mm
            → TPU de 28nm
```

**De los residuos de fundicion salen chips de IA.**

El [refinado zonal (zone refining)](https://en.wikipedia.org/wiki/Zone_melting) es mas ventajoso en el espacio. Es un metodo de purificacion que hace pasar una zona fundida estrecha a lo largo del lingote de silicio para expulsar impurezas:

- **Energia:** Calentamiento directo con calor solar. Coste cero
- **Vacio:** El espacio ya es vacio. Las impurezas se evaporan automaticamente
- **Microgravedad:** La zona fundida no se desploma. El metodo FZ (Float Zone) terrestre tiene un limite de 200mm de diametro — mas alla, el silicio fundido colapsa por gravedad. **En gravedad cero, 300mm o mas es posible**
- **Repeticion:** Solo hay que ajustar el angulo del espejo para repetir pasadas de refinado infinitamente. Coste adicional cero

En la Tierra, el refinado zonal es un proceso premium costoso y de pequena escala. En el espacio se convierte en el **proceso estandar**.

---

## La fab: el espacio es la sala limpia

Uno de los mayores costes de una fab terrestre de 28nm: sala limpia de Clase 1~10. Menos de 10 particulas de 0.5μm o mas por pie cubico de aire. Mantener esto requiere enormes sistemas de filtros HEPA, unidades de tratamiento de aire y gestion de presion positiva. Una parte considerable del coste de construccion de la fab se destina aqui.

En el espacio **no hay aire.** La fuente de contaminacion por particulas simplemente no existe. El vacio es la **sala limpia perfecta**.

Aptitud espacial de las 7 etapas principales del proceso:

| Proceso | Aptitud espacial | Razon |
|---------|-----------------|-------|
| Crecimiento del lingote | **Ventaja espacial** | Metodo FZ en microgravedad, lingotes de gran diametro |
| Corte de obleas | Posible | Proceso mecanico, independiente del entorno |
| Oxidacion/deposicion (CVD, PVD) | **Ventaja del vacio** | En la Tierra hay que hacer vacio en la camara — el espacio ya es vacio |
| Fotolitografia | Cuello de botella | Escaner ArF y fotoresistencia dependen de la Tierra |
| Grabado | **Ventaja del vacio** | Simplificacion de la camara de grabado por plasma |
| Implantacion ionica | **Ventaja del vacio** | Menor dispersion del haz, sin necesidad de bombas de alto vacio |
| Cableado/encapsulado | Posible | Cu se obtiene de asteroides/Luna |

**6 de 7 etapas son favorables o equivalentes en el espacio.** El unico cuello de botella es la fotolitografia — el escaner ArF en si no se puede fabricar en el espacio. Pero una vez llevado, dura decadas.

---

## Gestion termica de la fab: "¿Semiconductores en el espacio?"

"¿La cara al Sol a cientos de grados, la opuesta a -100°C, y se puede controlar a ±0.01°C?"

Si. Y **es mas facil que en la Tierra.**

### El nucleo del problema

El sistema de lentes de proyeccion del escaner de litografia ArF es extremadamente sensible a la expansion termica. Una fluctuacion de 0.01°C cambia la curvatura de las lentes, genera error de overlay y reduce el rendimiento. La tolerancia de overlay para el proceso de 28nm es de unos pocos nm.

Como se resuelve en las fabs terrestres:
- Toda la sala limpia se mantiene a 23.00 ± 0.1°C
- Interior del escaner con circuito de refrigeracion independiente a ±0.01°C
- **Problema:** Las perturbaciones externas son incesantes — variaciones de temperatura exterior, estaciones, dia/noche, clima, terremotos, vibraciones del trafico, calor de equipos adyacentes

### Diseno termico de la fab espacial

```
[Seccion del modulo fab]

Exterior: Vacio espacial (conduccion cero, conveccion cero)
  |
  +- Pared reflectante MLI (aislamiento multicapa, decenas de capas)
  |    → Bloqueo del 99.5%+ de la radiacion solar
  |    → Tambien bloquea la perdida por radiacion interior→exterior
  |
  +- Pared exterior estructural (Fe-Ni)
  |
  +- Capa de circulacion activa de liquido
  |    → Microcirculacion de agua ultrapura (UPW)
  |    → Bomba + calentador + valvula de disipacion para control activo
  |    → Pared interior uniforme a 23.00 ± 0.05°C
  |
  +- Interior de la fab (atmosfera de 1 atm N₂)
       → Calor de los equipos → absorbido por refrigerante en circulacion
       → Interior del escaner: bucle de refrigeracion dedicado ±0.01°C
```

### Por que es mas facil que en la Tierra

| Elemento | Fab terrestre | Modulo fab espacial |
|----------|--------------|---------------------|
| Perturbacion termica externa | Incesante (clima, estaciones, dia/noche) | **Ninguna** — aislamiento por vacio |
| Vibracion externa | Trafico, terremotos, fabricas adyacentes | **Ninguna** — espacio sin vibraciones |
| Coste de aislamiento | HVAC consume 30~40% de la energia de la fab | **El vacio es aislante gratuito** |
| Predictibilidad de fuentes de calor | Perturbaciones externas + equipos internos | **Solo equipos internos** (completamente predecible) |
| Disipacion de calor | Torres de refrigeracion, chillers (alto consumo de agua y electricidad) | **Paneles radiantes** (radiacion al vacio) |

La paradoja central: el entorno termico extremo del espacio (cientos de grados vs -100°C) **no llega al interior de la fab.** El vacio es el mejor aislante, y una vez que el MLI bloquea la radiacion, el interior de la fab queda completamente aislado termicamente del exterior. A partir de ahi solo hay que gestionar el calor generado por los equipos internos, y eso es mas facil que en la Tierra — porque las perturbaciones externas son cero.

Las fabs terrestres gastan el 30~40% de su energia total en HVAC porque **luchan constantemente contra el exterior**. La fab espacial no tiene esa batalla.

### UPW — viene del batolizador

El agua ultrapura (UPW) utilizada en la circulacion de temperatura constante de la fab proviene del producto del batolizador, no de una planta de purificacion dedicada:

```
Batolizador: H₂O → H₂ + O₂ (electrolisis)
Reaccion inversa: H₂ + O₂ → H₂O (celda de combustible)

Subproducto H₂O → Purificacion → UPW
  +→ Refrigerante de circulacion de temperatura de la fab
  +→ Limpieza de obleas
  +→ Liquido para litografia de inmersion
```

### Seccion de gravedad artificial

La litografia de inmersion requiere una pelicula de agua ultrapura sobre la oblea — se necesita gravedad. El modulo fab se divide en dos secciones:

```
Seccion de vacio (0G):
  +→ Deposicion CVD/PVD (requiere vacio)
  +→ Implantacion ionica (requiere vacio)
  +→ Grabado por plasma (requiere vacio)

Seccion de gravedad artificial (~1G por rotacion):
  +→ Litografia de inmersion ArF (gestion de liquidos requiere gravedad)
  +→ Limpieza humeda (limpieza UPW requiere gravedad)
  +→ Manipulacion de obleas (transporte robotizado)
```

Las obleas se mueven entre la seccion de vacio y la de gravedad artificial a traves de esclusas. La seccion rotativa no tiene fuentes externas de vibracion, por lo que **solo hay que gestionar la uniformidad de la propia rotacion** — mucho mas simple que defenderse contra terremotos y vibraciones del trafico en la Tierra.

---

## Dependencia externa: 5%

| Categoria | Suministro | Nota |
|-----------|-----------|------|
| Silicio | Local (escoria → Si) | |
| Energia | Local (calor solar) | |
| Sala limpia | Local (vacio espacial) | |
| Agua ultrapura | Local (batolizador H₂O → purificacion) | |
| Cableado de cobre | Local (asteroides/Luna) | |
| Escaner ArF | **Tierra 1 vez** | Vida util de decadas |
| Fotoresistencia | **Tierra 1 vez/ano** | Cientos de kg/ano |
| Gas de grabado | **Tierra 1 vez/ano** | Reciclable, pequenas cantidades |
| Elementos dopantes (B, As) | **Tierra 1 vez/ano** | Decenas de kg |

El 95% se obtiene en el espacio. El 5% restante — escaner ArF (unica vez) + consumibles (unas toneladas/ano) — cabe en un lanzamiento de Starship para decadas.

"¿La fotoresistencia no es quimica organica de precision?" — Correcto. Esto es dificil de fabricar localmente. Pero el consumo anual es de unos cientos de kg. Un lanzamiento de Starship puede llevar suministro para decadas. No es autosuficiencia total, sino **autosuficiencia de facto**.

---

## El bucle de autorreplicacion se cierra

```
Antes:
  Mineral de asteroide → Fundicion → Fe-Ni → Espejos · Estructuras · Baterias → Autorreplicacion
                                                                                ↑
                                                                    Chips de IA importados de la Tierra

Ahora:
  Mineral de asteroide → Fundicion → Fe-Ni → Espejos · Estructuras · Baterias · Turbinas
                                  → Escoria → Lingote Si → TPU 28nm → Control autonomo por IA
                                                                                ↓
                                                                    Bucle de autorreplicacion completamente cerrado
```

Los espejos fabrican espejos. Las baterias fabrican propelente. **La escoria fabrica chips de IA.** No hay nada que desechar.

---

## Resumen en una linea

El proceso de vanguardia de 3nm no se puede fabricar sin el EUV monopolizado por ASML — imposible en el espacio. 28nm es posible solo con ArF, y el Google TPU v1 lo demostro con 92 TOPS medidos. La desventaja de 4.6x en consumo equivale a 2.4 m² de espejo en un modulo de 370 MW. El silicio sale de la escoria, el espacio mismo es la sala limpia y el aislamiento por vacio hace que la gestion termica de ±0.01°C sea mas facil que en la Tierra. El ultimo eslabon del bucle de autorreplicacion.

![Foto del die de un chip NAND de 4 entradas TTL. Photo: Dgarte / Wikimedia Commons / CC BY-SA 3.0](/images/why-28nm.webp)
