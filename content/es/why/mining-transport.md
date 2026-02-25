---
title: "Por qué no fundir en el sitio"
date: 2026-02-24T12:00:04+09:00
lastmod: 2026-02-24T12:00:04+09:00
tags: ["minería-asteroide", "transporte", "SMR", "NTP"]
image: "/images/1986da-orbit.webp"
summary: "Diseño completo de ingeniería para minar el asteroide metálico 1986 DA con una nave minera propulsada por SMR, embalar mineral en mallas de alambre de Fe-Ni y transportar 200.000 toneladas por ventana de transferencia."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

*Orbital visualization: [SpaceReference.org](https://www.spacereference.org/asteroid/6178-1986-da), built with [SpaceKit](https://typpo.github.io/spacekit/). Data: JPL Small Body Database.*

## Minar suena genial, pero ¿cómo?

En el artículo anterior propusimos 1986 DA como fuente de materia prima para un enjambre de Dyson. Más del 90% Fe-Ni, microgravedad, cero residuos. Superior a Mercurio en todos los aspectos para el arranque inicial.

Pero queda una pregunta: **¿Cómo se mina realmente un bloque metálico en microgravedad y cómo se transporta?**

Primero el principio fundamental: **"En el sitio solo se excava, tritura y empaqueta. El trabajo pesado se hace donde la energía abunda."**

---

## División de roles: sitio vs base

| Tarea | Ubicación | Razón |
|-------|-----------|-------|
| Excavación y trituración | 1986 DA in situ | Donde está el mineral |
| Embalaje (malla de alambre) | 1986 DA in situ | Fabricado con Fe-Ni local |
| Clasificación | **No se hace** | Cada componente tiene uso |
| Fundición | **Base (espejos Dyson)** | Térmica solar de espejos GW >> SMR in situ kW |
| Fabricación y ensamblaje | **Base** | Clústeres especializados |

¿Por qué no fundir in situ? La fundición requiere 1.600°C. El SMR in situ produce 50~100 kW. Los espejos Dyson de la base entregan ~600 MW (térmicos). **La brecha energética es de miles de veces.** Construir una fundición en el asteroide es como poner una acería en la cima de una montaña — es más racional enviar el mineral.

---

![mining-transport](/images/post004.webp)

## La nave minera: una máquina que excava, tritura y empaqueta

### Energía: SMR + impulso solar

La órbita altamente elíptica de 1986 DA (excentricidad 0,58) hace que el flujo solar varíe más de 14 veces según la posición orbital.

| Posición orbital | Distancia | Flujo solar | vs Tierra |
|-----------------|-----------|-------------|-----------|
| Perihelio | 1,17 AU | ~995 W/m² | 73% |
| Semieje mayor | 2,81 AU | ~172 W/m² | 13% |
| Afelio | 4,46 AU | ~68 W/m² | 5% |

**La energía solar sola no puede sostener la minería continua.** Un SMR (Reactor Modular Pequeño, 50~100 kW) es la fuente de energía principal. Cerca del perihelio, los paneles solares se unen como refuerzo.

| Segmento orbital | SMR | Solar | Combinado | Modo |
|-----------------|-----|-------|-----------|------|
| Cerca del perihelio (~1,2 AU) | 50~100 kW | 50~100 kW | **100~200 kW** | Impulso |
| Órbita media (~2,8 AU) | 50~100 kW | ~15 kW | ~65~115 kW | Normal |
| Cerca del afelio (~4,5 AU) | 50~100 kW | ~5 kW | ~55~105 kW | Baja velocidad |

Incluso en el afelio, el SMR mantiene la minería en marcha. Solo se ralentiza.

### Equipo

| Equipo | Función | Consumo |
|--------|---------|---------|
| Excavadora | Minería superficial/subterránea | ~20~50 kW |
| Trituradora | Fracturar a tamaño de transporte | ~10~30 kW |
| Horno eléctrico pequeño | Fe-Ni → materia prima de alambre | ~10~20 kW |
| Trefiladora | Alambre → malla | ~5~10 kW |
| Control y comunicaciones | Control autónomo IA | ~5 kW |
| **Total** | | **~50~115 kW** |

Un solo SMR alimenta todo el equipo. La nave minera está **permanentemente estacionada** — orbita con 1986 DA y mina sin pausa.

### Productividad

Suposición conservadora: 50 kW promedio, ~100 kg de mineral procesados por kWh (trituración mecánica y embalaje en microgravedad; comparable a la trituración de roca terrestre a 10–25 Wh/kg; la fundición se realiza por separado en la base).

| Concepto | Valor |
|----------|-------|
| Producción diaria | ~120 toneladas |
| Producción anual | ~43.800 toneladas |
| **Por período orbital (4,71 años)** | **~200.000 toneladas** |

---

## Contenedores: redes, no cajas

¿Qué necesita un contenedor de carga en el espacio?
- Contención de presión — vacío, innecesario
- Soporte de peso propio — microgravedad, innecesario
- Resistencia del aire — vacío, innecesario
- **Que el mineral no se disperse durante el transporte**

Ese es el único requisito. No una caja rígida — **una red basta.**

### Proceso de fabricación

```
Mineral extraído
  ├─ 99,5% → Carga (paquetes de mineral)
  └─ 0,5% → Horno eléctrico pequeño → Trefilado → Tejido de malla
                                                  → Embalaje de paquetes
```

| Método | Ratio masa contenedor:carga |
|--------|---------------------------|
| Contenedores metálicos desde la Tierra | Desperdicio de transporte extremo |
| Cajas de Fe-Ni fundidas in situ | ~2~3% (excesivo) |
| **Malla de alambre Fe-Ni in situ** | **~0,1~0,5%** |

**La propia malla se convierte en materia prima de fundición al llegar.** Incluso el embalaje se aprovecha al 100%.

---

## Transporte: ventanas de transferencia y propulsión

### Mecánica orbital

Período orbital de 1986 DA: 4,71 años. La ventana de transferencia óptima hacia el espacio terrestre se abre una vez por período orbital.

| Concepto | Valor |
|----------|-------|
| LEO → encuentro con 1986 DA | delta-V ~7,1 km/s |
| Salida óptima | Cerca del perihelio (1,17 AU) |
| Próxima aproximación cercana | **2038 (0,21 AU)** |

### Opciones de propulsión

| Método | Impulso específico (Isp) | Características | Idoneidad |
|--------|------------------------|-----------------|-----------|
| Químico (LH2/LOX) | ~450 s | Fracción de carga útil extremadamente baja | ❌ |
| **Propulsión Nuclear Térmica (NTP)** | **~900 s** | Alto empuje, rápido | ✅ |
| **Propulsión Nuclear Eléctrica (NEP)** | **~3.000 s+** | Propelente mínimo, lento | ✅ Transporte masivo |
| Propulsión Solar Eléctrica (SEP) | ~3.000 s | Eficiencia cae en el afelio | ⚠️ Limitado |

**Un híbrido NTP + NEP puede ser óptimo:** un solo reactor sirve como fuente térmica NTP (alto empuje para la salida del perihelio) y fuente eléctrica NEP (bajo empuje, alta eficiencia en crucero).

### Ciclo logístico

```
[Año 0]  Nave minera llega a 1986 DA, comienza la minería
             │ 4,71 años de minería, embalaje, acopio (~200.000 toneladas)
[Año ~5] Ventana de transferencia → nave de transporte carga y parte
             │ Transferencia Hohmann (~2-3 años)
[Año ~7] Nave de transporte llega, descarga mineral
             │ Mantenimiento y reabastecimiento
[Año ~8] Nave de transporte parte de regreso
             │
[Año ~10] Segunda carga ... el ciclo se repite
```

La nave minera permanece; la nave de transporte hace el viaje de ida y vuelta. Minería y transporte operan **asincrónicamente en paralelo.**

---

## 2038: piérdelo y espera décadas

| Fecha | Evento |
|-------|--------|
| Década de 2030 | Starship comercializado, tecnología SMR espacial madura |
| **2038** | **1986 DA aproximación cercana (0,21 AU) — ventana óptima para desplegar nave minera** |
| 2038~2042 | Nave minera llega al sitio, comienza minería |
| ~2043 | Primera nave de transporte carga y parte |
| **~2046** | **Primera entrega de mineral** |

Después de 2038, la próxima aproximación de esta magnitud está a décadas de distancia. **Perder esta ventana retrasa significativamente el cronograma.**

### Estado de la tecnología necesaria

| Tecnología | Actual (2026) | Perspectiva 2038 |
|------------|--------------|------------------|
| Starship (vehículo de lanzamiento pesado) | Vuelos de prueba en curso | ✅ Comercialización esperada |
| SMR espacial | NASA FSP clase 40 kW en desarrollo | ✅ Demostración lunar esperada |
| Propulsión NTP | DARPA DRACO en desarrollo | ⚠️ Vuelo de prueba esperado |
| Minería de asteroides | OSIRIS-REx retorno de muestra exitoso | ⚠️ Gran escala no probada |
| IA autónoma espacial | Nivel rover marciano | ✅ Se espera madurez suficiente |

Ninguna de estas tecnologías es imposible. Todas están **en desarrollo o se espera que maduren en una década.**

---

## Después de la llegada: el Sol funde

Cuando el mineral llega, los espejos Dyson lo calientan directamente a 1.600°C. El vacío espacial es "equipo de refinación gratuito":

1. **Fusión óptica** — El calor concentrado del espejo funde el mineral crudo en metal fundido
2. **Desgasificación al vacío** — El azufre y el fósforo se vaporizan naturalmente en el vacío (capturados por trampas frías)
3. **Separación centrífuga** — Capa exterior: Fe-Ni + metales del grupo del platino / Capa interior: escoria de silicato

```
Paquete de mineral llega
  ├→ Malla de alambre Fe-Ni → Alimenta la fundición (el embalaje se convierte en materia prima)
  └→ Mineral → Calentamiento con espejo a 1.600°C
       ├→ Aleación Fe-Ni (90%+) → Elementos estructurales, marcos de espejo, tubos
       ├→ Escoria de silicato → Blindaje + materia prima para lingotes de silicio
       ├→ Metales del grupo del platino → Recubrimientos, catalizadores
       └→ S, P → Materia prima química, dopaje de semiconductores
```

Lo que las acerías terrestres logran con enormes cantidades de energía y productos químicos, **el vacío espacial y el calor solar lo proporcionan gratis.**

---

## Resumen en una línea

La nave minera excava, tritura y empaqueta con un solo SMR. Los contenedores son mallas de Fe-Ni local — hasta el embalaje es materia prima. La nave de transporte lleva 200.000 toneladas por ventana de transferencia. 2038 es la primera ventana de oportunidad. El mineral que llega lo funde el Sol. No se desperdicia nada.
