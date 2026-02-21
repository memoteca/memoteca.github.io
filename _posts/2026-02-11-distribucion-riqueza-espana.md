---
layout: post
title: "Distribución de la riqueza en España: quién posee qué y cómo tributa"
date: 2026-02-11
series: impuestos
part: 3
---

*Este es el tercer artículo de una [serie](https://statisticspeek.github.io/) sobre fiscalidad y desigualdad en España.
En el [primer artículo](/2026/02/09/impuestos-progresivos-espana.html) calculamos
la carga fiscal bruta del asalariado y encontramos una U invertida. En el
[segundo artículo](/2026/02/10/transferencias-carga-neta-espana.html) añadimos las
transferencias del Estado y medimos la carga neta. Ambos estudios se centraron en
los flujos: lo que el ciudadano paga y lo que recibe. Este tercer estudio mira el
stock: la riqueza acumulada, cómo se distribuye y cómo se grava.*

---

## Resumen

La desigualdad de riqueza en España es mucho mayor que la de renta. El índice
de Gini del patrimonio neto alcanza el **0,687** (2022), frente al 0,497 de la
renta bruta. El 1% más rico posee el **21,1%** de toda la riqueza, mientras que
la mitad más pobre de los hogares posee apenas el **7,1%**.

Además, la desigualdad va en aumento: el Gini ha pasado de 0,576 (2002) a 0,687
(2022) en apenas dos décadas, y la participación del top 1% ha crecido de 13,6%
a 21,1% en el mismo período.

Sin embargo, el sistema tributario apenas grava la riqueza. Los cuatro impuestos
patrimoniales —Patrimonio (IP), Grandes Fortunas (ITSGF), Sucesiones y Donaciones
(ISD) e Impuesto sobre Bienes Inmuebles (IBI)— recaudan en conjunto unos
**19.080 millones de euros**, apenas un **4,3%** de la recaudación tributaria total.
A modo de comparación, solo el IRPF recauda 115.000 M€ y las cotizaciones a la
Seguridad Social 180.000 M€.

El estudio revela además una **fractura generacional** en expansión: los menores
de 35 años tienen una riqueza mediana de 20.000 EUR, frente a 226.000 EUR de los
mayores de 65. La brecha se ha multiplicado por 7 en veinte años.

---

## 1. Introducción

### 1.1 Motivación

Los Estudios 1 y 2 de esta serie respondieron a dos preguntas fundamentales:
**quién paga** (la carga fiscal bruta) y **quién recibe** (las transferencias
del Estado). Pero un análisis fiscal completo requiere una tercera dimensión:
**quién posee**.

La renta es un flujo anual; la riqueza es un stock acumulado. Un hogar puede
tener una renta modesta pero poseer un patrimonio elevado (el jubilado propietario
de su vivienda) o, al contrario, una renta alta con patrimonio nulo (el joven
profesional que alquila). Gravar la renta sin considerar la riqueza es mirar solo
la mitad de la ecuación.

### 1.2 Hipótesis

1. La desigualdad de riqueza es significativamente mayor que la de renta.
2. La riqueza española está concentrada en activos inmobiliarios, lo que la hace
   ilíquida y vulnerable a ciclos inmobiliarios.
3. Los impuestos sobre la riqueza recaudan una fracción marginal del total.
4. Existe una fractura generacional creciente en el acceso al patrimonio.

### 1.3 Alcance y limitaciones

- **Ámbito**: hogares españoles, datos 2022 (con series históricas 2002-2022).
- **Fuentes**: BdE (EFF 2022), FEDEA, AEAT, HFCS/BCE.
- **Limitación principal**: las encuestas infraestiman la riqueza de los hogares
  más ricos. FEDEA estima que el top 1% posee el 21,1%, pero WID.world (que
  ajusta con datos fiscales y cuentas nacionales) lo eleva al 26-27%.
- **No incluye**: riqueza oculta en paraísos fiscales, criptoactivos, seguros
  de vida vinculados.

---

## 2. Marco conceptual: riqueza vs. renta

```
                    FLUJOS (Estudios 1 y 2)
                    ────────────────────────
    Salario bruto ──→ Impuestos ──→ Salario neto ──→ Consumo
         ↑                              ↓
    Transferencias ←── Estado ───── Servicios
                                        ↓
                    STOCK (Estudio 3)
                    ────────────────
                    Ahorro acumulado
                         ↓
            ┌────────────┴────────────┐
            │                         │
     Activos reales            Activos financieros
     (79% del total)           (21% del total)
            │                         │
     Vivienda (53%)            Cuentas, fondos,
     Otros inmuebles (36%)     acciones, planes
     Negocios (10%)            de pensiones
            │                         │
            └────────────┬────────────┘
                         │
                  Patrimonio neto
                  = Activos - Deudas
                         │
              Gini riqueza = 0,687
              (vs. Gini renta = 0,497)
```

La riqueza neta (patrimonio neto) es la diferencia entre los activos totales
del hogar y sus deudas. En España, los activos reales —fundamentalmente
inmobiliarios— representan el **78,9%** del total, una proporción muy superior
a la media de la eurozona. Esta concentración en ladrillo tiene consecuencias
profundas: la riqueza es ilíquida, volátil (depende del ciclo inmobiliario)
y geográficamente desigual.

---

## 3. Datos y metodología

### 3.1 Fuentes de datos

| Fuente | Qué aporta | Año |
|---|---|---|
| **BdE, EFF 2022** (DO-2413) | Distribución de riqueza por percentil, edad, composición | 2022 |
| **FEDEA eee2025-23** | Evolución Gini y top shares 2002-2022 (8 olas EFF) | 2025 |
| **AEAT** | Estadística declarantes Imp. Patrimonio, ITSGF | 2022-2023 |
| **Hacienda / IGAE** | Recaudación ISD, IBI, recaudación total | 2022-2023 |
| **BCE, HFCS Wave 4** | Comparación internacional (eurozona) | 2021 |
| **Eurofound / OCDE** | Tendencias desigualdad, impuestos patrimoniales | 2023-2025 |

### 3.2 Limitaciones de las encuestas de riqueza

La EFF entrevista a unas 6.300 familias, con sobremuestreo de hogares ricos
para garantizar representatividad en la cola superior. Aun así, las encuestas
tienden a infradeclarar la riqueza de los más ricos:

- **EFF 2022** (BdE): top 1% = 19,4% de la riqueza total
- **FEDEA** (mismos microdatos, metodología ajustada): top 1% = 21,1%
- **WID.world** (ajuste con cuentas nacionales y datos fiscales): top 1% ≈ 26-27%

Las cifras de este estudio se basan principalmente en la EFF y FEDEA. Los
valores reales de concentración podrían ser aún mayores.

---

## 4. Resultados

### 4.1 Distribución de la riqueza en España (2022)

La riqueza neta mediana de los hogares españoles es de **142.700 EUR**, pero la
media es más del doble: **309.000 EUR**. Esta divergencia ya indica una fuerte
asimetría: unos pocos hogares con patrimonios muy altos elevan la media.

**Riqueza neta por percentil de riqueza** (miles de EUR constantes de 2022):

| Grupo | Mediana | Media | % riqueza total |
|---|---|---|---|
| Bottom 25% (P0-P25) | 1,3 | 4,0 | ≈ 0,3% |
| P25-P50 | 85,7 | 87,3 | ≈ 7% |
| P50-P75 | 210,8 | 218,2 | ≈ 18% |
| P75-P90 | 444,0 | 458,9 | ≈ 22% |
| **P90-P100** | **1.062,3** | **1.625,6** | **≈ 53%** |

Fuente: BdE, EFF 2022 (DO-2413, Cuadro 1.B).

El **10% más rico** posee más riqueza que el **90% restante** combinado.
La cuartila inferior (P0-P25) tiene una riqueza mediana de apenas 1.300 EUR
—prácticamente nada.

**Concentración según FEDEA**:

| Grupo | % de la riqueza (2022) | Cambio vs 2002 |
|---|---|---|
| Top 1% | 21,1% | +7,5 pp (era 13,6%) |
| P91-P99 | 32,6% | +3,5 pp (era 29,1%) |
| P51-P90 | 39,2% | -9,6 pp (era 48,8%) |
| Bottom 50% | 7,1% | -1,4 pp (era 8,5%) |

![Curva de Lorenz: riqueza vs renta](/assets/images/impuestos/lorenz_riqueza_vs_renta.png)

La curva de Lorenz muestra con claridad el abismo: la curva de riqueza (roja) se
separa mucho más de la diagonal de igualdad que la de renta (azul). El área entre
la diagonal y la curva —que define el coeficiente de Gini— es sustancialmente mayor
para la riqueza (0,69) que para la renta (0,50).

### 4.2 Composición del patrimonio

El patrimonio español es, fundamentalmente, ladrillo:

| Componente | % del total de activos |
|---|---|
| **Activos reales** | **78,9%** |
| — Vivienda principal | 52,9% de los activos reales |
| — Otros inmuebles | 35,7% |
| — Negocios | 10,1% |
| — Joyas/arte | 1,2% |
| **Activos financieros** | **21,1%** |
| — Cuentas bancarias | 38,1% de los financieros |
| — Planes de pensiones | 14,1% |
| — Fondos de inversión | 11,8% |
| — Acciones no cotizadas | 10,5% |
| — Acciones cotizadas | 7,8% |

Fuente: BdE, EFF 2022 (DO-2413, Cuadros 2 y 4).

La composición varía drásticamente según el nivel de renta:

- En los hogares de **renta baja** (<P20), los activos reales representan el
  **85,6%** del total, y la vivienda principal supone el 68,8% de esos activos
  reales. Es decir: prácticamente toda su riqueza es su casa.
- En los hogares de **renta alta** (P90-P100), los activos reales son el 77,5%,
  pero la vivienda principal solo el 38,3%. El peso de negocios (23,1%) y
  activos financieros (22,5%) es mucho mayor.

![Composición del patrimonio por nivel de renta](/assets/images/impuestos/composicion_riqueza.png)

**Implicación clave**: las crisis inmobiliarias (2008-2014) destruyen proporcionalmente
más riqueza en los hogares medios y bajos, cuyo patrimonio es casi 100% vivienda.
Los hogares ricos, más diversificados, resisten mejor.

### 4.3 Evolución 2002-2022: veinte años de desigualdad creciente

La EFF se ha realizado 8 veces entre 2002 y 2022, lo que permite observar la
evolución con detalle:

| Año | Gini riqueza | Top 1% | Bottom 50% | Evento |
|---|---|---|---|---|
| 2002 | 0,576 | 13,6% | 8,5% | Pre-burbuja |
| 2005 | 0,570 | 15,0% | 8,0% | Expansión inmobiliaria |
| 2008 | 0,580 | 16,0% | 7,5% | Pico burbuja |
| 2011 | 0,620 | 18,5% | 6,5% | Crisis financiera |
| 2014 | 0,650 | 20,0% | 6,0% | Mínimo post-crisis |
| 2017 | 0,660 | 20,5% | 7,0% | Recuperación |
| 2020 | 0,675 | 20,5% | 7,5% | COVID |
| 2022 | **0,687** | **21,1%** | **7,1%** | Post-COVID |

Fuente: FEDEA eee2025-23, Figuras 7 y 14, a partir de microdatos EFF.

![Evolución del Gini y participación del Top 1%](/assets/images/impuestos/evolucion_gini_riqueza.png)

Tres observaciones:

1. **El Gini no ha dejado de crecer** en 20 años, pasando de 0,576 a 0,687
   (+19,3%). Ni la crisis, ni la recuperación, ni el COVID han invertido la
   tendencia.
2. **El top 1% ha ganado 7,5 puntos porcentuales** de participación, pasando del
   13,6% al 21,1%. Esto equivale a una transferencia neta de riqueza desde las
   clases medias hacia la cúspide.
3. **El bottom 50% ha perdido terreno**, pasando del 8,5% al 7,1%. La mitad de
   los hogares españoles posee hoy menos de lo que poseía hace dos décadas, en
   términos relativos.

### 4.4 La fractura generacional

Quizás el hallazgo más alarmante es la brecha creciente entre generaciones.

**Riqueza neta por grupo de edad** (miles EUR constantes de 2022, EFF):

| Edad cabeza familia | Mediana 2017 | Mediana 2022 | Media 2022 | Cambio mediana |
|---|---|---|---|---|
| **< 35 años** | 6,1 | **20,0** | 77,6 | +228% (desde muy poco) |
| 35-44 | 74,1 | 75,7 | 191,1 | +2% |
| 45-54 | 130,7 | 128,3 | 257,3 | -2% |
| 55-64 | 199,3 | 189,4 | 352,9 | -5% |
| 65-74 | 206,3 | **225,8** | 442,3 | +9% |
| **> 74 años** | 148,0 | **221,4** | 454,7 | +50% |

Fuente: BdE, EFF 2022 (DO-2413, Cuadro 1.B).

![La fractura generacional de la riqueza](/assets/images/impuestos/fractura_generacional.png)

Datos complementarios (FEDEA eee2025-23):

- La **brecha de riqueza media** entre menores de 35 y mayores de 75 ha pasado
  de **50.000 EUR en 2002 a más de 360.000 EUR en 2022**.
- Los hogares mayores de 75 han incrementado su participación en la riqueza
  total del **8,3% (2002) al 18,3% (2022)**.
- La **tasa de propiedad de vivienda** entre menores de 35 ha caído del 65%
  (2008) al **31,8%** (2022).
- La **riqueza mediana** de los menores de 35 era de 101.040 EUR en 2008
  (pico de la burbuja) y ha caído a 20.000 EUR en 2022: una destrucción del
  **80%** en 14 años.

La divergencia no es solo de nivel, sino de **composición**: mientras los
mayores de 65 tienen el 90%+ de su patrimonio en vivienda en propiedad
(pagada), los menores de 35 acumulan deuda relativa mucho mayor y menor
acceso a activos reales.

### 4.5 Cómo tributa la riqueza

España tiene cuatro impuestos que gravan directamente la riqueza o el
patrimonio:

#### Impuesto sobre el Patrimonio (IP)

- **Base**: patrimonio neto > 700.000 EUR (mínimo exento general)
- **Tipos**: 0,2% a 3,5% (escala estatal)
- **Declarantes 2022**: 230.365 (de ~19 millones de hogares = **1,2%**)
- **Declarantes con cuota**: 185.100
- **Recaudación 2022**: ~**1.246 M EUR**
- **Bonificaciones**: varias CCAA bonifican al 100% (efectivamente eliminado)

#### Impuesto Temporal de Solidaridad de las Grandes Fortunas (ITSGF)

- **Base**: patrimonio neto > 3.000.000 EUR
- **Tipos**: 1,7% a 3,5%
- **Declarantes 2023**: 12.010
- **Recaudación 2023**: **623 M EUR**
- **El 89%** de la recaudación (555 M€) procede de **Madrid**, porque era la
  única gran CCAA que bonificaba el IP al 100%

| CCAA | Declarantes | Recaudación | % del total |
|---|---|---|---|
| Madrid | 10.302 | 555 M€ | 89,0% |
| Andalucía | 865 | 29,7 M€ | 4,8% |
| Galicia | 91 | 9,8 M€ | 1,6% |
| Resto | 752 | 28,5 M€ | 4,6% |

**Nota**: la recaudación del ITSGF cayó un 94% en 2024 (a solo 38 M€) porque
Madrid, Andalucía y Galicia reactivaron sus propios impuestos de patrimonio
autonómicos, con lo que el ITSGF (que se deduce del IP ya pagado) queda
neutralizado.

#### Impuesto sobre Sucesiones y Donaciones (ISD)

- **Gestión**: cedido 100% a las CCAA
- **Recaudación 2023**: ~**3.011 M EUR**
- **Tendencia**: 8 CCAA han bonificado entre el 99% y el 100% para
  transmisiones entre familiares directos (padres-hijos, cónyuges)

| Bonificación | CCAA |
|---|---|
| 100% | Cantabria, Baleares |
| 99-99,9% | Madrid, Andalucía, Murcia, Extremadura, Castilla y León, C. Valenciana, La Rioja, Canarias |

**Implicación**: en la mayoría del territorio español, las grandes fortunas se
transmiten entre generaciones **prácticamente sin tributar**. Esto perpetúa y
amplifica la desigualdad de riqueza.

#### Impuesto sobre Bienes Inmuebles (IBI)

- **Base**: valor catastral (generalmente muy inferior al valor de mercado)
- **Recaudación 2022**: ~**14.200 M EUR**
- **Peso**: 67% de la recaudación tributaria local
- **Naturaleza**: es un impuesto sobre la propiedad inmobiliaria, no sobre la
  riqueza neta. Su tipo es fijo (no progresivo) sobre el valor catastral,
  lo que lo hace **regresivo** en la práctica: pesa más proporcionalmente
  sobre los hogares de menor patrimonio.

### 4.6 La insignificancia de la recaudación patrimonial

Sumando los cuatro impuestos patrimoniales:

| Impuesto | Recaudación | % del total |
|---|---|---|
| IBI | 14.200 M€ | 3,2% |
| ISD | 3.011 M€ | 0,7% |
| IP | 1.246 M€ | 0,3% |
| ITSGF | 623 M€ | 0,1% |
| **Total patrimonial** | **19.080 M€** | **4,3%** |

Frente a:

| Impuesto | Recaudación | % del total |
|---|---|---|
| Cotizaciones SS | 180.000 M€ | 40,3% |
| IRPF | 115.000 M€ | 25,8% |
| IVA | 80.000 M€ | 17,9% |
| Imp. Sociedades | 32.000 M€ | 7,2% |
| II.EE. | 20.000 M€ | 4,5% |
| **Total renta/consumo** | **427.000 M€** | **95,7%** |

Fuente: AEAT, Informe Anual de Recaudación 2023; Hacienda; IGAE.

![Impuestos patrimoniales en contexto](/assets/images/impuestos/riqueza_vs_recaudacion.png)

El contraste es demoledor: **el 95,7% de los impuestos gravan la renta y el
consumo** (es decir, el trabajo y el gasto), mientras que solo el **4,3%**
grava la riqueza acumulada. Y de ese 4,3%, las tres cuartas partes corresponden
al IBI, que es regresivo.

Si excluimos el IBI (que es más un impuesto local sobre la propiedad que un
impuesto sobre la riqueza neta), los impuestos propiamente patrimoniales (IP +
ITSGF + ISD) recaudan apenas **4.880 M€**, un **1,1%** del total.

![Recaudación por tipo de impuesto patrimonial](/assets/images/impuestos/recaudacion_patrimonio.png)

### 4.7 Comparación internacional

**Gini de riqueza neta en la eurozona** (HFCS 2021):

| País | Gini riqueza | Propiedad vivienda |
|---|---|---|
| Alemania | 0,724 | 49,5% |
| Austria | 0,710 | 55,0% |
| Francia | 0,700 | 61,0% |
| Países Bajos | 0,690 | 62,0% |
| **España** | **0,683** | **72,1%** |
| Finlandia | 0,680 | 73,0% |
| Italia | 0,670 | 72,0% |
| Bélgica | 0,640 | 72,0% |
| Portugal | 0,630 | 74,0% |
| Irlanda | 0,620 | 80,0% |
| Grecia | 0,590 | 75,0% |
| Eslovaquia | 0,508 | 91,0% |

Fuente: BCE, HFCS Wave 4 (2021); BdE EFF 2022 para España.

![Comparación internacional: Gini de riqueza](/assets/images/impuestos/comparativa_internacional_riqueza.png)

**Paradoja española**: España tiene un Gini de riqueza alto (0,683), pero
también una de las tasas de propiedad de vivienda más altas de Europa (72,1%).
¿Cómo es posible?

La explicación es que **la propiedad de vivienda oculta una desigualdad
enorme**. El 72% de hogares posee su vivienda principal, pero el valor de esas
viviendas varía enormemente: la mediana para el cuartil inferior de riqueza es
prácticamente cero, mientras que el decil superior tiene un patrimonio medio
de 1,6 millones de EUR. Además, el 47% de hogares posee otras propiedades
inmobiliarias además de su vivienda principal, llegando al 77% en el decil
superior de renta.

Alemania tiene un Gini más alto (0,724) pero una tasa de propiedad mucho más
baja (49,5%). Esto refleja un modelo diferente: en Alemania, el alquiler es la
norma y la riqueza se concentra aún más en los propietarios. Los países con
Gini más bajo (Eslovaquia, Grecia) tienden a ser aquellos donde la propiedad
es casi universal y el valor de los inmuebles es relativamente homogéneo.

**Tendencias 2010-2021** (Eurofound): España es uno de los países donde la
desigualdad de riqueza ha **aumentado más significativamente**, junto con
Finlandia y Estonia. En Alemania, paradójicamente, ha descendido ligeramente.

---

## 5. Discusión

### 5.1 Conexión con los Estudios 1 y 2: la foto completa

Los tres estudios de esta serie componen una imagen coherente y preocupante:

![La trilogía fiscal: pagar, recibir y poseer](/assets/images/impuestos/triptico_tres_estudios.png)

| Dimensión | Hallazgo clave | Gini |
|---|---|---|
| **Estudio 1: Quién PAGA** | U invertida: la carga fiscal pico (67,8%) recae en los 56.000 EUR; baja al 52,6% en 281.000 EUR | — |
| **Estudio 2: Quién RECIBE** | El 60% de hogares son receptores netos; la U invertida persiste tras transferencias | 0,497 → 0,327 |
| **Estudio 3: Quién POSEE** | El 1% más rico posee el 21% de la riqueza; los impuestos patrimoniales recaudan el 4,3% del total | 0,687 |

La conexión es directa:

1. **Los que más pagan** (proporcionalmente) son las rentas medias-altas
   (P80-P90), no los más ricos. La U invertida del Estudio 1 lo demuestra.
2. **Los que más se benefician** del sistema de transferencias son los hogares
   de renta baja (Q1 recibe un +85% neto de su renta), lo cual es lógico y
   deseable. Pero el top 1% también se beneficia de la caída en la carga
   neta (solo paga -18,1% neto frente al -23,6% del P91-99).
3. **Los que más poseen** son los mismos que menos pagan proporcionalmente.
   El 10% más rico posee el 53% de la riqueza pero la tributación patrimonial
   es mínima (1,1% del total sin IBI).

### 5.2 El papel de la vivienda

La vivienda es el eje vertebrador de la riqueza española:

- **El 53% de los activos reales** de los hogares es la vivienda principal.
- **El 72,1%** de los hogares son propietarios (pero el 31,8% de los menores de
  35 lo son, frente al 83% de los mayores de 65).
- **El 47%** de los hogares posee otras propiedades inmobiliarias, llegando al
  **77%** en el decil superior de renta.

La concentración inmobiliaria tiene tres consecuencias:

1. **Vulnerabilidad cíclica**: la crisis de 2008 destruyó la riqueza de las
   clases medias (concentrada en vivienda) mientras los más ricos, con activos
   financieros diversificados, resistieron mejor.
2. **Barrera de entrada**: los precios de vivienda, inflados por la demanda
   especulativa y la oferta insuficiente, impiden a los jóvenes acceder a la
   propiedad, perpetuando la fractura generacional.
3. **IBI regresivo**: el principal impuesto sobre inmuebles (14.200 M€)
   se aplica sobre valores catastrales, que están desactualizados y no reflejan
   el patrimonio neto real del contribuyente.

### 5.3 Bonificaciones del ISD: un diseño político deliberado

La práctica eliminación del Impuesto de Sucesiones y Donaciones en la mayoría
de CCAA no es un accidente, sino una decisión política deliberada que tiene
consecuencias directas sobre la desigualdad de riqueza:

- **8 CCAA** han bonificado entre el 99% y el 100% las transmisiones entre
  familiares directos (padres a hijos, cónyuges).
- Esto significa que las grandes fortunas se transmiten entre generaciones
  **sin tributar**, consolidando la concentración patrimonial.
- La recaudación por ISD (3.011 M€) ya es baja, y sería aún menor si las
  CCAA que aún no han bonificado (Cataluña, Asturias, Aragón) lo hicieran.

En contraste, países como **Francia** (0,50% del PIB en impuesto de sucesiones),
**Bélgica** (0,60%) o **Reino Unido** (0,25%) mantienen este impuesto como
herramienta redistributiva intergeneracional.

---

## 6. Conclusiones

1. **La desigualdad de riqueza (Gini 0,687) es un 38% mayor que la de renta
   (Gini 0,497)**. Son dos mundos diferentes: la renta se redistribuye
   parcialmente a través de impuestos y transferencias; la riqueza, apenas.

2. **El 1% más rico posee el 21,1% de toda la riqueza**, y su participación
   ha crecido 7,5 puntos porcentuales en 20 años (del 13,6% en 2002).
   La mitad más pobre posee apenas el 7,1%.

3. **La riqueza española es fundamentalmente inmobiliaria** (79% activos
   reales), lo que la hace vulnerable a crisis y difícil de gravar sin afectar
   a las clases medias propietarias de su única vivienda.

4. **Los impuestos patrimoniales recaudan solo el 4,3%** del total (19.080 M€),
   y si se excluye el IBI (que es regresivo), solo el 1,1% (4.880 M€).
   El sistema grava intensamente el trabajo y el consumo, pero apenas toca
   la riqueza acumulada.

5. **La fractura generacional es alarmante**: la brecha de riqueza entre
   menores de 35 y mayores de 75 se ha multiplicado por 7 en 20 años
   (de 50.000 a 360.000+ EUR). Los menores de 35 tienen una tasa de
   propiedad de vivienda del 31,8%, frente al 83% de los mayores de 65.

6. **La eliminación del ISD en 8 CCAA** consolida la transmisión
   intergeneracional de la riqueza sin tributación, perpetuando la
   desigualdad.

7. **España tiene un Gini de riqueza alto en el contexto europeo** (0,683),
   similar al de Francia y Países Bajos, y la tendencia es creciente
   (a diferencia de Alemania, donde ha descendido).

8. **Conectando los tres estudios**: el sistema fiscal español grava
   fuertemente el trabajo (U invertida del Estudio 1), redistribuye mediante
   transferencias (Estudio 2, reduciendo el Gini de renta del 0,50 al 0,33),
   pero apenas toca el stock de riqueza acumulada (Estudio 3). El resultado
   es una sociedad donde los flujos se redistribuyen, pero el stock se
   concentra cada vez más.

---

## 7. Limitaciones y trabajo futuro

- **Infradeclaración**: las encuestas (EFF) infraestiman la riqueza del top.
  Sería necesario complementar con datos fiscales (AEAT modelo 714) y fuentes
  como WID.world para ajustar al alza.
- **Datos intermedios estimados**: los valores Gini y de participación para las
  olas intermedias de la EFF (2005-2020) proceden del texto de FEDEA y de las
  figuras del informe; los datos exactos tabulados no estaban disponibles en
  formato descargable.
- **No se analiza la tributación efectiva** del patrimonio por tramos (tipos
  medios efectivos del IP), que requeriría acceder a las tablas detalladas de
  la AEAT por tramos de base imponible.
- **Futuro Estudio 4**: el protagonismo de la vivienda en estos resultados
  motiva un análisis específico: ¿cómo se distribuye la propiedad de
  viviendas en alquiler? ¿Existe concentración oligopolística?

---

## 8. Referencias

1. Banco de España (2024). *Encuesta Financiera de las Familias (EFF) 2022:
   métodos, resultados y cambios desde 2020*. Documento Ocasional 2413.
   [(PDF)](https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/PublicacionesSeriadas/DocumentosOcasionales/24/Fich/do2413.pdf)
2. Conde-Ruiz, J.I. y García-Rodríguez, F. (2025). *Evolución de la Riqueza
   de las Familias en España (2002-2022): Niveles, Composición y Fractura
   Generacional*. FEDEA, Estudios sobre la Economía Española 2025/23.
   [(PDF)](https://documentos.fedea.net/pubs/eee/2025/eee2025-23.pdf)
3. BCE (2023). *Household Finance and Consumption Survey, Wave 4 (2021)*.
   Statistical Tables, julio 2023.
   [(PDF)](https://www.ecb.europa.eu/home/pdf/research/hfcn/HFCS_Statistical_Tables_Wave_2021_July2023.pdf)
4. Eurofound (2023). *A picture of wealth inequality across EU Member States*.
   [(Web)](https://www.eurofound.europa.eu/en/publications/all/a-picture-of-wealth-inequality-across-eu-member-states)
5. AEAT (2024). *Estadística de los declarantes del Impuesto sobre el
   Patrimonio 2022-2023*.
   [(Web)](https://sede.agenciatributaria.gob.es/Sede/datosabiertos/catalogo/hacienda/Estadistica_de_los_declarantes_del_Impuesto_sobre_el_Patrimonio.shtml)
6. AEAT (2024). *Informe Anual de Recaudación Tributaria 2023*.
   [(PDF)](https://sede.agenciatributaria.gob.es/static_files/AEAT/Estudios/Estadisticas/Informes_Estadisticos/Informes_Anuales_de_Recaudacion_Tributaria/Ejercicio_2023/IART23_es_es.pdf)
7. Banco de España (2024). Blog: *El análisis de la riqueza en España: 20 años
   de la Encuesta Financiera de las Familias*.
   [(Web)](https://www.bde.es/wbe/en/noticias-eventos/blog/el-analisis-de-la-riqueza-en-espana-20-anos-de-la-encuesta-financiera-de-las-familias.html)
8. OCDE (2025). *Mapping trends and gaps in household wealth across OECD
   countries*.
   [(PDF)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/mapping-trends-and-gaps-in-household-wealth-across-oecd-countries_37e92f18/4bb6ec53-en.pdf)
