---
layout: default
title: "Plantas solares en el este de Madrid — Cuña A-2 / A-3"
---

# Plantas solares en el este de Madrid — Cuña A-2 / A-3

Seguimiento de macroplantas solares fotovoltaicas entre las autovías
A-2 (Zaragoza) y A-3 (Valencia), desde el área metropolitana de Madrid
hasta el límite con Castilla-La Mancha.

Ultima actualizacion: 26 de marzo de 2026.

---

## Mapa interactivo

- [Mapa Envatios XXIV + PFot 195/172](../data/mapa_envatios_xxiv.html)
  — Parcelas Envatios (Smartenergy), perímetros PFot (IGNIS),
  carreteras A-2/A-3, límite de la Comunidad de Madrid
- [Mapa PFot-195 + 172 completo](../data/mapa_pfot195_172_completo.html)
  — 7 plantas IGNIS con líneas AT y parcelas

---

## Documentacion

### Inventario y datos

| # | Documento | Contenido |
|---|---|---|
| 01 | [Inventario de proyectos solares](01_inventario_proyectos_solares.md) | PFot-195, PFot-172, Envatios XXIV, Pioz RT1/RD2, otros. Potencias, superficies, promotores |
| 03 | [Impacto por municipio](03_impacto_por_municipio.md) | Desglose detallado municipio a municipio (zona Henares) |
| 04 | [Superficie afectada (CSV)](04_superficie_afectada.csv) | Datos tabulados de superficie por municipio y proyecto |
| 06 | [Municipios zona A-2/A-3](06_municipios_zona_a2_a3.md) | **34 municipios** de la cuña completa — superficie municipal, superficie afectada, % afectado, proyectos. Incluye los ~30 proyectos nuevos identificados en marzo 2026 |

### Marco legal y fuentes

| # | Documento | Contenido |
|---|---|---|
| 02 | [Marco legal: expropiaciones](02_marco_legal_expropiaciones.md) | Competencias Estado/CCAA/municipio, base legal DUP, derechos de los afectados |
| 05 | [Referencias BOE](05_referencias_boe.md) | DIAs, autorizaciones, expropiaciones, recursos — con enlaces directos al BOE |
| 07 | [Fuentes oficiales](07_fuentes_oficiales.md) | Guia de fuentes: BOE, BOCM, MITECO, Catastro INSPIRE, IGN, prensa local. Como buscar nuevos proyectos |

---

## Zona de estudio

**33 municipios** entre la A-2 y la A-3, desde el area metropolitana
hasta el limite con Castilla-La Mancha (provincias de Guadalajara,
Cuenca y Toledo).

### Cifras clave

| Concepto | Valor |
|---|---:|
| Municipios con plantas autorizadas | 22 |
| Municipios sin proyectos conocidos | 10 |
| Superficie total de la zona | ~132.100 ha |
| Superficie afectada estimada | ~4.680 ha (~3,5%) |
| Potencia total estimada | **~2.600-2.800 MW** |

### Principales promotores

| Promotor | Proyectos | MW aprox |
|---|---|---:|
| **IGNIS / TotalEnergies** | PFot-195, 172, 187-191, Morena, Rececho, Postor, Driza, Mastil, Armada, Maladeta, Popa, Collarada, Recova, Rabiza, Regata, Mauricio | ~1.900 |
| **Smartenergy (Envatios)** | Envatios XXIV (3 fases), Los Pradillos (linea evacuacion) | ~600 |
| **Green Capital Power** | Galatea I, Galatea II | ~150 |
| **Blue Viking** | Pioz RT1, Pioz RD2 | ~148 |
| **Otros** | Arganda Solar II, La Carnerada, Tagus 2, Morata I... | ~350 |

### Municipios mas afectados

| Municipio | % termino | MW |
|---|---:|---:|
| Santorcaz | ~39% | ~330 |
| Anchuelo | ~19% | ~328 |
| Valdilecha | ~14% | ~250 |
| Torres de la Alameda | 8,4% | ~71 (Envatios) + ~582 (IGNIS) |
| Campo Real | ~6,5% | ~290 |
| Colmenar de Oreja | ~3,6% | ~310 |

---

## Datos GIS

| Capa | Formato | Fichero |
|---|---|---|
| PFot-195 plantas | Shapefile | `data/pfot195_gis/.../Pfot_195_PSFV.shp` |
| PFot-172 plantas | Shapefile | `data/pfot172/capas_gis/PFot_172_PFV.shp` |
| Parcelas clasificadas | GeoPackage | `data/catastro_clasificado.gpkg` |
| Servidumbres | GeoPackage | `data/servidumbres.gpkg` |
| Envatios XXIV parcelas | WFS en tiempo real | Catastro INSPIRE (refs del BOE) |
| Limites CM (municipios fronterizos) | GeoJSON | `data/cm_boundary_east.geojson` |
| Carreteras A-2, A-3 | GeoJSON | `data/a2_highway.geojson`, `data/a3_highway.geojson` |
| Limites provinciales GU/CU/TO | GeoJSON | `data/prov_*.geojson` |

---

## Articulos publicados

- [Plantas solares en el Corredor del Henares](https://memoteca.github.io/2026/03/25/plantas-solares-corredor-henares.html) — Madrid este
- [Plantas solares en Alicante y el Maigmo](https://memoteca.github.io/2026/03/25/plantas-solares-alicante-maigmo.html) — Alicante

---

## Scripts

| Script | Funcion |
|---|---|
| `build_envatios_map.py` | Genera el mapa interactivo principal (Folium) |
| `fetch_zone_boundaries.py` | Descarga limites de carreteras, municipios y provincias de Overpass/OSM |
| `data/query_catastro_usos.py` | Consulta usos del suelo en Catastro INSPIRE |
