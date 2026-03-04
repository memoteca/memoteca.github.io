---
layout: post
title: "Dos caminos al mismo resultado: Japon vs Espana en movilidad absoluta"
date: 2026-03-05
series: japon
part: 3
---

*Tercer y ultimo articulo de la serie sobre movilidad intergeneracional en Japon. El [primer articulo]({{ site.baseurl }}/2026/03/05/distribucion-renta-japon.html) analizo la distribucion de renta; el [segundo]({{ site.baseurl }}/2026/03/05/test-japones-movilidad.html) estimo la movilidad. Aqui comparamos Japon con Espana -- dos paises con movilidad similar pero por razones opuestas -- y extraemos implicaciones para la teoria de Chetty.*

> **Hallazgo central.** Espana (~44%) y Japon (~49%) tienen movilidades
> absolutas similares, pero llegan al mismo resultado por caminos
> opuestos. Espana tiene crecimiento real pero mala distribucion; Japon
> tiene buena distribucion pero crecimiento cero. La descomposicion de
> Chetty se confirma, pero en sentido bidireccional: **cualquiera** de
> los dos canales puede matar la movilidad.

---

## 1. El mismo numero, dos historias

Espana y Japon son dos de las economias mas grandes del mundo, con historias economicas recientes radicalmente distintas. Sin embargo, sus tasas de movilidad absoluta intergeneracional son notablemente similares:

![Espana vs Japon](/assets/images/japon/spain_vs_japan_comparison.png)
*Figura 1. Movilidad absoluta intergeneracional: Espana (cohortes 1972-88, edad 38) vs Japon (cohortes 1980-89, edad 30-39). Ambos paises estan en el entorno del 44-49%, por debajo del coin flip.*

Ambos paises estan por debajo o en el umbral del 50%, lo que significa que la mayoria (o casi la mitad) de los jovenes no ganan mas que sus padres a la misma edad en terminos reales. Pero las razones son diametralmente opuestas.

---

## 2. Tabla comparativa macro

| Indicador | Espana | Japon |
|-----------|--------|-------|
| Movilidad absoluta | ~44% (edad 38, Gaussian) | ~49% (edad 30-39, G=20) |
| Crecimiento PIB real per capita, 20 anos | +25-30% | ~0% |
| Gini renta disponible | 0.33 (post-transferencias) | 0.33 |
| Gini renta de mercado | ~0.50 | ~0.44 |
| Ratio P90/P10 renta laboral | ~3.6 | ~3.0 |
| Tasa de temporalidad juvenil | ~50% | ~15% |
| Deflacion sostenida | No | Si (1999-2013) |
| Tasa de desempleo juvenil (pico) | >55% (2013) | ~8% |

{: .wide }

El contraste es llamativo. Espana tuvo crecimiento real significativo: el PIB per capita subio un 25-30% entre las cohortes parentales y filiales. Japon no tuvo practicamente ningun crecimiento. Pero Espana tiene una de las distribuciones de renta de mercado mas desiguales de Europa (Gini ~0.50 antes de transferencias), mientras que Japon mantiene una distribucion comparativamente comprimida.

---

## 3. Los dos canales de Chetty

La descomposicion de Chetty (2017) separa la movilidad absoluta en dos componentes:

1. **Crecimiento**: si la renta media sube, la CDF de los hijos se desplaza a la derecha
2. **Distribucion**: si la renta esta concentrada (baja desigualdad), cada punto de crecimiento beneficia a mas hogares

![Esquema de descomposicion](/assets/images/japon/decomposition_schema.png)
*Figura 2. Descomposicion de la movilidad absoluta en dos canales. EEUU, Espana y Japon representan tres configuraciones distintas de los mismos dos ingredientes.*

La tabla siguiente resume como opera cada canal en los tres paises:

| Canal | EEUU | Espana | Japon |
|-------|------|--------|-------|
| Crecimiento | Alto (+30%) | Medio (+25%) | Cero (~0%) |
| Distribucion | Mala (Gini alto) | Mala (Gini alto) | Buena (Gini bajo) |
| Movilidad | ~50% | ~44% | ~49% |
| Canal que falla | Distribucion | Ambos (distribucion + precariedad) | Crecimiento |

{: .wide }

En EEUU, el crecimiento "deberia" haber producido movilidad alta, pero la mala distribucion lo impidio. En Japon, la buena distribucion "deberia" haber protegido la movilidad, pero sin crecimiento no habia nada que distribuir. Espana es un caso intermedio: tiene algo de crecimiento, pero la mala distribucion y la precariedad juvenil lo anulan.

---

## 4. El caso espanol: crecimiento mal distribuido

Los resultados para Espana (detallados en los articulos sobre [movilidad absoluta]({{ site.baseurl }}/2026/03/04/movilidad-absoluta-espana.html) y [edad optima]({{ site.baseurl }}/2026/03/04/edad-optima-movilidad.html)) muestran un patron especifico:

- **A los 30 anos**, la movilidad oscila entre 32% y 75%, con una caida dramatica para las cohortes que cumplieron 30 durante la Gran Recesion (2008-2014). La temporalidad y el desempleo juvenil masivo arrasaron la renta de los jovenes.
- **A los 38-40 anos**, la movilidad se estabiliza entre 37% y 49% (media 44%). La renta se recupera parcialmente, pero no lo suficiente para superar el umbral del 50%.

El motor principal de la caida en Espana no es la desigualdad (como en EEUU) sino el **menor crecimiento de la renta media** del grupo relevante. Nuestro analisis de descomposicion mostro que el crecimiento explica un 24% de la caida, frente a solo un 8% de la desigualdad.

Pero hay un matiz: la precariedad juvenil espanola funciona como un tercer canal que no aparece en la descomposicion de Chetty. La temporalidad, el desempleo ciclico y la emancipacion tardia no cambian el Gini de la distribucion global, pero destruyen la renta de la cohorte filial especifica que estamos midiendo.

---

## 5. El caso japones: igualdad sin crecimiento

Japon es el caso opuesto. Como documentamos en el [segundo articulo]({{ site.baseurl }}/2026/03/05/test-japones-movilidad.html):

- La movilidad del 49% es consistente con distribuciones identicas entre padres e hijos.
- La buena distribucion japonesa no pudo compensar 20 anos de crecimiento cero.
- La movilidad es casi insensible al rho porque las CDFs son identicas.

El mercado laboral japones no padece los problemas espanoles: la temporalidad juvenil es baja (~15% vs ~50%), el desempleo juvenil es minimo, y los jovenes acceden al empleo estable (*seishain*) de forma relativamente fluida. Pero ganan lo mismo que ganaban sus padres a la misma edad, simplemente porque la economia no crecio.

---

## 6. Contrafactuales cruzados

La comparacion sugiere dos contrafactuales reveladores:

### Japon con distribucion de EEUU
Si Japon tuviera la distribucion de EEUU (Gini ~0.39) pero el mismo crecimiento cero, la movilidad seria similar (~48-50%) pero por una razon distinta: los hogares pobres perderian y los ricos ganarian, pero el promedio no cambiaria mucho porque no hay crecimiento que redistribuir.

### EEUU con crecimiento de Japon
Si EEUU hubiera tenido crecimiento cero (en lugar del +30% real) manteniendo su distribucion actual, la movilidad habria sido ~45-48%, similar a la observada en Japon. El crecimiento es lo unico que evita que EEUU tenga movilidad aun menor.

### Espana con distribucion de Japon
Si Espana tuviera la distribucion japonesa (Gini de mercado ~0.44 en lugar de ~0.50), el crecimiento real existente se canalizaria de forma mas uniforme. La movilidad podria subir al 55-60% -- por encima del coin flip. Este es el contrafactual mas relevante para la politica publica espanola.

---

## 7. Conexion con la Great Gatsby Curve

Corak (2013) documento la "Great Gatsby Curve": una correlacion positiva entre desigualdad de renta (Gini) y persistencia intergeneracional (elasticidad de renta padre-hijo). Los paises con mas desigualdad tienden a tener menos movilidad relativa.

Nuestros resultados para movilidad *absoluta* (no relativa) complican esta narrativa. Japon tiene baja desigualdad y *deberia* estar en la parte alta de la curva, pero su movilidad absoluta es mediocre porque el crecimiento es cero. La Great Gatsby Curve funciona para movilidad relativa (posiciones en el ranking), pero la movilidad absoluta (superar a los padres en nivel de renta) requiere ademas crecimiento real.

La reformulacion seria:

- **Movilidad relativa** depende principalmente de la desigualdad (Great Gatsby Curve)
- **Movilidad absoluta** depende de crecimiento x distribucion (descomposicion de Chetty)
- Para que la movilidad absoluta sea alta, hacen falta **ambos ingredientes**

---

## 8. Implicaciones para la politica

| Leccion | Para Espana | Para Japon |
|---------|-------------|------------|
| Crecimiento | Ya existe, pero mal canalizado | Necesita reactivar crecimiento real |
| Distribucion | Reducir precariedad juvenil, temporalidad | Ya es buena, mantenerla |
| Prioridad | Mejorar distribucion (canal 2) | Generar crecimiento (canal 1) |

Para Espana, la palanca mas efectiva seria mejorar la distribucion: reducir la temporalidad, facilitar la emancipacion, y asegurar que el crecimiento agregado se traduce en mejoras de renta para los jovenes. El crecimiento existe; el problema es que no llega.

Para Japon, la buena distribucion ya esta en su sitio. Lo que falta es crecimiento real. Las politicas de "Abenomics" (expansion monetaria, fiscal y reformas estructurales) buscaban exactamente esto, con resultados mixtos.

---

## 9. Resumen de la serie

A lo largo de tres articulos hemos:

1. **Documentado** la distribucion de renta japonesa a partir de la NSFIE (1999-2019), mostrando 20 anos de estancamiento con desigualdad estable.
2. **Estimado** la movilidad absoluta intergeneracional en ~49% para la cohorte 1980-89, refutando la hipotesis de que la buena distribucion compensa la falta de crecimiento.
3. **Comparado** Japon con Espana (~44%), mostrando que llegan al mismo resultado por caminos opuestos y que la descomposicion de Chetty funciona en ambas direcciones.

La conclusion para la teoria de la movilidad: **no hay canal unico**. Crecimiento sin distribucion (EEUU), distribucion sin crecimiento (Japon), o crecimiento mal distribuido (Espana) producen el mismo resultado: movilidad en el entorno del coin flip. Para que la mayoria de los hijos supere a sus padres, hacen falta ambos ingredientes.

---

## Referencias

- Chetty, R., Grusky, D., Hell, M., Hendren, N., Manduca, R., & Naidu, J. (2017). "The Fading American Dream: Trends in Absolute Income Mobility Since 1940." *Science*, 356(6336), 398-406.
- Manduca, R., Hell, M., Adermon, A., et al. (2024). "Trends in Absolute Income Mobility in North America and Europe." *American Economic Journal: Applied Economics*.
- Corak, M. (2013). "Income Inequality, Equality of Opportunity, and Intergenerational Mobility." *Journal of Economic Perspectives*, 27(3), 79-102.
- Statistics Bureau of Japan. *National Survey of Family Income and Expenditure*. [e-Stat](https://www.e-stat.go.jp/).
- Lise, J., Sudo, N., Suzuki, M., Yamada, K., & Yamada, T. (2014). "Wage, Income and Consumption Inequality in Japan, 1981-2008." *Review of Economic Dynamics*, 17(4), 582-612.
