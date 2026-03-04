---
layout: post
title: "¿A qué edad medir la movilidad? Determinación de la edad óptima de medición"
date: 2026-03-04
series: movilidad
part: 2
---

*Este es el segundo artículo de una serie sobre movilidad intergeneracional
en España. Complementa el [primer artículo]({{ site.baseurl }}/2026/03/04/movilidad-absoluta-espana.html)
desarrollando un algoritmo sistemático para elegir la edad de medición óptima,
y enmarca el análisis español en un proyecto multicountry que extiende
Chetty/Manduca a países no cubiertos.*

> **Hallazgo central.** La edad óptima de medición en España es **38 años**
> (mediana de 13 cohortes con estabilización, umbral 2 pp). A esa edad,
> la movilidad oscila entre 36,7% y 49,4% (media 44,0%) — consistentemente
> por debajo del umbral del 50%. El algoritmo es country-agnostic y puede
> aplicarse a cualquier país con datos a múltiples edades.

---

## Motivación

El [primer estudio]({{ site.baseurl }}/2026/03/04/movilidad-absoluta-espana.html) de esta serie documentó una tensión: la movilidad absoluta en España aparece en caída dramática o crónicamente baja pero estable, según se mida a los 30 o a los 40 años. La diferencia no es trivial — 43 pp de caída a edad 30 vs. 9 pp de rango a edad 40. ¿Cuál es la edad "correcta"?

La edad a la que se mide la renta de los hijos tiene un impacto sustancial en las estimaciones de movilidad absoluta. En países con alta precariedad juvenil y emancipación tardía (especialmente el sur de Europa), la renta laboral a los 28–30 años subestima la renta permanente de las cohortes recientes, exagerando la caída de movilidad intergeneracional.

En lugar de elegir a priori entre edad 30 y 40, desarrollamos un **algoritmo de estabilización** que determina sistemáticamente la edad óptima de medición.

---

## 1. Contexto: movilidad absoluta vs. relativa

La literatura sobre movilidad intergeneracional distingue dos dimensiones conceptualmente independientes.

**Movilidad absoluta** mide la fracción de hijos cuya renta real supera la de sus padres a la misma edad. Es un indicador de progreso intergeneracional en nivel de vida que depende conjuntamente del crecimiento agregado y de su distribución. Chetty et al. (2017) estiman que en EEUU esta fracción cayó del 92% (cohorte 1940) al 50% (cohorte 1984), y que la descomposición contrafactual atribuye aproximadamente dos tercios de la caída al deterioro de la distribución, no a la desaceleración del crecimiento: con la distribución de 1940, la movilidad solo habría descendido al ~80%.

**Movilidad relativa** mide el grado de asociación entre la posición de padres e hijos en sus respectivas distribuciones de renta. Se estima mediante la elasticidad intergeneracional (IGE), la correlación rank-rank (RRC) o matrices de transición entre quintiles (e.g., Kenedi & Sirugue, 2023, para Francia). A diferencia de la movilidad absoluta, es invariante al nivel de crecimiento agregado: captura la igualdad de oportunidades en sentido posicional, pero no informa sobre si las generaciones sucesivas progresan en términos reales.

Ambas medidas pueden divergir. Una economía estancada con distribución igualitaria y baja persistencia intergeneracional exhibirá alta movilidad relativa pero movilidad absoluta próxima al 50% (ausencia de crecimiento). Inversamente, una economía con fuerte crecimiento y alta persistencia tendrá baja movilidad relativa pero alta movilidad absoluta, dado que el crecimiento eleva la renta de los hijos por encima de la de sus padres incluso en la cola inferior de la distribución.

### Interpretación del umbral del 50%

El 50% de movilidad absoluta es un umbral con significado sustantivo: por encima, la mayoría de los hijos supera a sus padres en renta real; por debajo, la mayoría no lo logra — hay regresión intergeneracional neta. Con crecimiento real nulo y redistribución aleatoria entre generaciones, la movilidad esperada es exactamente 50% (un coin flip). Valores significativamente superiores requieren crecimiento real positivo; valores inferiores indican crecimiento negativo o, crucialmente, crecimiento positivo cuyas ganancias se concentran en la parte alta de la distribución sin trasladarse a la mediana.

Éste es el resultado central de Chetty et al. (2017) para EEUU: la movilidad absoluta descendió del 92% (cohorte 1940) al 50% (cohorte 1984) — "The Fading American Dream" convertido en un coin flip. La descomposición contrafactual demuestra que el crecimiento agregado fue suficiente para sostener la movilidad; fue el aumento de la desigualdad lo que canalizó las ganancias hacia arriba, dejando a la mayoría por debajo de sus padres.

Para España, nuestras estimaciones a edad 38 oscilan entre 36,7% y 49,4% (media 44,0%) para las cohortes 1972–1988 — consistentemente por debajo del umbral. Esto implica que, incluso medida a una edad suficientemente madura para evitar sesgos de ciclo vital, la mayoría de los individuos de estas cohortes percibe rentas laborales reales inferiores a las de sus padres a la misma edad.

### ¿Tiene suelo la movilidad absoluta?

Chetty et al. (2017) acaba en la cohorte 1984 (observada a ~30 años en ~2014, el último dato disponible para el paper de 2017). No es una elección: es el límite de lo que los registros fiscales permitían observar a edad adulta en ese momento. Manduca et al. (2024) extiende la serie hasta ~1987 para algunos de sus 7 países (Canadá, Finlandia, Países Bajos, Noruega, Suecia, UK, EEUU). Chetty et al. (2024, NBER WP 32697, "Changing Opportunity") cubre cohortes 1978–1992 con datos fiscales, pero cambia de pregunta: analiza movilidad *relativa* desagregada por raza y clase, no actualiza la serie de movilidad absoluta.

Lo que sabemos de las cohortes posteriores a 1984:

- **EEUU y Canadá**: Manduca (2024) estima movilidad absoluta en torno al 50%, estable o en leve descenso. Chetty (2024) documenta que la brecha de clase creció un 30% entre cohortes 1978–1992 (blancos ricos mejoran, blancos pobres empeoran), lo que es compatible con una movilidad absoluta que no se recupera.
- **Nórdicos**: Noruega mantiene ~75% estable (cohortes 1964–1983). Finlandia desciende a 55% para la cohorte 1990.
- **UK y Países Bajos**: altas pero descendiendo al final del periodo.

¿Puede la movilidad absoluta caer significativamente por debajo del 50%? La respuesta es sí, y no es un escenario teórico: nuestras estimaciones para España ya están ahí (media 44%), y la cohorte 1976 registra un 36,7%. Una movilidad del 36,7% significa que casi dos de cada tres hijos ganan menos en términos reales que sus padres a la misma edad.

El 50% no es un suelo natural. Es el punto de equilibrio con crecimiento cero, pero la movilidad puede descender arbitrariamente si:

1. **La economía se contrae** en términos reales entre generaciones (el caso extremo: Grecia post-2010, donde el PIB real per cápita cayó un 25% — para esas cohortes la movilidad absoluta será muy baja).
2. **El crecimiento es positivo pero capturado por la parte alta de la distribución**: la renta media crece, pero la mediana se estanca o cae. Esto es lo que ocurre en EEUU desde los 80 y, en menor medida, en España.
3. **Ambas cosas simultáneamente**: bajo crecimiento + distribución que empeora. Es el peor escenario, y plausiblemente describe a Italia y Grecia.

¿Refleja un empobrecimiento del país? Depende de qué se entienda por "empobrecimiento". Una movilidad del 40% es compatible con un país cuyo PIB per cápita crece — pero cuyo crecimiento beneficia desproporcionadamente a las rentas altas, a los propietarios de activos, o a las cohortes que ya estaban establecidas. El *país* puede ser más rico; la *generación* que entra al mercado laboral, más pobre que la de sus padres. Es una divergencia entre riqueza agregada y experiencia generacional que la movilidad absoluta captura con precisión y que las métricas macroeconómicas convencionales (PIB, renta per cápita) invisibilizan.

Ésta es quizás la contribución más potente del marco de Chetty: reformula "¿va bien la economía?" como "¿viven los hijos mejor que sus padres?" — y la respuesta, para un número creciente de países y cohortes, es que no.

---

## 2. La curva del Gran Gatsby

La Great Gatsby Curve (Krueger, 2012) documenta la correlación cross-country positiva entre desigualdad de renta (Gini) e inmovilidad relativa intergeneracional (IGE):

```
Inmovilidad    EEUU ●
relativa         UK ●
(IGE)      Francia ●        ● Italia
                     Alemania ●
                        Canadá ●
                   ● Japón
                ● Suecia
             ● Dinamarca
             ● Noruega
           ──────────────────────────►
           baja           alta
                Desigualdad (Gini)
```

Nótese que se trata de una relación entre *niveles* de desigualdad y movilidad *relativa* — una regularidad estática entre países. La contribución de Chetty es distinta: muestra que *cambios* en la distribución dentro de un país se traducen en caídas de movilidad *absoluta* a lo largo del tiempo. La curva del Gran Gatsby ofrece el correlato cross-section; la descomposición de Chetty ofrece el mecanismo dinámico.

Un proyecto multicountry permite articular ambas perspectivas. Si la descomposición de Chetty se generaliza, los países cuya distribución se ha mantenido estable (Japón, nórdicos) deberían presentar trayectorias de movilidad absoluta más resistentes que aquellos donde la desigualdad creció (EEUU, UK), con independencia de sus tasas de crecimiento.

---

## 3. Algoritmo de determinación de la edad óptima

### Input

Un CSV con schema `(cohort, target_age, method, sex, mobility)` donde:
- `cohort`: año de nacimiento de la cohorte de hijos
- `target_age`: edad central de medición (la ventana real es `[age-2, age+2]`)
- `method`: método de cópula (`gaussian`, `rank_preserving`, `independence`)
- `sex`: `all`, `male`, `female`
- `mobility`: fracción de hijos que gana más que sus padres (0–1)

### Parámetros

- **Ventana de edad**: `[target_age - 2, target_age + 2]` (5 años)
- **Gap generacional G**: asumido 25 años (ver nota abajo)
- **Offset temporal**: `target_age - G`. Para un hijo nacido en año C medido a edad A, el padre (nacido en ~C-G) se observa en año C + (A - G), es decir, cuando el padre tenía la misma edad A.
- **Umbral de estabilización**: 2 pp (configurable)
- **Mínimo de puntos**: 4 edades de medición por cohorte

### Nota sobre el gap generacional

El gap G = 25 es la edad media aproximada de los padres al nacer el hijo. Este valor determina *a qué generación de padres estamos comparando*: un G más alto empareja a los hijos con padres más viejos (nacidos antes, observados en años anteriores).

El valor de 25 es una simplificación que procede de Chetty et al. (2017) y Manduca et al. (2024). En la práctica, la edad media al primer hijo varía entre países y cohortes:

| País | ~1975 | ~2000 | ~2020 |
|:---|:---:|:---:|:---:|
| España | ~25 | ~29 | ~32 |
| Francia | ~25 | ~28 | ~29 |
| Alemania | ~25 | ~28 | ~30 |
| Italia | ~25 | ~29 | ~32 |
| Japón | ~25 | ~29 | ~31 |
| Nórdicos | ~24 | ~28 | ~29 |

Para las cohortes de padres de los años 70 (que son los padres de nuestros hijos nacidos en 1975–1995), G ≈ 25 es razonable. Para cohortes más recientes, el gap real es mayor. Un error de ±3 años en G desplaza el año de observación del padre en 3 años; dado que las distribuciones de renta parental cambian lentamente entre años adyacentes, el efecto sobre la movilidad estimada es modesto.

### Procedimiento

1. **Filtrar** a method=gaussian, sex=all (estimación central)

2. **First differences** por cohorte:
   ```
   delta(A) = mobility(A+2) - mobility(A)
   ```
   donde A recorre las edades de medición disponibles en pasos de 2.

3. **Edad de estabilización** por cohorte: primer A tal que `|delta(A')| < umbral` para todo A' ≥ A. Es decir, la primera edad desde la cual todos los cambios subsiguientes son menores al umbral.

4. **Edad óptima global**: mediana de las edades de estabilización de todas las cohortes que estabilizan.

### Propiedades del algoritmo

- **Country-agnostic**: solo necesita el CSV descrito arriba
- **Robusto a datos faltantes**: excluye cohortes con <4 puntos de edad
- **Conservador**: exige que *todos* los cambios subsiguientes estén bajo el umbral, no solo el primero
- No todas las cohortes estabilizan (si las differences oscilan); estas se excluyen del cómputo de la mediana

---

## 4. Resultados para España

### Datos de entrada

- **Fuente hijos**: ECV (Encuesta de Condiciones de Vida), 2006–2025
- **Fuente padres**: ECPF per-earner (cabeza de hogar), 1985–2001
- **Edades de medición**: 28, 30, 32, 34, 36, 38, 40, 42
- **Cópula**: Gaussian con ρ = 0,34
- **Renta**: laboral, deflactada a euros constantes 2025

### Movilidad por edad de medición

| Edad de medición | Rango de movilidad (pp) | Movilidad media (%) |
|:---:|:---:|:---:|
| 28 | 18,2 | 36,8 |
| 30 | 14,7 | 40,2 |
| 32 | 11,9 | 42,1 |
| 34 | 8,4 | 43,1 |
| 36 | 8,1 | 43,7 |
| 38 | 12,7 | 44,0 |
| 40 | 9,4 | 44,5 |
| 42 | 9,4 | 44,6 |

*Nota: "rango" = max − min de movilidad Gaussian entre cohortes en esa edad.*

A medida que la edad de medición aumenta, la movilidad media sube (los hijos ganan más) y el rango inter-cohortes se comprime (menos ruido de ciclo vital). Sin embargo, medir a edades demasiado altas reduce el número de cohortes observables. El algoritmo busca el punto de estabilización: la edad mínima a partir de la cual las estimaciones dejan de cambiar significativamente.

### Ejemplo paso a paso: cohorte 1984

La cohorte 1984 tiene datos a las 8 edades. La movilidad Gaussian (% de hijos que gana más que sus padres) es:

| Edad | 28 | 30 | 32 | 34 | 36 | 38 | 40 | 42 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Movilidad (%) | 35,8 | 32,1 | 35,0 | 41,0 | 45,7 | 49,4 | 47,5 | 45,7 |

A edades jóvenes la estimación oscila mucho: sube, baja, vuelve a subir. Es ruido de ciclo vital — a los 28–32 muchos aún están terminando de estudiar o en empleos precarios.

Computamos las first differences (cambio al pasar de una edad a la siguiente, en puntos porcentuales):

| Paso | Delta | \|delta\| < 2? |
|:---|:---:|:---:|
| 28→30 | −3,8 pp | NO |
| 30→32 | +3,0 pp | NO |
| 32→34 | +6,0 pp | NO |
| 34→36 | +4,7 pp | NO |
| 36→38 | +3,7 pp | NO |
| **38→40** | **−1,9 pp** | **SÍ** |
| **40→42** | **−1,8 pp** | **SÍ** |

¿Dónde estabiliza? Buscamos la primera edad desde la cual **todos** los deltas subsiguientes son menores a 2 pp:

- ¿Desde 28? No — el delta 28→30 es −3,8
- ¿Desde 30? No — el delta 30→32 es +3,0
- ... (todos los pasos hasta 36→38 superan 2 pp)
- **¿Desde 38?** El delta 38→40 es −1,9 (< 2) Y el delta 40→42 es −1,8 (< 2). **SÍ** — todos los cambios desde 38 son menores a 2 pp.

**→ La cohorte 1984 estabiliza a edad 38.** Medir a 38, 40 o 42 da resultados similares (~46–49%), pero medir a 28–36 da resultados muy distintos (32–46%). La edad 38 es el punto a partir del cual la estimación ya no depende significativamente de la edad elegida.

### Segundo ejemplo: cohorte 1980

| Edad | 30 | 32 | 34 | 36 | 38 | 40 | 42 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Movilidad (%) | 42,3 | 40,1 | 37,7 | 39,3 | 43,8 | 45,4 | 44,1 |

| Paso | Delta | \|delta\| < 2? |
|:---|:---:|:---:|
| 30→32 | −2,2 pp | NO |
| 32→34 | −2,3 pp | NO |
| 34→36 | +1,6 pp | SÍ |
| 36→38 | +4,5 pp | NO |
| 38→40 | +1,6 pp | SÍ |
| 40→42 | −1,3 pp | SÍ |

- ¿Desde 34? No — 34→36 está bajo el umbral (+1,6), pero 36→38 lo supera (+4,5). El algoritmo exige que **todos** los pasos restantes estén bajo el umbral, no solo el primero.
- **¿Desde 38?** SÍ — +1,6 y −1,3, ambos bajo el umbral.

**→ La cohorte 1980 también estabiliza a edad 38.**

### Del ejemplo individual a la edad global

Se repite este cálculo para las 19 cohortes que tienen ≥4 edades de medición:

| Cohorte | N edades | Edad estab. | Grupo |
|:---:|:---:|:---:|:---|
| 1974 | 4 | 40 | Boom |
| 1975 | 4 | — | Boom |
| 1976 | 5 | — | Boom |
| 1977 | 5 | 40 | Boom |
| 1978 | 6 | — | Boom |
| 1979 | 6 | 40 | Boom |
| 1980 | 7 | 38 | Crisis |
| 1981 | 7 | 40 | Crisis |
| 1982 | 8 | 40 | Crisis |
| 1983 | 8 | — | Crisis |
| 1984 | 8 | 38 | Crisis |
| 1985 | 7 | 38 | Crisis |
| 1986 | 7 | 38 | Crisis |
| 1987 | 6 | 36 | Recuperación |
| 1988 | 6 | — | Recuperación |
| 1989 | 5 | — | Recuperación |
| 1990 | 5 | 30 | Recuperación |
| 1991 | 4 | 30 | Recuperación |
| 1992 | 4 | 30 | Recuperación |

13 de 19 cohortes estabilizan. 6 nunca estabilizan (sus deltas oscilan por encima de 2 pp en todo el rango) — se excluyen.

Las 13 edades de estabilización, ordenadas:

> 30, 30, 30, 36, **38**, 38, 38, 38, 40, 40, 40, 40, 40

La mediana (valor central, el 7.º de 13) es **38**.

### Resumen por grupo de cohortes

| Grupo | Cohortes | Mediana estab. | IQR |
|:---|:---:|:---:|:---:|
| Boom (≤1979) | 1974–1979 | 40 | [40–40] |
| Crisis (1980–1986) | 1980–1986 | 38 | [38–40] |
| Recuperación (≥1987) | 1987–1992 | 30 | [30–36] |

### Edad recomendada: 38

- **Mediana global**: **38**
- **Media**: 37,1
- **IQR**: [30–40]

### Caveat sobre cohortes de recuperación

Las cohortes 1990–1992 "estabilizan" a edad 30 porque solo se observan a 4–5 edades (28–36). Con tan pocos datos a edades mayores, no se detectan cambios — pero esto no indica estabilización real. Estas cohortes aún no han alcanzado los 38 años en los datos. Si se excluyen las cohortes con <6 puntos de edad, la mediana sube a 38–40.

---

## 5. Figuras

**Figura 1.** Perfil de movilidad por edad (cohortes representativas). Muestra cómo la curva se aplana con la edad.

![Perfil por edad (multiage)](/assets/images/movilidad/age_profile_multiage_spain.png)

**Figura 2.** Convergencia: first differences (delta) vs. edad. Banda verde = umbral ±2 pp. Muestra la convergencia a cero.

![Convergencia](/assets/images/movilidad/age_convergence_multiage_spain.png)

**Figura 3.** Distribución de edades de estabilización. Línea roja = mediana (38).

![Distribución edad estabilización](/assets/images/movilidad/optimal_age_distribution.png)

**Figura 4.** Movilidad a edad óptima (38). Las 3 cópulas con fill between. 17 cohortes: 1972–1988.

![Movilidad a edad óptima](/assets/images/movilidad/mobility_at_optimal_age_spain.png)

**Figura 5.** Comparación entre edades: movilidad Gaussian a edades 30, 38 y 40 para cohortes solapantes (1980–1986). Visualiza el efecto de la elección de edad.

![Comparación entre edades](/assets/images/movilidad/mobility_age_comparison_30_38_40.png)

---

## 6. Movilidad a edad 38: resultados definitivos

A la edad óptima de 38 años, la movilidad Gaussian (ρ=0,34) para las 17 cohortes observables (1972–1988) oscila entre **36,7% y 49,4%**, con una media de **44,0%**. Todas las cohortes están por debajo o en el borde del umbral del 50%.

El patrón temporal muestra:
- Cohortes **boom** (1972–1979): movilidad moderada (~40–49%), con variación notable
- Cohortes **crisis** (1980–1986): rango comprimido (~38–49%), sin la caída catastrófica visible a edad 30
- Cohortes **recuperación** (1987–1988): solo 2 cohortes observables, ~43–45%

Comparado con el análisis a edad 30 del primer estudio (caída de 75% a 32%), el panorama a edad 38 es cualitativamente diferente: no hay colapso, sino un nivel crónicamente bajo con variación moderada.

---

## 7. El proyecto multicountry: extensión a otros países

### Objetivo

Extender el análisis de movilidad absoluta de Chetty/Manduca a países no cubiertos por ellos. Manduca et al. (2024) cubre 7 países (Canadá, Finlandia, Países Bajos, Noruega, Suecia, UK, EEUU). Nosotros añadimos los grandes que faltan: **Italia, España, Grecia y Japón** con datos nacionales directos, más la validación contra Chetty con CPS para EEUU. Francia y Alemania quedan para un paquete LIS institucional.

### Países y fuentes de datos

**Accesibles sin afiliación institucional:**

| País | Encuesta nacional | Serie | Cohortes hijos est. |
|---|---|---|---|
| **España** | ECV + ECPF | 2006–2025 / 1985–2001 | ~1968–1998 |
| **Italia** | SHIW (Bank of Italy) | 1977–2022 (bienal) | ~1947–1992 |
| **EEUU** | CPS/ASEC (IPUMS) | 1962–presente | ~1932–1994 |
| **UK** | FRS (UK Data Service) | 1992–presente | ~1962–1994 |
| **Grecia** | EU-SILC (ELSTAT PUF) | 2005–presente | ~1975–1994 |

**Caso especial (tablas agregadas):**

| País | Fuente | Notas |
|---|---|---|
| **Japón** | NSFIE/FIES (e-Stat) | Tablas quinquenales 1959–2019. 30 cohortes potenciales. |

**Bloqueados (requieren afiliación institucional):**

| País | Encuesta | Barrera |
|---|---|---|
| **Francia** | ERFS (INSEE/CASD) | Sponsor institucional + comité confidencialidad |
| **Alemania** | SOEP (DIW) / EVS (Destatis) | Afiliación a institución científica |

**Nota sobre Francia**: no existe ningún estudio publicado de movilidad absoluta (fracción que gana más que sus padres) para Francia con el método Chetty/Manduca. Kenedi & Sirugue (2023, *J. Public Economics*) estiman movilidad *relativa* (rank-rank) con datos fiscales+censo para cohortes 1972–1981, pero no la medida absoluta. Francia es un hueco real en la literatura.

### Hipótesis por país

| País | Patrón esperado | Por qué |
|---|---|---|
| **EEUU** | Alta → baja (92% → 50%) | Ya medido por Chetty. Distribución cada vez peor. |
| **UK** | Moderada → baja | Thatcher destruyó la distribución, pero menos que Reagan. |
| **Italia** | Nunca alta → baja | Distribución mala (Mezzogiorno), crecimiento estancado desde los 90. |
| **España** | Moderada-alta → baja | Crecimiento enorme pero distribución mala siempre. Crisis 2008 devastadora. |
| **Grecia** | Moderada → catastrófica | Crisis 2010–2015 destruyó a una generación entera. |
| **Japón** | Muy alta → moderada | Milagro + buena distribución → estancamiento. Caída por crecimiento, no distribución. |

### El test japonés: la prueba de fuego de la tesis de Chetty

El caso japonés es la **prueba de fuego** de la tesis de Chetty. Japón y EEUU son opuestos simétricos:

| | EEUU | Japón |
|---|---|---|
| **Crecimiento 1980–2020** | Moderado (~2% real) | Bajo (~1% real) |
| **Distribución** | Muy desigual y empeorando | Relativamente igualitaria y estable |

Si Chetty tiene razón — si la distribución importa más que el crecimiento — entonces **Japón debería haber caído menos que EEUU** a pesar de 30 años de estancamiento. La movilidad absoluta japonesa debería haberse mantenido razonablemente alta (~65–75%) mientras que la americana colapsó al 50%.

Si esto se confirma con datos, es un resultado extraordinario: un país que apenas creció durante tres décadas mantuvo mejor el sueño de progreso intergeneracional que el país más rico del mundo, simplemente porque repartió mejor lo poco que creció.

Si por el contrario Japón cayó tanto como EEUU, eso sugeriría que el crecimiento importa más de lo que Chetty estima, y que la descomposición de la Figure 5 sobrevalora el papel de la distribución.

### Generalización del algoritmo

El algoritmo de edad óptima es completamente agnóstico respecto al país. Para aplicarlo a un nuevo país:

1. Ejecutar el pipeline de movilidad a múltiples edades (mínimo 28–42 en pasos de 2)
2. Generar el CSV con schema `(cohort, target_age, method, sex, mobility)`
3. Ejecutar `find_optimal_age.py` apuntando al CSV del país

La edad óptima puede variar entre países. En países con mercados laborales más fluidos (ej. nórdicos), la estabilización puede ocurrir antes. En países con precariedad juvenil extrema (ej. sur de Europa), será más tardía.

**Caveat sobre comparabilidad cross-country**: las estimaciones de movilidad absoluta NO son directamente comparables entre países si se miden a edades distintas. Nuestro 44% para España (edad 38) no puede contrastarse con el 50% de Chetty para EEUU (edad 30) — la diferencia podría ser enteramente un artefacto de la edad de medición. Para comparaciones legítimas, o bien se mide cada país a su edad óptima y se interpreta cada serie por separado, o bien se estima un rango común con el caveat de que puede no ser óptimo para cada país.

---

## Referencias

- Chetty, R., Grusky, D., Hell, M., Hendren, N., Manduca, R. y Naidu, S. (2017). "The Fading American Dream: Trends in Absolute Income Mobility Since 1940." *Science*, 356(6336), 398–406.

- Chetty, R. et al. (2024). "Changing Opportunity: Societal Factors Affecting Intergenerational Mobility." NBER Working Paper 32697.

- Manduca, R., Hell, M., Adermon, A. et al. (2024). "Trends in Absolute Income Mobility in North America and Europe." *American Economic Journal: Applied Economics*, 16(2), 1–30.

- Kenedi, G. y Sirugue, L. (2023). "Intergenerational Income Mobility in France: A Comparative and Geographic Analysis." *Journal of Public Economics*, 226, 104973.

- Krueger, A. (2012). "The Rise and Consequences of Inequality in the United States." Council of Economic Advisers.

- INE (2006–2025). *Encuesta de Condiciones de Vida. Microdatos.*

- INE (1985–2001). *ECPF Base 85 y Base 97. Microdatos.*

*Fuentes: INE (ECV 2006–2025, ECPF Base 85 y Base 97, IPC enlazado).*
