# CLAUDE.md — Memoteca

## Qué es

Esta carpeta es el sitio **Memoteca** — https://memoteca.github.io/. Hasta el
2026-10-16 se llamaba `statisticspeek` (nombre viejo del proyecto); en `~/claude` queda
un enlace simbólico `statisticspeek -> memoteca` para que las referencias antiguas
(p. ej. las de `../impuestos`) sigan resolviendo.

- Sitio: **Jekyll** (tema Minima) + **GitHub Pages**. Deploy automático al hacer push a `main`.
- Repo: `github.com/memoteca/memoteca.github.io.git`
- `memoteca` es una **organización de GitHub** de Jorge. Repos:
  - `memoteca.github.io` (este) — el **escaparate** que se publica
  - `memoteca/solares` — **taller** de plantas solares, en `/Users/jorge/claude/solares/`
- Contenido de Memoteca: plantas solares (Madrid A-2/A-3, Alicante) + estadística
  (vivienda, impuestos, movilidad, Japón, distribución de renta/riqueza España…),
  lacus ligustinus, etc.

## NO confundir con "Apuntes" / Fiona Hill

Son **sitios distintos**, no toques uno pensando en el otro:

| | Memoteca (aquí) | Apuntes |
|---|---|---|
| Carpeta | `/Users/jorge/claude/memoteca/` | `/Users/jorge/claude/FionaHill/` |
| Generador | Jekyll | mkdocs |
| Hosting | GitHub Pages (`memoteca.github.io`) | Cloudflare Pages (`apuntes-jorge.pages.dev`) |
| Repo | `memoteca/memoteca.github.io` | `jorgemelis/books` |
| Contenido | estadística + plantas solares | Fiona Hill, fichas de libros, notes, papers, votos, sahara, etc. |

El ensayo de **Fiona Hill vive en Apuntes (FionaHill), NO en Memoteca.**

## Modelo taller / escaparate (adoptado jul-2026)

Cada tema tiene un **taller** (repo hermano con fuentes/datos/borradores, no se
publica) y su salida publicable va al **escaparate** (este repo, Memoteca).

| Tema | Taller (fuentes) | Escaparate (aquí) |
|---|---|---|
| Plantas solares | `../solares` (`memoteca/solares`) | posts `plantas-solares-*`, `docs/solares/`, `assets/mapa_envatios_xxiv.html` |
| Estadística | `../estadistica` (`memoteca/estadistica`) | posts (vivienda, impuestos, movilidad, Japón…), `assets/images/<tema>/` |

**Regla para temas nuevos:** las **fuentes** van a un taller hermano `../<tema>`
(como `../solares`); la **publicación** aterriza aquí con estructura por tema
(`docs/<tema>/`, `assets/images/<tema>/`, posts en `_posts/`).

Este repo (escaparate) debe contener **solo lo publicable**. Lo que hay:

| ✍️ Contenido (edita) | 🔧 Maquinaria Jekyll (no tocar) |
|---|---|
| `_posts/` — artículos | `_config.yml`, `Gemfile`, `Gemfile.lock` |
| `index.md` — portada | `assets/main.scss` — estilos |
| `plantas-solares-madrid.md` | `_site/`, `.jekyll-cache/` — se regeneran |
| `docs/<tema>/` — docs de consulta | `.gitignore` |
| `assets/images/<tema>/`, `assets/*.html` | |

Con el **build clásico** de GitHub Pages, la maquinaria está obligada a vivir en
la raíz junto al contenido; no se puede esconder en subcarpetas sin migrar a
GitHub Actions. Por eso la separación real es por repos (taller vs. escaparate),
no por carpetas dentro de este repo.


---

## Desarrollo (Jekyll)

```bash
bundle exec jekyll serve   # servidor local
bundle exec jekyll build   # build sin servidor
```

Sin paso de build para desplegar: push a `main` dispara el build de GitHub Pages.
Actions: https://github.com/memoteca/memoteca.github.io/actions

### Estructura
- `_posts/` — artículos publicados (`YYYY-MM-DD-title.md`)
- `_drafts/` — borradores (no se despliegan)
- `assets/main.scss` — estilos, sobre todo formato de tablas

### Guías de contenido
- Posts en español, código/comentarios en inglés
- Tablas en Markdown o HTML con clases CSS
- `<td class="num">1.234,56</td>` para columnas numéricas alineadas a la derecha
