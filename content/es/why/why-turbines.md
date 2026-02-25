---
title: "Por qué turbinas, no paneles solares"
date: 2026-02-24T12:00:07+09:00
lastmod: 2026-02-24T12:00:07+09:00
tags: ["solar-térmico", "turbina", "autorreplicación", "fotovoltaica"]
summary: "Los paneles solares y las turbinas convierten la luz solar en electricidad con una eficiencia del 30% en el espacio. Pero las turbinas aprovechan el 70% restante como calor, se fabrican con materiales de asteroides y se reparan in situ — la unica opcion para un enjambre de Dyson autorreplicante."
image: "/images/why-turbines.webp"
author: "PARK JUN WOO"
imageCaption: "Instalacion de alabes de rotor de turbina de vapor en una fabrica de Siemens. Foto: Siemens Pressebild / Wikimedia Commons / CC BY-SA 3.0"
authorLink: "https://parkjunwoo.com/1/about"
---

## "¿Por que turbinas otra vez?"

Cuando se piensa en la generacion de energia de un enjambre de Dyson, los paneles solares (PV) son la opcion obvia. Son el estandar de la energia espacial. La ISS usa PV. La mayoria de las sondas espaciales usan PV.

Sin embargo, este diseno utiliza turbinas. ¿Por que volver a la tecnologia del siglo XIX en el siglo XXI?

La respuesta es sencilla: **no puedes fabricar paneles solares con asteroides, pero si puedes fabricar turbinas.**

---

## La eficiencia es la misma — 30%

Aclaremos esto primero. "¿No es el PV mas eficiente?"

| | Panel solar (GaAs multiunion) | Turbina solar termica |
|---|---|---|
| Eficiencia de conversion | ~30% (grado espacial) | ~30% (lado caliente 1.500 K / lado frio 500 K) |
| Limite de Carnot | No aplica | 66,7% (realizado ~45%) |
| Produccion electrica | **Igual** | **Igual** |

Si se recogen 1.225 MW(termicos) con un espejo de 1 km², ya sea con PV o con turbina, **la produccion electrica es ~370 MW en ambos casos.**

Si la eficiencia es la misma, las diferencias estan en otra parte.

---

## Diferencia 1: El otro 70%

Tanto el PV como las turbinas no logran convertir el 70% de la energia entrante en electricidad. Pero el destino de ese 70% es muy diferente.

### PV: El 70% se disipa como calor residual de baja temperatura

```
Entrada solar 1.225 MW
  ├→ 30% → 370 MW (electricidad)
  └→ 70% → 855 MW → superficie del panel a 60–80°C calor residual
                     → sin uso. Radiado al espacio mediante disipadores.
```

Con calor a 60–80°C no se puede fundir metal, operar una fabrica ni calentar un habitat. **El 70% de la energia simplemente desaparece.**

### Turbina: El 70% se aprovecha en cascada de alta a baja temperatura

```
Entrada solar termica 1.225 MW
  ├→ 30% → 370 MW (electricidad)
  └→ 70% → 855 MW (calor) → aprovechamiento escalonado por temperatura:
       ├→ 800–1.000°C: ~400 MW → fundicion (fusion de Fe-Ni)
       ├→ 400–600°C:   ~250 MW → recubrimiento, tratamiento termico, conformado
       ├→ 100–200°C:   ~120 MW → calefaccion del habitat
       └→ 30–60°C:      ~85 MW → calor ambiental del centro de datos
```

**El mismo 70% pasa secuencialmente por la fundicion → fabrica → habitat → centro de datos, y todo se aprovecha.** El "calor residual" de la turbina no es residual — es la fuente de energia del siguiente proceso.

Aprovechamiento real de la energia entrante:
- PV: ~30% (solo electricidad)
- **Turbina: ~30% + cascada termica → efectivamente 85%+**

---

## Diferencia 2: Compatibilidad con el ciclo de autorreplicacion

Este es el factor decisivo.

### Fabricar PV en el espacio

La fabricacion de paneles solares (GaAs multiunion) requiere:
1. Materia prima de galio (Ga) + arsenico (As) — **no se encuentra en asteroides**
2. Crecimiento de monocristal (MOCVD, MBE) — **equipos de precision extrema**
3. Deposicion epitaxial multicapa — **requiere sala limpia**
4. Recubrimiento antirreflectante, cableado, ensamblaje de modulos — **linea de fabricacion dedicada**

Los asteroides no tienen ni Ga ni As. Aunque tuvieras el equipo, no hay materia prima. **El PV no puede entrar en el ciclo de autorreplicacion.** Debe reabastecerse continuamente desde la Tierra.

¿Y el PV de silicio (Si)? Este diseno ya incluye un proceso para producir lingotes de Si de grado semiconductor a partir de escoria de silicato (refinacion por zonas, para chips de IA). Asi que la materia prima de Si esta disponible. Sin embargo:
- Eficiencia del Si PV en el espacio ~20% — inferior al GaAs (30%) y por debajo de las turbinas (30%)
- La linea de fabricacion de celdas PV (difusion, recubrimiento antirreflectante, patron de electrodos) es **independiente de la fabrica de chips**
- La eficiencia se degrada por la radiacion espacial → ciclo de reemplazo mas corto
- La misma oblea de Si es **mucho mas valiosa como chip de IA**

Incluso con Si disponible, fabricar PV con el es un desperdicio. **Si tienes silicio, fabricas chips.**

### Fabricar turbinas en el espacio

| Componente | Material | Origen | Fabricacion |
|------------|----------|--------|-------------|
| Alabes y toberas de alta temperatura | Superaleacion de Ni | Asteroide Fe-Ni | Fundicion de precision |
| Compresor y eje de baja temperatura | Aleacion de Ti | Ilmenita lunar | Mecanizado |
| Carcasa | Fe-Ni | Asteroide | Chapa metalica y soldadura |

**Todo se puede construir con materiales que ya estan en el ciclo de autorreplicacion (Fe-Ni, Ti).** No se necesita materia prima adicional ni lineas de fabricacion adicionales. Las turbinas salen de la misma linea de produccion que fabrica los marcos de los espejos.

---

## Diferencia 3: Vida util y mantenimiento

### El problema de la radiacion del PV espacial

El PV espacial es danado por particulas de alta energia (protones, iones pesados) que alteran la red cristalina. La eficiencia se degrada ~1–3% por ano.

- Despues de 10 anos: la eficiencia cae al 70–80%
- Se necesita reemplazo → **no se puede fabricar, hay que reabastecer desde la Tierra**
- Si el reabastecimiento no esta disponible: aceptar la reduccion de produccion

### Desgaste de las turbinas

Las turbinas tampoco duran para siempre. La fluencia de los alabes a alta temperatura y el desgaste de los rodamientos son los principales mecanismos de degradacion.

Pero:
- Los alabes se pueden **refundir localmente con superaleacion de Ni**
- Rodamientos → **rodamientos magneticos sin contacto**: cero desgaste
- Diseno modular: solo se reemplazan los componentes degradados, no la unidad completa

**Las piezas de la turbina se pueden fabricar y reemplazar in situ. Las del PV no.** En un sistema autorreplicante, esta diferencia es decisiva.

---

## Limitaciones reales de las turbinas — y soluciones

Seamos honestos con las desventajas.

### Limitacion 1: Se necesita un fluido de trabajo

Las turbinas necesitan un fluido que se expanda al calentarse para hacer girar el rotor. ¿De donde se obtiene este fluido en el espacio?

| Candidato | Ventajas | Desventajas | Obtencion |
|-----------|----------|-------------|-----------|
| Helio (He) | Inerte, estable a alta temperatura | Dificil de reponer si hay fugas | Captura del desgasificado de asteroides |
| CO₂ supercritico | Alta densidad, turbina compacta | Requiere gestion de corrosion | Desgasificado de asteroides |
| Sodio/Potasio (metal liquido) | Ultraalta temperatura, excelente transferencia de calor | Reactivo (seguro en vacio) | Trazas de asteroides |

El sistema opera en ciclo cerrado, asi que no hay consumo de fluido. Solo hay que asegurar la carga inicial. El gas se puede capturar durante el desgasificado de la fundicion de asteroides, o se puede suministrar una pequena cantidad desde la Tierra inicialmente.

### Limitacion 2: Piezas moviles — riesgo de fallo en el espacio

La debilidad fundamental de las turbinas: componentes rotativos de alta velocidad. Incluso en la Tierra, el mantenimiento de turbinas es un trabajo exigente.

**Soluciones:**
- **Rodamientos magneticos** — soporte rotacional sin contacto. Cero desgaste. Ya comercializado en turbomaquinaria de alta velocidad en la Tierra
- **Cartuchos de alabes modulares** — reemplazo de conjuntos de alabes como unidad. Sin necesidad de servicio individual
- **Fabricacion local** — fundicion de piezas de repuesto bajo demanda. Sin esperar reabastecimiento desde la Tierra
- **Redundancia** — multiples turbinas por modulo. Produccion mantenida incluso durante el mantenimiento de una unidad

### Limitacion 3: Vibracion

La rotacion a alta velocidad genera vibracion. Esto es un problema si hay fabricas de semiconductores o equipos opticos de precision en el mismo modulo.

**Soluciones:**
- **Clusters especializados** — separar fisicamente los modulos de turbinas de los modulos de fabricacion (estructuras distintas)
- **Montajes con amortiguacion de vibraciones** — instalar las turbinas en juntas estructurales flexibles
- En la Tierra tampoco se pone una planta electrica y una fabrica de semiconductores en el mismo edificio

### Limitacion 4: Rechazo de calor

El calor del lado frio de la turbina debe radiarse al espacio. No hay atmosfera en el espacio, asi que la refrigeracion por conveccion es imposible — solo funciona la refrigeracion por radiacion.

**Este es un gran tema independiente. Se cubrira en detalle en el proximo articulo.**

---

## Resumen en una linea

Los paneles solares y las turbinas tienen la misma eficiencia electrica (30%). Pero el PV desperdicia el otro 70%, mientras que las turbinas lo aprovechan. El PV no se puede fabricar en el espacio; las turbinas si. Cuando el PV falla, hay que esperar a la Tierra; cuando un alabe de turbina se desgasta, se refunde in situ. En un sistema autorreplicante, la respuesta es clara.
