---
layout: post
title: "La Encuesta Financiera de las Familias: qué mide, qué no, y cómo de bien"
date: 2026-02-11
series: impuestos
part: 4
---

*Este es el cuarto artículo de una [serie](https://statisticspeek.github.io/) sobre fiscalidad y desigualdad en España.
En el [tercer artículo](/2026/02/11/distribucion-riqueza-espana.html) analizamos la
distribución de la riqueza usando los microdatos de la EFF. Este artículo examina
la fiabilidad del instrumento de medida: la propia encuesta. Antes de interpretar
los datos, conviene saber qué captura bien, qué captura mal, y qué deja fuera.*

---

## Resumen

La Encuesta Financiera de las Familias (EFF) es la mejor fuente disponible para
estudiar la distribución de la riqueza en España a nivel micro. Ocho olas
(2002-2022) proporcionan 20 años de datos con metodología consistente. Sin embargo,
un análisis de sus microdatos revela limitaciones significativas:

- **Solo ~6.300 hogares** representan a 18,8 millones. El tamaño muestral efectivo
  se reduce a **1.100-1.800 hogares** por el efecto del sobremuestreo de ricos
  (DEFF = 2,2-4,2).
- **El 40-45% de los hogares contactados rechazan participar**, y la no respuesta
  es selectiva: los más ricos y los más excluidos cooperan menos.
- La encuesta **captura solo el 53% de los depósitos** y el 60-70% del valor
  inmobiliario con respecto a las Cuentas Nacionales. Las deudas, en cambio,
  se capturan bien (95-107%).
- **La renta es la variable más resistida**: las variables de ingreso detallado
  presentan tasas de imputación superiores al 99%.
- El **top 0,1%** (grandes fortunas, patrimonio offshore, trusts) es prácticamente
  invisible incluso con el sobremuestreo.

A pesar de todo, la EFF es fiable para **analizar tendencias temporales**: sus
sesgos son estables entre olas, de modo que las variaciones relativas
(la mediana bajó un 30% entre 2008 y 2014) son más creíbles que los niveles
absolutos. El investigador debe interpretar los datos como un **suelo** de la
desigualdad real.

---

## 1. Qué es la EFF y por qué importa

La Encuesta Financiera de las Familias es una operación estadística del
**Banco de España** que recopila información detallada sobre ingresos, activos,
deudas y gasto de los hogares españoles. Se enmarca en la Household Finance and
Consumption Survey (HFCS) del Eurosistema, lo que permite comparaciones
internacionales.

Desde 2002, se ha realizado cada tres años (2002, 2005, 2008, 2011, 2014, 2017,
2020) y desde 2020 pasa a ser bienal (2020, 2022). Cada ola entrevista a
unos 6.000-6.400 hogares.

**¿Por qué no usar datos fiscales directamente?** Porque los datos fiscales
solo capturan lo que se declara y lo que la ley obliga a declarar. No incluyen
activos exentos, riqueza en especie, ni a los hogares que no tributan patrimonio.
La EFF pregunta directamente a las familias, incluyendo a las que no presentan
declaración de patrimonio.

### 1.1 Veinte años de datos: qué ha revelado la EFF

El propio Banco de España
[celebra los 20 años de la encuesta](https://www.bde.es/wbe/es/noticias-eventos/blog/el-analisis-de-la-riqueza-en-espana-20-anos-de-la-encuesta-financiera-de-las-familias.html)
destacando tres características distintivas:

1. **Información exhaustiva en una sola base de datos**: activos, propiedades,
   fuentes de ingreso, situación laboral, deudas y gastos de los hogares
   españoles, con más de dos décadas de profundidad temporal.
2. **Representatividad de la riqueza total**: mediante el sobremuestreo de
   hogares ricos, que están infrarrepresentados en otras encuestas pese a
   concentrar una proporción desproporcionada de la riqueza nacional.
3. **Seguimiento longitudinal**: los mismos hogares se reentrevistan en
   sucesivas olas, permitiendo analizar cómo evolucionan la renta y la riqueza
   a lo largo de la vida.

Antes de 2002, no existía ninguna fuente que permitiera un análisis riguroso
de la situación financiera de las familias españolas. La EFF llenó ese vacío.

Entre los hallazgos más relevantes que los 20 años de datos han permitido
documentar destaca la **fractura generacional** en el acceso a la vivienda y la
acumulación de riqueza:

- Las generaciones nacidas entre 1945 y 1965 alcanzaron una tasa de propiedad
  de vivienda del **81%** a los 42 años.
- Las nacidas entre 1975 y 1985 solo alcanzan el **67%** a la misma edad:
  14 puntos porcentuales menos.
- En riqueza neta mediana, los nacidos en torno a 1960 acumulaban unos
  **200.000 EUR** a los 45 años. Los nacidos en torno a 1980 solo llegan a
  **107.000 EUR** a la misma edad — casi un **50% menos**.

Estas tendencias, invisibles en datos agregados, solo pueden documentarse con
una encuesta como la EFF que combine detalle micro, sobremuestreo del patrimonio
alto y seguimiento longitudinal.

---

## 2. Diseño muestral: quién se entrevista

### 2.1 Tamaño muestral y población representada

Del análisis directo de los microdatos (imputación 1 de cada ola):

| Edición | Hogares entrevistados | Población representada | Variables hogar | Variables individuo |
|---|---|---|---|---|
| 2002 | 5.143 | ~14,2 M | 813 | 2.243 |
| 2005 | 5.962 | ~15,4 M | 880 | 2.216 |
| 2008 | 6.197 | ~16,0 M | 1.088 | 1.508 |
| 2011 | 6.106 | ~17,1 M | 1.076 | 1.516 |
| 2014 | 6.120 | ~18,1 M | 1.179 | 1.513 |
| 2017 | 6.413 | ~18,4 M | 1.283 | 1.586 |
| 2020 | 6.313 | ~18,5 M | 1.356 | 1.676 |
| 2022 | 6.385 | ~18,8 M | 1.346 | 1.667 |

Cada hogar del fichero `otras_secciones` representa de media a **2.950 hogares
españoles**. Pero la distribución de pesos es enormemente desigual, como veremos
a continuación.

### 2.2 El sobremuestreo de hogares ricos

La distribución de la riqueza es extremadamente asimétrica: el 10% más rico
posee más del 50% de toda la riqueza. En una muestra aleatoria simple de 6.000
hogares, habría quizá 60 hogares en el top 1% — demasiado pocos para estimar
con precisión.

Para resolver esto, la EFF utiliza una colaboración entre el **INE** y la
**Agencia Tributaria** mediante un sistema ciego que preserva la confidencialidad
fiscal. El INE selecciona la muestra, pero la probabilidad de selección depende
del estrato de riqueza estimado a partir de datos del Impuesto sobre el
Patrimonio. Los hogares ricos tienen mayor probabilidad de ser seleccionados.

La consecuencia es que los **pesos muestrales** varían enormemente:

| Edición | Peso mínimo | Peso máximo | Ratio max/min | Peso medio |
|---|---|---|---|---|
| 2022 | 1,7 | 61.487 | 37.026 | 4.736 |
| 2020 | 2,3 | 85.841 | 37.584 | 4.839 |
| 2017 | 3,5 | 97.944 | 28.336 | 5.053 |
| 2014 | ~0 | 197.752 | ∞ | 2.950 |

Un hogar de la muestra de riqueza media puede representar a 60.000-98.000
hogares reales, mientras que un hogar del estrato más rico representa solo a
1-4 hogares. Esta desigualdad de pesos es necesaria pero tiene un coste: reduce
la **precisión estadística efectiva**.

### 2.3 Efecto diseño y tamaño muestral efectivo

El efecto diseño (DEFF) mide cuánta precisión se pierde por no usar una muestra
aleatoria simple. Un DEFF de 3 significa que la muestra equivale a un tercio
de su tamaño nominal en una muestra aleatoria simple.

Calculado a partir de la fórmula de Kish sobre los pesos `pesopan_1`
(componente transversal del panel):

| Edición | N con peso > 0 | N efectivo (Kish) | DEFF |
|---|---|---|---|
| 2022 | 3.974 | 1.839 | **2,16** |
| 2020 | 3.831 | 1.355 | **2,83** |
| 2017 | 3.634 | 1.148 | **3,16** |
| 2014 | 3.060 | 722 | **4,24** |
| 2011 | 3.711 | 924 | **4,02** |
| 2008 | 3.967 | 1.209 | **3,28** |
| 2005 | 2.580 | 896 | **2,88** |

**Interpretación**: la EFF 2022 tiene 6.385 hogares en el fichero, pero solo
3.974 tienen peso transversal positivo (el resto son hogares del panel sin peso
para análisis cross-section). De esos 3.974, la precisión equivale a unos
**1.839 hogares** en muestra aleatoria simple. Para la EFF 2014, apenas
**722 hogares equivalentes**.

Esto implica que las estimaciones para subgrupos pequeños (hogares jóvenes ricos,
monoparentales con negocios propios, etc.) tienen intervalos de confianza muy
amplios.

---

## 3. Método de recogida: entrevistas presenciales

### 3.1 CAPI: Computer Assisted Personal Interview

Las entrevistas de la EFF son **presenciales**, realizadas por entrevistadores
profesionales que visitan el hogar con un portátil. El cuestionario se administra
mediante software CAPI (Computer Assisted Personal Interview) que guía el flujo
de preguntas, valida respuestas en tiempo real y minimiza errores de registro.

La duración media de la entrevista es de **1 a 2 horas**, lo que permite un
nivel de detalle imposible en encuestas telefónicas o por internet. Se pregunta
sobre:

- Todos los inmuebles (vivienda principal, otras propiedades, terrenos)
- Todos los activos financieros (cuentas, fondos, acciones, planes de pensiones)
- Todos los préstamos y deudas (hipotecas, créditos al consumo, tarjetas)
- Negocios propios (tipo, valoración, deudas del negocio)
- Ingresos de todos los miembros del hogar
- Herencias y donaciones recibidas

### 3.2 La excepción del COVID

En la ola de 2020, debido a las restricciones sanitarias, un **11% de las
entrevistas se realizaron por teléfono (CATI)**. Esto introduce un potencial
sesgo de modo de recogida: las entrevistas telefónicas tienden a ser más cortas
y a obtener menos detalle en preguntas complejas sobre activos. En 2022 se volvió
mayoritariamente al formato presencial.

---

## 4. No respuesta: el problema principal

### 4.1 La magnitud del problema

La tasa de cooperación de la EFF se sitúa en torno al **55-60%**. Es decir,
**4 de cada 10 hogares contactados rechazan participar**. Esto es habitual en
encuestas voluntarias de riqueza a nivel internacional (la Survey of Consumer
Finances de EE.UU. tiene tasas similares), pero es preocupante por la naturaleza
de la variable de interés.

### 4.2 La no respuesta no es aleatoria

El problema no es que falte un 40% de respuestas — eso simplemente reduce el
tamaño muestral. El problema es que **quién no responde está correlacionado con
lo que se quiere medir**:

- **Los hogares más ricos** cooperan menos. Sus situaciones financieras son
  complejas (múltiples propiedades, inversiones internacionales, participaciones
  empresariales) y tienen más razones para la reserva. Exactamente los hogares
  que más afectan a las estimaciones de la cola superior de la distribución.
- **Los hogares más vulnerables** (exclusión social, irregularidad administrativa,
  barrera lingüística) también son difíciles de alcanzar.
- **Los hogares móviles** (jóvenes que cambian de domicilio, inmigrantes recientes)
  se pierden con mayor frecuencia en el componente panel.

### 4.3 Qué se hace para corregirlo

El Banco de España aplica dos correcciones:

1. **Ajuste de factores de elevación**: los pesos muestrales se recalibran para
   que la muestra resultante reproduzca la distribución conocida de la población
   por variables demográficas (tamaño del hogar, edad del cabeza de familia,
   CCAA, estrato de riqueza).

2. **Calibración con fuentes externas**: los pesos se ajustan para que los
   totales muestrales coincidan con los del Padrón y el Censo.

Sin embargo, estas correcciones solo funcionan si la no respuesta depende de
variables observables. Si la no respuesta depende de la propia riqueza (que es
lo que nos tememos), el sesgo residual persiste.

### 4.4 Contraste con encuestas obligatorias

Comparemos con la **EPA** (Encuesta de Población Activa), que en el período
1976-1985 era **obligatoria por ley**:

| Aspecto | EPA 1976-1985 | EFF 2002-2022 |
|---|---|---|
| Muestra | ~60.000 hogares/trimestre | ~6.300 hogares/ola |
| Frecuencia | Trimestral | Trienal → bienal |
| Obligatoriedad | Sí (ley estadística) | No, voluntaria |
| Tasa de respuesta | >90% | ~55-60% |
| Método | Presencial | Presencial (CAPI) |
| Ruptura metodológica | 1987T3 (adaptación OIT/CEE) | Sin rupturas mayores |
| Problema central | Cambios de definición (desempleo, actividad) | No respuesta selectiva |
| Economía sumergida | No capturada | No capturada |

La EPA de los 70 y 80 tenía mucha mayor tasa de respuesta — pero pagaba un
precio diferente: las **definiciones de actividad, empleo y desempleo** cambiaron
varias veces durante ese período. La gran revisión de 1987T3, que adaptó la EPA
a los estándares de la OIT y la CEE con motivo de la entrada de España en la
Comunidad Europea, implicó recalcular retrospectivamente las series desde 1976T3.
Antes de esa revisión, la EPA clasificaba de forma distinta a trabajadores
agrícolas estacionales, servicio militar, y buscadores de primer empleo, creando
discontinuidades difíciles de trazar.

La EFF tiene la ventaja inversa: **metodología muy estable** durante sus 20 años
de existencia, pero con un sesgo de selección potencialmente más severo al ser
voluntaria. La EPA medía bien *quién* participaba en el mercado laboral pero
con definiciones cambiantes de *qué significaba* estar activo; la EFF mide con
definiciones estables pero no está segura de *a quién* está midiendo.

---

## 5. Imputación: cuánto se estima y cuánto se observa

### 5.1 Las variables sombra

Cuando un hogar participa pero se niega a responder ciertas preguntas
(*item non-response*), el Banco de España no deja un hueco: **imputa** el valor
faltante usando modelos estadísticos basados en las variables sí observadas.
Para cuantificar la incertidumbre de estas imputaciones, se generan **5 conjuntos
de datos** (implicados), cada uno con diferentes valores imputados.

El fichero `sombra_YYYY.dta` indica para cada variable y cada hogar si el valor
fue observado (0) o imputado (≠0). Nuestro análisis directo de estos ficheros
revela:

| Edición | Variables sombra | Tasa media imputación | Variables con >30% imputación |
|---|---|---|---|
| 2022 | 2.848 | 7,8% | 251 (8,8%) |
| 2020 | 2.872 | 7,6% | 228 (7,9%) |
| 2017 | 2.712 | 7,5% | 206 (7,6%) |
| 2008 | 2.470 | 7,4% | 191 (7,7%) |
| 2002 | 2.967 | 5,6% | 172 (5,8%) |

La media general (~7-8%) es baja, pero oculta una distribución bimodal: la
mayoría de variables tienen tasas de imputación bajas (<5%), mientras que un
grupo de variables tiene tasas superiores al 95%.

### 5.2 Qué es lo que más se imputa

Las **10 variables más imputadas** en la EFF 2022 (todas con tasas ≥99%):

| Variable | Tasa imputación | Contenido |
|---|---|---|
| `j9_2b` | 100,0% | Componente de renta del hogar |
| `j4_2` - `j4_6` | 99,9% | Ingresos detallados por fuente |
| `j4_7_3` | 99,9% | Ingresos adicionales |
| `jrenthog` | 100,0% | Renta total del hogar (variable derivada) |

La variable de **renta del hogar** — una de las más importantes para cualquier
análisis — está imputada casi en su totalidad en el fichero de microdatos. Esto
no significa que sea una invención: el modelo de imputación utiliza las respuestas
parciales del hogar (tipo de trabajo, sector, categoría de ingresos cuando se da
en tramos) junto con las variables observadas. Pero es un dato sintético, no un
dato declarado directamente.

### 5.3 Estabilidad entre las 5 imputaciones

La variabilidad entre los 5 conjuntos imputados mide cuánta incertidumbre
introduce el proceso de imputación. De nuestro análisis:

| Variable | CV entre imputaciones (2022) | CV entre imputaciones (2020) |
|---|---|---|
| Riqueza neta (`riquezanet`) | 1,2% | 3,6% |
| Riqueza bruta (`riquezabr`) | 1,2% | 3,6% |
| Renta del hogar | 0,1% | 0,2% |
| Deuda (`vdeuda`) | 0,3% | 0,4% |

La variación entre imputaciones es inferior al 4% para todas las variables
clave, lo que indica que el **modelo de imputación es estable**: las 5 versiones
del dataset producen resultados similares. Pero estabilidad no es sinónimo de
ausencia de sesgo — un modelo podría imputar de forma consistentemente errónea.

---

## 6. El test de realidad: EFF vs. Cuentas Nacionales

La prueba más exigente de una encuesta de riqueza es comparar sus totales
agregados con las **Cuentas Financieras** y la **Contabilidad Nacional**, que
se compilan de forma independiente a partir de registros administrativos.

Según el análisis comparativo publicado por SUERF:

### 6.1 Activos

| Componente | % capturado por EFF (2020) | Tendencia 2002→2020 |
|---|---|---|
| **Depósitos bancarios** | **53,5%** | Estable (siempre bajo) |
| Acciones cotizadas | 117% | Mejora (59% → 117%) |
| Acciones no cotizadas | 89% | Mejora (60% → 89%) |
| Vivienda | 60-70% | Estable |

### 6.2 Pasivos

| Componente | % capturado por EFF (2020) | Tendencia |
|---|---|---|
| **Deuda total** | **95%** | Mejora (60% → 95%) |
| Hipotecas | 107% | Mejora (67% → 107%) |

### 6.3 Renta

| Comparación | Ratio EFF/fuente |
|---|---|
| EFF vs. EU-SILC | ~100% |
| EFF vs. Contabilidad Nacional | ~85% |

### 6.4 Interpretación

Los **depósitos están masivamente infradeclarados**: la encuesta solo capta la
mitad de lo que las Cuentas Financieras registran. Esto probablemente combina
infradeclaración deliberada (la gente minimiza sus ahorros líquidos) y
dificultad para contabilizar depósitos empresariales que pertenecen indirectamente
a hogares.

La **vivienda** se captura al 60-70%, en parte porque la EFF recoge
autovaloraciones del hogar que pueden diferir de los valores de mercado, y en
parte porque las Cuentas Nacionales asignan toda la vivienda al sector hogares
(ignorando la propiedad institucional).

En cambio, las **deudas se reportan bien** (95-107%). Es significativo: la gente
es más precisa declarando lo que debe que lo que tiene.

Las **acciones cotizadas** incluso superan el agregado (117%), lo que sugiere que
el sobremuestreo de ricos funciona bien para este tipo de activo concentrado en
las colas.

---

## 7. Qué queda fuera: los ángulos muertos

### 7.1 Poblaciones no cubiertas

- **Hogares institucionales**: residencias de mayores, centros de acogida,
  prisiones. Estas personas tienen patrimonio (o la ausencia de él) pero no
  aparecen en la muestra.
- **Personas sin hogar**: completamente invisibles en cualquier encuesta basada
  en viviendas.
- **Ultra-ricos** (top 0,01%): a pesar del sobremuestreo, las grandes fortunas
  familiares con patrimonio diversificado internacionalmente, trusts y
  estructuras societarias complejas son prácticamente imposibles de alcanzar
  y encuestar.
- **Inmigrantes irregulares**: no están en el marco muestral del INE.
- **Nómadas fiscales**: personas con residencia fiscal difusa o en transición.

### 7.2 Activos mal cubiertos o no cubiertos

- **Criptoactivos**: no se preguntaba hasta fechas recientes. Aun preguntando,
  la infradeclaración sería alta.
- **Activos en el extranjero**: una familia con un apartamento en Londres o una
  cuenta en Suiza puede no declararlos (o infravalorarlos).
- **Seguros de vida con componente de ahorro**: cobertura parcial y confusa.
- **Obras de arte, joyería, colecciones**: riqueza informal no preguntada.
- **Efectivo fuera del sistema bancario**: imposible de medir.
- **Capital humano**: el valor presente de los ingresos futuros de una persona
  no se mide, pero es la principal "riqueza" de los hogares jóvenes.

### 7.3 Problemas de medición en lo que sí se cubre

- **Valoración de inmuebles**: se pide al hogar que estime el valor de mercado
  de su vivienda. Es una autovaloración, no un precio de transacción ni una
  tasación profesional. Puede estar inflada (sesgo optimista del propietario)
  o desfasada.
- **Negocios propios**: se pide estimar cuánto se obtendría vendiendo el
  negocio. Para pequeños comercios o profesionales liberales, esta valoración
  es altamente especulativa.
- **Renta**: se refiere al año anterior a la entrevista, no al momento de la
  encuesta. Esto introduce un desfase temporal, especialmente relevante en
  años de cambio de ciclo.

---

## 8. La dimensión panel: seguimiento longitudinal

### 8.1 Estructura del panel

La EFF reentrevista a una fracción de los hogares de olas anteriores, lo que
permite seguir la evolución de los mismos hogares en el tiempo. Del análisis
de las variables `pan_1` y `pan_2` en los microdatos:

| Edición | Hogares panel (reentrevistados) | Hogares nuevos | % panel |
|---|---|---|---|
| 2022 | 3.974 | 2.411 | 62,2% |
| 2020 | 3.831 | 2.482 | 60,7% |
| 2017 | 3.634 | 2.779 | 56,7% |
| 2014 | 3.060 | 3.060 | 50,0% |
| 2011 | 3.711 | 2.395 | 60,8% |

### 8.2 Atrición

La atrición entre olas es del **30-40%**: de los hogares entrevistados en una
ola, un tercio a dos quintos no vuelve a participar en la siguiente. Las causas
incluyen:

- Cambio de domicilio (especialmente hogares jóvenes)
- Fallecimiento o disolución del hogar
- Rechazo a repetir la entrevista
- Imposibilidad de contacto

La atrición **no es aleatoria**: los hogares que abandonan el panel tienden a
ser más jóvenes, más móviles, o en situaciones de estrés financiero. Esto
introduce un sesgo de supervivencia en los análisis longitudinales: los hogares
que seguimos durante múltiples olas son, en promedio, más estables y
posiblemente más acomodados que los que perdemos.

---

## 9. Riqueza estimada: qué dicen los datos

### 9.1 Estimaciones ponderadas principales

Del análisis directo de los microdatos (imputación 1, pesos transversales
`pesopan_1`):

**Riqueza neta** (EUR):

| Edición | Media | Mediana | P10 | P90 | P99 |
|---|---|---|---|---|---|
| 2022 | 293.214 | 145.473 | 220 | 655.200 | 2.471.842 |
| 2020 | 263.814 | 125.100 | -167 | 561.181 | 2.064.689 |
| 2017 | 259.831 | 122.323 | 87 | 534.402 | 2.035.000 |
| 2014 | 265.954 | 124.399 | 100 | 524.940 | 2.212.926 |
| 2008 | 296.659 | 183.304 | 10.169 | 628.860 | 1.940.652 |

**Renta del hogar** (EUR):

| Edición | Media | Mediana |
|---|---|---|
| 2022 | 42.520 | 32.559 |
| 2020 | 37.793 | 29.344 |
| 2017 | 36.796 | 26.895 |
| 2014 | 31.542 | 22.761 |
| 2008 | 34.907 | 26.506 |

### 9.2 Lo que revelan estos números

1. **La mediana de riqueza neta se desplomó entre 2008 y 2014** (de 183.304 a
   124.399 EUR, un -32%), reflejando el impacto del estallido de la burbuja
   inmobiliaria y la crisis financiera.

2. **La recuperación posterior ha sido lenta**: en 2022 la mediana (145.473 EUR)
   aún está un 21% por debajo del nivel de 2008.

3. **El P10 muestra la fragilidad de la base**: en 2008, el hogar en el percentil
   10 tenía 10.169 EUR; en 2014-2022, apenas tiene 100-220 EUR. La crisis
   destruyó el escaso colchón financiero de los hogares más vulnerables.

4. **El P99 crece**: de 1,9 M€ en 2008 a 2,5 M€ en 2022. Los hogares más ricos
   no solo se recuperaron sino que superaron los niveles precrisis.

---

## 10. Veredicto: ¿es fiable la EFF?

### Lo que hace bien

- **Mejor fuente micro sobre riqueza en España**, y una de las mejores de
  Europa. No hay alternativa comparable.
- **Sobremuestreo de ricos** bien diseñado, con apoyo de datos fiscales reales,
  que mejora la cobertura de la cola superior de la distribución.
- **5 imputaciones múltiples** que permiten cuantificar la incertidumbre de los
  datos faltantes.
- **Entrevistas presenciales** largas y detalladas, con entrevistadores
  profesionales.
- **20 años de serie temporal** (2002-2022, 8 olas) con metodología consistente,
  sin rupturas mayores.
- **Componente panel** que permite análisis longitudinal a nivel de hogar.
- **Buena cobertura de deudas** (95-107% del agregado), acciones cotizadas
  (117%) y renta (85-100% según la fuente de comparación).

### Lo que hace mal o no hace

- **Subestimación sistemática de depósitos** (solo capta el 53%).
- **No respuesta selectiva** del 40-45%, correlacionada con la variable de
  interés (riqueza).
- **Tamaño muestral efectivo reducido** (DEFF 2-4) que limita la precisión para
  subgrupos.
- **El top 0,1% es invisible**: grandes fortunas, patrimonio offshore, trusts y
  estructuras societarias complejas quedan fuera.
- **Autovaloración de inmuebles y negocios** en vez de valores de mercado o
  tasaciones.
- **Sin cobertura de hogares institucionales**, personas sin hogar ni economía
  sumergida.
- **Renta casi totalmente imputada** a nivel de detalle (tasas >99% en las
  variables j4_x de ingresos por fuente).
- **Frecuencia trienal/bienal** que impide capturar dinámicas de corto plazo.

### Recomendación para el investigador

Los datos de la EFF deben interpretarse como un **suelo** de la desigualdad
real. La concentración de riqueza es probablemente **mayor** que la que la
encuesta indica. Los niveles absolutos tienen márgenes de error amplios, pero
las **tendencias temporales son fiables** porque los sesgos son estables entre
olas.

Para los estudios de esta serie, utilizamos la EFF como fuente principal,
complementada con las estimaciones ajustadas de FEDEA y WID.world cuando estas
aportan correcciones relevantes (especialmente para el top 1%).

---

## Fuentes y referencias

- Banco de España (2024). *Encuesta Financiera de las Familias (EFF) 2022:
  métodos, resultados y cambios desde 2020*. Documentos Ocasionales 2413.
  [Enlace](https://www.bde.es/wbe/en/publicaciones/analisis-economico-investigacion/documentos-ocasionales/encuesta-financiera-de-las-familias--eff--2022--metodos--resultados-y-cambios-desde-2020.html)

- Banco de España (2024). *El análisis de la riqueza en España: 20 años de la
  Encuesta Financiera de las Familias*. Blog BdE.
  [Enlace](https://www.bde.es/wbe/en/noticias-eventos/blog/el-analisis-de-la-riqueza-en-espana-20-anos-de-la-encuesta-financiera-de-las-familias.html)

- Bover, O. (2008). *The oversampling of the wealthy in the Spanish Survey of
  Household Finances*. BIS IFC Bulletin No. 28.
  [Enlace](https://www.bis.org/ifc/publ/ifcb28zzm.pdf)

- SUERF (2024). *Micro and macro data on household wealth, income and
  expenditure: comparing the Spanish Survey of Household Finances (EFF) to
  other statistical sources*.
  [Enlace](https://www.suerf.org/publications/suerf-policy-notes-and-briefs/micro-and-macro-data-on-household-wealth-income-and-expenditure-comparing-the-spanish-survey-of-household-finances-eff-to-other-statistical-sources/)

- FEDEA (2025). *Evolución de la Riqueza de las Familias en España (2002-2022)*.
  Estudios sobre la Economía Española 2025-23.
  [Enlace](https://documentos.fedea.net/pubs/eee/2025/eee2025-23.pdf)

- INE. *Encuesta de Población Activa: Metodología*.
  [Enlace](https://www.ine.es/daco/daco43/resumetepa.pdf)

- García-Ferrer, A. y Queralt, D. (1997). *Evolución de la población activa,
  ocupación y paro en España 1976-1996*. Política y Sociedad, 26, 113-130.
  [Enlace](https://revistas.ucm.es/index.php/POSO/article/download/POSO9797330113A/25117/26278)

---

*Los análisis de este artículo se basan en la explotación directa de los
microdatos de la EFF (todas las olas, 2002-2022), obtenidos del Banco de España
previa solicitud de acceso. Los cálculos de DEFF, tasas de imputación y
estadísticas ponderadas son propios, realizados sobre los ficheros Stata
originales.*
