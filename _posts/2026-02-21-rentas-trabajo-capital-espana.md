---
layout: post
title: "Rentas del trabajo vs rentas del capital en España (2009-2024)"
date: 2026-02-21
series: impuestos
part: 6
---

*Este es el sexto artículo de una [serie](https://memoteca.github.io/) sobre fiscalidad y desigualdad en España.
En los artículos anteriores calculamos la
[carga fiscal bruta del asalariado](/2026/02/09/impuestos-progresivos-espana.html),
las [transferencias y carga neta](/2026/02/10/transferencias-carga-neta-espana.html),
la [distribución de la riqueza](/2026/02/11/distribucion-riqueza-espana.html),
la [situación de la vivienda](/2026/02/12/vivienda-propiedad-alquiler-espana.html) y
la [tributación corporativa en la UE](/2026/02/14/tributacion-corporativa-ue.html).
Aquí comparamos cómo han evolucionado las rentas del trabajo y las del capital
en España durante la última década, utilizando datos fiscales reales de la AEAT.*

---

## Resumen

Entre 2013 y 2023, las **rentas del capital han crecido sistemáticamente más
que las del trabajo** en España, según los datos de declaraciones fiscales
de la Agencia Tributaria:

- **IRPF**: las rentas del capital crecieron un +46% real frente al +31% del trabajo.
- **Sociedades**: el EBITDA empresarial creció un +90% real, mientras que los gastos
  de personal lo hicieron un +43%.
- **Salario medio puro** (modelo 190): pasó de 14,245€
  a 16,853€ nominales (+18.3%), pero solo
  +-0.9% en términos reales (descontando inflación).
- **Labor share**: la participación de los salarios en el valor añadido cayó del
  67.5% al 61.1% (-6.4 puntos porcentuales).

![Evolución de rentas IRPF](/assets/images/rentas/01_irpf_rentas_real_ipc.png)

---

## Fuentes de datos

| Fuente | Descripción | Acceso |
|--------|-------------|--------|
| AEAT modelo100.csv | Declaraciones IRPF por partidas, serie 2009-2023 | [Descarga masiva](https://sede.agenciatributaria.gob.es/Sede/estadisticas/anuario-estadistico/acceso-descarga-masiva-datos.html) |
| AEAT modelo200.csv | Impuesto de Sociedades, serie 2009-2023 | Misma página |
| AEAT DistribucionSalarios.xlsx | Salarios puros (modelo 190), serie 2001-2024 | [Informes de Recaudación](https://sede.agenciatributaria.gob.es/Sede/datosabiertos/catalogo/hacienda/Informes_anuales_de_Recaudacion_Tributaria.shtml) |
| AyudaCSV_AnuarioTotal.pdf | Diccionario de variables (M100_\*, M200_\*) | Misma página que modelo100 |
| INE tabla 50934 | IPC general, media anual (base 2021=100) | [INE API](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/50934) |
| INE tablas 67196 / 67822 | PIB nominal e índices de volumen (CNTr) | [INE API](https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/67196) |

## Metodología

### Variables del IRPF (modelo 100)

| Concepto | Columnas | Descripción |
|----------|----------|-------------|
| Rendimientos del trabajo | M100_2 | Rendimiento neto reducido. Incluye salarios, pensiones y prestaciones |
| Capital mobiliario | M100_3 + M100_4 | Dividendos, intereses, seguros (base ahorro + general) |
| Capital inmobiliario | M100_6 | Rendimiento neto de alquileres (excluye rentas imputadas M100_5) |
| Actividades económicas | M100_7 + M100_8 + M100_9 | Autónomos: estimación directa + módulos |
| Ganancias patrimoniales | M100_10 + M100_11 | Plusvalías por venta de activos |

**Capital total** = mobiliario + inmobiliario + ganancias. Se excluyen las rentas imputadas
(M100_5) porque son una ficción fiscal que no representa ingresos reales.

### Variables de Sociedades (modelo 200)

| Concepto | Columna | Descripción |
|----------|---------|-------------|
| Valor añadido | M200_16 | Producción menos consumos intermedios |
| Gastos de personal | M200_17 | Salarios + cotizaciones sociales empresariales |
| EBITDA | M200_18 | Resultado bruto de explotación = VA − gastos personal |
| Resultado contable | M200_22 | Beneficio/pérdida neta |

### Salarios puros (modelo 190)

El fichero DistribucionSalarios.xlsx contiene la masa salarial y el número de asalariados
declarados en el modelo 190 (retenciones sobre rendimientos del trabajo), desglosados
por tramos de 1.000€. A diferencia del IRPF (M100_2), estos datos **excluyen pensiones
y prestaciones de desempleo**, por lo que reflejan mejor la evolución de los salarios puros.

### Deflactores

Todos los resultados se presentan en precios corrientes y en **precios constantes de 2021**
usando dos deflactores independientes como test de robustez:

1. **IPC** (Índice de Precios al Consumo): media anual del INE, base 2021=100.
2. **Deflactor del PIB**: calculado como (PIB nominal / índice de volumen) × 100 a partir
   de datos trimestrales de la Contabilidad Nacional del INE, anualizado y rebasado a 2021=100.

La diferencia entre ambos deflactores es de 1-2 puntos porcentuales en todos los indicadores,
lo que confirma la robustez de los resultados.

### Año base y per cápita

Se usa **2013** como año base por ser el punto más bajo del ciclo tras la crisis financiera.
Los indicadores per cápita dividen los agregados entre el número de declarantes (IRPF),
empresas (Sociedades) o asalariados (modelo 190), para corregir por cambios en empleo.

### Limitaciones

- El IRPF solo captura renta declarada; la economía sumergida queda excluida.
- Las ganancias patrimoniales son volátiles (dependen de ventas de activos puntuales).
- Los rendimientos del trabajo en IRPF incluyen pensiones y prestaciones de desempleo.
- El resultado contable de Sociedades en 2013 era casi cero (15.146 M€), lo que distorsiona
  su variación porcentual. El EBITDA es más estable y representativo.
- «Gastos de personal por empresa» no equivale a «salario medio por trabajador»:
  una empresa tiene múltiples empleados y las plantillas varían.

---

## Resultados

### El salario mínimo: +67% en una década

El SMI (Salario Mínimo Interprofesional) ha sido la principal herramienta de política
salarial del período analizado. Su evolución, según datos del
[Ministerio de Trabajo](https://www.mites.gob.es/estadisticas/bel/SMI/index.htm):

| Año | SMI mensual | SMI anual (14 pagas) | Var. acumulada |
|----:|------------:|---------------------:|---------------:|
| 2013 | 645.3€ | 9,034€ | +0.0% |
| 2014 | 645.3€ | 9,034€ | +0.0% |
| 2015 | 648.6€ | 9,080€ | +0.5% |
| 2016 | 655.2€ | 9,173€ | +1.5% |
| 2017 | 707.7€ | 9,908€ | +9.7% |
| 2018 | 735.9€ | 10,303€ | +14.0% |
| 2019 | 900.0€ | 12,600€ | +39.5% |
| 2020 | 950.0€ | 13,300€ | +47.2% |
| 2021 | 950.0€ | 13,300€ | +47.2% |
| 2022 | 1,000.0€ | 14,000€ | +55.0% |
| 2023 | 1,080.0€ | 15,120€ | +67.4% |
| 2024 | 1,134.0€ | 15,876€ | +75.7% |

El SMI creció un **+67.4%** entre 2013 y 2023
(de 645€ a 1,080€/mes), muy por encima del salario medio
(+18.3% nominal). ¿Ha arrastrado a los demás salarios hacia arriba?

### Efecto del SMI en la distribución salarial

La subida del SMI ha reordenado la distribución por tramos. Los datos del modelo 190
([DistribucionSalarios.xlsx](https://sede.agenciatributaria.gob.es/Sede/datosabiertos/catalogo/hacienda/Informes_anuales_de_Recaudacion_Tributaria.shtml))
muestran:

| Tramo salarial anual | Asalariados 2013 | Asalariados 2023 | Variación |
|---------------------:|-----------------:|-----------------:|----------:|
| 0-10k (por debajo del SMI 2023) | 2,144,055 | 1,442,902 | -32.7% |
| 10-15k (entorno del SMI 2023) | 654,213 | 496,929 | -24.0% |
| 15-20k | 571,099 | 458,846 | -19.7% |
| 20-30k | 988,220 | 829,277 | -16.1% |
| 30-50k | 1,801,945 | 1,693,611 | -6.0% |
| 50k+ | 4,390,251 | 5,270,378 | +20.0% |
| **Total** | **10,549,783** | **10,191,943** | **-3.4%** |

La subida del SMI ha sacado a cientos de miles de trabajadores de los tramos más bajos,
pero **no ha arrastrado los salarios medios hacia arriba**: los tramos de 20-50k pierden
entre un 6% y un 20% de asalariados, mientras que el único tramo que crece significativamente
es el de **50k+** (+20%). La polarización salarial se ha acentuado: hay menos trabajadores
en el medio de la distribución y más en los extremos (efecto SMI abajo, efecto mercado arriba).

### Salarios puros (modelo 190, AEAT)

Esta es la serie más limpia para medir la evolución salarial en España,
ya que excluye pensiones y prestaciones.

| Año | Masa salarial (M€) | Asalariados | Salario medio | Var. nominal | Var. real (IPC) |
|----:|-------------------:|------------:|--------------:|-------------:|----------------:|
| 2009 | 242,485 | 16,630,934 | 14,580€ | — | — |
| 2010 | 237,839 | 16,257,775 | 14,629€ | +0.3% | -1.4% |
| 2011 | 235,449 | 16,068,939 | 14,652€ | +0.2% | -2.9% |
| 2012 | 225,023 | 15,556,975 | 14,464€ | -1.3% | -3.6% |
| 2013 | 215,818 | 15,150,285 | 14,245€ | -1.5% | -2.9% |
| 2014 | 217,263 | 15,354,064 | 14,150€ | -0.7% | -0.5% |
| 2015 | 221,983 | 15,684,597 | 14,153€ | +0.0% | +0.5% |
| 2016 | 229,280 | 16,134,410 | 14,211€ | +0.4% | +0.6% |
| 2017 | 239,858 | 16,523,592 | 14,516€ | +2.1% | +0.2% |
| 2018 | 252,174 | 16,909,353 | 14,913€ | +2.7% | +1.0% |
| 2019 | 260,674 | 16,995,939 | 15,337€ | +2.8% | +2.1% |
| 2020 | 241,773 | 16,258,994 | 14,870€ | -3.0% | -2.7% |
| 2021 | 258,664 | 16,554,152 | 15,625€ | +5.1% | +1.9% |
| 2022 | 275,690 | 16,883,561 | 16,329€ | +4.5% | -3.6% |
| 2023 | 285,931 | 16,966,070 | 16,853€ | +3.2% | -0.3% |
| 2024 | 293,685 | 17,123,713 | 17,151€ | +1.8% | -1.0% |

**Resumen 2013→2023**: el salario medio pasó de 14,245€ a
16,853€ (nominal: +18.3%, real IPC: -0.9%).
En 2024 alcanzó 17,151€ (nominal: +20.4% vs 2013).

### IRPF: rentas declaradas por tipo (millones €, precios corrientes)

| Año | Trabajo | Capital total | Cap. mobiliario | Cap. inmobiliario | Ganancias patrim. | Act. económicas | Declarantes |
|----:|--------:|--------------:|----------------:|------------------:|-------------------:|----------------:|------------:|
| 2009 | 324,276 | 46,730 | 25,436 | 7,985 | 13,309 | 24,936 | 23.211 M |
| 2010 | 321,436 | 37,152 | 18,544 | 7,848 | 10,760 | 24,279 | 23.018 M |
| 2011 | 322,958 | 39,348 | 22,421 | 7,486 | 9,442 | 23,104 | 23.160 M |
| 2012 | 309,091 | 33,830 | 18,907 | 7,138 | 7,785 | 22,146 | 23.026 M |
| 2013 | 306,553 | 33,320 | 18,093 | 6,830 | 8,397 | 22,389 | 22.802 M |
| 2014 | 309,934 | 34,847 | 16,631 | 6,907 | 11,310 | 23,461 | 22.908 M |
| 2015 | 320,211 | 37,136 | 15,417 | 7,339 | 14,380 | 26,516 | 22.943 M |
| 2016 | 333,116 | 37,305 | 15,234 | 7,810 | 14,261 | 28,939 | 23.006 M |
| 2017 | 346,942 | 40,829 | 14,449 | 8,404 | 17,975 | 30,951 | 23.155 M |
| 2018 | 361,236 | 48,442 | 16,745 | 9,139 | 22,558 | 33,340 | 23.697 M |
| 2019 | 375,324 | 49,935 | 18,004 | 9,618 | 22,312 | 34,241 | 23.900 M |
| 2020 | 385,497 | 42,678 | 14,425 | 8,630 | 19,622 | 29,173 | 24.431 M |
| 2021 | 405,965 | 49,854 | 14,022 | 9,322 | 26,510 | 38,360 | 24.697 M |
| 2022 | 448,118 | 56,635 | 17,722 | 10,773 | 28,139 | 41,620 | 25.455 M |
| 2023 | 479,165 | 58,056 | 20,553 | 11,626 | 25,877 | 43,897 | 26.423 M |

### IRPF: variación interanual (precios constantes 2021, deflactor IPC)

| Año | Trabajo | Capital total | Act. económicas | Declarantes |
|----:|--------:|--------------:|----------------:|------------:|
| 2009 | — | — | — | — |
| 2010 | -2.6% | -21.9% | -4.4% | -0.8% |
| 2011 | -2.6% | +2.6% | -7.8% | +0.6% |
| 2012 | -6.6% | -16.1% | -6.4% | -0.6% |
| 2013 | -2.2% | -2.9% | -0.3% | -1.0% |
| 2014 | +1.3% | +4.7% | +4.9% | +0.5% |
| 2015 | +3.8% | +7.1% | +13.6% | +0.2% |
| 2016 | +4.2% | +0.7% | +9.4% | +0.3% |
| 2017 | +2.2% | +7.3% | +4.9% | +0.6% |
| 2018 | +2.4% | +16.7% | +5.9% | +2.3% |
| 2019 | +3.2% | +2.4% | +2.0% | +0.9% |
| 2020 | +3.0% | -14.3% | -14.5% | +2.2% |
| 2021 | +2.2% | +13.3% | +27.5% | +1.1% |
| 2022 | +1.8% | +4.8% | +0.1% | +3.1% |
| 2023 | +3.3% | -1.0% | +1.9% | +3.8% |

![Renta media por declarante](/assets/images/rentas/02_irpf_per_declarante_real.png)

### IRPF: renta media por declarante (precios constantes 2021, IPC)

| Año | Trabajo/decl. | Capital/decl. | Trabajo (€ de 2021) | Capital (€ de 2021) |
|----:|--------------:|--------------:|--------------------:|--------------------:|
| 2009 | — | — | 16,217 | 2,337 |
| 2010 | -1.8% | -21.2% | 15,923 | 1,840 |
| 2011 | -3.2% | +2.0% | 15,407 | 1,877 |
| 2012 | -6.0% | -15.6% | 14,478 | 1,585 |
| 2013 | -1.2% | -1.9% | 14,299 | 1,554 |
| 2014 | +0.8% | +4.3% | 14,412 | 1,620 |
| 2015 | +3.7% | +6.9% | 14,941 | 1,733 |
| 2016 | +4.0% | +0.4% | 15,532 | 1,739 |
| 2017 | +1.5% | +6.7% | 15,764 | 1,855 |
| 2018 | +0.1% | +14.0% | 15,775 | 2,115 |
| 2019 | +2.3% | +1.5% | 16,137 | 2,147 |
| 2020 | +0.8% | -16.1% | 16,267 | 1,801 |
| 2021 | +1.0% | +12.1% | 16,438 | 2,019 |
| 2022 | -1.2% | +1.7% | 16,241 | 2,053 |
| 2023 | -0.5% | -4.6% | 16,160 | 1,958 |

### Sociedades: magnitudes agregadas (millones €, precios corrientes)

| Año | Valor añadido | Gastos personal | EBITDA | Resultado contable | Empresas |
|----:|--------------:|----------------:|-------:|-------------------:|---------:|
| 2009 | 428,094 | 298,730 | 129,364 | 62,275 | 1,412.3 k |
| 2010 | 428,988 | 290,775 | 138,213 | 52,481 | 1,414.1 k |
| 2011 | 409,352 | 290,619 | 118,733 | 19,909 | 1,415.0 k |
| 2012 | 372,329 | 274,607 | 97,723 | -31,172 | 1,416.9 k |
| 2013 | 393,525 | 265,675 | 127,851 | 15,146 | 1,428.7 k |
| 2014 | 425,915 | 271,344 | 154,572 | 72,182 | 1,447.3 k |
| 2015 | 458,166 | 285,492 | 172,673 | 69,973 | 1,479.0 k |
| 2016 | 483,525 | 300,889 | 182,635 | 83,933 | 1,552.7 k |
| 2017 | 518,553 | 321,097 | 197,457 | 114,487 | 1,595.9 k |
| 2018 | 561,335 | 341,917 | 219,418 | 134,860 | 1,613.1 k |
| 2019 | 602,845 | 363,041 | 239,804 | 164,345 | 1,642.3 k |
| 2020 | 531,499 | 341,990 | 189,509 | 77,113 | 1,650.8 k |
| 2021 | 606,189 | 375,262 | 230,927 | 155,130 | 1,681.0 k |
| 2022 | 677,007 | 413,759 | 263,248 | 147,143 | 1,702.3 k |
| 2023 | 744,435 | 454,850 | 289,585 | 191,234 | 1,734.8 k |

![EBITDA vs gastos de personal](/assets/images/rentas/03_sociedades_ebitda_vs_salarios.png)

### Sociedades: variación interanual (precios constantes 2021, deflactor IPC)

| Año | Valor añadido | Gastos personal | EBITDA | Empresas |
|----:|--------------:|----------------:|-------:|---------:|
| 2009 | — | — | — | — |
| 2010 | -1.6% | -4.4% | +5.0% | +0.1% |
| 2011 | -7.5% | -3.1% | -16.8% | +0.1% |
| 2012 | -11.2% | -7.8% | -19.7% | +0.1% |
| 2013 | +4.2% | -4.6% | +29.0% | +0.8% |
| 2014 | +8.4% | +2.3% | +21.1% | +1.3% |
| 2015 | +8.1% | +5.7% | +12.3% | +2.2% |
| 2016 | +5.7% | +5.6% | +6.0% | +5.0% |
| 2017 | +5.2% | +4.7% | +6.0% | +2.8% |
| 2018 | +6.5% | +4.7% | +9.3% | +1.1% |
| 2019 | +6.6% | +5.4% | +8.5% | +1.8% |
| 2020 | -11.5% | -5.5% | -20.7% | +0.5% |
| 2021 | +10.6% | +6.4% | +18.2% | +1.8% |
| 2022 | +3.0% | +1.7% | +5.2% | +1.3% |
| 2023 | +6.2% | +6.2% | +6.3% | +1.9% |

![Medias por empresa](/assets/images/rentas/04_sociedades_per_empresa_real.png)

### Labor share: reparto del valor añadido

| Año | Labor share (%) | Capital share (%) |
|----:|----------------:|------------------:|
| 2009 | 69.8% | 30.2% |
| 2010 | 67.8% | 32.2% |
| 2011 | 71.0% | 29.0% |
| 2012 | 73.8% | 26.2% |
| 2013 | 67.5% | 32.5% |
| 2014 | 63.7% | 36.3% |
| 2015 | 62.3% | 37.7% |
| 2016 | 62.2% | 37.8% |
| 2017 | 61.9% | 38.1% |
| 2018 | 60.9% | 39.1% |
| 2019 | 60.2% | 39.8% |
| 2020 | 64.3% | 35.7% |
| 2021 | 61.9% | 38.1% |
| 2022 | 61.1% | 38.9% |
| 2023 | 61.1% | 38.9% |

![Labor share](/assets/images/rentas/05_labor_share.png)

### Deflactores utilizados (base 2021 = 100)

| Año | IPC (media anual) | Deflactor PIB |
|----:|------------------:|--------------:|
| 2009 | 86.150 | 91.776 |
| 2010 | 87.701 | 92.044 |
| 2011 | 90.504 | 91.910 |
| 2012 | 92.717 | 91.723 |
| 2013 | 94.023 | 92.125 |
| 2014 | 93.881 | 91.922 |
| 2015 | 93.412 | 92.430 |
| 2016 | 93.222 | 92.774 |
| 2017 | 95.046 | 93.941 |
| 2018 | 96.638 | 95.056 |
| 2019 | 97.314 | 96.414 |
| 2020 | 97.000 | 97.508 |
| 2021 | 100.000 | 100.000 |
| 2022 | 108.391 | 104.694 |
| 2023 | 112.219 | 111.232 |

---

## Resumen cuantitativo: variación acumulada 2013→2023

### Agregado

| Concepto | Nominal | Real (IPC) | Real (defl. PIB) |
|----------|--------:|-----------:|-----------------:|
| IRPF Trabajo | +56.3% | +31.0% | +29.5% |
| IRPF Capital | +74.2% | +46.0% | +44.3% |
| IRPF Act. económicas | +96.1% | +64.3% | +62.4% |
| Salario medio (mod. 190) | +18.3% | -0.9% | -2.0% |
| IS Valor añadido | +89.2% | +58.5% | +56.7% |
| IS Gastos de personal | +71.2% | +43.4% | +41.8% |
| IS EBITDA | +126.5% | +89.8% | +87.6% |

Declarantes IRPF: +15.9% · Empresas IS: +21.4% · Asalariados mod. 190: +12.0%

### Per cápita

| Concepto | Nominal | Real (IPC) | Real (defl. PIB) |
|----------|--------:|-----------:|-----------------:|
| IRPF Trabajo / declarante | +34.9% | +13.0% | +11.7% |
| IRPF Capital / declarante | +50.4% | +26.0% | +24.5% |
| Salario medio puro (mod. 190) | +18.3% | -0.9% | -2.0% |
| IS EBITDA / empresa | +86.5% | +56.3% | +54.5% |
| IS G. Personal / empresa | +41.0% | +18.1% | +16.8% |

**Labor share**: 67.5% (2013) → 61.1% (2023) = **-6.4 puntos porcentuales**

![Test de robustez: IPC vs deflactor del PIB](/assets/images/rentas/06_robustez_deflactores.png)

---

## Conclusiones

1. **Las rentas del capital crecen sistemáticamente más que las del trabajo.**
   En términos reales (IPC), las rentas del capital declaradas en IRPF crecieron
   un +46.0% entre 2013 y 2023, frente al +31.0%
   de las rentas del trabajo. Per cápita: +26.0% vs +13.0%.

2. **El beneficio empresarial crece más del doble que los salarios.**
   El EBITDA agregado creció un +89.8% real,
   mientras que los gastos de personal crecieron un +43.4%.
   Por empresa: EBITDA +56.3% vs gastos personal +18.1%.

3. **El salario medio real apenas ha subido un -0.9% en diez años**
   (modelo 190, precios constantes IPC). El grueso del aumento nominal (+18.3%)
   se lo ha comido la inflación. El poder adquisitivo del asalariado medio se
   ha estancado desde 2019.

4. **La labor share cayó -6.4 puntos porcentuales** en una década,
   del 67.5% al 61.1% del valor añadido. Una proporción creciente de
   la riqueza generada por las empresas se destina a beneficios y una proporción
   decreciente a retribuir a los trabajadores.

5. **Los resultados son robustos al deflactor elegido.** Las diferencias entre
   IPC y deflactor del PIB son de 1-2 pp en todos los indicadores.

![Desglose del capital IRPF](/assets/images/rentas/07_irpf_capital_desglose.png)

---

## Reproducibilidad

Los datos y scripts están disponibles en el repositorio del proyecto:

```bash
# 1. Datos fuente
# AEAT: modelo100.csv, modelo200.csv, DistribucionSalarios.xlsx
#   https://sede.agenciatributaria.gob.es/Sede/estadisticas/anuario-estadistico/
# INE: tablas 50934, 67196, 67822 vía API JSON

# 2. Ejecutar análisis y generar series deflactadas
python src/25_rentas_trabajo_capital.py

# 3. Generar gráficas
python src/26_rentas_graficas.py

# 4. Generar este informe
python src/27_rentas_informe.py
```