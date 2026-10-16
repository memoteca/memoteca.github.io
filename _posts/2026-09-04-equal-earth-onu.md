---
layout: post
title: "La ONU adopta Equal Earth, y la web donde estaban los mapas se cae"
date: 2026-09-04
---

El 4 de septiembre de 2026 la Asamblea General de Naciones Unidas votó adoptar la
proyección Equal Earth en sustitución gradual de la de Mercator: 164 votos a
favor, 6 abstenciones y el voto en contra de Estados Unidos. España y la mayoría
de los Estados de la Unión Europea votaron a favor.

La resolución la impulsó Togo y no es vinculante: ni obliga a usar la nueva
proyección en exclusiva ni prohíbe la anterior. Robert Dussey, ministro de
Exteriores togolés, dijo antes de la votación que «esta discusión no es política,
sino científica, porque existen pruebas científicas y todos debemos aceptar la
realidad». Francia anunció que empezará a usar «representaciones cartográficas
adaptadas a usos específicos, más fieles a las superficies reales». La Unión
Africana había aprobado una resolución en el mismo sentido a principios de año.

---

## Qué es Equal Earth

Una proyección publicada en 2018 por Bojan Šavrič, Tom Patterson y Bernhard Jenny.
Es equivalente: conserva las proporciones de superficie. África aparece catorce
veces mayor que Groenlandia, que es la proporción real. La de Mercator, diseñada
en el siglo XVI para navegar, agranda lo que está cerca de los polos y encoge lo
que está cerca del ecuador.

## Y ese mismo día se cayó la web

`equal-earth.com` es el sitio desde el que Patterson repartía los mapas gratis.
Comparte cuenta de hosting con `shadedrelief.com`, su otro sitio, y desde
principios de septiembre los dos devuelven la página de cuenta suspendida de
cPanel. No es una caída por saturación, que daría un 503 o un tiempo de espera
agotado: es el panel de hosting el que ha cortado la cuenta, que es lo que pasa
cuando una cuenta compartida se sale de su cuota de transferencia.

Los mapas están **en dominio público**. Los términos de uso del propio sitio
decían:

> The Equal Earth Wall Maps are in the public domain. You may use the maps any way
> you like, including modifying the content, reproducing it on any type of media,
> and selling it for profit. Consider them as yours.

Así que se pueden copiar y redistribuir sin pedir permiso a nadie. Todo lo que
había sigue en el Internet Archive, que capturó también los ficheros grandes: 257
mapas, 6,6 GB, con capturas de hasta julio de 2026.

## Los mapas

Los originales miden 140 × 74 cm impresos a 350 ppp — 19250 × 10150 píxeles los
políticos, 19268 × 10630 los físicos. Aquí van reducidos; debajo de cada uno, el
enlace al original.

### Político, en español

![Mapa político Equal Earth en español, centrado en 11°E](/assets/images/equal-earth/equal-earth-politico-es-1600.jpg)

Centrado en 11°E, África y Europa. Más de 2.600 topónimos.
[Original, 24 MiB](https://1drv.ms/i/c/2a8aab1ffe1714b0/IQAs8NYKdufuR6TrZ31bCRI_AXD8zwF1AsMifx76hIGg4kI)
· [vectorial de Illustrator, 60 MiB](https://1drv.ms/u/c/2a8aab1ffe1714b0/IQDSsMROxplPTIUyCN_Cn2JbAUNBvijTQJq0i2w29GocwyU)

### Físico con relieve

![Mapa físico Equal Earth con relieve sombreado](/assets/images/equal-earth/equal-earth-fisico-1600.jpg)

[Original, 30 MiB](https://1drv.ms/i/c/2a8aab1ffe1714b0/IQDQO20v_cQQSrV86uBbSH98AdtRYzu3bra3PdfKSg4WRFg)
· [centrado en 11°E, 30 MiB](https://1drv.ms/i/c/2a8aab1ffe1714b0/IQA3bQF1HdnBQYy54BaaBe_LAYeZvhQBY_1LMWb8p8nL2Hk)
· [vectorial, 196 MiB](https://1drv.ms/u/c/2a8aab1ffe1714b0/IQBDHaP6dcp4S6FujI6mmYETAaQb9U78-WxMfcwfrkCSpzY)

### Físico sin rótulos

![Mapa físico Equal Earth sin rótulos](/assets/images/equal-earth/equal-earth-fisico-sin-rotulos-1600.jpg)

Base limpia, para rotular encima.
[Original, 21 MiB](https://1drv.ms/i/c/2a8aab1ffe1714b0/IQDjh7uUY6YZRaDq-19rBAzSAaEOhZ0jb-f0kZMfMuIFwMs)
· [relieve sombreado en gris, 36 MiB](https://1drv.ms/u/c/2a8aab1ffe1714b0/IQDJIXZyGjjxS564QN49lfmBAbYGLWQNg5dVevrazxgDyCQ)

## Recuperar cualquiera del Archive

El sufijo `if_` sirve el binario sin la barra del Wayback:

```
aria2c -c -x1 -s1 --max-connection-per-server=1 -o mapa.jpg \
  "https://web.archive.org/web/20250717131508if_/https://www.equal-earth.com/physical/Equal-Earth-Physical-Map-Raster.jpg"
```

El listado completo de lo capturado está en el índice CDX del Archive:
`web.archive.org/cdx/search/cdx?url=equal-earth.com&matchType=domain`.

## Generar uno propio

Sin depender de la web de nadie, partiendo del ráster Natural Earth II con relieve
sombreado (21600 × 10800, `NE2_HR_LC_SR_W`, en
[naturalearthdata.com](https://www.naturalearthdata.com/)):

```bash
gdalwarp -t_srs EPSG:8857 -r lanczos -ts 20000 0 \
         NE2_HR_LC_SR_W.tif ne2_eqearth.tif
```

`EPSG:8857` es WGS 84 / Equal Earth Greenwich. Para centrar en el Pacífico,
`-t_srs "+proj=eqearth +lon_0=-150 +datum=WGS84"`. Necesita PROJ ≥ 6 y GDAL ≥ 3.
Lo que no se reconstruye así es la rotulación y la paleta de Patterson.

---

Fuente de la votación: [elDiario.es, 4 de septiembre de
2026](https://www.eldiario.es/internacional/asamblea-general-onu-vota-favor-nuevo-mapamundi-refleja-tamano-real-africa_1_13487401.html).
