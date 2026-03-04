---
layout: post
title: "Las tres decadas perdidas en numeros: distribucion de renta en Japon, 1999-2019"
date: 2026-03-05
series: japon
part: 1
---

*Este es el primer articulo de una serie de tres sobre movilidad intergeneracional en Japon. Analiza la distribucion de renta de los hogares japoneses a partir de la National Survey of Family Income and Expenditure (NSFIE), la encuesta quinquenal mas importante de Japon sobre ingresos familiares. Los articulos siguientes estiman la [movilidad absoluta]({{ site.baseurl }}/2026/03/05/test-japones-movilidad.html) y [comparan Japon con Espana]({{ site.baseurl }}/2026/03/05/japon-vs-espana-movilidad.html).*

> **Hallazgo central.** En 20 anos (1999-2019), la renta mediana real de
> los hogares japoneses de 30-39 anos apenas se movio: 621 万円 en 1999,
> 583 万円 en 2004, 619 万円 en 2019. La distribucion permanecio
> notablemente estable, con un Gini bajo en comparacion internacional.
> Japon no se hizo mas desigual -- simplemente dejo de crecer.

---

## 1. La NSFIE: la encuesta que radiografia Japon cada cinco anos

La *National Survey of Family Income and Expenditure* (全国家計構造調査, antes llamada *Zensho*) es la encuesta de hogares mas completa de Japon. La realiza el Statistics Bureau cada cinco anos desde 1959 y cubre aproximadamente 90.000 hogares en cada ola. A diferencia de otras encuestas, la NSFIE recopila informacion detallada sobre ingresos, gastos, ahorro y patrimonio.

Para este analisis usamos las tablas agregadas publicadas en [e-Stat](https://www.e-stat.go.jp/), el portal de estadisticas oficiales de Japon. Las tablas proporcionan la distribucion de hogares por grupo de edad del cabeza de familia y tramo de renta anual. Disponemos de datos para cinco olas: 1999, 2004, 2009, 2014 y 2019.

**Limitacion importante**: no disponemos de microdatos, sino de tablas agregadas. Esto significa que trabajamos con distribuciones discretizadas en 10 tramos de renta (para 1999-2014) o 41 tramos (para 2019). Los calculos de medianas y percentiles son interpolaciones lineales dentro de cada tramo.

| Ola | Tipo de hogar | Grupos de edad | Tramos de renta |
|-----|--------------|----------------|-----------------|
| 1999 | 2+ personas | 6 (decenales) | 10 |
| 2004 | 2+ personas | 6 (decenales) | 10 |
| 2009 | Solo trabajadores | 6 (decenales) | 10 |
| 2014 | 2+ personas | 6 (decenales) | 10 |
| 2019 | 2+ personas | 10 (quinquenales) | 41 |

{: .wide }

La ola de 2009 solo cubre hogares con miembros empleados (*workers' households*), no todos los hogares de 2+ personas, lo que introduce un sesgo ascendente en las rentas. Por ello, en los analisis principales la excluimos o la marcamos como no comparable.

---

## 2. El perfil age-earnings japones: el pico a los 55-59

El perfil de renta por edad en Japon tiene una forma caracteristica: sube de forma continua hasta los 50-59 anos y cae bruscamente a partir de los 60, coincidiendo con la edad de jubilacion (*teinen taishoku*, tipicamente a los 60 en el sector privado, aunque muchos son recontratados a salarios mas bajos).

![Perfil age-earnings de Japon en 2019](/assets/images/japon/income_by_age_2019.png)
*Figura 1. Mediana de renta anual del hogar por grupo de edad del cabeza de familia, NSFIE 2019. El pico se situa en 50-59 anos, antes de la jubilacion.*

Este patron contrasta con EEUU, donde el pico se situa antes (45-54) y la caida es mas gradual. La rigidez del mercado laboral japones -- con salarios basados en antiguedad (*nenko joretsu*) -- explica el pico tardio: los trabajadores acumulan salario de forma casi lineal con los anos de servicio, hasta que la jubilacion corta la trayectoria de forma abrupta.

La caida a los 60+ es especialmente pronunciada: la mediana cae casi a la mitad. Esto refleja dos factores: (1) la transicion de salario a pension, y (2) el sistema de "reempleo" (*sai-koyo*) en el que muchos jubilados vuelven a trabajar en puestos de menor responsabilidad y salario.

---

## 3. Veinte anos de estancamiento: 1999-2019

La pregunta central es: ¿como evoluciono la distribucion de renta durante las "decadas perdidas"? Para responderla, comparamos la renta del grupo de 30-39 anos -- la cohorte clave para nuestro analisis de movilidad -- a lo largo de las cuatro olas comparables.

![Evolucion de la renta del grupo 30-39](/assets/images/japon/income_shift_30_39.png)
*Figura 2. P25, mediana y P75 de la renta anual del hogar para el grupo de 30-39 anos, en yenes reales de 2019. La mediana oscila entre 583 y 621 万円 sin tendencia clara.*

Los numeros cuentan una historia de estancamiento casi total:

| Ano | P25 (万円) | P50 (万円) | P75 (万円) | Tipo de hogar |
|-----|----------|----------|----------|---------------|
| 1999 | 434 | 621 | 826 | 2+ personas |
| 2004 | 412 | 583 | 755 | 2+ personas |
| 2014 | 415 | 584 | 773 | 2+ personas |
| 2019 | 425 | 619 | 827 | 2+ personas |

{: .wide }

La mediana del grupo 30-39 cayo de 621 万円 en 1999 a 583 万円 en 2004 (una caida real del 6%) y tardo 15 anos en volver al punto de partida. En 2019, con 619 万円, la mediana es practicamente identica a la de 1999.

Esto es extraordinario en perspectiva comparada. En la mayoria de paises desarrollados, 20 anos de crecimiento economico (incluso moderado) desplazan significativamente la distribucion hacia la derecha. En Japon, la distribucion se quedo clavada.

---

## 4. Distribucion estable, crecimiento cero

La comparacion directa de las CDFs (funciones de distribucion acumulada) de 1999 y 2019 revela hasta que punto las distribuciones se superponen:

![CDFs superpuestas 1999 vs 2019](/assets/images/japon/cdf_comparison_1999_2019.png)
*Figura 3. CDFs de renta del hogar para el grupo 30-39, 1999 (gris) vs 2019 (rojo), en yenes reales de 2019. Las dos curvas son practicamente identicas.*

Las dos CDFs son casi indistinguibles. Esto tiene una implicacion directa para la movilidad intergeneracional: si la distribucion de los hijos (medida en 2019) es identica a la de los padres (medida en 1999), la probabilidad de que un hijo gane mas que su padre -- en terminos reales, a la misma edad -- es esencialmente del 50%. Un coin flip.

---

## 5. La deflacion japonesa, visible en el CPI

La estabilidad de las rentas reales se produce en un contexto macroeconomico unico: Japon es el unico pais desarrollado que ha experimentado deflacion sostenida. El IPC japones (base 2020=100) muestra el patron:

| Ano | CPI (2020=100) | Variacion desde 1999 |
|-----|---------------|---------------------|
| 1999 | 98.02 | -- |
| 2004 | 95.49 | -2.6% |
| 2009 | 95.51 | -2.6% |
| 2014 | 97.46 | -0.6% |
| 2019 | 100.02 | +2.0% |

En 20 anos, los precios subieron apenas un 2%. Comparado con Espana (donde el IPC subio un ~40% en el mismo periodo) o EEUU (~50%), Japon vivio en un regimen de precios practicamente congelados.

Esto significa que las rentas nominales japonesas reflejan bastante bien las rentas reales. No hubo inflacion que pudiera "inflar" las rentas nominales y dar una falsa sensacion de progreso. El estancamiento es real.

---

## 6. Lo que Japon hizo bien: desigualdad contenida

Si la historia japonesa es de estancamiento, tiene un punto fuerte: la desigualdad no aumento significativamente. El Gini de renta del hogar en Japon se situa en torno a 0.33 (despues de transferencias), significativamente por debajo de EEUU (0.39) y similar a Francia o Alemania.

La amplitud intercuartilica (P75/P25) para el grupo 30-39 se mantuvo notablemente estable:

| Ano | Ratio P75/P25 |
|-----|--------------|
| 1999 | 1.90 |
| 2004 | 1.83 |
| 2014 | 1.86 |
| 2019 | 1.95 |

Mientras que en EEUU el ratio equivalente ha ido creciendo de forma sostenida, en Japon la distribucion de renta mantuvo su forma. Los hogares del percentil 75 ganan aproximadamente el doble que los del percentil 25, y eso no cambio en dos decadas.

Esta estabilidad distributiva es el punto de partida del "test japones" que desarrollamos en el [siguiente articulo]({{ site.baseurl }}/2026/03/05/test-japones-movilidad.html): si la tesis de Chetty es correcta (que la distribucion importa mas que el crecimiento), Japon deberia tener una movilidad intergeneracional alta a pesar del estancamiento. ?Es asi?

---

## 7. Resumen

1. La NSFIE proporciona distribuciones de renta de hogares japoneses para 1999-2019, discretizadas en tramos de renta por grupo de edad.
2. El perfil age-earnings japones tiene un pico tardio (50-59) y una caida brusca a los 60+, consistente con el sistema salarial basado en antiguedad.
3. La renta mediana del grupo 30-39 oscilo entre 583 y 621 万円 reales durante 20 anos -- estancamiento practicamente total.
4. Las CDFs de 1999 y 2019 son casi identicas, lo que anticipa una movilidad cercana al 50%.
5. La deflacion japonesa fue real pero leve (CPI +2% en 20 anos).
6. A diferencia de EEUU, Japon no vio un aumento significativo de la desigualdad.

---

## Referencias

- Statistics Bureau of Japan. *National Survey of Family Income and Expenditure* (全国家計構造調査). Tablas agregadas disponibles en [e-Stat](https://www.e-stat.go.jp/).
- Chetty, R., Grusky, D., Hell, M., Hendren, N., Manduca, R., & Naidu, J. (2017). "The Fading American Dream: Trends in Absolute Income Mobility Since 1940." *Science*, 356(6336), 398-406.
- Lise, J., Sudo, N., Suzuki, M., Yamada, K., & Yamada, T. (2014). "Wage, Income and Consumption Inequality in Japan, 1981-2008." *Review of Economic Dynamics*, 17(4), 582-612.
