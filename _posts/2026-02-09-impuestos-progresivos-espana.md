---
layout: post
title: "Carga fiscal total del asalariado en España: un análisis de progresividad"
date: 2026-02-09
series: impuestos
part: 1
---

*Este es el primer artículo de una [serie](https://statisticspeek.github.io/) sobre fiscalidad en España.
El [segundo artículo](/2026/02/10/transferencias-carga-neta-espana.html)
completa este análisis añadiendo las transferencias del Estado (pensiones,
sanidad, educación, prestaciones sociales) y calcula la carga fiscal neta.*

> **Nota del autor.** Este estudio analiza exclusivamente los impuestos
> pagados, no lo que el ciudadano recibe a cambio. Sin las transferencias
> del Estado, la foto queda incompleta: el sistema fiscal español es
> fuertemente redistributivo y el 60% de los hogares son receptores netos.
> La U invertida que aquí se describe persiste incluso tras las
> transferencias, pero su magnitud se reduce drásticamente. Se recomienda
> leer ambos estudios conjuntamente.

---

## Resumen

El sistema fiscal español se presenta como progresivo gracias a la escala
del IRPF. Sin embargo, el IRPF es solo uno de los tributos que soporta un
asalariado. Este estudio calcula la **carga fiscal total** — IRPF,
cotizaciones a la Seguridad Social (trabajador y empresa), IVA e impuestos
especiales — para cada tramo de renta salarial, utilizando datos del INE
(Encuesta de Presupuestos Familiares, 2024) y de la AEAT (Mercado de
Trabajo en las Fuentes Tributarias, 2023).

Los resultados muestran que, cuando se incluyen las cotizaciones
empresariales a la Seguridad Social — como recomienda la literatura
económica mayoritaria —, la carga fiscal total describe una **U invertida**:
sube hasta un máximo del 67.8% del salario bruto en el tramo de 56.000 EUR
y después **desciende** hasta el 52.6% para salarios de 281.000 EUR. El
mecanismo principal es la base máxima de cotización (61.214 EUR/año), que
convierte las cotizaciones sociales en un tributo fuertemente regresivo por
encima de ese umbral.

**Nota importante.** Este estudio analiza exclusivamente el lado de la
recaudación. No contabiliza las transferencias del Estado (pensiones,
sanidad, educación, prestaciones sociales), que benefician
desproporcionadamente a las rentas bajas y reducen significativamente la
desigualdad. El efecto redistributivo neto del sistema fiscal+gasto es
considerablemente más favorable para las rentas bajas de lo que sugieren
las cifras de carga fiscal bruta aquí presentadas. Cuantificar ese efecto
neto es objeto de un trabajo posterior.

---

## 1. Introducción

### 1.1 Motivación

El debate sobre la progresividad fiscal en España se centra casi
exclusivamente en el IRPF, cuya escala va del 19% al 47%. Sin embargo,
un asalariado no paga solo IRPF: paga cotizaciones a la Seguridad Social
(directamente un 6.5%, e indirectamente hasta un 30.6% a cargo de la
empresa), IVA sobre todo lo que consume, e impuestos especiales sobre
determinados bienes.

Cada uno de estos tributos tiene una estructura diferente:

- El **IRPF** es progresivo: quien más gana, más porcentaje paga.
- Las **cotizaciones sociales** tienen una base máxima (61.214 EUR/año en
  2026), por encima de la cual apenas se cotiza. Esto las hace regresivas
  para rentas altas.
- El **IVA** grava el consumo, no la renta. Como los hogares de renta baja
  gastan una fracción mayor de sus ingresos, el IVA supone un porcentaje
  mayor de su renta.

La pregunta que motiva este estudio es: **cuando se suman todos estos
tributos, ¿es realmente progresivo el sistema fiscal para los asalariados
en España?**

### 1.2 Hipótesis

Los impuestos en España, considerados en su conjunto, no son progresivos
para los asalariados. La progresividad nominal del IRPF no compensa la
regresividad de las cotizaciones sociales y del IVA, especialmente a
partir de rentas medias-altas.

### 1.3 Alcance y limitaciones

Este estudio se limita a **asalariados con contrato** que declaran la
totalidad de sus ingresos. No incluye autónomos, rentas del capital,
impuestos patrimoniales ni transferencias del Estado (véase Sección 5.2).
Se modela el caso de un asalariado soltero sin hijos, que representa
el escenario de máxima carga fiscal. Los resultados se validan contra
datos agregados reales de la AEAT.

---

## 2. Conceptos previos: del coste laboral al bolsillo

Para un asalariado con un salario bruto de 30.000 EUR/año:

```
COSTE LABORAL (lo que paga la empresa)
  = Salario bruto + SS empresa
  = 30.000 + 9.195 (30.65%)
  = 39.195 EUR
       │
       ├── SS empresa: 9.195 EUR ──────────> Seguridad Social
       │   (la empresa lo paga, el trabajador no lo ve)
       │
       ▼
SALARIO BRUTO (lo que aparece en el contrato)
  = 30.000 EUR
       │
       ├── SS trabajador: 1.950 EUR (6.5%) ──> Seguridad Social
       │
       ├── Retención IRPF: ~4.300 EUR ────────> Hacienda
       │
       ▼
SALARIO NETO (lo que llega a la cuenta)
  = 30.000 - 1.950 - 4.300
  = ~23.750 EUR
       │
       ├── IVA: ~2.250 EUR ──────────────────> Hacienda (vía comercios)
       │   (ya incluido en los precios)
       │
       ▼
CAPACIDAD REAL DE COMPRA
  = ~21.500 EUR
```

| Concepto | Cantidad | % del bruto | % del coste laboral |
|---|---|---|---|
| SS empresa | 9.195 | 30.7% | 23.5% |
| SS trabajador | 1.950 | 6.5% | 5.0% |
| IRPF | 4.300 | 14.3% | 11.0% |
| IVA (estimado) | 2.250 | 7.5% | 5.7% |
| **Total** | **17.695** | **59.0%** | **45.1%** |

De los 39.195 EUR que cuesta este trabajador, solo 21.500 se convierten
en capacidad de compra. En este estudio utilizamos el **porcentaje del
salario bruto** como medida principal, por ser la más comprensible, y
mostramos el porcentaje del coste laboral como referencia.

---

## 3. Datos y metodología

### 3.1 Fuentes de datos

| Fuente | Contenido | Periodo |
|---|---|---|
| INE, Tabla 73809 (Encuesta de Presupuestos Familiares) | Gasto medio por hogar en 14 categorías COICOP, cruzado con 8 tramos de ingreso mensual neto | 2024 |
| AEAT, Mercado de Trabajo en las Fuentes Tributarias | Número de asalariados, salario medio, retenciones y tipo medio de retención por tramo salarial (en múltiplos del SMI) | 2023 |
| BOE, tipos de cotización a la Seguridad Social | Tipos de cotización, bases mínima y máxima, cotización de solidaridad | 2026 |

### 3.2 Modelo 1: IVA por nivel de renta

Para cada uno de los 8 tramos de ingreso del INE:

1. Se toma el gasto medio por hogar en cada categoría COICOP.
2. Se asigna a cada categoría su tipo de IVA predominante (4%, 10%, 21%
   o exento), según el mapeo detallado en el Apéndice A.
3. Se calcula el IVA implícito en el gasto:
   `IVA = gasto × tipo_iva / (1 + tipo_iva)`
4. Se divide el IVA total entre la renta del hogar.

La asignación COICOP-IVA es aproximada a nivel de 2 dígitos. Se analiza
la sensibilidad de los resultados a variaciones de +/- 3 puntos en los
tipos asumidos (Sección 4).

### 3.3 Modelo 2: IRPF efectivo

Se calcula el IRPF teórico para un asalariado soltero sin hijos,
aplicando:

- La escala estatal + autonómica vigente
- La reducción por rendimientos del trabajo
- El mínimo personal (5.550 EUR)
- La deducción de cotizaciones SS del trabajador

Los salarios brutos utilizados corresponden a los salarios medios reales
por tramo de la estadística de Mercado de Trabajo de la AEAT (2023),
expresados en múltiplos del SMI (15.120 EUR/año).

### 3.4 Modelo 3: Cotizaciones a la Seguridad Social

Las cotizaciones se calculan con los tipos oficiales de 2026:

| Concepto | Trabajador | Empresa | Total |
|---|---|---|---|
| Contingencias comunes | 4.70% | 23.60% | 28.30% |
| Desempleo (indefinido) | 1.55% | 5.50% | 7.05% |
| Formación profesional | 0.10% | 0.60% | 0.70% |
| MEI | 0.15% | 0.75% | 0.90% |
| FOGASA | — | 0.20% | 0.20% |
| **Total** | **6.50%** | **30.65%** | **37.15%** |

La base máxima de cotización es 61.214 EUR/año. Por encima, solo se
aplica la cotización adicional de solidaridad (entre 0.92% y 1.17%
adicional, según el tramo, en 2026).

Se presentan dos escenarios:
- **Escenario A (visible)**: solo cotización del trabajador (6.5%).
- **Escenario B (económico)**: cotización total (trabajador + empresa).

La inclusión de la cotización empresarial como carga del trabajador es
el tratamiento estándar en economía pública (OCDE, FMI). La evidencia
empírica en reformas de reparto (Suecia 2007, Colombia 2013) muestra que
el 60-100% de la cotización empresarial se traslada a menores salarios
a largo plazo. No obstante, se reconoce que parte de las cotizaciones
genera derechos (pensión, desempleo) y no es un impuesto puro.

### 3.5 Síntesis

Se combinan los tres modelos para cada tramo salarial. Para el IVA, se
interpola a partir de los datos del INE estimando el gasto en función de
la renta neta disponible tras IRPF y SS.

### 3.6 Validación

El modelo de IRPF se valida contra los datos agregados reales de la AEAT:
masa salarial total, retenciones totales y tipo medio de retención.

---

## 4. Resultados

### 4.1 IVA: regresivo como porcentaje de la renta

| Tramo renta (neta mensual hogar) | Renta neta anual | Gasto total | Gasto/Renta | IVA pagado | **IVA % renta** |
|---|---|---|---|---|---|
| Hasta 499 EUR | 4.200 | 14.973 | 356% | 1.339 | **31.9%** |
| 500 - 999 EUR | 9.000 | 16.615 | 185% | 1.491 | **16.6%** |
| 1.000 - 1.499 EUR | 15.000 | 21.956 | 146% | 2.049 | **13.7%** |
| 1.500 - 1.999 EUR | 21.000 | 26.459 | 126% | 2.501 | **11.9%** |
| 2.000 - 2.499 EUR | 27.000 | 33.210 | 123% | 3.194 | **11.8%** |
| 2.500 - 2.999 EUR | 33.000 | 37.716 | 114% | 3.681 | **11.2%** |
| 3.000 - 4.999 EUR | 48.000 | 44.518 | 93% | 4.369 | **9.1%** |
| 5.000+ EUR | 84.000 | 64.823 | 77% | 6.326 | **7.5%** |

El IVA supone un 31.9% de la renta del tramo más bajo frente a un 7.5%
del más alto: un ratio de 4:1. Sin embargo, el tipo efectivo de IVA
sobre el gasto (IVA/gasto) es prácticamente plano (~9% en todos los
tramos). Esto indica que **la regresividad no proviene de que los pobres
consuman productos con más IVA, sino de que gastan una fracción mucho
mayor de su renta**. Los tipos reducidos en alimentación no compensan
este efecto.

El tramo más bajo (hasta 499 EUR/mes) muestra un gasto de 3.5 veces su
renta declarada, lo que sugiere fuentes de ingreso no contabilizadas
(economía sumergida, ayudas familiares, desahorro). Aun duplicando su
renta estimada, el IVA seguiría siendo el 16% — el doble que para el
tramo alto.

### 4.2 IRPF: progresivo

| Tramo | Salario bruto | SS trabajador | Base liquidable | Cuota IRPF | **Tipo efectivo** |
|---|---|---|---|---|---|
| 0-0.5 SMI | 3.239 | 211 | 0 | 0 | **0.0%** |
| 0.5-1 SMI | 11.549 | 751 | 3.496 | 0 | **0.0%** |
| 1-1.5 SMI | 18.718 | 1.217 | 14.836 | 1.884 | **10.1%** |
| 1.5-2 SMI | 26.101 | 1.697 | 22.040 | 3.723 | **14.3%** |
| 2-2.5 SMI | 33.858 | 2.201 | 29.293 | 5.899 | **17.4%** |
| 2.5-3 SMI | 41.256 | 2.682 | 36.210 | 8.045 | **19.5%** |
| 3-3.5 SMI | 48.769 | 3.170 | 43.235 | 10.644 | **21.8%** |
| 3.5-4 SMI | 56.388 | 3.665 | 50.359 | 13.280 | **23.6%** |
| 4-4.5 SMI | 64.037 | 3.979 | 57.694 | 15.994 | **25.0%** |
| 4.5-5 SMI | 71.586 | 3.979 | 65.243 | 19.206 | **26.8%** |
| 5-7.5 SMI | 89.452 | 3.979 | 83.109 | 27.246 | **30.5%** |
| 7.5-10 SMI | 128.465 | 3.979 | 122.122 | 44.802 | **34.9%** |
| 10+ SMI | 280.847 | 3.979 | 274.504 | 113.374 | **40.4%** |

El IRPF es genuinamente progresivo: del 0% al 40.4%. Los primeros
~12.000 EUR no pagan IRPF gracias a la reducción por rendimientos del
trabajo y el mínimo personal. Estos son tipos máximos (soltero sin hijos);
las deducciones familiares y autonómicas los reducen en la práctica.

### 4.3 Seguridad Social: regresiva por encima de la base máxima

**Cotización del trabajador:**

| Tramo | Salario bruto | SS trabajador | **SS % salario** |
|---|---|---|---|
| 0-0.5 a 3.5-4 SMI | 3.239 - 56.388 | 211 - 3.665 | **6.50%** |
| 4-4.5 SMI | 64.037 | 3.984 | **6.22%** |
| 5-7.5 SMI | 89.452 | 4.037 | **4.51%** |
| 7.5-10 SMI | 128.465 | 4.130 | **3.21%** |
| 10+ SMI | 280.847 | 4.496 | **1.60%** |

**Cotización total (trabajador + empresa):**

| Tramo | Salario bruto | SS total | **SS % bruto** |
|---|---|---|---|
| Hasta 3.5-4 SMI | hasta 56.388 | hasta 20.948 | **37.15%** |
| 5-7.5 SMI | 89.452 | 23.088 | **25.81%** |
| 7.5-10 SMI | 128.465 | 23.653 | **18.41%** |
| 10+ SMI | 280.847 | 25.877 | **9.21%** |

Las cotizaciones son el tributo más regresivo del sistema. Medidas como
porcentaje del salario bruto, **solo en concepto de SS**: un asalariado
de 56.000 EUR paga un 37.15%; uno de 280.000 EUR, un 9.21%. Ratio 4:1.
La cotización adicional de solidaridad apenas compensa: añade solo ~0.4
puntos para un salario de 280.000 EUR.

### 4.4 Carga fiscal total: la U invertida

#### Escenario A: carga visible (IRPF + SS trabajador + IVA)

| Tramo | Bruto | IRPF % | SS trab. % | IVA % | **TOTAL %** |
|---|---|---|---|---|---|
| 0-0.5 SMI | 3.239 | 0.0 | 6.5 | 41.3 | **47.8** |
| 0.5-1 SMI | 11.549 | 0.0 | 6.5 | 14.4 | **20.9** |
| 1-1.5 SMI | 18.718 | 10.1 | 6.5 | 11.2 | **27.8** |
| 1.5-2 SMI | 26.101 | 14.3 | 6.5 | 9.5 | **30.3** |
| 2-2.5 SMI | 33.858 | 17.4 | 6.5 | 9.0 | **32.9** |
| 2.5-3 SMI | 41.256 | 19.5 | 6.5 | 8.4 | **34.4** |
| 3-3.5 SMI | 48.769 | 21.8 | 6.5 | 7.7 | **36.1** |
| 3.5-4 SMI | 56.388 | 23.6 | 6.5 | 7.1 | **37.1** |
| 4-4.5 SMI | 64.037 | 25.0 | 6.2 | 6.5 | **37.7** |
| 4.5-5 SMI | 71.586 | 26.8 | 5.6 | 6.1 | **38.5** |
| 5-7.5 SMI | 89.452 | 30.5 | 4.5 | 5.5 | **40.5** |
| 7.5-10 SMI | 128.465 | 34.9 | 3.2 | 4.7 | **42.8** |
| 10+ SMI | 280.847 | 40.4 | 1.6 | 3.0 | **45.0** |

El escenario A muestra progresividad, pero muy débil: del 20.9% al 45.0%
(ratio 2:1). La curva se aplana a partir de los 50.000 EUR.

#### Escenario B: carga económica total (IRPF + SS total + IVA)

| Tramo | Bruto | Coste laboral | IRPF % | SS total % | IVA % | **TOTAL % bruto** | **TOTAL % coste** |
|---|---|---|---|---|---|---|---|
| 0-0.5 SMI | 3.239 | 4.232 | 0.0 | 37.2 | 41.3 | **78.5** | **60.1** |
| 0.5-1 SMI | 11.549 | 15.089 | 0.0 | 37.2 | 14.4 | **51.5** | **39.4** |
| 1-1.5 SMI | 18.718 | 24.455 | 10.1 | 37.2 | 11.2 | **58.4** | **44.7** |
| 1.5-2 SMI | 26.101 | 34.101 | 14.3 | 37.2 | 9.5 | **60.9** | **46.6** |
| 2-2.5 SMI | 33.858 | 44.235 | 17.4 | 37.2 | 9.0 | **63.6** | **48.7** |
| 2.5-3 SMI | 41.256 | 53.901 | 19.5 | 37.2 | 8.4 | **65.1** | **49.8** |
| 3-3.5 SMI | 48.769 | 63.717 | 21.8 | 37.2 | 7.7 | **66.7** | **51.1** |
| 3.5-4 SMI | 56.388 | 73.671 | 23.6 | 37.2 | 7.1 | **67.8** | **51.9** |
| 4-4.5 SMI | 64.037 | 82.826 | 25.0 | 35.6 | 6.5 | **67.1** | **51.9** |
| 4.5-5 SMI | 71.586 | 90.451 | 26.8 | 31.9 | 6.1 | **64.9** | **51.4** |
| 5-7.5 SMI | 89.452 | 108.503 | 30.5 | 25.8 | 5.5 | **61.8** | **50.9** |
| 7.5-10 SMI | 128.465 | 147.988 | 34.9 | 18.4 | 4.7 | **58.0** | **50.4** |
| 10+ SMI | 280.847 | 302.229 | 40.4 | 9.2 | 3.0 | **52.6** | **48.9** |

En el escenario B, la carga fiscal describe una U invertida:

- Sube hasta un **máximo del 67.8%** en el tramo de 56.388 EUR.
- A partir de ahí, **desciende**: 64.9% para 71k, 61.8% para 89k,
  58.0% para 128k, y **52.6% para 281k**.
- **El asalariado que gana 56.000 EUR paga proporcionalmente más que
  el que gana 280.000 EUR** (67.8% vs 52.6%).

**Nota importante:** como porcentaje del coste laboral, la carga *total*
(IRPF + SS + IVA) es sorprendentemente plana (48-52%) para todos los
tramos medios-altos. Esto no contradice la regresividad de la SS: lo que
ocurre es que el IRPF sube (+17pp de 56k a 281k) mientras la SS baja
(-28pp), y se compensan parcialmente. Además, el denominador aquí es el
coste laboral (bruto + SS empresa), que es mayor que el salario bruto.

![Carga fiscal total: la U invertida](/assets/images/impuestos/u_invertida.png)

### 4.5 Las tres fuerzas en tensión

```
IRPF (progresivo)       ↑  del 0% al 40%      — sube siempre
SS   (regresivo)        ↓  del 37% al 9%       — cae a partir de 61k
IVA  (regresivo)        ↓  del 32% al 7%       — cae suavemente
```

La Seguridad Social es la fuerza dominante. La base máxima de cotización
(61.214 EUR/año) crea un corte abrupto: por debajo, la SS total supone
el 37.15% del salario; por encima, la tasa efectiva se desploma. El IRPF
sube, pero no lo suficiente para compensar la caída combinada de SS e IVA.

![Tres componentes de la carga fiscal](/assets/images/impuestos/componentes.png)

![Escenario A: carga visible](/assets/images/impuestos/escenario_a_visible.png)

![Escenario B: carga total](/assets/images/impuestos/escenario_b_total.png)

![Comparación de ambos escenarios](/assets/images/impuestos/comparacion_escenarios.png)

---

## 5. Análisis de sensibilidad

Los resultados se someten a cuatro pruebas de sensibilidad.

**Test 1: variación de +/- 3 puntos en los tipos de IVA estimados.** La
carga total varía entre 2 y 7 puntos según el tramo, pero la forma de la
curva no cambia. El tramo bajo es el más sensible (más gasto = más IVA).

**Test 2: IVA de vivienda (la mayor incertidumbre).** La categoría
"Vivienda, agua, electricidad, gas" mezcla gasto exento (alquiler) con
gasto gravado (energía). Se prueban tipos efectivos del 3%, 8% y 12%.
El impacto es de 1 a 5 puntos según el tramo. No altera las conclusiones.

**Test 3: inclusión de la SS empresarial.** Este es el factor decisivo:

| Tramo | Solo IRPF+IVA | +SS trabajador | +SS total | Diferencia SS emp. |
|---|---|---|---|---|
| 1-1.5 SMI (19k) | 21.3% | 27.8% | 58.4% | +30.6pp |
| 3.5-4 SMI (56k) | 30.6% | 37.1% | 67.8% | +30.6pp |
| 10+ SMI (281k) | 43.4% | 45.0% | 52.6% | +7.6pp |

La SS empresarial añade 30.6 puntos a un trabajador de 56.000 EUR, pero
solo 7.6 al de 281.000 EUR. Es la principal fuente de regresividad.

**Test 4: ¿se mantiene la U invertida en todos los escenarios?**

| Escenario | Pico | A 281k | ¿U invertida? |
|---|---|---|---|
| Peor caso (IVA bajo, sin SS emp.) | 44.3% a 281k | 44.3% | **No** — creciente/plana |
| Base (con SS emp.) | 67.8% a 56k | 52.6% | **Sí** — cae 15.2pp |
| Mejor caso (IVA alto, con SS emp.) | 69.3% a 56k | 53.3% | **Sí** — cae 16.0pp |

**La U invertida depende de incluir la SS empresarial.** Sin ella, el
sistema es progresivo pero muy aplanado (del 17% al 44%). Con ella — que
es lo correcto económicamente —, la carga máxima está en 56.000 EUR y
baja 15 puntos para los salarios más altos.

![Sensibilidad de la U invertida](/assets/images/impuestos/sensibilidad_u_invertida.png)

---

## 6. Validación con datos reales

El modelo de IRPF se valida contra la estadística "Mercado de Trabajo en
las Fuentes Tributarias" de la AEAT (2023).

### 6.1 Datos agregados

- **20.098.799** asalariados
- **481.981M EUR** en salarios
- **79.914M EUR** en retenciones
- Tipo medio de retención (asalariados puros): **17.30%**
- Tipo medio de retención (todos los asalariados): **16.58%**

### 6.2 Modelo vs. realidad

| Concepto | Modelo | AEAT real | Ratio |
|---|---|---|---|
| IRPF total (miles de millones EUR) | 83.4 | 79.9 | 1.04 |
| Tipo medio ponderado | **17.29%** | **16.58-17.30%** | ~1.0 |
| Salarios (miles de millones EUR) | 482.0 | 482.0 | 1.00 |

El modelo predice un tipo medio del 17.29%, prácticamente idéntico al
17.30% de los asalariados puros. La sobreestimación del 4% en recaudación
se explica por las deducciones que no incluimos (hijos, vivienda, planes
de pensiones, autonómicas), cuyo impacto estimado es de -1.2 a -3.1
puntos porcentuales.

### 6.3 Distribución de la carga

| Tramo | Asalariados | % total | IRPF/persona | Tipo efectivo | % recaudación |
|---|---|---|---|---|---|
| 0-0.5 SMI | 3.858.491 | 19.2% | 0 | **0.0%** | 0.0% |
| 0.5-1 SMI | 3.552.234 | 17.7% | 0 | **0.0%** | 0.0% |
| 1-1.5 SMI | 4.646.097 | 23.1% | 1.884 | **10.1%** | 10.5% |
| 1.5-2 SMI | 2.878.080 | 14.3% | 3.723 | **14.3%** | 12.9% |
| 2-2.5 SMI | 1.703.923 | 8.5% | 5.899 | **17.4%** | 12.1% |
| 2.5-3 SMI | 1.287.300 | 6.4% | 8.045 | **19.5%** | 12.4% |
| 3-3.5 SMI | 765.569 | 3.8% | 10.644 | **21.8%** | 9.8% |
| 3.5-4 SMI | 419.551 | 2.1% | 13.280 | **23.6%** | 6.7% |
| 4-4.5 SMI | 274.064 | 1.4% | 15.994 | **25.0%** | 5.3% |
| 4.5-5 SMI | 187.519 | 0.9% | 19.206 | **26.8%** | 4.3% |
| 5-7.5 SMI | 375.427 | 1.9% | 27.246 | **30.5%** | 12.3% |
| 7.5-10 SMI | 80.463 | 0.4% | 44.802 | **34.9%** | 4.3% |
| 10+ SMI | 70.081 | 0.3% | 113.374 | **40.4%** | 9.5% |

**7.4 millones de trabajadores (37%) no pagan IRPF.** Para ellos, la carga
fiscal entera proviene de la SS y del IVA. Esto refuerza la observación
de regresividad: para más de un tercio de los asalariados, el único
impuesto progresivo del sistema es irrelevante.

![Validación: modelo vs. AEAT](/assets/images/impuestos/validacion_irpf.png)

---

## 7. Discusión

### 7.1 Elusión y evasión fiscal en rentas altas

Todo lo anterior asume que los asalariados de renta alta declaran y pagan
lo que les corresponde. Sin embargo, las rentas muy altas disponen de
mecanismos que reducen su carga real:

**Sociedades interpuestas.** En vez de cobrar como asalariado (IRPF hasta
47%), el alto directivo puede canalizar ingresos a través de una SL (IS
al 25%, a menudo efectivo del 5-9% en grandes empresas). La ruta
IS + dividendo da un tipo combinado del 39-44%, pero la ventaja real
es el diferimiento indefinido al 25%.

**Dualidad rentas del trabajo / rentas del capital.** La base del ahorro
tributa al 19-28% (30% desde 2025), frente al 47% máximo de rentas del
trabajo. Para el percentil más alto, el 63% de sus ingresos son rentas
del capital.

**Datos de FEDEA.** El 10.º Informe del Observatorio sobre el Reparto de
los Impuestos y las Prestaciones entre los Hogares Españoles (febrero 2025)
calcula el tipo efectivo real por nivel de renta:

| Grupo de renta | Tipo efectivo total |
|---|---|
| 20% más pobre | ~27.5% |
| Renta media (Q3) | ~33% |
| Percentil 91-99 | ~38% (máximo) |
| **Top 1%** | **~24%** |

Según estos datos, **el 1% más rico paga un tipo efectivo inferior al del
20% más pobre**.

**Economía sumergida.** Estimada en el 15.8-24% del PIB. Según el
sindicato de técnicos de Hacienda (Gestha), el fraude fiscal anual asciende
a 91.600 millones EUR, de los cuales el 72% es atribuible a grandes
empresas y grandes fortunas.

### 7.2 Lo que falta: las transferencias del Estado

**Este es el punto crítico que limita el alcance de nuestras conclusiones.**

El sistema fiscal no es solo recaudación: el Estado devuelve una parte
sustancial en forma de transferencias y servicios públicos que benefician
desproporcionadamente a las rentas bajas:

- **Pensiones** (~170.000M EUR/año): la mayor partida del presupuesto.
  Las pensiones mínimas y no contributivas son redistributivas.
- **Sanidad pública** (~90.000M EUR): uso universal, pero proporcionalmente
  más valioso para quien no podría pagar sanidad privada.
- **Educación pública** (~55.000M EUR): ídem.
- **Prestaciones por desempleo** (~22.000M EUR): concentradas en rentas
  bajas y medias.
- **Ingreso Mínimo Vital, rentas mínimas autonómicas, becas, ayudas a
  vivienda, dependencia, prestaciones por hijo.**

Según el INE (Encuesta de Condiciones de Vida) y el modelo EUROMOD, el
coeficiente de Gini en España pasa de ~0.50 (renta de mercado) a ~0.33
(renta disponible tras impuestos y transferencias). **Las transferencias
reducen la desigualdad más que los propios impuestos.**

Esto no invalida los hallazgos del presente estudio — la estructura de
la recaudación sigue teniendo la forma de U invertida —, pero significa
que el efecto neto del sistema fiscal + gasto público es
**significativamente más redistributivo** de lo que sugiere mirar solo los
impuestos. Para una evaluación completa habría que calcular, para cada
tramo de renta:

```
Carga neta = Impuestos pagados - Transferencias recibidas - Valor de servicios públicos utilizados
```

Este cálculo es el próximo paso natural de este trabajo.

### 7.3 La paradoja del asalariado

El resultado más llamativo es que **el asalariado de 56.000 EUR paga
proporcionalmente más impuestos que el de 280.000 EUR** (67.8% vs 52.6%).
Esto no es un defecto del IRPF, sino un defecto estructural del sistema,
causado por:

1. **El tope de cotización a la SS**, que convierte una carga plana del
   37% en una carga fuertemente regresiva por encima de 61.000 EUR.
2. **La regresividad del IVA**, que afecta más a quien gasta más de su
   renta.
3. **La dualidad rentas del trabajo / rentas del capital**, que permite
   a las rentas muy altas tributar a tipos inferiores.
4. **La elusión fiscal**, facilitada por sociedades interpuestas y la
   arquitectura del IS + dividendo.

---

## 8. Conclusiones

1. **El IRPF es progresivo** (del 0% al 40.4%), pero es solo una pieza
   del sistema.

2. **Las cotizaciones a la Seguridad Social son el tributo más regresivo**
   del sistema. La base máxima de cotización (61.214 EUR/año) hace que,
   medido solo en concepto de SS como porcentaje del salario bruto, un
   asalariado de 56.000 EUR pague un 37.15% frente al 9.21% de uno de
   280.000 EUR. Sin embargo, cuando se suman todos los impuestos (IRPF +
   SS + IVA), la carga total sobre el coste laboral queda en el rango
   48-52% para los tramos medios-altos, porque el IRPF compensa
   parcialmente la caída de la SS.

3. **El IVA es regresivo como porcentaje de la renta**, con un ratio de
   4:1 entre el tramo más bajo y el más alto. Los tipos reducidos no
   compensan este efecto.

4. **La carga fiscal total (incluyendo SS empresarial) describe una U
   invertida**: sube hasta un máximo del 67.8% en los 56.000 EUR y
   desciende al 52.6% en los 280.000 EUR. Este resultado es robusto bajo
   distintos supuestos de IVA, pero depende de incluir la cotización
   empresarial.

5. **Sin cotización empresarial**, el sistema es progresivo pero muy
   aplanado (ratio 2:1).

6. **El 37% de los asalariados (7.4 millones) no pagan IRPF.** Para
   ellos, la carga fiscal proviene exclusivamente de tributos regresivos
   (SS e IVA).

7. **Las transferencias del Estado no están incluidas** en este análisis.
   Su inclusión reduciría sustancialmente la regresividad aparente,
   especialmente para las rentas bajas. El coeficiente de Gini pasa de
   ~0.50 a ~0.33 gracias a impuestos y transferencias conjuntamente.

---

## 9. Limitaciones y trabajo futuro

1. **No se contabilizan las transferencias del Estado** (pensiones,
   sanidad, educación, prestaciones). Este es el trabajo pendiente más
   importante.

2. Los tramos de renta del INE (ingreso neto del hogar) y de la AEAT
   (salario individual en múltiplos del SMI) no coinciden. La
   armonización requiere supuestos sobre la composición del hogar.

3. El mapeo COICOP a tipos de IVA es aproximado a nivel de 2 dígitos.

4. El modelo asume un asalariado soltero sin hijos (caso de máxima carga).

5. No se incluyen: Impuesto de Patrimonio, IBI, impuestos especiales,
   tasas municipales. Su inclusión reforzaría la regresividad en
   algunos tramos.

6. No se modela la elusión fiscal cuantitativamente; los datos de FEDEA
   se citan como referencia externa.

**Trabajo futuro previsto en esta serie:**
- **impuestos_2**: Tributación de las rentas del capital en España.
- **impuestos_3**: Tributación corporativa en jurisdicciones de baja
  fiscalidad (Irlanda, Luxemburgo, Países Bajos).
- **impuestos_4**: Comparativa de carga fiscal con países europeos de
  tamaño comparable (Francia, Italia, Alemania, Reino Unido).

---

## Apéndice A: Mapeo COICOP a tipos de IVA

| Cód. | Categoría COICOP | IVA estimado | Notas |
|------|-----------------|-------------|-------|
| 01 | Alimentos y bebidas no alcohólicas | ~7% (mix 4%/10%) | Básicos al 4%, procesados al 10% |
| 02 | Bebidas alcohólicas, tabaco | 21% + especiales | Impuestos especiales adicionales |
| 03 | Vestido y calzado | 21% | |
| 04 | Vivienda, agua, electricidad, gas | ~8% (mix) | Alquiler exento, energía 10-21%, agua 10% |
| 05 | Muebles, artículos del hogar | 21% | |
| 06 | Sanidad | ~5% (mix) | Pública exenta, fármacos 4%, privada 21% |
| 07 | Transporte | ~18% (mix) | Coches/gasolina 21%, público 10% |
| 08 | Comunicaciones | 21% | |
| 09 | Ocio y cultura | ~15% (mix) | Libros 4%, espectáculos 10-21% |
| 10 | Educación | 0% (exento) | |
| 11 | Restaurantes y hoteles | 10% | |
| 12 | Seguros y servicios financieros | 0% (exento) | |
| 13 | Cuidado personal y otros | ~18% (mix) | |

---

## Referencias

- INE, Encuesta de Presupuestos Familiares, Tabla 73809 (2024).
  [ine.es/jaxiT3/Tabla.htm?t=73809](https://www.ine.es/jaxiT3/Tabla.htm?t=73809)
- AEAT, Mercado de Trabajo y Pensiones en las Fuentes Tributarias (2023).
  [sede.agenciatributaria.gob.es](https://sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/mercado/2023/)
- AEAT, Informe Anual de Recaudación Tributaria, ejercicio 2023.
  [sede.agenciatributaria.gob.es](https://sede.agenciatributaria.gob.es/Sede/estadisticas/recaudacion-tributaria/informe-anual/ejercicio-2023/2-impuesto-sobre-renta-personas-fisicas.html)
- FEDEA, 10.º Informe del Observatorio sobre el Reparto de los Impuestos
  y las Prestaciones entre los Hogares Españoles (febrero 2025).
- Gestha, Sindicato de Técnicos del Ministerio de Hacienda. Estimaciones
  de fraude fiscal.
- Zucman, G., et al. (2019). "Tax Evasion and Inequality." American
  Economic Review, 109(6), pp. 2073-2103.
- OCDE, Taxing Wages (series anual). Metodología de cuña fiscal.
- Gruber, J. (1997). "The Incidence of Payroll Taxation: Evidence from
  Chile." Journal of Labor Economics, 15(S3), pp. 72-101.
