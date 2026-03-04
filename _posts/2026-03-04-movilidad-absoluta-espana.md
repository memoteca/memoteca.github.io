---
layout: post
title: "¿Se desvanece el sueño español? Movilidad absoluta de renta en España, 1973–1996"
date: 2026-03-04
series: movilidad
part: 1
---

*Este es el primer artículo de una serie sobre movilidad intergeneracional
en España. Replica la metodología de Chetty et al. (2017) —"The Fading
American Dream"— con datos españoles (ECV + EPF/ECPF históricas).*

> **Hallazgo central.** La respuesta depende críticamente de la edad a la
> que se mida la renta. A los ~30 años, la movilidad cae 43 puntos
> porcentuales en 9 cohortes. A los ~40, el rango total es de apenas 9 pp.
> La divergencia cuantifica la precariedad del mercado laboral juvenil
> español, no un colapso estructural de la movilidad intergeneracional.

---

## Resumen

¿Qué fracción de los españoles nacidos entre 1973 y 1996 ganan más que sus padres a la misma edad? Este trabajo replica la metodología de Chetty et al. (2017) —"The Fading American Dream"— para España, combinando 20 olas de la Encuesta de Condiciones de Vida (ECV, 2006–2025) con las Encuestas de Presupuestos Familiares históricas (EPF 1980–81 y 1990–91) y las Encuestas Continuas de Presupuestos Familiares trimestrales (ECPF Base 85, 1985–1997; ECPF Base 97, 1998–2001).

Estimamos la movilidad absoluta de renta para 24 cohortes de nacimiento (1973–1996) utilizando tres métodos de cópula (rank-preserving, Gaussian con ρ=0,34, e independencia). El hallazgo central es que **la respuesta depende críticamente de a qué edad se mida la renta**:

- **A edad ~30** (replicando a Chetty), la movilidad per-earner cae desde un 75% (cohorte 1975) hasta un 32% (cohorte 1984) — una caída de 43 pp concentrada en las cohortes que cumplieron 30 años durante la Gran Recesión.
- **A edad ~40**, con datos parentales íntegramente observados y renta consolidada, la caída se comprime a apenas **9 pp** (rango 39%–48%). Con **renta del hogar** — la medida estándar en comparaciones internacionales (Manduca et al. 2024) — la movilidad a edad 40 es del **72%–79%** para todas las cohortes, comparable a los países europeos más móviles.

Esta divergencia revela que una parte sustancial de la caída medida a los 30 refleja la precariedad del mercado laboral juvenil español — temporalidad, emancipación tardía, vulnerabilidad cíclica — más que un deterioro estructural de la movilidad intergeneracional. Un perfil de movilidad a 8 edades (28–42) indica que la renta se estabiliza a una mediana de 36 años en España, frente a los 30 que usa Chetty para EEUU.

La descomposición en crecimiento vs. desigualdad revela que, a diferencia de EEUU (donde la desigualdad domina), en España el **menor crecimiento de la renta media es el motor principal** de la caída (24%), mientras que la desigualdad explica solo un 8%. Las cotas formales LP sobre la cópula son amplias (23–71 pp), demostrando que — a diferencia del caso americano — la cópula **sí importa** con datos de encuesta. La suite de sensibilidad (deflactores, renta neta, ajuste por tamaño familiar, variación de ρ) confirma la robustez cualitativa del patrón.

Las dos lecturas — caída dramática a los 30, estabilidad a los 40 — son compatibles y cuentan historias complementarias. Pero la ambigüedad entre ambas no puede resolverse con datos de encuesta: la confirmación definitiva requiere datos fiscales longitudinales (AEAT/IEF) que permitan medir la renta permanente, observar la cópula directamente y desagregar por CCAA.

---

## 1. Introducción

Chetty, Grusky, Hell, Hendren, Manduca y Naidu (2017) documentaron un hallazgo inquietante: la probabilidad de que un estadounidense ganara más que sus padres a la misma edad cayó del 92% para los nacidos en 1940 al 50% para los nacidos en 1984. Este declive de la movilidad absoluta de renta se explica más por el aumento de la desigualdad que por la desaceleración del crecimiento económico.

¿Ocurre algo similar en España? La economía española experimentó una transformación extraordinaria entre 1960 y 2000: renta per cápita multiplicada por cinco, integración europea, expansión del estado del bienestar. Pero también ha sufrido crisis severas —la reconversión industrial de los 80, la burbuja inmobiliaria y su colapso en 2008, la pandemia de 2020— que han golpeado de forma desproporcionada a los jóvenes.

Este trabajo estima la movilidad absoluta de renta en España siguiendo la metodología de Chetty et al. (2017), que descompone la movilidad en tres ingredientes: la distribución de renta de los hijos, la distribución de renta de los padres y la cópula que las relaciona. Para los hijos, utilizamos 20 olas de la ECV (2006–2025); para los padres, las EPF quinquenales (1980–81 y 1990–91) y las ECPF trimestrales Base 85 (1985–1997) y Base 97 (1998–2001), lo que proporciona cobertura anual de las distribuciones parentales para los años de renta 1978–2001. Para la cópula, asumimos una cópula estable calibrada con la correlación rank-rank intergeneracional ρ=0,34 de Chetty et al., y computamos además cotas de robustez (rank-preserving e independencia).

Los resultados documentan una caída profunda de la movilidad absoluta en España, con un patrón diferenciado del declive suave americano: una caída abrupta asociada a la Gran Recesión, una brecha de género que se ha cerrado dramáticamente entre generaciones, y un nivel general que, incluso en su punto más alto, probablemente no alcanzó los máximos estadounidenses de la postguerra.

---

## 2. Datos

### 2.1. Encuesta de Condiciones de Vida (ECV), 2006–2025

La ECV es la versión española de la EU-SILC (European Union Statistics on Income and Living Conditions) y la realiza el INE con periodicidad anual. Proporciona microdatos representativos de la población residente en España con información detallada sobre renta personal, condiciones de vida y características sociodemográficas.

Utilizamos los ficheros de microdatos transversales de personas (fichero P) de las 20 olas disponibles (2006–2025). De cada individuo empleamos:

| Variable | Descripción |
|----------|-------------|
| PB010 | Año de encuesta |
| PB140 | Año de nacimiento |
| PB150 | Sexo (1 = hombre, 2 = mujer) |
| PB040 | Factor de elevación personal (peso muestral) |
| PY010G | Renta bruta del trabajo por cuenta ajena |
| PY020G | Renta bruta del trabajo por cuenta propia |

La renta de la ECV es referida al año anterior al de la encuesta (p. ej., la ECV 2025 recoge renta de 2024). Las olas 2004 y 2005 se excluyen por no disponer de las variables de renta bruta (PY\*G).

### 2.2. Encuestas de Presupuestos Familiares (EPF)

Para la distribución de renta de los padres utilizamos las dos encuestas estructurales de presupuestos familiares del INE con microdatos de ingresos individuales por miembro del hogar:

- **EPF 1980–81**: formato fixed-width, un registro por hogar con datos de hasta 20 miembros y hasta 4 perceptores de ingresos. 23.972 hogares, 88.543 registros de miembros. Año de referencia de renta: 1980. Filtrados a edad 28–32: 4.943 individuos (cohortes parentales 1948–1952).
- **EPF 1990–91**: formato fixed-width (fichero TIPREG3), un registro por miembro del hogar. 72.123 registros totales. Año de referencia de renta: 1990. Filtrados a edad 28–32: 4.858 individuos (cohortes parentales 1958–1962).

Ambas encuestas registran importes en pesetas. Se aplica la conversión 1 € = 166,386 ptas y posteriormente se deflacta con IPC a euros constantes de 2025.

La variable de renta laboral individual se construye como la suma de ingresos por cuenta ajena e ingresos por cuenta propia (netos de gastos deducibles en la EPF 90-91), de forma análoga a la definición PY010G + PY020G empleada para los hijos. En la EPF 80-81, los miembros del hogar que no aparecen en el cuadro de perceptores se incluyen con renta laboral cero, para mantener la consistencia con la EPF 90-91 y la ECV (que registran todos los miembros independientemente de su situación laboral).

### 2.3. Encuestas Continuas de Presupuestos Familiares (ECPF)

Para cubrir las distribuciones parentales de los años intermedios (1985–2001) se utilizan las ECPF trimestrales del INE:

- **ECPF Base 85** (1985–1997): registros fixed-width a nivel de hogar. Dos layouts: 4.939 bytes/registro para 1985–87 y 4.945 bytes para 1988–97 (diferencia de 6 bytes por ampliación de campos de vivienda). Se extraen: edad y sexo del sustentador principal, factor de elevación y corrector seccional, número de perceptores de ingresos (NPerc), y rentas del trabajo (códigos 01=empleo, 02=autoempleo) del bloque de 11 fuentes de ingreso. Las rentas se almacenan "elevadas" (×factor×corrector); la renta por hogar trimestral se obtiene dividiendo por el peso. Se agrupan 4 trimestres por año de renta.
- **ECPF Base 97** (1998–2001): registros de 216 bytes/hogar. Importes mensuales en euros (incluso para datos pre-2002). Se filtran hogares cuya fuente principal de renta es el trabajo (FUENTEIN=1,2). Cuando el importe exacto no se conoce, se usa el punto medio del intervalo declarado (INTERVIN). El factor de elevación tiene 6 decimales implícitos.

Ambas ECPF ofrecen **renta a nivel de hogar**, no individual. Este desajuste con la renta individual de los hijos (ECV) es el principal reto metodológico del estudio y se aborda en la Sección 5.

Para cada ECPF, se seleccionan hogares cuyo sustentador principal tiene 28–32 años. Se recodifica sexo (6=mujer→2) y se deflacta con IPC a euros constantes de 2025.

### 2.4. Índice de Precios al Consumo (IPC)

Todas las rentas se deflactan a euros constantes de 2025 utilizando una serie enlazada del IPC general construida a partir de dos fuentes del INE:

- Tabla 268 (base 1992): medias anuales 1961–2001.
- Tabla 24077 (serie enlazada): medias anuales 2002–2026.

La serie resultante cubre 1961–2026 con base 2025 = 100.

---

## 3. Metodología

### 3.1. Variable de renta y ventana de edad

Definimos la renta laboral bruta individual como la suma de ingresos por cuenta ajena e ingresos por cuenta propia (netos de gastos deducibles cuando el dato está disponible). En la ECV esto corresponde a PY010G + PY020G; en las EPF, a los campos equivalentes de empleo y autoempleo del cuadro de ingresos individuales. Los valores nulos se tratan como cero. Se incluyen los individuos con renta cero (desempleados, inactivos) para no sesgar la distribución al alza.

Tanto para hijos como para padres seleccionamos las personas de 28 a 32 años (ventana centrada en 30). Para los hijos, cada ola de la ECV del año *s* recoge renta del año *s* − 1; un individuo nacido en el año *c* se observa en la ECV del año *c* + 29 a *c* + 33, y cada cohorte se observa hasta en 5 olas cuyas observaciones se agrupan. Para los padres, la EPF 80-81 recoge renta de 1980 y la EPF 90-91 renta de 1990, cada una en una única ola.

Los importes de las EPF, expresados en pesetas, se convierten a euros con el tipo de cambio oficial (1 € = 166,386 ptas) y se deflactan a euros constantes de 2025 con la misma serie de IPC enlazado utilizada para los hijos.

### 3.2. Percentiles ponderados

Los percentiles se calculan con un método de CDF de punto medio (*midpoint CDF*) con interpolación lineal, aplicando los pesos muestrales (PB040). Este método evita el sesgo de las CDFs discretas convencionales y es el estándar en la literatura de desigualdad.

### 3.3. Distribuciones parentales por año de renta

Para cada cohorte de hijos *C* (nacidos 1973–1996), la distribución parental corresponde al año de renta *C* + 5, asumiendo que los padres nacieron ~25 años antes que los hijos y se observan también a los ~30 años. Esto requiere distribuciones parentales para los años de renta 1978–2001.

| Años de renta | Fuente | Método |
|---|---|---|
| 1978–1979 | Extrapolación | Crecimiento log-lineal por percentil desde 1980 |
| 1980 | EPF 80-81 | Observado directamente |
| 1981–1984 | Interpolación | Log-lineal entre 1980 y 1985, por percentil |
| 1985–1997 | ECPF Base 85 | Pool de 4 trimestres/año |
| 1998–2001 | ECPF Base 97 | Pool de 4 trimestres/año |

La validación cruzada de la ECPF85 1990 contra la EPF 90-91 revela un ratio de medianas de 2,17× (hogar/individual), coherente con ~1,5 perceptores y ~1,4× por incluir otras rentas del hogar.

### 3.4. Cópula y cálculo de movilidad

Siguiendo a Chetty et al. (2017), la movilidad absoluta de la cohorte *C* se define como la fracción de hijos que ganan más (en euros constantes) que sus padres a la misma edad (~30 años). Para calcularla se requiere la distribución conjunta de rangos padres-hijos (la cópula). Dado que la ECV no vincula padres e hijos directamente, asumimos tres cópulas:

1. **Rank-preserving** (cota inferior): el hijo en el percentil *p* tuvo un padre en el percentil *p*. Movilidad = media de I(Y_hijo(p) > Y_padre(p)).

2. **Gaussian** (estimación central): la distribución conjunta de los rangos (transformados a z-scores vía Φ⁻¹) es normal bivariante con correlación ρ=0,34 (valor calibrado por Chetty et al.). Para cada percentil parental *p*, se integra Pr(Y_hijo > Y_padre(p)) sobre la distribución condicional del rango del hijo dado el rango del padre.

3. **Independence** (cota superior): el rango del hijo es independiente del rango del padre. Para cada percentil parental *p*, la movilidad es la fracción de la distribución de hijos que supera Y_padre(p). Promedio sobre *p*.

Se realiza además un análisis de sensibilidad variando ρ entre 0 y 0,50.

### 3.5. Escenarios de ajuste hogar/individual

El principal problema metodológico es la comparación de renta del **hogar** (padres, ECPF/EPF) con renta **individual** (hijos, ECV). Para cuantificar este sesgo, implementamos tres correcciones:

- **Escenario A (HH-HH)**: usar también renta del hogar (HY010) para los hijos, vinculando persona→hogar vía PB030÷100=HB030.
- **Escenario B (Ratio)**: dividir la distribución parental por 2,17 (el ratio de validación cruzada), aproximando renta individual.
- **Escenario C (Per-earner)**: dividir la renta del hogar parental por el número real de perceptores de cada hogar (campo NPerc en ECPF85, MIOCUSEM en ECPF97).

---

## 4. Resultados

### 4.1. Cobertura y tamaño muestral

La combinación de 20 olas de ECV (2006–2025) y la ventana de edad 28–32 produce observaciones para 24 cohortes de nacimiento (1973–1996). El tamaño muestral total es de 39.854 individuos (ponderados: ~65 millones de persona-observaciones).

### 4.2. Distribución de renta por cohorte

**Tabla 1.** Renta laboral bruta a los ~30 años por cohorte de nacimiento (euros constantes de 2025, ambos sexos).

| Cohorte | n | N ponderado | Media | Mediana | p10 | p25 | p75 | p90 |
|--------:|------:|------------:|--------:|--------:|------:|------:|--------:|--------:|
| 1973 | 459 | 780.434 | 19.587 | 18.751 | 0 | 0 | 29.222 | 44.750 |
| 1974 | 927 | 1.683.940 | 19.789 | 17.689 | 0 | 2.935 | 27.319 | 40.517 |
| 1975 | 1.484 | 2.580.833 | 19.502 | 20.034 | 0 | 7.747 | 27.517 | 37.727 |
| 1976 | 1.825 | 3.127.067 | 19.409 | 18.866 | 0 | 8.956 | 27.412 | 37.938 |
| 1977 | 2.484 | 4.169.847 | 17.442 | 17.319 | 0 | 3.564 | 26.054 | 36.627 |
| 1978 | 2.351 | 4.060.293 | 18.352 | 18.903 | 0 | 3.180 | 26.921 | 38.049 |
| 1979 | 2.241 | 4.001.482 | 17.273 | 16.663 | 0 | 821 | 26.309 | 37.806 |
| 1980 | 2.015 | 3.601.932 | 15.423 | 14.398 | 0 | 0 | 24.888 | 33.222 |
| 1981 | 1.844 | 3.577.920 | 15.631 | 14.048 | 0 | 161 | 24.304 | 35.703 |
| 1982 | 1.752 | 3.267.320 | 14.754 | 12.016 | 0 | 0 | 23.551 | 34.983 |
| 1983 | 1.621 | 2.954.354 | 14.283 | 12.700 | 0 | 1.619 | 21.912 | 33.401 |
| 1984 | 1.759 | 3.503.543 | 13.095 | 10.138 | 0 | 708 | 20.546 | 31.815 |
| 1985 | 1.478 | 2.550.702 | 13.431 | 11.281 | 0 | 2.318 | 21.062 | 31.360 |
| 1986 | 1.517 | 2.625.747 | 14.692 | 11.376 | 0 | 1.609 | 22.084 | 34.000 |
| 1987 | 1.569 | 2.431.743 | 13.964 | 11.615 | 0 | 1.014 | 21.175 | 31.751 |
| 1988 | 1.693 | 2.799.584 | 16.615 | 13.924 | 0 | 3.828 | 23.797 | 38.610 |
| 1989 | 1.882 | 2.831.763 | 15.644 | 13.271 | 0 | 2.589 | 23.705 | 38.311 |
| 1990 | 2.071 | 2.774.597 | 16.792 | 14.118 | 0 | 4.210 | 24.789 | 35.911 |
| 1991 | 2.219 | 2.563.214 | 16.165 | 14.687 | 0 | 2.684 | 23.314 | 35.604 |
| 1992 | 2.415 | 2.645.871 | 17.634 | 15.828 | 0 | 5.145 | 24.791 | 36.636 |
| 1993 | 1.981 | 2.066.839 | 18.458 | 16.600 | 0 | 5.864 | 26.313 | 40.168 |
| 1994 | 1.514 | 1.572.128 | 16.806 | 14.117 | 0 | 3.571 | 23.824 | 37.375 |
| 1995 | 1.047 | 1.039.942 | 16.847 | 15.889 | 0 | 5.266 | 25.025 | 34.985 |
| 1996 | 506 | 529.313 | 17.234 | 15.308 | 0 | 4.373 | 24.146 | 36.298 |

*Nota.* Renta laboral bruta = PY010G + PY020G, deflactada con IPC (base 2025). Ventana de edad 28–32 años. Incluye individuos con renta cero. Percentiles calculados con pesos muestrales (midpoint CDF). Fuente: ECV 2006–2025 (INE).

La evolución es clara: la renta mediana a los ~30 años alcanza su máximo para la cohorte de 1975 (~20.000 €), cae a un mínimo para la cohorte de 1984 (~10.100 €, un descenso del 49%), y se recupera parcialmente hasta ~16.600 € para la cohorte de 1993.

### 4.3. Distribución de renta por cohorte y sexo

**Tabla 2.** Renta laboral bruta mediana a los ~30 años por cohorte y sexo (euros constantes de 2025, cohortes seleccionadas).

| Cohorte | Mediana hombres | Mediana mujeres | Ratio F/M | n hombres | n mujeres |
|--------:|----------------:|----------------:|----------:|----------:|----------:|
| 1975 | 22.864 | 15.054 | 0,66 | 724 | 760 |
| 1978 | 21.113 | 15.225 | 0,72 | 1.262 | 1.089 |
| 1980 | 17.118 | 12.148 | 0,71 | 965 | 1.050 |
| 1983 | 17.757 | 9.142 | 0,51 | 818 | 803 |
| 1984 | 12.021 | 9.073 | 0,75 | 830 | 929 |
| 1987 | 14.466 | 9.289 | 0,64 | 729 | 840 |
| 1990 | 15.231 | 13.616 | 0,89 | 1.001 | 1.070 |
| 1993 | 17.426 | 14.996 | 0,86 | 973 | 1.008 |
| 1996 | 15.904 | 14.536 | 0,91 | 263 | 243 |

*Nota.* Misma definición que Tabla 1, desglosada por sexo (PB150: 1 = hombre, 2 = mujer). Fuente: ECV 2006–2025 (INE).

### 4.4. Figuras

**Figura 1.** Mediana y media de renta laboral a los ~30 años por cohorte y sexo.

![Mediana y media por cohorte](/assets/images/movilidad/child_income_by_cohort.png)

**Figura 2.** Evolución distribucional de la renta laboral por cohorte (fan chart).

![Fan chart p10-p90](/assets/images/movilidad/child_income_fan.png)

*Nota.* Bandas: azul claro = p10–p90; azul medio = p25–p75; línea = mediana. Ambos sexos. Euros constantes de 2025.

**Figura 3.** Brecha de género en la renta laboral mediana a los ~30 años.

![Brecha de género](/assets/images/movilidad/child_gender_gap.png)

*Nota.* Líneas: mediana de hombres (azul) y mujeres (rojo). Línea gris discontinua: ratio mujer/hombre (eje derecho, %).

### 4.5. Distribuciones parentales: cobertura por año de renta

La combinación de EPF quinquenales, ECPF trimestrales e interpolación/extrapolación proporciona distribuciones parentales para los 24 años de renta necesarios (1978–2001):

**Tabla 3.** Renta del hogar (sustentador principal 28–32 años) por año de renta (euros constantes de 2025, ambos sexos, años seleccionados).

| Año renta | Fuente | n | N ponderado | Media | Mediana | p10 | p90 |
|----------:|--------|------:|----------:|------:|--------:|----:|------:|
| 1980 | EPF 80-81 | 4.943 | 2.032.082 | 11.294 | 6.868 | 0 | 28.164 |
| 1985 | ECPF85 | 962 | 3.144.290 | 23.407 | 20.575 | 3.513 | 42.984 |
| 1990 | ECPF85 | 895 | 3.192.990 | 25.943 | 22.558 | 11.279 | 45.429 |
| 1995 | ECPF85 | 719 | 2.847.819 | 24.980 | 22.898 | 6.557 | 43.847 |
| 2000 | ECPF97 | 1.364 | 2.305.619 | 28.412 | 26.449 | 12.522 | 45.916 |

*Nota.* Los años 1978–79 son extrapolados, 1981–84 interpolados, 1985–97 observados (ECPF85), 1998–2001 observados (ECPF97). Los niveles a partir de 1985 son de renta del hogar (no individual), lo que los hace superiores a los de la EPF 80-81 (que sí es individual). Fuente: EPF 80-81 (INE), ECPF85, ECPF97 (INE).

El salto entre 1980 (EPF individual, mediana 6.868 €) y 1985 (ECPF hogar, mediana 20.575 €) refleja no solo el crecimiento real sino el cambio de concepto: renta individual → renta del hogar. Esta discrepancia se cuantifica con la validación cruzada.

### 4.6. Validación cruzada ECPF85 vs EPF 90-91

La comparación de la ECPF85 (renta del hogar) con la EPF 90-91 (renta individual) para el año 1990 arroja un ratio de medianas de **2,17×**. Este ratio es coherente con: (a) ~1,5 perceptores por hogar en la franja 28–32 años, y (b) la inclusión de rentas no laborales en la ECPF.

### 4.7. Movilidad absoluta: estimación principal

**Tabla 4.** Movilidad absoluta por cohorte de nacimiento, cópula Gaussian (ρ=0,34), escenario C (per-earner).

| Cohorte | Movilidad (%) | Contexto |
|--------:|--------------:|----------|
| 1973 | 69,7 | Pre-crisis boom |
| 1975 | 75,2 | Pre-crisis boom |
| 1977 | 63,9 | Transición |
| 1980 | 42,3 | Crisis |
| 1983 | 38,6 | Crisis |
| 1984 | 32,1 | Crisis (mínimo) |
| 1988 | 42,4 | Recuperación |
| 1990 | 46,7 | Recuperación |
| 1993 | 43,6 | COVID |
| 1996 | 39,5 | COVID |

*Nota.* Movilidad = fracción de hijos que ganan más que sus padres a la misma edad (~30 años), en euros constantes de 2025. Cópula Gaussian con ρ=0,34. Distribución parental = renta del hogar dividida por número de perceptores (escenario C). Fuentes: ECV 2006–2025, ECPF85 1985–1997, ECPF97 1998–2001 (INE).

**Figura 7.** Movilidad absoluta en España (tres cópulas, distribuciones baseline).

![Movilidad absoluta España](/assets/images/movilidad/absolute_mobility_spain.png)

*Nota.* Línea continua: cópula Gaussian (ρ=0,34). Líneas discontinuas: cotas rank-preserving (inferior) e independencia (superior). Área sombreada: rango entre cotas. Distribuciones baseline (individual hijo vs. hogar padre).

### 4.8. Escenarios de ajuste hogar/individual

**Tabla 5.** Movilidad media por escenario (Gaussian, ρ=0,34, todos los sexos).

| Escenario | Descripción | Movilidad media | Rango |
|---|---|---:|---|
| Baseline | Individual hijo vs hogar padre | 34,9% | 19,7–65,0% |
| A: HH-HH | Hogar hijo (HY010) vs hogar padre | 83,1% | 70,6–97,5% |
| B: Ratio | Individual hijo vs padre ÷ 2,17 | 60,1% | 46,7–78,6% |
| C: Per-earner | Individual hijo vs padre ÷ NPerc | 47,9% | 32,1–75,2% |

*Nota.* El escenario A sobreestima porque HY010 incluye todas las fuentes de renta del hogar, no solo laboral. El escenario C (per-earner) es el más satisfactorio conceptualmente.

**Figura 4.** Movilidad absoluta: comparación de escenarios de ajuste.

![Escenarios de ajuste](/assets/images/movilidad/mobility_scenarios_comparison.png)

*Nota.* Cópula Gaussian (ρ=0,34). Las cuatro series comparten el mismo patrón temporal: caída pronunciada desde las cohortes pre-crisis hasta las de la Gran Recesión, recuperación parcial posterior y nueva caída para las cohortes COVID. La diferencia de nivel refleja el sesgo del desajuste hogar/individual.

### 4.9. Sensibilidad al parámetro de la cópula

**Figura 5.** Sensibilidad de la movilidad a la correlación rank-rank (ρ).

![Sensibilidad rho](/assets/images/movilidad/mobility_sensitivity_rho.png)

*Nota.* La movilidad es decreciente en ρ: mayor correlación intergeneracional → menos movilidad. Para valores razonables de ρ (0,20–0,50), el patrón temporal se mantiene estable.

### 4.10. Movilidad por sexo

**Figura 6.** Movilidad absoluta por sexo (Gaussian, ρ=0,34).

![Movilidad por sexo](/assets/images/movilidad/mobility_by_sex.png)

*Nota.* La movilidad femenina es superior a la masculina para las cohortes más antiguas (1973–1982), reflejando la masiva incorporación de la mujer al empleo entre generaciones. Para las cohortes recientes, la brecha se reduce.

### 4.11. Descomposición crecimiento vs. desigualdad

Siguiendo la Figure 5 de Chetty et al. (2017), descomponemos la caída de movilidad en dos componentes: (a) menor crecimiento de la renta media y (b) mayor desigualdad en la distribución. La cohorte de referencia es 1975 (la de máxima movilidad, 75,2% en el escenario C).

Para cada cohorte *C*, construimos dos contrafactuales:

- **CF1 — "Más crecimiento"**: ¿qué movilidad tendría la cohorte *C* si su renta media hubiera sido la de 1975, manteniendo la forma distribucional actual? Se escalan todos los percentiles de *C* por el ratio media(1975)/media(*C*).

- **CF2 — "Más igualdad"**: ¿qué movilidad tendría la cohorte *C* si la distribución tuviera la misma forma (percentile shares) que la de 1975, manteniendo la renta media actual? Se aplican las proporciones relativas de 1975 a la media de *C*.

**Tabla 7.** Descomposición de la caída de movilidad (escenario C, ρ=0,34, cohortes seleccionadas).

| Cohorte | Actual (%) | CF1 Crecimiento (%) | CF2 Igualdad (%) | Caída vs 1975 (pp) | % explicado por crecimiento | % explicado por igualdad |
|--------:|-----------:|--------------------:|------------------:|-------------------:|----------------------------:|-------------------------:|
| 1975 | 75,2 | 75,2 | 75,2 | 0,0 | — | — |
| 1977 | 63,9 | 66,3 | 67,0 | 11,3 | 21% | 27% |
| 1980 | 42,3 | 50,8 | 44,0 | 32,9 | 26% | 5% |
| 1984 | 32,1 | 46,4 | 31,8 | 43,2 | 33% | −1% |
| 1988 | 42,4 | 48,8 | 45,3 | 32,8 | 19% | 9% |
| 1990 | 46,7 | 53,0 | 50,3 | 28,5 | 22% | 12% |
| 1993 | 43,6 | 46,6 | 48,4 | 31,6 | 9% | 15% |
| 1996 | 39,5 | 45,1 | 42,4 | 35,7 | 16% | 8% |

*Nota.* CF1 escala la distribución de *C* para igualar la renta media de 1975. CF2 aplica las percentile shares de 1975 manteniendo la media de *C*. Movilidad calculada con cópula Gaussian (ρ=0,34), distribuciones parentales per-earner (escenario C). Fuente: cálculo propio.

En media, para las cohortes post-1975 la caída es de 30,8 puntos porcentuales, de los cuales el crecimiento explica 7,3 pp (24%) y la igualdad 2,4 pp (8%). El grueso de la caída (~68%) refleja la interacción entre ambos factores.

**Figura 8.** Descomposición de la caída de movilidad: crecimiento vs. desigualdad.

![Descomposición](/assets/images/movilidad/decomposition_spain.png)

*Nota.* Línea continua negra: movilidad actual (escenario C). Línea discontinua azul: contrafactual CF1 (más crecimiento). Línea punto-raya naranja: contrafactual CF2 (más igualdad). Línea gris punteada: referencia cohorte 1975 (75,2%). Cópula Gaussian (ρ=0,34).

A diferencia del resultado de Chetty et al. para EEUU —donde la desigualdad es el motor dominante de la caída—, en España el **menor crecimiento de la renta media es el factor más importante**. El contrafactual CF1 ("más crecimiento") recupera consistentemente más movilidad que el CF2 ("más igualdad"). Esto es coherente con la realidad española: la renta mediana de los nacidos en 1984 a los ~30 años es menos de la mitad que la de los nacidos en 1975, mientras que los indicadores de desigualdad (Gini) se han mantenido relativamente estables.

### 4.12. Estimación de la cópula con co-residentes

Para contrastar la asunción de ρ=0,34, identificamos pares padre-hijo co-residentes en la ECV: individuos de 28–32 años ("hijos") que conviven con un adulto de 50–65 años ("padre") en el mismo hogar (vía PB030÷100). Se requiere que ambos tengan renta laboral positiva.

**Tabla 8.** Estimación de la correlación rank-rank con co-residentes.

| Estadístico | Valor |
|---|---|
| Pares co-residentes (ambos income > 0) | 9.801 |
| Mediana edad hijo | 29 años |
| Mediana edad padre | 58 años |
| Media renta hijo (€ 2025) | 18.031 |
| Media renta padre (€ 2025) | 27.510 |
| Spearman ρ | 0,161 |
| IC 95% (bootstrap) | [0,140; 0,181] |
| ρ asumido (Chetty) | 0,340 |

*Nota.* 9.801 pares de 20 olas ECV (2006–2025). Rango asignado dentro de la muestra pooled. Bootstrap con 1.000 réplicas.

El ρ estimado (0,16) es significativamente inferior al asumido (0,34). Sin embargo, esto es esperable: los co-residentes son una **muestra seleccionada** de jóvenes que no se han emancipado, probablemente con menores ingresos y en hogares de menor renta. La selección endógena tiende a comprimir la varianza de ambas variables y a reducir la correlación observada. Además, comparamos renta **actual** de padres a los 50–65 (no a los ~30, que sería lo comparativo), lo que introduce ruido adicional.

La recálculo de movilidad con ρ=0,16 produce cambios modestos (<1,5 pp por cohorte). Para las cohortes pre-1979, la movilidad baja marginalmente (~1 pp); para las post-1980, sube ~1 pp. El patrón temporal y las conclusiones sustantivas son robustos a esta variación del parámetro.

**Interpretación**: el ρ de co-residentes no sustituye al ρ poblacional, pero su bajo valor es coherente con una correlación intergeneracional moderada en España. La asunción de ρ=0,34 se sitúa en el rango plausible y los resultados son poco sensibles a su valor exacto (como ya mostraba el análisis de sensibilidad de la Figura 5).

### 4.13. Robustez: movilidad medida a edad ~40

#### Motivación

El análisis principal mide la movilidad a los ~30 años (ventana 28–32), replicando la elección de Chetty et al. (2017). Sin embargo, en España el empleo estable se alcanza considerablemente más tarde que en EEUU: la tasa de temporalidad juvenil (25–34 años) ha oscilado entre el 35% y el 55% en las últimas tres décadas, la emancipación media se produce a los 29–30 años, y la precariedad contractual se prolonga frecuentemente hasta bien entrada la treintena. En este contexto, la renta laboral a los 28–32 años puede subestimar sustancialmente la renta permanente de las cohortes recientes, sesgando la movilidad medida a la baja.

Este problema no es simétrico entre cohortes: las cohortes nacidas en 1980–1986 cumplieron 30 años entre 2008 y 2016, justo durante la Gran Recesión y la lenta recuperación posterior — un momento excepcionalmente desfavorable del mercado laboral. Las cohortes de los 70, en cambio, cumplieron 30 durante el boom de los 2000.

Para evaluar la magnitud de este sesgo, replicamos el análisis completo midiendo la renta de hijos y padres a los ~40 años (ventana 38–42).

#### Diseño del ejercicio

Medir la movilidad a edad 40 implica recalcular los dos ingredientes de la estimación:

**Renta de los hijos a los 40.** Utilizamos las mismas 20 olas de la ECV (2006–2025), pero seleccionando personas de 38–42 años en vez de 28–32. La ECV 2006 (renta de 2005) captura la cohorte central 1965; la ECV 2025 (renta de 2024) captura la cohorte central 1984. El rango de cohortes resultante es 1963–1986.

**Renta de los padres a los 40.** Asumiendo la misma brecha intergeneracional de 25 años, los padres de la cohorte *C* nacieron alrededor del año *C*−25 y tenían 40 años en el año *C*+15 (en vez de *C*+5 como a edad 30). Las cohortes 1973–1986 requieren distribuciones parentales para los años 1988–2001. Esta ventana está íntegramente cubierta por la ECPF Base 85 (1988–1997) y la ECPF Base 97 (1998–2001), de modo que **todas las distribuciones parentales están directamente observadas**, sin necesidad de interpolación ni extrapolación. Esto elimina una fuente importante de incertidumbre del análisis a edad 30, donde los años 1978–1984 (padres de las cohortes 1973–1979) dependían de la extrapolación desde la EPF 80-81 y la interpolación log-lineal hasta 1985.

Utilizamos el ingreso per-earner (escenario C) para los padres, por coherencia con el análisis principal. Adicionalmente, calculamos una segunda pista con **renta del hogar** (HY010 de la ECV para los hijos; renta laboral del hogar de la ECPF para los padres), que es la medida empleada por Manduca et al. (2024) en su comparación internacional de movilidad absoluta.

Este ejercicio tiene tres ventajas metodológicas:

1. **Renta más representativa de la renta permanente**: a los 40, la renta laboral está consolidada, las carreras son estables y los efectos transitorios de la crisis se han amortiguado.
2. **Datos parentales 100% observados**: se elimina la incertidumbre asociada a la extrapolación de 1978–79 y la interpolación de 1981–84.
3. **Cobertura de la crisis completa**: las 6 cohortes más afectadas por la crisis (1980–85) están incluidas.

La contrapartida: las cohortes 1987–1996 (recuperación y COVID) aún no han cumplido 40 años, por lo que el análisis se limita a 14 cohortes (1973–1986).

#### Resultados

**Tabla 9.** Movilidad absoluta: comparación edad ~30 vs. edad ~40, por medida de renta (Gaussian, ρ=0,34).

| Cohorte | PE edad 30 (%) | PE edad 40 (%) | HH edad 30 (%) | HH edad 40 (%) |
|---:|---:|---:|---:|---:|
| 1973 | 69,7 | 44,6 | 97,2 | 78,3 |
| 1974 | 71,4 | 38,7 | 97,5 | 73,3 |
| 1975 | 75,2 | 42,4 | 97,0 | 74,1 |
| 1976 | 73,5 | 39,7 | 95,7 | 72,0 |
| 1977 | 63,9 | 46,9 | 91,8 | 76,8 |
| 1978 | 61,1 | 44,0 | 89,9 | 75,4 |
| 1979 | 52,9 | 47,0 | 86,8 | 79,0 |
| 1980 | 42,3 | 45,4 | 81,8 | 77,5 |
| 1981 | 42,8 | 48,1 | 80,5 | 79,1 |
| 1982 | 41,7 | 46,8 | 81,3 | 76,8 |
| 1983 | 38,6 | 46,7 | 77,6 | 78,0 |
| 1984 | 32,1 | 47,5 | 70,6 | 77,6 |
| 1985 | 34,2 | 42,9 | 71,4 | 74,9 |
| 1986 | 35,1 | 45,4 | 73,4 | 77,2 |

*Nota.* PE = per-earner (renta laboral individual para hijos, renta del hogar / n.º de perceptores para padres). HH = renta del hogar (HY010 para hijos, renta laboral total del hogar para padres). Ventana de edad 38–42 para edad 40; 28–32 para edad 30. Parent_year = cohorte + 15 (edad 40) o cohorte + 5 (edad 30). Todos los datos parentales a edad 40 directamente observados (ECPF85 1988–1997, ECPF97 1998–2001). Edad 30: escenarios C (PE) y A (HH) de la Sección 4.8.

**Figura 9.** Movilidad absoluta a edad ~30 (línea discontinua azul) vs. edad ~40 (línea continua verde con sombreado de cotas), cohortes 1973–1986.

![Movilidad edad 30 vs 40](/assets/images/movilidad/mobility_age40_comparison.png)

#### Interpretación

Los resultados revelan un patrón inesperado y muy informativo. Hay que distinguir dos grupos de cohortes cuyo comportamiento es radicalmente diferente.

**Las cohortes tempranas (1973–1978) muestran movilidad mucho más baja a edad 40 que a edad 30** (diferencias de −17 a −34 pp). ¿Por qué? Intervienen dos mecanismos:

- *Umbral parental más exigente.* A edad 30, los padres de la cohorte 1975 se miden en el año de renta 1980 (parent_year = 1975+5), basado en la EPF 80-81 y parcialmente extrapolado. A edad 40, los padres de la misma cohorte se miden en 1990 (parent_year = 1975+15), con datos directamente observados de la ECPF85. La mediana parental per-earner a edad 40 en 1990 (~18.800 €) es sustancialmente más alta que la mediana a edad 30 en 1980 (datos extrapolados y en un período de rentas reales más bajas). Los padres a los 40 tienen carreras consolidadas y rentas más altas; superar ese umbral es más difícil.
- *Renta de los hijos: sube, pero no lo suficiente.* La renta mediana de la cohorte 1975 sube de ~12.000 € (edad 30) a ~16.000 € (edad 40), un aumento del 33%. Pero el umbral parental sube aún más, de modo que la fracción que supera a sus padres baja del 75% al 42%.

Esto sugiere que la movilidad del 75% medida a edad 30 para las cohortes de los 70 estaba **inflada artificialmente** por dos factores: (a) la renta parental a edad 30 estaba parcialmente basada en extrapolaciones desde la EPF 80-81, que pueden subestimar las distribuciones parentales reales; y (b) a los 30, los padres de esas cohortes estaban en una fase temprana de su carrera y con rentas más bajas en términos reales, lo que establece un "listón" fácil de superar.

**Las cohortes de la crisis (1980–1986) muestran movilidad más alta a edad 40 que a edad 30** (+3 a +16 pp). Los mecanismos son los inversos:

- *Recuperación laboral de los hijos.* La cohorte 1984 tenía 30 años en 2014, en plena crisis, con una renta mediana deprimida (~8.000 € a edad 30 en el escenario per-earner). A los 40, en 2024, su renta mediana ha subido a ~19.400 €: han tenido una década para encontrar empleo estable, desarrollar carreras profesionales y consolidar trayectorias. El efecto ciclo vital les beneficia enormemente.
- *El listón parental no sube proporcionalmente.* Los padres de la cohorte 1984 se miden en 1999 (parent_year = 1984+15), con una mediana per-earner de ~21.600 €. Es un listón alto pero asumible para hijos con carreras consolidadas. El aumento del listón parental entre 1993 (padres de cohorte 1978) y 1999 (padres de cohorte 1984) es modesto comparado con la recuperación de los hijos.

El caso más ilustrativo es la **cohorte 1984**: a edad 30, tiene la movilidad más baja de toda la serie (32%, el "valle" de la caída); a edad 40, tiene una de las más altas (48%). Una diferencia de +15,5 pp que cuantifica directamente cuánto la Gran Recesión deprimió *artificialmente* la movilidad de esta cohorte por medirla en el peor momento de su ciclo vital.

**El cruce de las dos curvas** se produce alrededor de la cohorte 1979–1980 (Figura 9). Este cruce tiene una interpretación precisa: es el punto donde el efecto "listón parental más exigente" (que perjudica a las cohortes tempranas) se compensa exactamente con el efecto "recuperación laboral" (que beneficia a las cohortes tardías). Las cohortes anteriores a 1979 se beneficiaban a edad 30 de un umbral parental bajo (datos extrapolados, padres jóvenes); las posteriores se veían perjudicadas por una renta propia deprimida por la crisis.

#### Renta del hogar: comparabilidad con Manduca et al. (2024)

Las dos columnas de la derecha de la Tabla 9 (HH) presentan la movilidad medida con **renta del hogar**, la definición empleada por Manduca et al. (2024) en su comparación internacional. Los resultados cambian radicalmente:

- **A edad 40, la movilidad de hogar es 72%–79%** para todas las cohortes, siempre muy por encima del 50%.
- **La caída entre cohortes es mínima**: de 78% (1973) a 77% (1986), apenas 1 pp.
- **El rango total es de 7 pp** (72%–79%), frente a los 9 pp del per-earner (39%–48%).

Estos niveles son comparables a los que Manduca et al. estiman para los países con mayor movilidad de su muestra: Países Bajos (~70–80%), Noruega (~70–75%) y los países nórdicos (~55–70%). España con renta del hogar a edad 40 no es un outlier por debajo, sino que se sitúa en el rango alto.

¿Por qué la diferencia es tan grande entre per-earner y hogar? Dos mecanismos:

1. **El denominador per-earner deprime la renta parental.** Dividir la renta del hogar por el número de perceptores (~1,5 de media en las ECPF) genera rentas parentales más bajas que usar la renta total del hogar. Pero la renta de los hijos (ECV) es individual en el caso per-earner y del hogar en el caso HH. Cuando ambos lados de la comparación son rentas del hogar, el crecimiento secular de la renta — particularmente la incorporación masiva de la mujer al mercado laboral — se refleja plenamente: los hogares de los hijos tienen más perceptores y rentas totales más altas que los de los padres.

2. **La renta del hogar es menos sensible a la precariedad individual.** Un joven de 40 años con empleo temporal pero que convive con pareja empleada tiene una renta del hogar que puede superar la de sus padres, aunque su renta individual per-earner no lo haga. La renta del hogar es un "seguro" contra la precariedad individual que eleva la movilidad medida.

La movilidad de hogar a edad 30 (70%–97%) muestra una caída mayor (27 pp) que a edad 40 (7 pp), confirmando que el sesgo de ciclo vital también afecta a la medida de hogar, aunque con menor intensidad que en el caso per-earner.

#### Cuantificación del sesgo de ciclo vital

La comparación permite descomponer la caída medida a edad 30 en dos componentes:

- **Caída a edad 30**: 75% (cohorte 1975) → 32% (cohorte 1984) = **43 pp**
- **Caída a edad 40**: 42% (cohorte 1975) → 48% (cohorte 1984) = **+6 pp** (ligero aumento, no caída)

Esto implica que, de los 43 pp de caída medidos a edad 30, como máximo ~9 pp reflejan diferencias persistentes en movilidad entre cohortes (el rango total a edad 40 es 39%–48%), y el resto (~34 pp) se debe a la interacción entre efectos de ciclo vital, la precariedad del mercado laboral español a edades jóvenes, y artefactos de las fuentes de datos parentales (extrapolación/interpolación).

Es importante notar que esto **no significa que no haya un problema real**. Una movilidad del 42–48% indica que más de la mitad de los españoles nacidos en los 70 y 80 *no* superan la renta de sus padres a la misma edad — un resultado preocupante. Pero el diagnóstico cambia cualitativamente: de un "colapso catastrófico" (43 pp de caída) a un "nivel crónicamente bajo con variación moderada" (~9 pp de rango). El titular no es "la movilidad se ha hundido" sino "la movilidad *siempre fue baja* y la precariedad juvenil la hace parecer aún peor cuando se mide a los 30".

#### Implicaciones para la interpretación del estudio

Este ejercicio de robustez tiene cuatro implicaciones directas:

1. **La caída de 43 pp medida a edad 30 exagera la pérdida de movilidad intergeneracional.** Una parte sustancial refleja el efecto transitorio de medir la renta en un momento del ciclo vital donde la precariedad es alta y la renta no es representativa de la renta permanente. La caída "verdadera" es más moderada.

2. **La ventaja de medir a edad 40 no es solo teórica sino empírica**: los datos parentales están íntegramente observados, eliminando la incertidumbre de la extrapolación. El hecho de que la movilidad de las cohortes tempranas baje drásticamente cuando se usan datos parentales observados sugiere que las distribuciones parentales extrapoladas a edad 30 podrían estar subestimando la renta de los padres.

3. **La precariedad juvenil española es un fenómeno real con consecuencias medibles.** La diferencia entre movilidad a 30 y a 40 para las cohortes de la crisis (+8 a +16 pp) cuantifica directamente el "déficit de renta juvenil" que afecta a estas generaciones. Si la renta a los 30 representase bien la renta permanente, ambas medidas deberían coincidir. La discrepancia confirma que España tiene un problema específico de inserción laboral temprana que no se observaría con esta intensidad en un país como EEUU, donde la transición al empleo estable es más rápida.

4. **España no es un outlier internacional cuando se usa renta del hogar.** La movilidad de hogar a edad 40 (72%–79%) sitúa a España en el rango de los países más móviles de Manduca et al. (2024). La alarma que producía la movilidad per-earner íntegramente bajo 50% se explica en gran parte por una cuestión de definición: cuando se compara renta individual de hijos con renta del hogar/perceptores de padres, se penaliza a los hijos que no conviven con otro perceptor. La renta del hogar — que es la variable estándar en las comparaciones internacionales — da un panorama mucho más favorable.

La confirmación definitiva requeriría datos fiscales longitudinales (AEAT) que permitiesen medir la renta permanente (promedio de varios años) en vez de la renta corriente a una edad fija.

### 4.14. Renta familiar baseline (replicación de Chetty Fig 1)

#### Motivación

Chetty et al. (2017) miden la movilidad con *pretax family income* — la suma de rentas brutas del declarante y su cónyuge. Nuestro análisis principal (Secciones 4.7–4.11) usa renta laboral **individual** para los hijos. Para alinear la especificación con el paper, construimos una medida de renta familiar a nivel de pareja a partir de la ECV.

#### Construcción de la renta familiar

Para cada ola de la ECV (2006–2025), identificamos parejas dentro del hogar mediante dos mecanismos:

1. **PB180 (ID de cónyuge/pareja)**: enlace directo al PB030 del partner. Disponible en las olas recientes.
2. **Fallback PB190 (estado civil)**: si PB180 no está disponible o no encuentra pareja, buscamos dentro del mismo hogar (PB030÷100) un segundo adulto de sexo opuesto con diferencia de edad ≤15 años y estado civil casado/cohabitante.

La renta familiar se define como la suma de PY010G+PY020G de ambos miembros de la pareja (o solo del individuo si no se identifica pareja). Entre el 40% y el 53% de las personas de 28–32 años tienen pareja identificada. El ratio renta familiar / renta individual varía entre 1,22× y 1,82× (mediana ~1,43×).

#### Resultados

**Tabla 10.** Movilidad absoluta con renta familiar (Gaussian, ρ=0,34, ambos sexos, cohortes seleccionadas).

| Cohorte | Familiar (%) | Individual (%) | Diferencia (pp) |
|--------:|-------------:|---------------:|----------------:|
| 1975 | 78,9 | 75,2 | +3,7 |
| 1978 | 66,2 | 61,1 | +5,1 |
| 1980 | 50,3 | 42,3 | +8,0 |
| 1984 | 38,6 | 32,1 | +6,5 |
| 1988 | 44,7 | 42,4 | +2,3 |
| 1990 | 45,7 | 46,7 | −1,0 |
| 1993 | 45,2 | 43,6 | +1,6 |
| 1996 | 32,9 | 39,5 | −6,6 |

*Nota.* Renta familiar = suma de PY010G+PY020G de ambos miembros de la pareja (o individual si sin pareja). Distribuciones parentales: renta del hogar de la ECPF/EPF. Parent_year = cohort + 5. Fuente: ECV 2006–2025, ECPF85, ECPF97, EPF 80-81 (INE).

La movilidad familiar es generalmente superior a la individual (+3–8 pp para cohortes 1975–1984), lo que es coherente con el hecho de que la renta de pareja supera la individual. La brecha se reduce para cohortes recientes, donde la tasa de emparejamiento a los 28–32 es menor. El patrón temporal — caída pronunciada desde las cohortes pre-crisis hasta las de la Gran Recesión, recuperación parcial y nueva caída — se mantiene idéntico.

**Figura 10.** Movilidad absoluta con renta familiar (Fig 1B de Chetty).

![Movilidad familiar baseline](/assets/images/movilidad/absolute_mobility_family_baseline.png)

### 4.15. Cotas LP sobre la cópula (replicación de Chetty Fig 2A)

#### Motivación

Una contribución metodológica clave de Chetty et al. es demostrar que la cópula es irrelevante para las cohortes tempranas. Lo hacen buscando los extremos de movilidad compatibles con las marginales observadas, sujeto a la restricción de dominancia estocástica de primer orden (FOSD): los hijos de padres más ricos no pueden tener *peores* perspectivas que los hijos de padres más pobres.

#### Algoritmo

Para cada cohorte, resolvemos dos problemas de programación lineal con 99×99 = 9.801 variables C[i,j] (probabilidad conjunta del percentil i del hijo y percentil j del padre):

- **Restricciones de marginal**: las distribuciones marginales del hijo y del padre son uniformes (1/99 por percentil).
- **Restricción FOSD**: la CDF acumulada de la distribución del hijo, condicional al percentil j del padre, es débilmente decreciente en j.
- **Objetivo**: minimizar (cota inferior) o maximizar (cota superior) la movilidad absoluta.

Los LP se resuelven con `scipy.optimize.linprog` (solver HiGHS).

#### Resultados

**Tabla 11.** Cotas LP sobre la movilidad absoluta (renta familiar, cohortes seleccionadas).

| Cohorte | Cota inferior | Gaussian | Cota superior | Anchura (pp) |
|--------:|--------------:|---------:|--------------:|-------------:|
| 1973 | 77,1% | 78,7% | 100,0% | 22,9 |
| 1975 | 75,2% | 78,9% | 100,0% | 24,8 |
| 1977 | 50,4% | 68,7% | 92,9% | 42,5 |
| 1980 | 17,8% | 50,3% | 85,6% | 67,8 |
| 1984 | 8,0% | 38,6% | 69,9% | 61,9 |
| 1988 | 12,5% | 44,7% | 81,3% | 68,9 |
| 1990 | 15,1% | 45,7% | 79,4% | 64,3 |
| 1993 | 16,9% | 45,2% | 69,1% | 52,2 |
| 1996 | 5,3% | 32,9% | 56,0% | 50,7 |

*Nota.* Las cotas se obtienen resolviendo un LP con 9.801 variables sujeto a restricciones de marginal uniforme y FOSD. "Gaussian" = estimación central con cópula Gaussian (ρ=0,34). Distribuciones de renta familiar. Fuente: cálculo propio.

**Figura 11.** Cotas LP y estimación Gaussian (Fig 2A de Chetty).

![Cotas LP](/assets/images/movilidad/copula_bounds_spain.png)

#### Interpretación

A diferencia del resultado de Chetty — donde las cotas son estrechas (~14 pp) para las cohortes tempranas (1940–1950), demostrando la irrelevancia de la cópula —, en España las cotas son **considerablemente más amplias**: ~23 pp para las cohortes más tempranas (1973–1975) y 50–70 pp para las posteriores. Esto refleja que, con datos sintéticos (sin enlace directo padre-hijo), la cópula **sí importa**, especialmente para las cohortes donde las distribuciones de hijos y padres se solapan mucho.

La implicación es directa: **los datos del Lab de Oportunidades (AEAT+Padrón), que permiten observar la cópula directamente, resolverían la principal fuente de incertidumbre del estudio**. Con los datos de la ECV/ECPF, solo podemos acotar.

### 4.16. Suite de sensibilidad (replicación de Chetty Fig 3)

Para verificar la robustez de los resultados a decisiones metodológicas secundarias, replicamos los cuatro paneles de la Figure 3 de Chetty et al. (2017). Todos usan renta familiar como medida base.

#### 4.16a. Deflactores alternativos (Fig 3A)

Se compara la movilidad con tres deflactores: (1) IPC general (baseline), (2) IPC ajustado −0,8%/año (sesgo de calidad, como en Chetty), y (3) proxy del deflactor del PIB (IPC −0,4%/año). Las diferencias máximas entre series son inferiores a 3 pp, confirmando que la elección del deflactor es irrelevante.

#### 4.16b. Renta post-impuestos (Fig 3B)

Se sustituye la renta bruta familiar (PY010G+PY020G) por la renta neta familiar (PY010N+PY020N, cuando disponible). La movilidad con renta neta es ~6 pp inferior a la bruta, coherente con el hecho de que la progresividad fiscal comprime la distribución de renta de los hijos pero no afecta a las distribuciones parentales históricas.

#### 4.16c. Edad 40 (Fig 3C)

Se presenta como serie adicional la movilidad a edad 40 (del script 08). Véase la Sección 4.13 para el análisis completo.

#### 4.16d. Ajuste por tamaño familiar (Fig 3D)

Se equivaliza la renta familiar dividiéndola por la raíz cuadrada del tamaño del hogar (HX040 de la ECV). También se incluye la serie de renta individual (Sección 4.7) como referencia. La equivalización reduce la movilidad ~16 pp respecto a la renta familiar sin ajustar, situándola en niveles similares a la renta individual — lo que sugiere que buena parte de la ventaja de la renta familiar proviene del efecto mecánico del tamaño del hogar.

**Figura 12.** Panel de sensibilidad 2×2 (equivalente a Fig 3 de Chetty).

![Panel sensibilidad](/assets/images/movilidad/sensitivity_combined.png)

### 4.17. Perfil por edad y edad óptima de medición (extensión)

#### Motivación

¿A qué edad debe medirse la movilidad? Chetty usa edad 30, pero el mercado laboral español es distinto: la temporalidad juvenil y la emancipación tardía sugieren que la renta se estabiliza más tarde. Implementamos un perfil de movilidad a 8 edades (28, 30, 32, 34, 36, 38, 40, 42) para identificar la edad de estabilización.

#### Algoritmo

Para cada edad objetivo A ∈ {28, 30, ..., 42}, se construyen distribuciones de renta familiar de los hijos (ECV, ventana [A−2, A+2]) y distribuciones de renta del hogar de los padres (ECPF/EPF, cabeza de hogar [A−2, A+2]). Se calcula la movilidad con los 3 métodos de cópula.

La **edad de estabilización** para cada cohorte es la primera edad A tal que |Δ(A')| < 2 pp para toda A' ≥ A, donde Δ(A) = mobility(A+2) − mobility(A).

#### Resultados

De 19 cohortes con ≥4 puntos de edad, 14 alcanzan la estabilización. La distribución de edades de estabilización es:

| Edad estabilización | N cohortes |
|---:|---:|
| 30 | 3 |
| 32 | 2 |
| 34 | 1 |
| 36 | 2 |
| 38 | 3 |
| 40 | 3 |
| No estabiliza | 5 |

**Mediana = 36 años** (IQR: 32–38). Las cohortes recientes (≥1988) estabilizan antes (30–32) porque alcanzan edades menores en los datos; las cohortes tempranas (1974–1981) requieren edades 38–40 para estabilizarse. La edad recomendada de medición es **36 años**, que es un compromiso entre estabilidad y cobertura de cohortes.

**Figura 13.** Perfil de movilidad por edad (cohortes seleccionadas).

![Perfil por edad](/assets/images/movilidad/age_profile_spain.png)

### 4.18. Sensibilidad a la brecha generacional G (extensión)

#### Motivación

La brecha generacional G — la diferencia de edad entre padres e hijos — determina qué año de renta parental se compara con cada cohorte de hijos: parent_year = cohort + (age − G). Chetty asume G=25 (valor medio en EEUU); en España, la edad media a la maternidad ha variado entre 28,2 (1970s) y 32,3 (2020s), lo que podría sesgar los resultados.

#### Diseño

Fijamos la edad de medición en el valor óptimo (36 años) y computamos la movilidad para G ∈ {25, 28, 30}. Esto implica offsets parent−child de 11, 8 y 6 años respectivamente.

#### Resultados

La diferencia media entre la movilidad más alta y más baja (variando G) para las cohortes con cobertura completa es de **3,8 pp** — superior al umbral de 2 pp, lo que indica que la brecha generacional **sí importa** en España. Las diferencias se acentúan para las cohortes recientes, donde G=30 produce movilidad más alta porque los padres se miden en años de renta más tardíos (y con rentas más altas).

**Tabla 12.** Calibración de G con datos demográficos del INE.

| Década | Edad media a la maternidad |
|--------|---------------------------:|
| 1960s | 28,8 |
| 1970s | 28,2 |
| 1980s | 28,5 |
| 1990s | 29,7 |
| 2000s | 30,8 |
| 2010s | 31,8 |
| 2020s | 32,3 |

*Nota.* Fuente: INE, Indicadores demográficos básicos. "Edad media a la maternidad" incluye todos los nacimientos, no solo los primogénitos.

La calibración recomendada es usar G=28 para las cohortes parentales de los 60s–70s (padres de las cohortes observadas 1973–1978) y G=30 para las posteriores. Sin embargo, dado que la sensibilidad es moderada (3,8 pp en media) y que el rango de G plausibles (25–30) es estrecho, el impacto en las conclusiones sustantivas es limitado.

**Figura 15.** Sensibilidad a la brecha generacional G.

![Sensibilidad G](/assets/images/movilidad/g_sensitivity.png)

### 4.19. Fuentes de datos alternativas y qué resolverían

Una contribución de este trabajo es identificar con precisión **qué resolverían** los datos de mejor calidad. La tabla siguiente resume las capacidades y limitaciones de las cuatro fuentes principales:

| Elemento | ECV/ECPF (este estudio) | IEF IRPF | Lab Oportunidades (AEAT+Padrón) | LIS |
|---|---|---|---|---|
| Renta por cohorte | Sí (miles/cohorte) | Sí (millones) | Sí (millones) | Sí (post-2007 bruta) |
| Renta familiar (pareja) | Sí (PB180/PB190) | Sí (fichero cónyuge) | Sí | Sí (var. relación) |
| Enlace padre-hijo | No (solo co-residentes) | No (NIF anonimizado) | **SÍ** (Padrón) | No (co-residentes) |
| Cópula observada | No | No | **SÍ** | No |
| Cotas LP útiles | **Sí** (nuestra contribución) | Sí (mejores marginales) | Innecesario (cópula conocida) | Sí |
| Regional (CCAA) | Inviable (muestras) | Sí (provincia) | Sí | Limitado |
| Serie temporal | 2006–2025 | 1999–2022 (panel) | Depende de convenio | 1980–2022 |
| Comparación internacional | No | No | No | **SÍ** (50+ países) |

*Nota.* IEF IRPF = muestra de 3,67M declaraciones del Instituto de Estudios Fiscales. Lab Oportunidades = proyecto AEAT+Padrón tipo Opportunity Atlas. LIS = Luxembourg Income Study. La referencia principal para el enlace padre-hijo en España es Soria y Medina (2025), "Spanish Opportunity Atlas 2.0", que demuestra la viabilidad del enlace vía Padrón municipal.

Las cotas LP (Sección 4.15) cuantifican exactamente lo que el Lab de Oportunidades resolvería: para la cohorte 1984, la movilidad podría estar entre 8% y 70%; con la cópula observada, tendríamos un punto único.

#### Pipeline completo a edad 40

Para consolidar estos resultados, el análisis a edad 40 replica íntegramente el pipeline ejecutado a edad 30. En concreto, el script `08_age40_robustness.py` produce:

- **4 escenarios de ajuste hogar/individual** (Baseline, A, B, C): la ordenación esperada se mantiene (A > B > C > Baseline), con movilidad media del 76% (escenario A, hogar-hogar) al 32% (Baseline, individual vs. hogar). El escenario C per-earner da una media del 45%.
- **Descomposición crecimiento vs. desigualdad** (referencia: cohorte 1981, movilidad máxima PE a edad 40 = 48,1%). A diferencia de la descomposición a edad 30 (donde el crecimiento explicaba la mayor parte), a edad 40 el rango de variación es tan reducido (~9 pp) que la descomposición tiene poca capacidad explicativa: ambos contrafactuales producen cambios modestos.
- **Sensibilidad a ρ**: los 7 valores de ρ entre 0 y 0,50 confirman que la variación entre cohortes es robusta al parámetro de la cópula. El rango de movilidad para ρ=0,34 (39%–48%) se comprime a 44%–52% con ρ=0,20 y se expande a 35%–44% con ρ=0,50, manteniendo el mismo perfil temporal plano.
- **Cópula co-residente re-estimada a edad 40** (hijos 38–42, padres 60–75): 1.050 pares con ambos ingresos positivos, ρ_Spearman = 0,083 [0,019; 0,146]. Este valor es aún más bajo que el estimado a edad 30 (0,161), consistente con la mayor selección de co-residentes adultos de 38–42 años (quienes a esa edad viven con sus padres representan una submuestra más extrema que los de 28–32).
- **Movilidad por sexo**: los hombres mantienen movilidad más estable (~50–57%) mientras que las mujeres muestran mayor variación (34%–53%), con un deterioro notable para las cohortes 1984–1986 que podría reflejar la persistencia de brechas de género en la renta laboral consolidada.

Las 11 figuras y 6 tablas producidas (con sufijo `_age40`) son los equivalentes exactos de los producidos a edad 30, permitiendo una comparación visual directa entre ambas edades de medición.

---

## 5. Discusión

### 5.1. Dos retratos de la movilidad española

El resultado más importante de este trabajo no es una cifra, sino una tensión. Los mismos datos, las mismas cohortes, la misma metodología producen dos diagnósticos cualitativamente distintos según la edad a la que se mida la renta:

**A edad ~30**, la movilidad per-earner cae del 75% (cohorte 1975) al 32% (cohorte 1984) — 43 pp en 9 cohortes. El patrón es robusto a la elección de cópula, al valor de ρ y al tratamiento del desajuste hogar/individual. La lectura directa es alarmante: un colapso de movilidad intergeneracional asociado a la Gran Recesión.

**A edad ~40**, con renta consolidada y datos parentales íntegramente observados, el panorama cambia radicalmente. La movilidad per-earner oscila entre 39% y 48% — un rango de apenas 9 pp, sin tendencia descendente clara. Con **renta del hogar**, la movilidad es del 72%–79% para todas las cohortes, comparable a Países Bajos o Noruega (Manduca et al. 2024). La incorporación masiva de la mujer al empleo y la formación de hogares con dos perceptores han sostenido la movilidad de hogar a niveles que la renta individual no refleja.

Ambos retratos son legítimos, y la diferencia entre ellos es en sí misma un hallazgo. Los 34 pp de divergencia (43 pp de caída a edad 30 menos 9 pp de rango a edad 40) cuantifican el efecto combinado de tres factores: (a) la precariedad del mercado laboral juvenil español, que deprime transitoriamente la renta a los 30; (b) la vulnerabilidad cíclica extrema de las cohortes que entraron al mercado durante la Gran Recesión; y (c) posibles artefactos en las distribuciones parentales extrapoladas para las cohortes tempranas a edad 30. El perfil de movilidad a 8 edades confirma que la renta laboral en España se estabiliza a una mediana de 36 años — considerablemente más tarde que los 30 usados por Chetty para EEUU, coherente con la dualidad contractual del mercado laboral español.

El diagnóstico correcto probablemente se sitúa entre ambos extremos: España tiene un problema real de movilidad intergeneracional (la movilidad per-earner nunca supera el 50% ni siquiera a edad 40), agravado por un problema específico de inserción laboral juvenil que lo hace parecer catastrófico cuando se mide a los 30. Pero discriminar cuánto hay de cada factor requiere datos que las encuestas no pueden proporcionar.

### 5.2. Comparación con Chetty et al.

Chetty et al. documentan un declive monotónico de la movilidad en EEUU: del 92% (cohorte 1940) al 50% (cohorte 1984). España muestra un patrón diferente en varios aspectos:

1. **La edad de medición importa mucho más que en EEUU**: a edad 30, la caída es abrupta y se concentra en las cohortes que alcanzaron esa edad durante la Gran Recesión (2008–2013); a edad 40, la misma caída se disipa casi por completo. En EEUU, donde la transición al empleo estable es más rápida, la renta a los 30 es buen predictor de la renta permanente. En España, la dualidad contractual y la emancipación tardía hacen que medir a los 30 capture tanto movilidad intergeneracional como precariedad juvenil, sin posibilidad de separar ambos efectos con datos de encuesta.

2. **Hay recuperación parcial**: las cohortes 1988–1992, que cumplieron 30 en 2018–2022 (recuperación económica), muestran un repunte a ~43–47%. Las cohortes 1993–1996 (generación COVID) vuelven a caer a ~39–40%.

3. **El motor de la caída es diferente**: Chetty et al. encuentran que en EEUU la desigualdad es el motor dominante (explicando ~70% de la caída). En España, el **menor crecimiento de la renta media** es el factor más importante (24% de la caída vs. 8% por desigualdad), con una parte sustancial (~68%) explicada por la interacción de ambos. La renta mediana de la cohorte 1984 es menos de la mitad que la de 1975.

4. **El nivel máximo español (~75%) es inferior al americano de postguerra (~92%)**, consistente con una distribución de renta más desigual en España que en el EEUU de postguerra y un crecimiento de la renta mediana más moderado. La Tabla 6 documenta esta diferencia con datos de Gini.

**Tabla 6.** Coeficiente de Gini: España vs. EEUU en momentos clave.

| Año | EEUU (familias) | España (World Bank) | Nota |
|----:|:---:|:---:|------|
| 1947 | 0,376 | n/d | Postguerra: *Great Compression* |
| 1968 | 0,348 | n/d | Mínimo histórico EEUU |
| 1980 | 0,365 | 0,345 | España: primeras EPF post-transición |
| 1985 | 0,389 | 0,344 | |
| 1990 | 0,396 | 0,320 | España: mínimo; EEUU: desigualdad creciente |
| 2000 | 0,433 | 0,341 | |
| 2013 | 0,455 | 0,362 | Post-Gran Recesión |
| 2023 | 0,452 | 0,334 | |

*Nota.* Las series no son estrictamente comparables: EEUU = Gini de renta familiar bruta (Census Bureau, CPS); España = Gini de renta disponible equivalente (World Bank). La serie española subestima la desigualdad relativa porque usa renta después de impuestos y transferencias y escala equivalente, mientras que la americana usa renta bruta. No hay datos de Gini para España anteriores a 1980.

En 1980, España y EEUU tenían Ginis superficialmente similares (~0,35), pero con dos matices cruciales. Primero, la serie española mide renta disponible equivalente (post-impuestos, post-transferencias, ajustada por tamaño del hogar) mientras que la americana mide renta bruta familiar: a igualdad de distribución subyacente, el Gini español sería mecánicamente más bajo. Segundo, y más importante para nuestro análisis: las cohortes parentales de Chetty (nacidos ~1910–1954) vivieron su juventud durante la *Great Compression* americana (1940s–1960s), cuando el Gini de familias cayó a 0,348 — un nivel de igualdad que España probablemente nunca alcanzó. Este menor punto de partida de desigualdad en EEUU, combinado con un crecimiento de la renta mediana más alto en la postguerra, explica por qué la movilidad absoluta americana pudo alcanzar el 92% mientras que la española se quedó en ~75%.

### 5.3. La revolución de género como motor de movilidad

La movilidad femenina es consistentemente superior a la masculina para las cohortes más antiguas (1973–1982). Esto se explica por un cambio estructural sin equivalente en el caso americano: la mediana de renta laboral de las madres era literalmente cero (más del 50% sin empleo remunerado), mientras que las hijas alcanzan ratios mujer/hombre de 0,86–0,91 para las cohortes recientes. La masiva incorporación de la mujer al empleo es probablemente el factor individual que más ha sostenido la movilidad absoluta agregada en España.

### 5.4. Limitaciones

- **Desajuste hogar/individual**: el principal reto metodológico. Las ECPF solo registran renta del hogar; la ECV da renta individual. Los tres escenarios de corrección dan resultados que difieren en ~30 puntos de nivel (baseline 35% vs. escenario B 60%). Solo datos que ofrezcan renta individual para ambas generaciones resolverían esta ambigüedad.
- **Renta laboral vs. renta total**: excluimos transferencias, rentas de capital y prestaciones. Esto subestima la renta de desempleados y exagera la caída durante la crisis. A la vez, la inclusión de ceros laborales (desempleados a los 28–32) es necesaria para evitar sesgo de selección pero deprime los percentiles inferiores.
- **Cópula asumida, no observada directamente**: no disponemos de enlace directo padre-hijo. La cópula estable es una hipótesis razonable; la estimación con co-residentes (ρ=0,16, Sección 4.12) sugiere un valor inferior al asumido (0,34), pero la muestra de co-residentes tiene sesgo de selección severo. Los resultados son robustos al valor de ρ en el rango 0,15–0,50.
- **Ventana de edad 28–32**: las cohortes más recientes pueden tener carreras laborales más tardías (efecto ciclo vital), lo que subestimaría su renta permanente. El análisis de robustez a edad ~40 (Sección 4.13) confirma que este efecto es significativo: la caída de movilidad se comprime de 43 pp a 9 pp cuando se mide a los 40.
- **Tamaño muestral**: las ECPF tienen ~800–1.000 hogares por año en la franja 28–32, suficiente para percentiles pero no para desagregaciones finas. Las cohortes extremas de hijos (1973, 1996) tienen menos de 600 observaciones.
- **EPF 80-81 (año 1980)**: esta encuesta da renta individual, pero es el ancla de la interpolación 1981–84 y la extrapolación 1978–79. Un error en el parsing de esta encuesta se propagaría a 7 años de distribuciones parentales.

---

## 6. La necesidad de datos fiscales (AEAT)

Este trabajo documenta una tensión que los datos de encuesta no pueden resolver: la movilidad absoluta de renta en España aparece en caída dramática o crónicamente baja pero estable, según se mida a los 30 o a los 40 años. Discriminar entre ambos diagnósticos — y cuantificar qué parte de la caída a edad 30 es transitoria y qué parte es estructural — requiere datos que solo la Agencia Tributaria puede proporcionar.

### 6.1. Lo que aportan los datos fiscales

Las declaraciones de IRPF de la AEAT —o la muestra de 3,67 millones de declaraciones del IEF— resolverían simultáneamente los tres principales problemas metodológicos de este estudio:

1. **Renta individual para ambas generaciones**: la base imponible general del IRPF es renta individual del declarante, eliminando la ambigüedad hogar/individual que domina nuestra incertidumbre (la diferencia entre los escenarios B y C es de ~12 puntos de movilidad).

2. **Enlace directo padre-hijo**: a través de las declaraciones conjuntas, los dependientes económicos o el cruce por NIF familiar, sería posible **observar la cópula directamente** (como hizo Chetty con los datos del IRS para las cohortes 1980–82), en lugar de asumirla estable.

3. **Millones de observaciones**: frente a los ~800–1.000 hogares por año de las ECPF y los ~1.500–2.500 individuos por cohorte de la ECV, los datos fiscales permitirían:
   - Estimar la movilidad por CCAA con muestras suficientes.
   - Distinguir renta permanente (promedio de varios años) de renta corriente.
   - Desagregar por sector, tipo de contrato o nivel educativo.

### 6.2. Extensiones pendientes

Sin acceso a datos fiscales, las mejoras restantes incluyen:

1. **Módulo intergeneracional EU-SILC 2011**: no disponible vía INE (requiere acceso acreditado a Eurostat), pero contiene educación y ocupación de los padres del encuestado a los ~14 años, lo que permitiría estimar la cópula de forma indirecta.

2. **IPC sin vivienda**: para controlar el efecto de la burbuja inmobiliaria sobre el poder adquisitivo real (la serie de IPC−0,8% ya captura parte de este efecto).

3. **Variación por CCAA**: inviable con la ECV (muestras insuficientes por comunidad en la franja 28–32), pero factible con datos fiscales.

4. **Calibración G variable por cohorte**: usar G(cohort) = edad media a la maternidad en el año de nacimiento de cada cohorte, en vez de G fijo.

---

## Referencias

- Chetty, R., Grusky, D., Hell, M., Hendren, N., Manduca, R. y Naidu, S. (2017). "The Fading American Dream: Trends in Absolute Income Mobility Since 1940." *Science*, 356(6336), 398–406.

- Manduca, R., Hell, M., Adermon, A., Blanden, J., Bratberg, E., Eriksson, K., ... y Vosters, K. (2024). "Trends in Absolute Income Mobility in North America and Europe." *American Economic Journal: Applied Economics*, 16(2), 1–30.

- INE (2006–2025). *Encuesta de Condiciones de Vida. Microdatos.* Instituto Nacional de Estadística.

- INE (1980–2005). *Encuesta de Presupuestos Familiares / Encuesta Continua de Presupuestos Familiares. Microdatos.* Instituto Nacional de Estadística.

- INE (1961–2026). *Índice de Precios de Consumo. Serie enlazada.* Instituto Nacional de Estadística. Tablas 268 y 24077.

- OCDE (2018). *A Broken Social Elevator? How to Promote Social Mobility.* OECD Publishing.

- Soria, J. y Medina, P. (2025). "Spanish Opportunity Atlas 2.0." Working paper. [Enlace padre-hijo vía Padrón municipal + datos AEAT.]

*Fuentes: INE (ECV 2006–2025, EPF 1980–81 y 1990–91, ECPF Base 85 y Base 97, IPC enlazado).*
