---
layout: post
title: "El test japones: protege la igualdad contra el estancamiento?"
date: 2026-03-05
series: japon
part: 2
---

*Segundo articulo de la serie sobre movilidad intergeneracional en Japon. El [primer articulo]({{ site.baseurl }}/2026/03/05/distribucion-renta-japon.html) analizo la distribucion de renta; aqui estimamos la movilidad absoluta usando la metodologia de Chetty et al. (2017). El [tercer articulo]({{ site.baseurl }}/2026/03/05/japon-vs-espana-movilidad.html) compara los resultados con Espana.*

> **Hallazgo central.** La movilidad absoluta intergeneracional de Japon
> es de ~49% -- en el umbral del coin flip. La hipotesis de que una buena
> distribucion protege la movilidad incluso sin crecimiento queda
> refutada: ambos canales (crecimiento y distribucion) son necesarios.

---

## 1. La tesis de Chetty y el experimento natural japones

En 2017, Chetty et al. publicaron su celebre estudio "The Fading American Dream", documentando que la probabilidad de que un estadounidense ganara mas que sus padres habia caido del 92% (nacidos en 1940) al 50% (nacidos en 1984). Su conclusion mas provocadora fue la descomposicion: si se hubiera mantenido la distribucion de 1940 con el crecimiento real observado, la movilidad solo habria caido al 80%. Es decir, **la desigualdad creciente, mas que la desaceleracion del crecimiento, fue la causa principal** de la caida.

Esta conclusion implica una prediccion testeable: un pais con distribucion igualitaria deberia mantener movilidad alta incluso con poco crecimiento. Japon es el experimento natural perfecto para este test:

| Factor | EEUU | Japon |
|--------|------|-------|
| Crecimiento real (1999-2019) | ~30% | ~0% |
| Gini (renta disponible) | 0.39 | 0.33 |
| Desigualdad | Alta y creciente | Baja y estable |

Si la distribucion es lo que mas importa, **Japon deberia tener una movilidad alta** (~65-75%), porque su buena distribucion compensaria el crecimiento nulo. Esta era nuestra hipotesis previa.

---

## 2. Metodologia: copula Gaussiana con tablas agregadas

Seguimos la metodologia de Chetty et al. (2017), adaptada a las restricciones de los datos japoneses. La movilidad absoluta se define como:

**P(renta_hijo > renta_padre | misma edad)**

donde padres e hijos se miden al mismo grupo de edad, separados por G anos en el tiempo.

### 2.1. Distribuciones marginales

De las tablas NSFIE construimos las CDFs (funciones de distribucion acumulada) de renta del hogar para cada grupo de edad y ano de encuesta. Para 1999-2014, las distribuciones tienen 10 tramos de renta; para 2019, 41 tramos. Todas las rentas se deflactan a yenes constantes de 2019 usando el CPI japones.

### 2.2. Copula Gaussiana

Sin microdatos longitudinales (que vinculen padres e hijos), necesitamos una asuncion sobre la dependencia intergeneracional. Seguimos a Chetty et al. en usar una copula Gaussiana con correlacion rank-rank rho = 0.34.

Para cada percentil p del padre, la probabilidad de que el hijo gane mas es:

$$P(\text{hijo} > \text{padre} | p) = 1 - \Phi\left(\frac{\Phi^{-1}(q) - \rho \cdot \Phi^{-1}(p)}{\sqrt{1 - \rho^2}}\right)$$

donde q = F_hijo(Q_padre(p)) es la fraccion de hijos por debajo de la renta del padre en el percentil p, y Phi es la CDF normal estandar.

### 2.3. Gap generacional

Las encuestas NSFIE son quinquenales (1999, 2004, 2009, 2014, 2019). El gap ideal seria G=25 (la asuncion de Chetty), pero con encuestas separadas 5 anos, el gap mas cercano es G=20 (comparar la misma banda de edad en encuestas separadas 20 anos: 2019 vs 1999).

### 2.4. Interpretacion de las cohortes

Comparamos hogares con cabeza de familia de 30-39 anos:
- **Padres**: 30-39 anos en 1999 → nacidos aproximadamente 1960-1969
- **Hijos**: 30-39 anos en 2019 → nacidos aproximadamente 1980-1989

La cohorte de "hijos" (1980-89) crecio durante la primera decada perdida y entro al mercado laboral durante la segunda. La cohorte de "padres" (1960-69) vivio el Japon del alto crecimiento y la burbuja.

---

## 3. Resultado: movilidad ~49%

El resultado central:

| Comparacion | Edad | Gap | Cohorte hijos | Movilidad |
|-------------|------|-----|---------------|-----------|
| 2019 vs 1999 | 30-39 | 20 | ~1980-89 | **48.7%** |
| 2014 vs 1999 | 30-39 | 15 | ~1975-84 | 44.3% |
| 2014 vs 1999 | 40-49 | 15 | ~1965-74 | 39.2% |
| 2009 vs 1999 | 30-39 | 10 | ~1970-79 | 44.2% |
| 2009 vs 1999 | 40-49 | 10 | ~1960-69 | 43.8% |

{: .wide }

![Movilidad absoluta en Japon](/assets/images/japon/mobility_japan.png)
*Figura 1. Movilidad absoluta intergeneracional por comparacion. La linea punteada marca el 50% (coin flip). El resultado principal (G=20, edad 30-39) es del 48.7%.*

La movilidad de la cohorte 1980-89 es del **48.7%** -- esencialmente un coin flip. Algo menos de la mitad de los hogares jovenes japoneses ganan mas que sus padres a la misma edad en terminos reales.

---

## 4. Por que no el 65-75% que predecia la hipotesis

La prediccion basada en la tesis de Chetty era clara: con Gini de 0.33 (similar a los paises nordicos), Japon deberia tener una movilidad en el rango 65-75%. La movilidad real del 49% esta 15-25 puntos por debajo.

La razon es sencilla y la vimos en el [articulo anterior]({{ site.baseurl }}/2026/03/05/distribucion-renta-japon.html): **las distribuciones de 1999 y 2019 son practicamente identicas**. Si los hijos ganan lo mismo que los padres a la misma edad, la probabilidad de ganar *mas* es, por definicion, del 50%.

![CDFs de hijos vs padres](/assets/images/japon/cdf_child_vs_parent.png)
*Figura 2. CDFs de renta del hogar para padres (30-39 en 1999, gris) e hijos (30-39 en 2019, rojo). Las distribuciones se superponen casi completamente.*

La descomposicion de Chetty tiene dos canales:

1. **Canal de crecimiento**: si la renta media sube, la CDF de los hijos se desplaza a la derecha → mas hijos ganan mas que sus padres
2. **Canal de distribucion**: si la desigualdad es baja, los padres estan "apilados" cerca de la mediana → cualquier desplazamiento de la CDF afecta a mas hogares

En EEUU, el canal 1 estaba activo (crecimiento real positivo) pero el canal 2 estaba en contra (alta desigualdad). En Japon, el canal 2 esta a favor (baja desigualdad) pero el canal 1 esta completamente desactivado (crecimiento real cero).

**El resultado japones demuestra que ambos canales son necesarios.** Una buena distribucion amplifica el efecto del crecimiento, pero no puede crear movilidad de la nada. Sin crecimiento real, la movilidad converge al 50% independientemente de la distribucion.

---

## 5. Sensibilidad al rho

Una propiedad interesante del caso japones: la movilidad es casi insensible al parametro rho (la correlacion intergeneracional).

![Sensibilidad al rho](/assets/images/japon/sensitivity_rho.png)
*Figura 3. Movilidad absoluta como funcion de rho, para la comparacion 30-39 (2019 vs 1999). El rango total es de apenas 3-4 puntos porcentuales.*

| rho | Movilidad |
|-----|-----------|
| 0.00 | 49.7% |
| 0.20 | 49.3% |
| 0.34 | 48.7% |
| 0.50 | 47.6% |
| 0.60 | 46.8% |

Esto tiene una explicacion matematica elegante. La copula solo importa cuando las dos distribuciones son diferentes: reordena la asociacion entre posiciones parentales e ingresos filiales. Pero cuando las dos CDFs son identicas, el rango de la renta parental en la distribucion filial es el mismo que en la parental. La copula apenas tiene efecto.

En contraste, en Espana (donde hay crecimiento real y las CDFs son distintas), la movilidad varia significativamente con rho (de 40% a 70% entre rank-preserving e independencia). En Japon, la incertidumbre sobre rho es irrelevante.

Esto es tanto una buena y una mala noticia. Buena: nuestro resultado es robusto a la principal asuncion no testeable del modelo. Mala: confirma que no hay crecimiento real que "activar" con mejor distribucion.

---

## 6. Caveats

Varias limitaciones deben acompanar la interpretacion:

1. **Gap G=20, no G=25.** Las encuestas quinquenales imponen G=20 como el gap mas cercano al ideal de Chetty. Un gap menor (G=15, G=10) produce movilidades similares o ligeramente menores, lo que sugiere que G=20 no introduce un sesgo significativo.

2. **Bandas de edad amplias.** El grupo 30-39 abarca 10 anos. Dentro de la banda, los de 39 pueden tener rentas muy distintas a los de 30. La NSFIE 2019, con bandas de 5 anos, permite algo mas de granularidad, pero la comparacion con 1999 (bandas de 10 anos) obliga a agregar.

3. **Renta del hogar, no individual.** Medimos renta del hogar (household income), no renta per earner. La composicion del hogar ha cambiado en Japon (hogares mas pequenos, mas mujeres trabajando). Esto puede afectar la comparabilidad.

4. **Tablas agregadas, no microdatos.** Las medianas y percentiles son interpolaciones lineales dentro de tramos. Con 10 tramos (1999-2014), la precision es limitada. Con 41 tramos (2019), es razonable.

5. **2009 no comparable.** La ola 2009 solo cubre hogares con trabajadores, no todos los hogares de 2+ personas. La incluimos en analisis de sensibilidad pero no en el resultado principal.

---

## 7. Implicaciones

El resultado japones es importante para la economia de la movilidad intergeneracional:

- **Chetty tenia media razon.** La desigualdad importa, pero no es el unico factor. El crecimiento tambien importa. La descomposicion de Chetty funciona, pero en ambas direcciones.
- **Japon refuta el extremo "solo distribucion".** Un pais puede tener la distribucion mas igualitaria del G7 y aun asi tener movilidad del 50% si la renta no crece.
- **El contrafactual cruzado es revelador.** Si Japon hubiera tenido el crecimiento de EEUU (+30% real) con su propia distribucion, la movilidad habria sido ~70-75%. Si EEUU hubiera tenido el crecimiento de Japon (0%) con su propia distribucion, la movilidad habria sido similar: ~50%.

El [siguiente articulo]({{ site.baseurl }}/2026/03/05/japon-vs-espana-movilidad.html) compara estos resultados con los de Espana, otro pais con movilidad similar (~44%) pero por razones opuestas.

---

## Referencias

- Chetty, R., Grusky, D., Hell, M., Hendren, N., Manduca, R., & Naidu, J. (2017). "The Fading American Dream: Trends in Absolute Income Mobility Since 1940." *Science*, 356(6336), 398-406.
- Manduca, R., Hell, M., Adermon, A., et al. (2024). "Trends in Absolute Income Mobility in North America and Europe." *American Economic Journal: Applied Economics*.
- Statistics Bureau of Japan. *National Survey of Family Income and Expenditure* (全国家計構造調査). [e-Stat](https://www.e-stat.go.jp/).
- Corak, M. (2013). "Income Inequality, Equality of Opportunity, and Intergenerational Mobility." *Journal of Economic Perspectives*, 27(3), 79-102.
