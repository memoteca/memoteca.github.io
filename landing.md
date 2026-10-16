# Portada de Memoteca

Cada línea es un bloque de la portada (`index.md`), en el orden en que aparece.
`[x]` lo publica, `[ ]` lo deja fuera. Reordenar las líneas reordena la portada.
El texto de cada bloque está en `landing/<nombre>.md`. La sangría es solo visual:
los bloques sin sangrar son los encabezados de tema (`##`), los de un nivel son
las series (`###`) y los de dos niveles las entradas (`####`). Mover una entrada
bajo otra serie la cambia de serie; apagar una serie no apaga sus entradas.

Tras editar, regenerar la portada y subir ambos ficheros:

    python3 build_landing.py && git add landing.md index.md && git commit && git push

- [x] reclus — Reclus
  - [x] reclus_textos — Élisée Reclus, Nouvelle géographie universelle
- [x] lacus_ligustinus — El Lacus Ligustinus, el bajo Guadalquivir en época romana
- [x] equal_earth — La ONU adopta la proyección Equal Earth
- [x] plantas_solares — Plantas solares
  - [x] madrid — Madrid — cuña A-2 / A-3 (este y sureste)
    - [x] madrid_docs — Documentación: cuña A-2 / A-3
    - [x] madrid_henares — Plantas solares en el este de Madrid
  - [x] alicante — Alicante — Maigmó, Ibi, Castalla y ciudad
    - [x] alicante_maigmo — Plantas solares en Alicante: Maigmó, Ibi, Castalla y ciudad
- [ ] estadistica — Estadística
  - [ ] movilidad — Movilidad intergeneracional
    - [ ] movilidad_absoluta — Movilidad absoluta de renta en España, 1973–1996
    - [ ] edad_optima — La edad de medición de la movilidad
  - [ ] japon — Japón
    - [ ] japon_renta — Distribución de la renta en Japón, 1999–2019
    - [ ] japon_test — Igualdad y estancamiento en Japón
    - [ ] japon_vs_espana — Movilidad absoluta en Japón y en España
  - [ ] impuestos — Impuestos
    - [ ] impuestos_progresivos — Carga fiscal total del asalariado y progresividad
    - [ ] transferencias — Transferencias del Estado y carga fiscal neta
    - [ ] riqueza — Distribución de la riqueza en España y su tributación
    - [ ] eff — La Encuesta Financiera de las Familias: qué mide y con qué fiabilidad
    - [ ] vivienda_propiedad — Vivienda en España: propiedad, alquiler y viviendas vacías
    - [ ] rentas — Rentas del trabajo vs rentas del capital en España (2009–2024)
    - [ ] corporativa — Tributación corporativa en la UE
    - [ ] comparativa_europea — Comparativa europea de carga fiscal sobre el trabajo
  - [ ] otros — Otros análisis
    - [ ] vivienda_ecv — La vivienda en la ECV del INE
