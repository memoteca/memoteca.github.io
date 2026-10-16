# Portada de Memoteca

Cada línea es un bloque de la portada (`index.md`), en el orden en que aparece.
`[x]` lo publica, `[ ]` lo deja fuera. Reordenar las líneas reordena la portada.
El texto de cada bloque está en `landing/<nombre>.md`. La sangría es solo visual:
los bloques sin sangrar son los encabezados de tema (`##`), los de un nivel son
las series (`###`) y los de dos niveles las entradas (`####`). Mover una entrada
bajo otra serie la cambia de serie; apagar una serie no apaga sus entradas.

Tras editar, regenerar la portada y subir ambos ficheros:

    python3 build_landing.py && git add landing.md index.md && git commit && git push

- [x] Reclus
- [x] lacus_ligustinus — El Lacus Ligustinus (no estaba en la portada)
- [x] equal_earth — La ONU adopta Equal Earth (no estaba en la portada)
- [x] plantas_solares — Plantas solares
  - [x] madrid — Madrid — cuña A-2 / A-3 (este y sureste)
    - [x] madrid_docs — Documentacion completa: cuña A-2 / A-3
    - [x] madrid_henares — Plantas solares en el este de Madrid: qué se sabe
  - [x] alicante — Alicante — Maigmó, Ibi, Castalla y ciudad
    - [x] alicante_maigmo — Plantas solares en Alicante: Maigmó, Ibi, Castalla y ciudad
- [ ] estadistica — Estadística
  - [ ] movilidad — Movilidad intergeneracional
    - [ ] movilidad_absoluta — ¿Se desvanece el sueño español? Movilidad absoluta de renta, 1973–1996
    - [ ] edad_optima — ¿A qué edad medir la movilidad? Determinación de la edad óptima de medición
  - [ ] japon — Japón
    - [ ] japon_renta — Las tres décadas perdidas en números: distribución de renta en Japón, 1999–2019
    - [ ] japon_test — El test japonés: ¿protege la igualdad contra el estancamiento?
    - [ ] japon_vs_espana — Dos caminos al mismo resultado: Japón vs España en movilidad absoluta
  - [ ] impuestos — Impuestos
    - [ ] impuestos_progresivos — Carga fiscal total del asalariado: un análisis de progresividad
    - [ ] transferencias — Transferencias del Estado y carga fiscal neta
    - [ ] riqueza — Distribución de la riqueza en España: quién posee qué y cómo tributa
    - [ ] eff — La Encuesta Financiera de las Familias: qué mide, qué no, y cómo de bien
    - [ ] vivienda_propiedad — Vivienda en España: propiedad, alquiler y el mito de las viviendas vacías
    - [ ] rentas — Rentas del trabajo vs rentas del capital en España (2009–2024)
    - [ ] corporativa — Tributación corporativa en la UE: la carrera a la baja y la paradoja recaudatoria
    - [ ] comparativa_europea — Comparativa europea de carga fiscal sobre el trabajo
  - [ ] otros — Otros análisis
    - [ ] vivienda_ecv — La vivienda en la ECV del INE
