---
title: "Por que metal fundido, no baterias"
date: 2026-02-25T12:00:02+09:00
lastmod: 2026-02-25T12:00:02+09:00
tags: ["metal-fundido-termico", "ESS", "levitacion-electromagnetica", "almacenamiento-termico", "autorreplicacion"]
image: "/images/molten-metal-thermal-ess.webp"
summary: "Un modulo Dyson es una central solar termica — almacenar calor directamente como Fe-Ni fundido en gravedad cero. ~145 Wh/kg con calor latente, ciclos infinitos, todo de mineral de asteroide."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Masa de Fe-Ni fundido en levitacion electromagnetica en vacio de gravedad cero — mantiene su forma esferica por tension superficial. Image: Gemini"
---

## Lo que faltaba en el articulo anterior

En [el articulo anterior](/es/why/why-iron-nickel-battery/) mostramos por que las baterias de hierro-niquel superan a las de litio-ion. No hay litio en los asteroides, no se puede extinguir un incendio en el vacio, el hierro-niquel dura 30~50 anos y la sobrecarga produce hidrogeno.

Todo correcto. **Pero faltaba algo.**

Un modulo Dyson es una central solar termica. Los espejos concentran la luz y el calor mueve las turbinas. Cuando se necesita almacenar energia para el eclipse, el diseno actual funciona asi:

```
Calor solar (1,600°C) → Turbina → Electricidad (370 MW)
                              → Excedente (~50 MW)
                                   → Bateria (energia quimica)    ← 2 conversiones
                                   → Durante eclipse → Electricidad ← 3 conversiones
```

Calor → electricidad → quimica → electricidad. **3 conversiones.** Perdida del 20~30% en cada paso.

¿Y si almacenamos el calor directamente?

```
Calor solar (1,600°C) → Parte se almacena directamente en el deposito termico ← 0 conversiones
                     → Durante eclipse → Deposito → Turbina → Electricidad    ← 1 conversion
```

**1 conversion.** La diferencia de eficiencia es aplastante.

Convertir el excedente de una central solar termica en electricidad, luego en quimica y de vuelta a electricidad es como convertir agua en vapor, descomponerla en hidrogeno y oxigeno, y luego volver a sintetizarla en agua. **Se puede hacer, pero ¿por que?**

El almacenamiento termico es la respuesta. Entonces, ¿por que no se hace en la Tierra?

---

## Por que no funciona en la Tierra, por que si funciona en el espacio

Almacenar calor en metal fundido en la Tierra es un tema de investigacion academica, no una realidad industrial. Hay razones:

| Problema | Tierra | Espacio (gravedad cero, vacio) |
|----------|--------|-------------------------------|
| Contenedor | Debe soportar miles de toneladas de material fundido → enorme y caro | **Sin peso propio** — paredes delgadas o totalmente sin contacto |
| Aislamiento | Hay que bloquear conveccion + conduccion + radiacion | **Solo bloquear radiacion** — decenas de capas de MLI bastan |
| Perdida termica | Alta — la conveccion del aire es la causa principal | **Extremadamente baja** — conveccion cero en el vacio |
| Corrosion | El material fundido a 1,500°C ataca las paredes | **Levitacion electromagnetica sin contacto** → corrosion cero |
| Seguridad | Fuga = accidente grave | Sin fuego en el vacio, sin medio de propagacion |

**Las debilidades terrestres desaparecen o se invierten en el espacio.** Exactamente el mismo patron repetido en articulos anteriores — [turbinas vs PV](/es/why/why-turbines/), hierro-niquel vs litio-ion.

---

## Almacenamiento termico por levitacion electromagnetica

El Fe-Ni fundido es conductor electrico incluso a 1,500°C (pierde su magnetismo por encima del punto de Curie del niquel, pero conserva la conductividad). Al aplicar un campo electromagnetico alterno se inducen corrientes parasitas (eddy currents), y la fuerza de repulsion entre estas corrientes y el campo permite la **levitacion sin contacto**.

Es una tecnica que ya se usa en laboratorios terrestres. Se llama fusion por [EML (Electromagnetic Levitation)](https://en.wikipedia.org/wiki/Electromagnetic_levitation). Se hacen flotar y fundir muestras de metal de unos gramos a unos kilogramos. La unica razon por la que no se puede escalar mas en la Tierra es la **gravedad**. Vencer la gravedad requiere campos magneticos fuertes, y los campos fuertes consumen energia. Unos kilogramos es el limite.

¿En gravedad cero? **No hay gravedad que vencer.** Solo se necesita el campo magnetico minimo para estabilizar la posicion. Toneladas, cientos de toneladas, decenas de miles de toneladas.

```
[Seccion del deposito termico]

        +--- Pared reflectante MLI (aislamiento multicapa) ---+
        |                                                      |
        |    +-- Bobina electromagnetica (refrigerada) --+     |
        |    |                                           |     |
        |    |   @@@@@@@@@@@@@@@@                        |     |
        |    |   @ Masa de Fe-Ni fundido @               |     |
        |    |   @ (1,200~1,500°C)       @               |     |
        |    |   @@@@@@@@@@@@@@@@                        |     |
        |    |                                           |     |
        |    +-------------------------------------------+     |
        |                                                      |
        +------------------------------------------------------+
```

En gravedad cero, el metal fundido adopta **naturalmente una forma esferica** por tension superficial. La esfera tiene la minima relacion superficie/volumen — minima perdida termica por radiacion. La pared reflectante MLI atrapa el calor radiante, el campo electromagnetico mantiene la posicion y no hay contacto con las paredes, asi que la corrosion es cero.

**Fundir el Fe-Ni extraido del asteroide y dejarlo flotar: eso es un deposito termico.**

---

## Carga y descarga

```
[Carga — operacion normal]
Concentracion solar → Apertura del obturador radiante → Calentamiento de la masa metalica → 1,200°C → 1,500°C

[Descarga — durante eclipse]
Apertura del obturador radiante → El calor radiante de la masa metalica calienta el intercambiador → Fluido de trabajo → Turbina
1,500°C → 1,200°C (aprovechando ΔT=300°C)
```

Carga: basta con dirigir parte del calor solar recogido por los espejos hacia el deposito termico. Se abre el obturador y la luz calienta la masa metalica.

Descarga: cuando llega el eclipse se abre el obturador y el intercambiador de calor recibe la radiacion de la masa metalica. El intercambiador calienta el fluido de trabajo y mueve la turbina. Se usa la misma turbina — en operacion normal los espejos son la fuente de calor, durante el eclipse lo es el deposito termico. **Para la turbina, solo cambia la fuente de calor; el resto es identico.**

El medio de intercambio termico es la radiacion. No se puede insertar una tuberia en una masa fundida sin contacto, asi que la transferencia de calor por obturador radiante es el mecanismo basico. La energia radiante del metal fundido a 1,500°C es proporcional a T⁴ segun la ley de Stefan-Boltzmann — suficientemente potente.

---

## Densidad energetica: calor especifico + calor latente

Calor especifico de la aleacion Fe-Ni: ~0.5 kJ/(kg·K) = ~0.14 Wh/(kg·K). Si calculamos solo el **calor sensible (sensible heat)** proporcional al cambio de temperatura (ΔT):

| Rango de temperatura (ΔT) | Calor sensible | Nota |
|----------------------------|----------------|------|
| 300°C (1,200→1,500°C) | ~42 Wh/kg | Conservador |
| 500°C (1,000→1,500°C) | ~70 Wh/kg | Intermedio |
| 1,000°C (500→1,500°C) | ~140 Wh/kg | Agresivo |

Pero no termina ahi.

### Bonificacion por calor latente

El punto de fusion de la aleacion Fe-Ni es ~1,430~1,450°C. El rango operativo 1,000~1,500°C **atraviesa ese punto de fusion.** Al cargar, el metal se funde; al descargar, se solidifica — cambio de fase (phase change).

Cuando un material se funde, su temperatura no sube pero absorbe una enorme cantidad de calor. Ese es el **calor latente de fusion (latent heat of fusion).**

```
Calor latente de fusion del hierro (Fe): ~270 kJ/kg ≈ 75 Wh/kg
Aleacion Fe-Ni: rango similar
```

Sumando calor sensible y calor latente:

| Rango de temperatura | Sensible | Latente | **Total** |
|----------------------|----------|---------|-----------|
| 300°C (1,200→1,500°C) | ~42 | ~75 | **~117 Wh/kg** |
| 500°C (1,000→1,500°C) | ~70 | ~75 | **~145 Wh/kg** |
| 1,000°C (500→1,500°C) | ~140 | ~75 | **~215 Wh/kg** |

**Solo el calor latente duplica la densidad energetica.** Un trozo de hierro fundiendose y solidificandose ya se solapa con el extremo inferior de las baterias de litio-ion (150~270 Wh/kg).

### Comparacion ESS (incluyendo calor latente)

| Metodo | Densidad energetica | Vida ciclica | Suministro de materiales |
|--------|---------------------|--------------|--------------------------|
| Litio-ion | 150~270 Wh/kg | 3,000~10,000 ciclos | Imposible (sin Li en asteroides) |
| Bateria hierro-niquel | 30~50 Wh/kg | Practicamente infinita | Asteroide Fe-Ni |
| **Almacenamiento termico Fe-Ni fundido** | **117~215 Wh/kg** | **Practicamente infinita** | **Asteroide Fe-Ni** |

Densidad energetica equivalente al litio-ion, vida ciclica infinita, y los materiales se encuentran por todas partes en los asteroides. Ademas, la conversion calor → electricidad es de solo 1 paso, por lo que la eficiencia del sistema es aplastante.

Por que la vida ciclica es infinita: se calienta y se enfria un trozo de metal. Sin reaccion quimica. Sin electrodos. Sin electrolito. No hay nada que se degrade.

---

## Escala: por que no una esfera gigante sino 60 unidades pequenas

Eclipse maximo de 12 horas, potencia de turbina 370 MW. No es necesario cubrir todo con almacenamiento termico — las celdas de combustible H₂ y las baterias comparten la carga.

### Calculo hibrido

```
De las 12 horas de eclipse:
  Deposito termico: 6 horas
  Celda de combustible H₂: 4 horas (acumulacion anual del batolizador)
  Bateria hierro-niquel: 2 horas (seguimiento de carga instantanea + respaldo)
```

Deposito termico para 6 horas (incluyendo calor latente):

```
370 MW ÷ 0.30 (eficiencia de turbina) = ~1,233 MW(th) × 6h = ~7,400 MWh(th)

Base ΔT=500°C + calor latente (145 Wh/kg):
  Masa necesaria = 7,400,000 kWh ÷ 0.145 kWh/kg = ~51,000 toneladas

(Sin calor latente: 105,000 toneladas → la bonificacion por calor latente reduce la masa a la mitad)
```

Poner 51,000 toneladas en una sola esfera da un radio de ~12 m. Intuitivamente simple. **Pero no funciona.** Hay tres razones de ingenieria.

### Razon 1: superficie insuficiente para la descarga

Durante el eclipse, el deposito termico transfiere calor al intercambiador **solo por radiacion**. La potencia radiante es proporcional a la superficie (P = ε σ A T⁴).

La esfera es la forma con minima relacion superficie/volumen. Optima para **conservar** calor, pero un cuello de botella para **liberarlo** rapidamente.

```
Potencia termica necesaria: ~1,233 MW(th)

Radiacion a 1,500°C (1,773K) (ε=0.5):
  P/A = ε × σ × T⁴ = 0.5 × 5.67e-8 × 1,773⁴ ≈ 280 kW/m²

Superficie necesaria: 1,233,000 kW ÷ 280 kW/m² ≈ 4,400 m²

Superficie de una esfera de radio 12 m: 4π(12)² ≈ 1,810 m² → Insuficiente (41% de lo necesario)
```

**Una sola esfera no puede fisicamente liberar el calor necesario.** La superficie es menos de la mitad.

Dividir en ~58 unidades de radio 3 m:

```
Superficie por unidad: 4π(3)² ≈ 113 m²
Superficie total de 58 unidades: 113 × 58 ≈ 6,560 m² → 149% de lo necesario (con margen)
Masa por unidad: (4/3)π(3)³ × 7,800 ≈ 880 toneladas
```

**Al almacenar, cada unidad mantiene su forma esferica para minimizar perdidas; al descargar, la superficie total de multiples unidades proporciona suficiente potencia termica.** Se resuelve el defecto de la esfera con el numero de unidades.

### Razon 2: chapoteo (sloshing) — una bola de demolicion de 100,000 toneladas de lava

Cuando 51,000 toneladas de metal liquido flotan como una sola esfera, si el modulo rota o vibra aunque sea ligeramente para el control de actitud, se generan **olas enormes (sloshing)** en el interior. Sumada la inestabilidad magnetohidrodinamica (MHD), existe el riesgo de que esta masa de lava oscile hasta romper el confinamiento electromagnetico.

¿Con unidades de radio 3 m y 880 toneladas? La energia de flujo es proporcional al cubo del tamano de la unidad, por lo que **la energia de sloshing de cada unidad es menos de 1/10,000 respecto a la esfera unica**. El riesgo de escape del confinamiento se elimina virtualmente.

### Razon 3: expansion volumetrica durante el cambio de fase

Al alternar entre 1,200°C (solido) y 1,500°C (liquido), el Fe-Ni se expande y contrae repetidamente. Si una esfera de radio 12 m se enfria desde la superficie, se forma una costra solida, y al contraerse el liquido interior existe el riesgo de que **la costra se fracture y los fragmentos salgan disparados al vacio**. Las unidades pequenas permiten gestionar uniformemente el gradiente de temperatura interior-exterior, eliminando este problema.

### Conclusion del diseno

```
Especificaciones de la unidad termica:
  Forma: esferica (formacion natural por tension superficial)
  Radio: ~3 m
  Masa: ~880 toneladas/unidad
  Numero de unidades: ~58 (por modulo)
  Masa total: ~51,000 toneladas
  Disposicion: distribuida en la estructura detras de los espejos (tambien como contrapeso)

Rendimiento de descarga:
  Superficie total: ~6,560 m² (149% de los 4,400 m² necesarios)
  Margen de 1,233 MW(th) de potencia asegurado
```

Las 51,000 toneladas no se obtienen por separado. El Fe-Ni refinado del asteroide se **mantiene fundido sin dejar que solidifique** y ya es una unidad termica. Distribuido en la estructura del modulo, **tambien sirve como contrapeso**.

---

## ESS de 3 niveles: separacion de roles

Las baterias ya no necesitan asumir el ESS masivo. Se asigna la tecnologia optima a cada nivel:

```
Nivel 1 — Masivo (escala de horas)
  └→ Deposito termico de metal fundido
       Carga: calor solar directo
       Descarga: deposito termico → turbina → electricidad
       Rol: respuesta al eclipse, minima perdida de conversion

Nivel 2 — Buffer (escala de segundos~minutos)
  └→ Bateria hierro-niquel
       Carga: excedente electrico
       Descarga: electroquimica (respuesta en ms)
       Rol: seguimiento de carga instantanea, energia de arranque

Nivel 3 — Emergencia + produccion quimica
  └→ H₂/O₂ (producto del batolizador)
       Celda de combustible para generacion de emergencia
       Propelente · agente reductor · oxigeno respirable
       Respaldo secundario en caso de eclipse prolongado
```

### Lo que aporta esta estructura

**El banco de baterias se reduce drasticamente.** En el diseno anterior, cubrir 12 horas de eclipse solo con baterias requeria 111,000 m³. Con el deposito termico asumiendo la carga masiva, las baterias solo cubren 2 horas — reducidas a unos miles de m³.

**El rol del batolizador queda claro.** El articulo anterior describia el batolizador (electrolisis del agua por sobrecarga) como una funcion que combina ESS y produccion quimica. Con el deposito termico asumiendo el ESS masivo, el batolizador se posiciona como **planta quimica** — la produccion de propelente de hidrogeno, oxigeno y agentes reductores es su funcion principal; la generacion de emergencia es secundaria.

**Los materiales son los mismos.** Deposito termico = Fe-Ni fundido. Bateria = electrodos de Fe-Ni. Batolizador = la misma bateria con sobrecarga. Los 3 niveles provienen del Fe-Ni de asteroides. No se anade ninguna materia prima nueva al bucle de autorreplicacion.

---

## Relacion con el articulo anterior (bateria hierro-niquel)

Los argumentos centrales del articulo anterior **siguen siendo todos validos:**

- No hay litio en los asteroides → sin cambios
- Vida util de 30~50 anos de la bateria hierro-niquel → sin cambios
- Riesgo de incendio en el vacio → sin cambios
- Produccion de H₂/O₂ del batolizador → sin cambios
- Fabricacion local posible → sin cambios

**Lo que se complementa:** el articulo anterior podia leerse como si la bateria hierro-niquel asumiera sola todo el ESS masivo (12 horas de eclipse). En realidad, para el almacenamiento masivo de energia, el almacenamiento termico es abrumadoramente superior, y la bateria brilla en su propio dominio: la respuesta instantanea.

**Cada uno hace lo que mejor sabe.** El deposito termico para almacenamiento de horas. La bateria para respuesta electrica en milisegundos. La celda de combustible para emergencias y produccion quimica. No es necesario que uno solo haga todo.

---

## Resumen en una linea

Un modulo Dyson es una central solar termica, pero convertir calor en electricidad, luego en quimica y de vuelta es una triple perdida de conversion. Fundir Fe-Ni de asteroides y dejarlo flotar en gravedad cero da un deposito termico con 0 conversiones para cargar y 1 para descargar. Sumando el calor latente del cambio de fase, la densidad energetica es ~145 Wh/kg — equivalente al litio-ion. 58 unidades de radio 3 m en configuracion distribuida resuelven el cuello de botella de superficie en la descarga, el sloshing y la expansion por cambio de fase. Todo con el mismo Fe-Ni de asteroides.

![Masa de Fe-Ni fundido en levitacion electromagnetica en vacio de gravedad cero. Image: Gemini](/images/molten-metal-thermal-ess.webp)
