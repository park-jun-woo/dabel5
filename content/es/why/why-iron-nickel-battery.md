---
title: "Por que baterias de niquel-hierro y no de litio"
date: 2026-02-25T12:00:01+09:00
lastmod: 2026-02-25T12:00:01+09:00
tags: ["bateria-niquel-hierro", "bateria-edison", "battolyser", "ESS", "autorreplicacion"]
image: "/images/why-iron-nickel-battery.webp"
summary: "En los asteroides no hay litio, en el espacio no se puede reemplazar cada 10 anos, y en el vacio no se puede apagar un incendio. Las baterias de niquel-hierro se fabrican con subproductos de la fundicion de asteroides, duran 30-50 anos y, una vez cargadas, producen hidrogeno y oxigeno."
author: "Park Jun Woo"
authorLink: "https://parkjunwoo.com/1/about"
imageCaption: "Baterias de niquel-hierro desarrolladas por Edison en 1901. Thomas Edison National Historical Park. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0"
---

## "El almacenamiento de energia es obviamente litio-ion, no?"

El modulo Dyson concentra calor solar con espejos para mover turbinas. Seria ideal que el sol brillara 24 horas al dia, 365 dias al ano, pero la realidad es otra.

- **Eclipse:** La base en EML5 entra en la sombra de la Tierra o la Luna 2-3 veces al ano, durante un total de 3-12 horas
- **Fluctuacion de carga:** Las turbinas responden lentamente a cambios bruscos de carga. Sin ESS, la tension oscila ante cambios instantaneos de demanda
- **Parada de emergencia:** Durante el mantenimiento de espejos o averias de turbinas, los sistemas criticos — soporte vital, IA, comunicaciones — no pueden detenerse
- **Potencia de maniobra:** Se necesita alta potencia instantanea para maniobras de acoplamiento y evasion de remolcadores

Sin baterias, un modulo Dyson no funciona. Entonces, que tipo de bateria?

En la Tierra, la respuesta es obvia. Litio-ion. Densidad energetica, eficiencia de carga/descarga, ligereza — la mejor en todos los indicadores. Pero, por la misma razon que las turbinas superaron a los paneles solares en el articulo anterior, **en el espacio los criterios son diferentes.**

El litio-ion debe reemplazarse cada 10 anos, y la mina de litio mas cercana esta en la Tierra. En los asteroides, el hierro y el niquel se encuentran a cada paso.

---

## Criterios terrestres vs criterios espaciales

| Aspecto | Niquel-hierro (Edison) | Litio-ion | Que importa en el espacio |
|---------|----------------------|-----------|--------------------------|
| Densidad energetica volumetrica | 30~60 Wh/L | 250~700 Wh/L | A escala de 1 km², el volumen es irrelevante |
| Densidad energetica gravimetrica | 30~50 Wh/kg | 150~270 Wh/kg | Estructura fija sin transporte → irrelevante |
| Vida util | **30~50 anos** | 5~15 anos | El coste de reemplazo en el espacio es **astronomico** |
| Tolerancia a sobrecarga | **Extremadamente alta** | Baja (fuga termica/incendio) | En el vacio, incendio = perdida total del modulo |
| Tolerancia a sobredescarga | **Alta** | Dano irreversible | Posibilidad de descarga total durante eclipse |
| Abastecimiento local de materiales | **Posible** (Fe, Ni, KOH) | **Imposible** (Li, Co, electrolito organico) | La supervivencia del bucle de autorreplicacion |
| Electrolito | Solucion acuosa de hidroxido de potasio (base agua) | Solvente organico (inflamable) | Estabilidad a la radiacion, seguridad contra incendios |
| Autodescarga | Alta (~1%/dia) | Baja (~0.1%/dia) | Irrelevante en un entorno de carga continua |

**Lo que importa en la Tierra: ligero, compacto, alta densidad energetica.**
**Lo que importa en el espacio: que se pueda fabricar localmente, que no mate, que dure.**

Si cambian los criterios, cambia la respuesta.

---

## Materiales — en los asteroides no hay litio

Para fabricar una bateria de litio-ion se necesita:

| Material | Uso | Disponibilidad en asteroides |
|----------|-----|------------------------------|
| Litio (Li) | Material activo del catodo | **No existe** — elemento de nucleosintesis del Big Bang, cantidades infimas en asteroides rocosos |
| Cobalto (Co) | Estabilizador del catodo | Cantidades infimas — extraccion economicamente inviable |
| Grafito (C) | Anodo | Existe en asteroides carbonaceos, pero no es grafito cristalino |
| Electrolito organico | Conduccion ionica | **Requiere sintesis** — quimica organica compleja como carbonato de etileno |
| Separador (PE/PP) | Prevencion de cortocircuitos | **Requiere sintesis** — fabricacion precisa de polimeros |

No hay litio. Solo con eso, se acabo el juego. Si hay que recibir suministros continuos de la Tierra, **eso no es autorreplicacion sino dependencia logistica**.

"Y el sodio-ion?" El Na existe en los asteroides. Pero no tiene una vida util verificada de 30-50 anos, no tiene funcion de battolyser, y requiere electrolito organico. El problema de la radiacion cosmica degradando el electrolito organico es identico con el sodio-ion.

"Las baterias de estado solido estan por llegar, no?" Si no se pueden fabricar en un asteroide, por muy buenas que sean, no tienen sentido. La clave no es la densidad energetica sino la **capacidad de fabricacion local**.

Para fabricar una bateria de niquel-hierro se necesita:

| Material | Uso | Origen |
|----------|-----|--------|
| Hierro (Fe) | Anodo | Componente principal de 1986 DA — **se encuentra a cada paso** |
| Niquel (Ni) | Catodo | Componente principal de 1986 DA — **se encuentra a cada paso** |
| Hidroxido de potasio (KOH) | Electrolito | K presente en silicatos de asteroides, agua extraida de asteroides carbonaceos |
| Lamina de acero | Carcasa | Procesamiento de aleacion Fe-Ni |

**Todos los componentes de la bateria son subproductos del proceso de fundicion.** Se pueden fabricar baterias mientras se hacen marcos de espejos. Cero importacion de materias primas adicionales.

---

## Vida util — el coste de reemplazo lo decide todo

En la Tierra, la vida util de 10-15 anos del litio-ion es suficiente. El coste de reemplazo es solo el precio de la bateria.

En el espacio, el coste de reemplazo incluye:
1. Fabricar una nueva bateria (si es posible)
2. Transporte (si no es posible fabricarla, desde la Tierra — **miles de dolares por kg**)
3. Trabajo de reemplazo por EVA o robot
4. Tiempo de inactividad del sistema durante el reemplazo

**Vida util de la bateria de niquel-hierro: 30-50 anos.** Existen **casos de baterias de niquel-hierro fabricadas por Edison en 1901 que aun funcionan**. Solo hay que reponer el electrolito (solucion acuosa de KOH) cada 10-15 anos; los electrodos son practicamente permanentes.

La unica quimica de bateria que permite **cero reemplazos** durante toda la vida util de diseno del modulo.

---

## Seguridad — en el vacio, un incendio significa muerte

El electrolito organico de las baterias de litio-ion es inflamable. En caso de sobrecarga, dano fisico o cortocircuito interno:

```
Aumento de temperatura interna → contraccion del separador → expansion del cortocircuito → descomposicion del electrolito
→ emision de gas inflamable → ignicion → fuga termica en cascada a celdas adyacentes
```

En la Tierra: llegan los bomberos.
En el espacio: **en el vacio no hay bomberos.** Un incendio dentro de un modulo sellado = perdida de soporte vital + llenado de gas toxico + imposibilidad de rescate.

Incluso en la ISS, un incendio de litio-ion es uno de los escenarios mas temidos. Si se instala litio-ion en miles de modulos Dyson, **estadisticamente, un incendio es una certeza**.

Seguridad intrinseca del niquel-hierro:

- Electrolito: **solucion acuosa** de hidroxido de potasio — base agua. No arde
- En sobrecarga: el agua se electroliza produciendo H₂ + O₂ — no es fuga termica
- En sobredescarga: sin dano irreversible a los electrodos — se recupera con recarga
- En caso de dano fisico: fuga de KOH — corrosivo pero **sin explosion ni incendio**

**"Una bateria que no se incendia" no es un lujo en el espacio, es una necesidad.**

---

## Battolyser — una bateria que tambien hace electrolisis

Aqui es donde el niquel-hierro supera la categoria de "segunda opcion" y ofrece una **ventaja unica**.

### Principio

Concepto de Battolyser desarrollado por la Universidad Tecnica de Delft (TU Delft). Aprovecha activamente la tolerancia a sobrecarga de las baterias de niquel-hierro:

```
[Cargando]         Energia electrica → almacenamiento quimico en electrodos Fe/Ni
[Carga completa]   Corriente adicional → electrolisis del agua en la solucion acuosa de KOH
                   Catodo: 2H₂O + 2e⁻ → H₂↑ + 2OH⁻
                   Anodo: 2OH⁻ → ½O₂↑ + H₂O + 2e⁻
```

**Un solo dispositivo funciona como bateria + electrolizador.** No se necesita equipo de electrolisis separado. Reduccion de masa, volumen y complejidad.

En litio-ion, sobrecarga = incendio. En niquel-hierro, sobrecarga = **produccion de hidrogeno**.

### Ciclo operativo en el modulo Dyson

```
[Operacion normal] Turbina 370 MW en funcionamiento
  ├→ Consumo de carga (~320 MW)
  └→ Excedente de potencia (~50 MW) → modo Battolyser
       └→ Acumulacion de H₂ ~890 kg/h + O₂ ~7.100 kg/h (asumiendo ~70% de eficiencia de electrolisis)

[Eclipse] 3-12 horas/ano
  ├→ Descarga de bateria (modo ESS)
  └→ H₂ acumulado → generacion por celda de combustible (en paralelo)
       → Energia disponible 2x+ respecto a bateria sola

[Parada de emergencia]
  └→ Doble almacenamiento H₂/O₂ → extension del soporte vital
```

### Mas alla del almacenamiento de energia

El H₂ y O₂ producidos por el Battolyser trascienden el simple almacenamiento de energia y se integran en el **ciclo material completo del modulo**:

| Producto | Aplicacion | Notas |
|----------|------------|-------|
| H₂ | Reabastecimiento de propulsante para remolcadores NTP | Fluido de trabajo de la propulsion termica nuclear |
| H₂ | Agente reductor en el proceso de fundicion | Oxido metalico → metal puro (FeO + H₂ → Fe + H₂O) |
| H₂ | Generacion de emergencia por celda de combustible | Energia de respaldo durante eclipse/mantenimiento |
| H₂ | Haber-Bosch → NH₃ → fertilizante | Agricultura del modulo de habitat |
| O₂ | Soporte vital (respiracion) | Esencial para el modulo de habitat |
| O₂ | Oxidante (soldadura, medicina) | Procesos de fabricacion local |

Una bateria que almacena energia y al mismo tiempo produce propulsante, agente reductor y oxigeno para respirar. El litio-ion solo almacena electricidad.

---

## "Si la densidad energetica es 1/10, no es demasiado grande?"

Correcto. Para almacenar la misma energia, el niquel-hierro necesita **5-10 veces el volumen** del litio-ion.

Pero:

```
Escala del modulo Dyson:
  Espejo: 1 km × 1 km = 1.000.000 m²
  Estructura: se extiende varios km detras del espejo
  Volumen total: millones de m³

Capacidad ESS necesaria (12 horas × 370 MW):
  4.440 MWh = 4.440.000 kWh

Niquel-hierro (base 40 Wh/L):
  111.000 m³ = 111 m × 111 m × 9 m

→ <1% del volumen total de la estructura
```

En una estructura de millones de m³ detras de un espejo de 1 km², 111.000 m³ es **una esquina**. Ademas, la elevada masa del niquel-hierro puede utilizarse como **contrapeso para estructuras rotatorias**. La desventaja se convierte en ventaja.

La alta autodescarga de ~1% diario tambien es un problema solo en tierra. Con la turbina funcionando 24/7/365, la bateria esta siempre en estado de carga. La autodescarga es **irrelevante**.

"Si simplemente se aumenta la potencia de la turbina, no se elimina la necesidad de ESS?" El eclipse y la parada de emergencia son situaciones en las que la turbina **se detiene por completo**. Generacion y almacenamiento son problemas separados.

---

## Diseno adaptado al entorno espacial

No se puede llevar una bateria de niquel-hierro terrestre al espacio tal cual. Se necesitan tres adaptaciones.

### 1. Prevencion de evaporacion del electrolito

La solucion acuosa de KOH pierde humedad al exponerse al vacio. Es imprescindible una **estructura de celdas selladas**. Afortunadamente, las celdas de bateria ya tienen un diseno sellado. Para uso espacial, solo hay que reforzar el nivel de hermeticidad.

### 2. Separacion de gas en microgravedad

En modo Battolyser, las burbujas de H₂/O₂ se adhieren a la superficie de los electrodos. En la Tierra, la flotabilidad separa las burbujas, pero en microgravedad no funciona.

**Solucion:** Recubrimiento hidrofobico en la superficie de los electrodos + fuerza centrifuga generada por la rotacion del propio modulo para la separacion de gas. Una aceleracion centrifuga de tan solo ~0,01G es suficiente para separar las burbujas.

### 3. Resistencia a la radiacion

La solucion acuosa de KOH es **extremadamente estable a la radiacion**, a diferencia de los electrolitos organicos. Los electrolitos organicos se degradan cuando la radiacion rompe las cadenas moleculares. En la solucion acuosa, la radiolisis del agua produce pequenas cantidades de descomposicion, pero se regenera naturalmente por recombinacion. En un entorno de radiacion, el niquel-hierro es **intrinsecamente superior** al litio-ion.

---

## Resumen en una linea

El litio-ion es la mejor bateria de la Tierra. Pero en los asteroides no hay litio, en el espacio no se puede reemplazar cada 10 anos y en el vacio no se puede apagar un incendio. Las baterias de niquel-hierro se pueden fabricar con subproductos de la fundicion de asteroides, duran 30-50 anos sin reemplazo, no se incendian y, una vez completamente cargadas, se transforman en electrolizadores que producen propulsante y oxigeno para respirar. Que la densidad energetica sea 1/10 no tiene sentido a escala de 1 km².

Para las aplicaciones terrestres de las baterias de niquel-hierro, vease [Baterias de niquel-hierro como ESS fuera de red](https://www.parkjunwoo.com/1/tech/iron-nickel-ess-rural-energy/).

![Baterias de niquel-hierro desarrolladas por Edison en 1901. Photo: z22 / Wikimedia Commons / CC BY-SA 3.0](/images/why-iron-nickel-battery.webp)
