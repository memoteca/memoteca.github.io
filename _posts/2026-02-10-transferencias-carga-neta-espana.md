---
layout: post
title: "Transferencias del Estado y carga fiscal neta en España"
date: 2026-02-10
series: impuestos
part: 2
---

*Este es el segundo artículo de una [serie](https://statisticspeek.github.io/) sobre fiscalidad en España.
En el [primer artículo](/2026/02/09/impuestos-progresivos-espana.html)
calculamos la carga fiscal bruta del asalariado y encontramos una
U invertida: la carga total alcanza su máximo en los 56.000 EUR de salario
y desciende para rentas más altas. Pero advertimos que ese análisis era
parcial: solo miraba lo que el ciudadano paga al Estado, no lo que recibe.
Este estudio completa la foto.*

---

## Resumen

El sistema fiscal español no se limita a recaudar: también redistribuye.
Pensiones, prestaciones por desempleo, sanidad pública y educación pública
fluyen del Estado hacia los hogares, y lo hacen de forma desigual — los
hogares de renta baja reciben proporcionalmente mucho más de lo que pagan.

Utilizando datos del 9.º Informe del Observatorio de FEDEA (datos de 2022),
este estudio calcula la **carga fiscal neta** de cada nivel de renta:

```
Carga neta = Impuestos pagados - Transferencias monetarias - Servicios públicos en especie
```

Los resultados muestran que:

1. **El 60% de los hogares españoles son receptores netos** del Estado:
   reciben más en transferencias y servicios de lo que pagan en impuestos.
2. **El punto de cruce** se sitúa en torno a los 55.000 EUR de renta bruta
   del hogar (entre el tercer y cuarto quintil).
3. **El sistema es fuertemente redistributivo**: el coeficiente de Gini
   pasa de 0.497 (renta de mercado) a 0.327 (renta final), una reducción
   del 34%.
4. **Sin embargo, la U invertida persiste**: el percentil 91-99 soporta
   una carga neta del -23.6%, mientras que el top 1% solo paga -18.1%.
   El mecanismo es el mismo que identificamos en el Estudio 1 — la base
   máxima de cotización — agravado por el acceso a rentas del capital
   y al Impuesto de Sociedades.

---

## 1. Introducción

### 1.1 Motivación

En el Estudio 1 concluimos que la carga fiscal bruta del asalariado
dibuja una U invertida: sube hasta el 67.8% del salario bruto en los
56.000 EUR y después cae al 52.6% para los 280.000 EUR. El mecanismo
principal es la base máxima de cotización a la Seguridad Social (61.214
EUR/año), que convierte las cotizaciones en un tributo fuertemente
regresivo por encima de ese umbral.

Sin embargo, como advertimos entonces, ese análisis solo miraba un lado
del balance. El Estado recauda impuestos, sí, pero también devuelve una
fracción muy importante en forma de:

- **Pensiones** (contributivas y no contributivas).
- **Prestaciones por desempleo, invalidez, supervivencia, maternidad.**
- **Asistencia social** (Ingreso Mínimo Vital, rentas mínimas autonómicas).
- **Servicios públicos** valorados en especie: sanidad y educación.

Sin contabilizar estas transferencias, el análisis fiscal queda sesgado:
sobreestima la carga real sobre las rentas bajas (que son las principales
receptoras) y subestima el efecto redistributivo del sistema.

La pregunta de este estudio es: **cuando descontamos las transferencias
del Estado, ¿sigue existiendo la U invertida?**

### 1.2 Hipótesis

Las transferencias reducen significativamente la desigualdad y convierten
al 60% de los hogares en receptores netos del Estado. Sin embargo, la
anomalía del tramo más alto (el top 1% pagando proporcionalmente menos
que el percentil 91-99) persiste, porque tiene causas estructurales
— base máxima de SS, dualidad rentas del trabajo/capital, Impuesto de
Sociedades — que las transferencias no corrigen.

### 1.3 Alcance

Este estudio utiliza datos agregados del Observatorio de FEDEA, que
cubre **todos los hogares españoles** (no solo asalariados). Esto es
más amplio que el Estudio 1, que se limitaba a asalariados con contrato.
La contrapartida es que los resultados no son directamente comparables
tramo a tramo con los del Estudio 1, aunque las conclusiones
cualitativas se refuerzan mutuamente.

---

## 2. Marco conceptual: de la renta de mercado a la renta final

El proceso redistributivo del Estado se puede descomponer en etapas.
En cada una, el coeficiente de Gini se reduce:

```
RENTA DE MERCADO (antes de impuestos y transferencias)
  Gini = 0.497
       │
       ├── + Pensiones contributivas y no contributivas
       ├── + Prestaciones desempleo, invalidez, supervivencia
       ├── + Asistencia social (IMV, rentas mínimas)
       │
       ▼
RENTA BRUTA (incluye transferencias monetarias)
  Gini ≈ 0.397
       │
       ├── - IRPF
       ├── - Cotizaciones SS (trabajador + empresa)
       ├── - IVA e impuestos especiales
       ├── - Impuesto de Sociedades (incidencia sobre accionistas)
       ├── - IBI, Patrimonio, otros
       │
       ▼
RENTA DISPONIBLE (después de impuestos)
  Gini ≈ 0.360
       │
       ├── + Sanidad pública (valor per cápita)
       ├── + Educación pública (valor per cápita)
       │
       ▼
RENTA FINAL (incluye servicios públicos en especie)
  Gini ≈ 0.327
```

**Las pensiones y prestaciones** son la herramienta redistributiva
más potente: reducen el Gini en 0.100 puntos (de 0.497 a 0.397). Los
impuestos directos contribuyen otros 0.032 puntos. Los servicios en
especie (sanidad y educación) aportan los últimos 0.033 puntos.

---

## 3. Datos y metodología

### 3.1 Fuente: FEDEA

Los datos proceden del **9.º Informe del Observatorio sobre el Reparto
de los Impuestos y las Prestaciones entre los Hogares Españoles**
(FEDEA, 2022), publicado en febrero de 2025. Este informe combina:

- Microdatos de la Encuesta de Condiciones de Vida (ECV) del INE.
- Registros administrativos de la AEAT (IRPF, IS, IVA).
- Registros de la Seguridad Social (cotizaciones, pensiones).
- Datos presupuestarios (gasto sanitario y educativo).

Los hogares se clasifican por **renta bruta** (incluidas transferencias
monetarias) en quintiles, con el quinto quintil desagregado en decil 9,
percentiles 91-99 y percentil 100 (el top 1%).

| Grupo | Hogares | Renta bruta media | Renta total (Md EUR) | % renta total |
|---|---|---|---|---|
| Quintil 1 (0-20%) | 3.829.801 | 12.030 EUR | 46,1 | 4,4% |
| Quintil 2 (20-40%) | 3.829.801 | 26.956 EUR | 103,2 | 9,8% |
| Quintil 3 (40-60%) | 3.829.800 | 41.672 EUR | 159,6 | 15,1% |
| Quintil 4 (60-80%) | 3.829.801 | 62.667 EUR | 239,9 | 22,7% |
| Decil 9 (80-90%) | 1.914.900 | 89.431 EUR | 171,3 | 16,2% |
| Percentil 91-99 | 1.723.410 | 143.053 EUR | 246,6 | 23,4% |
| Top 1% (P100) | 191.488 | 465.466 EUR | 89,1 | 8,4% |
| **Total** | **19.149.001** | | **1.055,7** | **100%** |

### 3.2 Impuestos incluidos

FEDEA contabiliza la totalidad de la carga fiscal:

| Impuesto | Tipo | Observaciones |
|---|---|---|
| IRPF | Directo, progresivo | Tipo efectivo del 2.3% (Q1) al 16.0% (P91-99) |
| Cotizaciones SS trabajador | Directo | Del 5.3% (Q1) al 1.1% (top 1%) — regresivo |
| Cotizaciones SS empresa | Directo (incidencia) | Del 6.6% (Q1) al 4.1% (top 1%) — regresivo |
| Impuesto de Sociedades | Directo (incidencia) | Del 0.08% (Q1) al 6.78% (top 1%) |
| IVA e impuestos especiales | Indirecto | Incluido en el TME total |
| IBI | Directo | Del 1.50% (Q1) al 0.14% (top 1%) — regresivo |
| Impuesto de Patrimonio | Directo | 0.06-0.12% en todos los tramos |

**Nota sobre el Impuesto de Sociedades.** FEDEA imputa la carga del IS
a los hogares propietarios de las empresas (accionistas). El top 1%
paga un 6.78% de su renta por esta vía, frente al 0.08% del quintil 1.
Esto refleja que las rentas del capital están concentradas en la parte
alta de la distribución — pero también que el IS permite tributar a un
tipo combinado inferior al del IRPF.

### 3.3 Transferencias monetarias

Las transferencias monetarias incluyen todas las prestaciones públicas
que el hogar recibe en efectivo:

| Prestación | Q1 | Q2 | Q3 | Q4 | D9 | P91-99 | Top 1% |
|---|---|---|---|---|---|---|---|
| Jubilación | 3.626 | 6.793 | 9.231 | 7.695 | 8.246 | 8.182 | 13.323 |
| Supervivencia | 2.200 | 1.668 | 1.184 | 1.091 | 849 | 750 | 1.289 |
| Desempleo | 841 | 1.086 | 1.147 | 1.200 | 949 | 965 | 643 |
| Invalidez | 484 | 859 | 888 | 865 | 646 | 682 | 992 |
| Asistencia social | 565 | 231 | 104 | 63 | 88 | 62 | 739 * |
| Resto | 249 | 477 | 561 | 671 | 701 | 724 | 501 |
| **Total** | **7.965** | **11.114** | **13.115** | **11.585** | **11.479** | **11.365** | **17.487** |

*(Cifras en EUR/hogar/año.)*

*\* El dato de asistencia social del top 1% (739 EUR, superior al del
quintil 1) es contraintuitivo para una prestación sujeta a requisitos
de renta. Puede deberse a un artefacto muestral — la ECV representa
este grupo con muy pocas observaciones — o a la composición del hogar
(un miembro dependiente que recibe prestaciones dentro de un hogar de
renta alta). Pendiente de verificación con datos desagregados.*

Tres hallazgos llaman la atención:

1. **Las pensiones de jubilación son la mayor partida** en todos los
   tramos. En el quintil 3, representan el 70% del total de
   transferencias. En el top 1%, el 76%.

2. **El top 1% recibe más transferencias monetarias (17.487 EUR) que
   cualquier otro grupo.** Esto se debe a las pensiones contributivas:
   quien tuvo mayores salarios acumuló más derechos y cobra pensiones
   más altas. La pensión máxima en 2022 rondaba los 39.000 EUR/año.

3. **La asistencia social del top 1% (739 EUR) supera a la del quintil
   más pobre (565 EUR).** Este dato es anómalo y requiere cautela
   (véase nota al pie de la tabla).

### 3.4 Transferencias en especie

FEDEA valora los servicios públicos de sanidad y educación e imputa
su coste a los hogares. El valor es relativamente uniforme en términos
absolutos (5.612 EUR en Q1 vs 10.441 EUR en top 1%), pero como
porcentaje de la renta es enormemente redistributivo:

| Grupo | Valor en especie | % de la renta |
|---|---|---|
| Quintil 1 | 5.612 EUR | **46.6%** |
| Quintil 2 | 6.979 EUR | **25.9%** |
| Quintil 3 | 7.563 EUR | **18.1%** |
| Quintil 4 | 8.677 EUR | **13.8%** |
| Decil 9 | 9.811 EUR | **11.0%** |
| P91-99 | 10.304 EUR | **7.2%** |
| Top 1% | 10.441 EUR | **2.2%** |

El valor ligeramente creciente en términos absolutos refleja que los
hogares de renta alta tienen más miembros, hijos en edad escolar y
mayor esperanza de vida. Pero como porcentaje de la renta, los
servicios en especie suponen casi la mitad de los ingresos del quintil
1, frente al 2% del top 1%.

### 3.5 Cálculo de la carga neta

Para cada grupo de renta:

```
Carga neta (EUR) = Impuestos pagados - Transferencias monetarias - Servicios en especie
Carga neta (%)   = Carga neta / Renta bruta × 100
```

Un valor **positivo** indica que el hogar recibe más de lo que paga
(receptor neto). Un valor **negativo** indica que paga más de lo que
recibe (contribuyente neto).

---

## 4. Resultados

### 4.1 Impuestos pagados: confirmación de la U invertida

Los tipos medios efectivos totales (TME) que calcula FEDEA confirman
el patrón del Estudio 1, ahora con datos reales — no modelados — y
para todos los hogares (no solo asalariados):

| Grupo | Renta bruta | Impuestos pagados | TME total |
|---|---|---|---|
| Quintil 1 | 12.030 | 3.305 | **27.5%** |
| Quintil 2 | 26.956 | 8.286 | **30.7%** |
| Quintil 3 | 41.672 | 14.056 | **33.7%** |
| Quintil 4 | 62.667 | 23.211 | **37.0%** |
| Decil 9 | 89.431 | 34.749 | **38.9%** |
| P91-99 | 143.053 | 55.474 | **38.8%** |
| Top 1% | 465.466 | 112.110 | **24.1%** |

El TME sube del 27.5% al 38.9%, alcanza su máximo en el decil 9, y
**cae 14.8 puntos** hasta el 24.1% del top 1%. ¿Por qué?

![Tipos efectivos de impuestos directos por nivel de renta](/assets/images/impuestos/tipos_efectivos_fedea.png)

La respuesta está en la composición de los impuestos pagados:

| Grupo | IRPF | SS trabajador | SS empresa | I. Sociedades |
|---|---|---|---|---|
| Q1 | 2.3% | 5.3% | 6.6% | 0.08% |
| Q3 | 7.9% | 4.2% | 14.3% | 0.10% |
| P91-99 | 16.0% | 3.6% | 13.9% | 1.04% |
| **Top 1%** | **10.5%** | **1.1%** | **4.1%** | **6.78%** |

El top 1% paga un IRPF efectivo del **10.5%**, inferior al 16.0% del
percentil 91-99. Esto solo es posible si una parte importante de sus
ingresos no son rendimientos del trabajo (que tributan al 19-47%), sino
rentas del capital (19-28%), dividendos canalizados vía sociedades, o
ganancias patrimoniales. Además, su cotización a la SS empresa es solo
del 4.1%, frente al 13.9-16.7% de las rentas medias y altas — el
efecto techo de la base máxima.

### 4.2 Transferencias recibidas

Las transferencias totales (monetarias + en especie) son
sorprendentemente uniformes en términos absolutos:

| Grupo | Transfer. monetarias | En especie | **Total** | **% de la renta** |
|---|---|---|---|---|
| Q1 | 7.965 | 5.612 | **13.577** | **112.9%** |
| Q2 | 11.114 | 6.979 | **18.093** | **67.1%** |
| Q3 | 13.115 | 7.563 | **20.678** | **49.6%** |
| Q4 | 11.585 | 8.677 | **20.262** | **32.3%** |
| D9 | 11.479 | 9.811 | **21.290** | **23.8%** |
| P91-99 | 11.365 | 10.304 | **21.669** | **15.1%** |
| Top 1% | 17.487 | 10.441 | **27.928** | **6.0%** |

El quintil 1 recibe 13.577 EUR en transferencias totales, más que su
renta de mercado. **Sin las transferencias del Estado, este quintil
no podría subsistir.** En el otro extremo, el top 1% recibe 27.928 EUR
— la cifra más alta en términos absolutos — pero esto supone solo
el 6% de sus ingresos.

![Composición de las transferencias del Estado](/assets/images/impuestos/composicion_transferencias.png)

### 4.3 Carga fiscal neta: el balance completo

| Grupo | Impuestos | Transferencias | **Neto (EUR)** | **Neto (% renta)** | Estatus |
|---|---|---|---|---|---|
| Q1 | 3.305 | 13.577 | **+10.271** | **+85.4%** | Receptor neto |
| Q2 | 8.286 | 18.093 | **+9.806** | **+36.4%** | Receptor neto |
| Q3 | 14.056 | 20.678 | **+6.622** | **+15.9%** | Receptor neto |
| Q4 | 23.211 | 20.262 | **-2.949** | **-4.7%** | Contribuyente neto |
| D9 | 34.749 | 21.290 | **-13.458** | **-15.0%** | Contribuyente neto |
| P91-99 | 55.474 | 21.669 | **-33.804** | **-23.6%** | Contribuyente neto |
| Top 1% | 112.110 | 27.928 | **-84.182** | **-18.1%** | Contribuyente neto |

**El 60% de los hogares españoles (quintiles 1 a 3, unos 11.5 millones
de hogares) son receptores netos del Estado.** El punto de cruce se
sitúa en torno a los 55.000 EUR de renta bruta del hogar — no por
casualidad, cerca de la base máxima de cotización a la SS.

![Carga fiscal neta por nivel de renta](/assets/images/impuestos/carga_neta.png)

![Impuestos pagados vs transferencias recibidas](/assets/images/impuestos/impuestos_vs_transferencias.png)

### 4.4 La U invertida persiste

La carga neta máxima no recae sobre el top 1%, sino sobre el percentil
91-99 (contribuyentes con rentas entre ~100.000 y ~300.000 EUR):

- **P91-99**: -23.6% de carga neta → **máximo**
- **Top 1%**: -18.1% de carga neta → **5.5 puntos menos**

El top 1% paga un 24.1% en impuestos totales frente al 38.8% del
percentil 91-99. Recibe un 6.0% en transferencias frente al 15.1%.
Pero la diferencia neta sigue siendo favorable al top 1%: paga
proporcionalmente menos.

Esto confirma la hipótesis del Estudio 1: la anomalía no es un
artefacto del modelo, sino una realidad estructural del sistema fiscal
español. Las transferencias redistribuyen intensamente entre los
quintiles 1-4, pero no corrigen la inversión de la cola.

![Carga bruta vs neta: la U invertida persiste](/assets/images/impuestos/u_invertida_neta.png)

![La U invertida antes y después de las transferencias](/assets/images/impuestos/comparativa_bruta_neta.png)

### 4.5 Impacto en la desigualdad: el Gini

El coeficiente de Gini mide la desigualdad de una distribución (0 =
igualdad perfecta, 1 = un hogar lo tiene todo). El proceso
redistributivo español reduce el Gini en 0.170 puntos:

| Etapa | Gini | Reducción |
|---|---|---|
| Renta de mercado | 0.497 | — |
| + Pensiones y prestaciones | 0.397 | -0.100 |
| - IRPF y cotizaciones | 0.365 | -0.032 |
| - IVA e indirectos | 0.360 | -0.005 |
| + Sanidad y educación | 0.327 | -0.033 |
| **Total** | **0.327** | **-0.170 (34%)** |

**Las pensiones y prestaciones son el instrumento redistributivo más
potente** (reducen el Gini en 0.100 puntos, el 59% de la reducción
total). Los impuestos directos aportan el 19%. Los servicios públicos
en especie, otro 19%.

Esto tiene implicaciones de política: una reforma del IRPF que añada
2 puntos de tipo marginal al tramo más alto tendrá un efecto
redistributivo modesto comparado con, por ejemplo, una subida de las
pensiones mínimas o una expansión de la sanidad pública.

![Impacto redistributivo del sistema fiscal](/assets/images/impuestos/impacto_gini.png)

### 4.6 El caso especial del top 1%

El top 1% merece un análisis detallado porque rompe el patrón
esperado. Si el sistema fuera progresivo de principio a fin, este grupo
debería soportar la mayor carga neta. Pero paga -18.1%, frente al
-23.6% del percentil 91-99.

Los mecanismos son cuatro:

**1. Base máxima de cotización a la SS.** Con una renta de 465.466 EUR,
el tope de 61.214 EUR hace que las cotizaciones (empresa + trabajador)
supongan solo el 5.2% de su renta, frente al 17.5% del percentil
91-99. Este efecto se demostró en el Estudio 1 y FEDEA lo confirma
con datos reales.

**2. IRPF efectivo del 10.5%.** El tipo marginal máximo del IRPF es
el 47%, pero el tipo efectivo real del top 1% es solo el 10.5%.
La explicación está en la composición de la renta: una parte importante
son rendimientos del capital (base del ahorro, tipos 19-28%) y
ganancias patrimoniales, no rendimientos del trabajo. Además, las
sociedades interpuestas permiten diferir la tributación.

**3. Impuesto de Sociedades.** El top 1% soporta un 6.78% de carga
por el IS. Esto puede parecer un impuesto adicional, pero en realidad
es la contrapartida de no tributar esos beneficios en el IRPF. El tipo
efectivo del IS (~15-20% para grandes empresas) es inferior al tipo
marginal del IRPF (47%). La ruta IS + dividendo produce un tipo
combinado inferior al del asalariado puro.

**4. Pensiones altas.** El top 1% recibe 17.487 EUR/año en
transferencias monetarias — 6.122 EUR más que el percentil 91-99.
La mayor parte son pensiones de jubilación (13.323 EUR): quien cobró
salarios altos acumuló bases de cotización altas y, por tanto, pensiones
altas. Esto reduce su carga neta.

---

## 5. Discusión

### 5.1 Comparación con el Estudio 1

| Concepto | Estudio 1 (datos AEAT/INE + modelo fiscal) | Estudio 2 (datos observados FEDEA) |
|---|---|---|
| Población | Asalariados con contrato | Todos los hogares |
| Fuente | Salarios reales AEAT + gasto real INE + escala IRPF teórica | Microdatos ECV + registros administrativos AEAT/SS |
| Método | Calcula impuestos teóricos sobre salarios reales | Observa impuestos realmente pagados por cada hogar |
| Carga bruta pico | 67.8% en 56.000 EUR (como % bruto) | 38.9% en D9 / 89.000 EUR (TME) |
| U invertida bruta | Sí (cae 15.2pp hasta 281k) | Sí (cae 14.8pp hasta top 1%) |
| Carga neta | No calculada | -23.6% (P91-99) vs -18.1% (top 1%) |
| U invertida neta | No calculada | **Sí** (cae 5.5pp en el top 1%) |

Ambos estudios parten de datos reales, pero el método difiere: el
Estudio 1 **calcula** la carga fiscal teórica aplicando la normativa
vigente a los salarios reales de cada tramo (y la valida contra los
agregados de la AEAT, con un ajuste del 17.29% vs 17.30%). FEDEA, en
cambio, **observa** los impuestos que cada hogar pagó realmente, lo que
captura deducciones, rentas del capital, sociedades interpuestas y
cualquier otra circunstancia individual. Por eso el IRPF efectivo del
top 1% es del 10.5% en FEDEA (lo que realmente pagaron) frente al
40%+ que predice un modelo de asalariado puro (lo que teóricamente
les correspondería).

Las cifras absolutas también difieren porque las poblaciones y métricas
son distintas: el Estudio 1 mide la carga como porcentaje del salario
bruto individual e incluye la SS empresarial como porcentaje del bruto;
FEDEA mide el tipo medio efectivo (TME) sobre la renta bruta del hogar.
Pero la conclusión cualitativa es la misma: **el sistema es progresivo
hasta cierto punto, y después se invierte.**

### 5.2 Las pensiones: ¿transferencia o salario diferido?

Una crítica legítima a este análisis es que las pensiones contributivas
no son propiamente una "transferencia" del Estado, sino un **salario
diferido**: el trabajador cotizó durante 35-40 años y la pensión es
la contrapartida de esas cotizaciones. Si eliminásemos las pensiones
contributivas del cálculo, el top 1% pasaría de receptor de 17.487 EUR
a receptor de ~4.164 EUR, y su carga neta aumentaría.

Sin embargo, hay dos razones para incluirlas:

1. **Las pensiones se financian con impuestos corrientes** (sistema de
   reparto, no de capitalización). No existe un "fondo" individual. Lo
   que paga hoy un trabajador financia la pensión de hoy de un jubilado.
2. **El sistema de pensiones es redistributivo en sí mismo**: las
   pensiones mínimas, la pensión de viudedad y las no contributivas
   benefician desproporcionadamente a las rentas bajas. La tasa de
   reemplazo (pensión/último salario) es mayor para salarios bajos.

### 5.3 La transferencia oculta: de rentas medias a rentas altas

Hay un mecanismo dentro de la propia Seguridad Social que merece
atención especial, porque conecta los hallazgos del Estudio 1 con los
del Estudio 2 y revela una transferencia implícita que rara vez se
articula.

El circuito es el siguiente:

1. **Mientras trabaja**, el asalariado de 50.000 EUR paga un 37.15%
   en cotizaciones SS (empresa + trabajador) = 18.575 EUR/año. El de
   300.000 EUR paga ~25.000 EUR/año, un 8.3%. En proporción, el
   trabajador de renta media aporta 4.5 veces más que el de renta alta.

2. **Todas las cotizaciones van al mismo fondo común** (sistema de
   reparto): los trabajadores de hoy financian las pensiones de hoy.

3. **Del fondo salen pensiones altas** (hasta ~39.000 EUR/año en 2022)
   para jubilados que, cuando trabajaban, ganaban salarios muy por
   encima de la base máxima y cotizaban a tipos efectivos del 5-9%.

4. **Esos jubilados de renta alta aparecen en el top 1%** recibiendo
   13.323 EUR de media en pensiones de jubilación — financiadas
   desproporcionadamente por los trabajadores actuales de rentas medias.

El resultado es una **transferencia implícita de rentas medias a rentas
altas** dentro del propio sistema de Seguridad Social:

- Quien más gana, menos aporta en proporción (por el tope de
  cotización).
- Quien más ganó, más extrae del sistema (por la contributividad
  de las pensiones).
- Y quienes financian el sistema son los trabajadores actuales de
  rentas medias, que pagan el 37.15% íntegro sobre todo su salario.

```
TRABAJADOR ACTUAL (50k)          JUBILADO ANTIGUO (ganaba 200k)
Cotiza 37.15% = 18.575 €  ───►  Cobra pensión de 39.000 €
                                 (cotizó al ~9% cuando trabajaba)
```

Este mecanismo no es una decisión deliberada de política, sino una
**consecuencia estructural** de combinar tres elementos:

- Un **tope de cotización** que hace la contribución regresiva.
- Una **pensión contributiva** proporcional al salario previo.
- Un **sistema de reparto** donde los activos financian a los pasivos.

Existen matices redistributivos dentro del sistema de pensiones: las
pensiones mínimas, las no contributivas, los complementos a mínimos
y la tasa de reemplazo decreciente (los salarios bajos recuperan un
porcentaje mayor de su último sueldo). Pero estos mecanismos no
compensan plenamente la regresividad de la contribución, como muestra
el hecho de que el top 1% reciba más en transferencias absolutas que
cualquier otro grupo.

La eliminación o elevación sustancial del tope de cotización — como
ya se ha hecho en Suecia (sin tope) o en Francia (tope mucho más
alto) — corregiría simultáneamente dos problemas: la regresividad de
las cotizaciones (Estudio 1) y la transferencia implícita hacia
pensiones altas (Estudio 2).

### 5.4 ¿Es suficiente la redistribución?

El sistema fiscal español reduce el Gini en un 34%, de 0.497 a 0.327.
¿Es mucho o poco?

Comparativa OCDE (datos de 2020-2022):

| País | Gini mercado | Gini disponible | Reducción |
|---|---|---|---|
| Suecia | 0.434 | 0.268 | 38% |
| Francia | 0.519 | 0.292 | 44% |
| Alemania | 0.504 | 0.296 | 41% |
| **España** | **0.497** | **0.327** | **34%** |
| Italia | 0.504 | 0.330 | 35% |
| Reino Unido | 0.512 | 0.351 | 31% |

España redistribuye menos que Francia o Alemania, pero más que el
Reino Unido. El Gini disponible español (0.327) es de los más altos
de la Europa occidental, lo que sugiere que hay margen para mejorar
la redistribución — especialmente en la cola alta de la distribución,
donde la U invertida reduce la eficacia del sistema.

### 5.5 ¿Qué pasaría si se eliminara la base máxima de cotización?

Es la pregunta natural tras estos dos estudios. Si se destopase la
cotización a la SS (eliminando el techo de 61.214 EUR), el percentil
91-99 y el top 1% verían aumentar significativamente su carga por SS.
Una estimación aproximada:

- **P91-99** (renta media 143.053 EUR): la SS empresa pasaría del
  13.9% al ~22-24% → la carga neta subiría de -23.6% a ~-33%.
- **Top 1%** (renta media 465.466 EUR): la SS empresa pasaría del
  4.1% al ~22-24% → la carga neta subiría de -18.1% a ~-38%.

Esto eliminaría la U invertida y haría el sistema genuinamente
progresivo en toda la distribución. Es lo que ya hacen Suecia
(sin tope) y Francia (tope muy alto). El contraargumento habitual
es que la SS genera derechos y que un destope total desvincularía
cotización y prestación. La cotización de solidaridad (0.92-1.17%
adicional) introducida en 2024 va en esta dirección, pero su
impacto es limitado.

---

## 6. Conclusiones

1. **El 60% de los hogares españoles son receptores netos del Estado.**
   Reciben más en transferencias y servicios públicos de lo que pagan
   en impuestos. El punto de cruce está en torno a los 55.000 EUR de
   renta bruta del hogar.

2. **El sistema es fuertemente redistributivo**: reduce el Gini un 34%,
   de 0.497 a 0.327. Las pensiones y prestaciones (no los impuestos)
   son el principal mecanismo.

3. **La U invertida del Estudio 1 se confirma con datos reales de FEDEA**
   y persiste después de descontar transferencias. El percentil 91-99
   soporta una carga neta del 23.6%, frente al 18.1% del top 1%.

4. **El top 1% paga un IRPF efectivo del 10.5%** — inferior al 16.0%
   del percentil 91-99 — gracias a la composición de su renta (capital
   vs trabajo) y al acceso al IS como vehículo fiscal.

5. **La base máxima de cotización es el mecanismo principal** de la
   U invertida: convierte las cotizaciones en un impuesto regresivo
   por encima de 61.214 EUR. Su eliminación (como en Suecia) haría
   el sistema progresivo en toda la distribución.

6. **Las pensiones de jubilación son la mayor transferencia** en todos
   los tramos, incluido el top 1%. Su carácter contributivo las
   vincula al salario previo, lo que atenúa parcialmente su efecto
   redistributivo.

---

## 7. Limitaciones

1. **Los datos son de 2022** (último año disponible en el 9.º Informe
   FEDEA). Desde entonces se ha introducido la cotización de
   solidaridad (2024) y el tipo máximo de la base del ahorro ha subido
   al 30%.

2. **La clasificación por renta bruta del hogar** (no del individuo)
   dificulta la comparación directa con el Estudio 1, que usaba
   salario individual.

3. **FEDEA imputa la incidencia del IS a los accionistas**, lo que
   es el tratamiento estándar en economía pública pero introduce
   supuestos sobre la traslación.

4. **Las transferencias en especie se valoran al coste**, no al valor
   percibido por el receptor. Un hogar que no utilice la sanidad
   pública porque tiene seguro privado sigue contabilizando el valor
   imputado.

5. **No se incluye la economía sumergida ni la elusión fiscal.** Los
   datos de FEDEA reflejan la renta y los impuestos declarados. Si la
   renta real del top 1% es superior a la declarada, su carga neta
   real sería aún menor.

6. **Las pensiones contributivas** se tratan como transferencia, pero
   tienen un componente de seguro/salario diferido que las diferencia
   de otras prestaciones.

---

## Referencias

- FEDEA, 9.º Informe del Observatorio sobre el Reparto de los Impuestos
  y las Prestaciones entre los Hogares Españoles (febrero 2025). Datos
  de 2022.
  [fedea.net](https://www.fedea.net/observatorio-fiscal/)

- Estudio 1 de esta serie: "Carga fiscal total del asalariado en España:
  un análisis de progresividad."
  [statisticspeek.github.io](/2026/02/09/impuestos-progresivos-espana.html)

- INE, Encuesta de Condiciones de Vida (ECV), 2022.
  [ine.es](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176807&menu=ultiDatos&idp=1254735976608)

- EUROSTAT, Income and Living Conditions (EU-SILC).
  [ec.europa.eu/eurostat](https://ec.europa.eu/eurostat/web/income-and-living-conditions)

- OCDE, Income Distribution Database.
  [oecd.org](https://www.oecd.org/social/income-distribution-database.htm)

- López-Laborda, J., Marín-González, C. y Onrubia, J. (2023).
  "Observatorio sobre el Reparto de los Impuestos y las Prestaciones
  Monetarias entre los Hogares Españoles." Estudios sobre la Economía
  Española, FEDEA.

- Zucman, G. et al. (2019). "Tax Evasion and Inequality." American
  Economic Review, 109(6), pp. 2073-2103.
