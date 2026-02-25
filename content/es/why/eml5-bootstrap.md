---
title: "Por qué el primer paso es L5 Tierra-Luna, no Mercurio"
date: 2026-02-24T12:00:01+09:00
lastmod: 2026-02-24T12:00:01+09:00
tags: ["enjambre-dyson", "EML5", "arranque", "punto-lagrange"]
image: "/images/eml5-bootstrap.webp"
imageCaption: "Puntos de Lagrange del sistema Tierra-Luna. Credito: NASA/WMAP Science Team. Dominio publico."
summary: "El primer espejo de un enjambre de Dyson debería colocarse en el punto L5 Tierra-Luna, no en Mercurio. Con 1,3 segundos de retardo en las comunicaciones, recursos lunares directos y reabastecimiento desde la Tierra, EML5 es el sitio óptimo para el bootstrap."
author: "PARK JUN WOO"
authorLink: "https://parkjunwoo.com/1/about"
---

## ¿Dónde se comienza un enjambre de Dyson?

Las discusiones sobre enjambres de Dyson siempre parten de la forma final. Desmantelamiento de Mercurio, despliegue cerca del Sol, potencias de varios TW a PW. Es el marco que estableció la serie de Isaac Arthur, y la mayoría lo da por sentado.

Pero antes de debatir la civilización K2 terminada, hay una pregunta mucho más importante: **¿dónde se coloca el primer espejo?**

La humanidad está actualmente en K 0.73. Aquí están los cálculos sobre dónde dar ese primer paso.

---

## Por qué EML5 (L5 Tierra-Luna)

### Hoja de ruta en 3 fases

| Fase | Ubicación | Distancia a la Tierra | Retardo de comunicación | Función |
|------|-----------|----------------------|------------------------|---------|
| **1. Bootstrap** | **EML5** | **~380 000 km** | **~1,3 s** | **Primera base industrial** |
| 2. Scale-up | SEL5 (L5 Sol-Tierra) | 150 millones km | ~8 min 20 s | Enjambre de Dyson a gran escala |
| 3. Full-scale | Mercurio | Variable | Variable | Desmantelamiento planetario K2+ |

La mayoría de las discusiones comienzan en la Fase 2 o 3. **Pero no hay Fase 2 sin Fase 1.**

### Las ventajas decisivas de EML5

**1. Retardo de comunicación de 1,3 segundos — prácticamente tiempo real**

Mercurio tiene retardos de ida de varios a más de diez minutos, además de periodos de apagón por conjunción solar. EML5 está a 1,3 segundos — suficientemente cerca para el control remoto. **Se puede empezar sin IA completamente autónoma.** Esto no es un lujo; es decisivo para el bootstrap. Confiar todo a una IA de fabricación autónoma nunca validada en el espacio versus supervisar en tiempo real desde la Tierra — son proposiciones completamente distintas.

**2. Suministro directo de recursos lunares**

| Recurso | Fuente | Uso | Método de transporte |
|---------|--------|-----|---------------------|
| Aluminio (Al) | Regolito Al₂O₃ (~15%) | Recubrimiento reflectante del espejo | Mass driver |
| Titanio (Ti) | Ilmenita FeTiO₃ | Material estructural (ligero) | Delta-V ~2,5 km/s |
| Oxígeno (O₂) | Subproducto de reducción | Soporte vital | Sin necesidad de cohete químico |
| Silicatos | Regolito | Blindaje contra radiación | — |

Sin el enorme prerrequisito de una flota de minería de asteroides, **se pueden lanzar recursos directamente desde la Luna con un mass driver.** El delta-V de la Luna a EML5 es ~2,5 km/s — alcanzable con cohetes químicos, y con un mass driver electromagnético el consumo de combustible es cero.

**3. Reabastecimiento fácil desde la Tierra**

El delta-V de LEO a EML5 es mucho menor que al espacio profundo. Equipos iniciales, electrónica y materiales de alto rendimiento que aún no se pueden fabricar en el espacio pueden ser suministrados desde la Tierra. La fase de bootstrap no necesita exigir un 100% de autosuficiencia.

**4. Punto de estabilidad gravitacional**

EML5 es un punto de Lagrange del sistema Tierra-Luna. El coste de mantenimiento orbital es casi cero.

---

## Qué se hace en EML5

### Primer objetivo: capacidad de fabricación in situ de espejos semilla

1. Desplegar desde la Tierra el primer espejo semilla + equipo de fundición a EML5
2. Transportar Al, Ti y silicatos desde la Luna mediante mass driver
3. Usar la energía solar térmica concentrada del espejo semilla para fundir al vacío los materiales lunares
4. Usar la producción para **fabricar un segundo espejo in situ** — el punto de partida del bucle de autorreplicación

### Entorno solar

EML5 está a la misma distancia de 1 AU que la órbita terrestre. Flujo solar de 1 361 W/m². No alcanza el flujo 6,6 veces mayor cerca de Mercurio (0,39 AU), pero la vida útil del espejo y las condiciones de operación son incomparablemente mejores.

### Fase de validación

EML5 también sirve como escenario de validación tecnológica:
- ¿Funciona realmente la fundición al vacío?
- ¿Coincide el periodo de duplicación del bucle de autorreplicación con los cálculos?
- ¿La vida útil del recubrimiento del espejo cumple las predicciones?

Todo esto puede validarse **bajo supervisión desde 1,3 segundos de distancia.** Depurar con retardos de minutos a decenas de minutos en el espacio profundo es una historia completamente diferente.

---

## Por qué empezar en EML5

| Enfoque | Prerrequisitos para el primer espejo | Riesgo |
|---------|--------------------------------------|--------|
| Desmantelamiento de Mercurio | Aterrizaje en Mercurio, minería, escape, despliegue orbital | Extremadamente alto |
| Espacio profundo directo | Flota de minería de asteroides, IA totalmente autónoma | Alto |
| **EML5** | **Mass driver lunar, supervisión en tiempo real desde la Tierra** | **El más bajo** |

La diferencia clave: **si EML5 falla, se puede reparar.** A 1,3 segundos, un joystick todavía llega.

---

## Pero EML5 no es para siempre

EML5 no es la solución universal. Es óptimo como sitio de bootstrap, pero sus límites son claros.

### 1. Sombra de la Tierra

EML5 orbita en el mismo plano que la Luna (inclinación 5,14°), pasando al lado opuesto de la Tierra cada ~27,3 días. Cuando está cerca del plano de la eclíptica, entra en la umbra de la Tierra y la energía solar se bloquea por completo.

```
Diámetro de la umbra terrestre a 384 400 km:
  r = R_earth - d × (R_sun - R_earth) / d_sun
  = 6 371 - 384 400 × 689 629 / 149 600 000
  = 6 371 - 1 772 = 4 599 km (radio)
  → Diámetro ~9 200 km

Condición de entrada: latitud eclíptica < arctan(4 599 / 384 400) ≈ 0,69°
Inclinación orbital lunar 5,14° → solo ocurre cerca de los nodos ascendente/descendente ±7,7°
```

La geometría es idéntica a un eclipse lunar (desplazada 60°, así que ocurre en momentos diferentes):

| Parámetro | Valor |
|-----------|-------|
| Frecuencia | 2–3 veces al año |
| Duración máxima por evento | ~2,5 horas (tránsito central por la umbra) |
| Incluyendo penumbra | ~4,3 horas |
| **Tiempo de inactividad anual total** | **3–12 horas** |
| **Disponibilidad anual** | **99,86–99,97%** |

Unas pocas horas de almacenamiento térmico permiten operación ininterrumpida. No es fatal, pero **la mera existencia de una sombra es una limitación.**

### 2. Región estable pequeña

Debido a la relación de masas Tierra-Luna (81:1), la región estable de EML5 abarca solo decenas de miles de km. Cientos a miles de módulos caben, pero **más allá de eso, se satura.**

### 3. Los recursos lunares solos no bastan

La Luna no tiene recursos masivos de Fe-Ni. La aleación hierro-níquel — el principal material estructural para los marcos de los espejos — solo puede obtenerse en cantidad de los asteroides.

| Recurso | Luna | Asteroide (1986 DA) |
|---------|------|-------------------|
| Al, Ti, O₂ | Abundante | Nulo / traza |
| Aleación Fe-Ni | **Casi cero** | **90%+** |
| Silicatos | Abundante | Subproducto de escoria |

Los espejos iniciales pueden usar marcos de Ti + recubrimiento de Al, pero **escalar más allá de miles de unidades es imposible sin Fe-Ni de asteroides.**

### 4. Perturbación solar

La perturbación gravitacional solar hace que EML5 sea quasi-stable en lugar de perfectamente estable. Se requiere mantenimiento orbital a largo plazo.

### Resumen de restricciones

| Restricción | Gravedad |
|-------------|----------|
| Sombra de la Tierra (3–12 h/año) | Baja — mitigable con almacenamiento térmico |
| Región estable (se satura en miles de módulos) | **Media** |
| Sin Fe-Ni | **Alta** |
| Perturbación solar | Baja |

---

## Entonces, ¿qué sigue?

EML5 es el primer paso óptimo para un enjambre de Dyson. Retardo de comunicación de 1,3 segundos, suministro directo de recursos lunares, capacidad de reabastecimiento desde la Tierra — no existen mejores condiciones para el bootstrap.

Pero los límites son igualmente claros:
- 3–12 horas/año de inactividad por sombra terrestre
- Región estable de decenas de miles de km — se satura en miles de módulos
- **La Luna no tiene Fe-Ni** — el muro para escalar

En EML5 se valida el bucle de autorreplicación y se crecen cientos a miles de módulos. La tecnología funciona. **Pero no se puede crecer más aquí.**

Entonces, ¿dónde está la siguiente etapa?
