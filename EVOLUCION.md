# EVOLUCION — de cáscara a semilla

## Lo que era la cáscara

`miu-auto-jaimedanielmartinez75-6`, cáscara #16 del censo miu-auto
(`~/workspace/mineria/CENSO_MIU_AUTO_2026-11-09.md`): 2 commits de
FranBot-Evolucion el 2026-08-25. `Initial commit` `6e18deae…`
(17:30:22Z) con un README de título solo (32 B); cabeza `3fff0bc9…`
("polen v133 - suelo que sostiene a otros", 17:42:19Z) que añadió
`polen_v133.html` (844 B, SHA `47717d47…`).

El archivo `polen_v133.html` es byte a byte el mismo que en las
cáscaras #6–8 (mismo SHA). Su contenido: una página con un fragmento
de worker que devuelve un JSON fijo y la afirmación "Endpoints vivos:
24 Pages + 40 CF + R2 100GB" con un enlace a `miu-mesh/index.json`.
Esa afirmación no se verifica aquí: no hay lista de 24 páginas ni de
40 workers que la respalde en la cáscara, y el enlace apunta fuera del
repo. Queda como afirmación de la plantilla, no como hecho medido.
El stub (el título) no afirma nada falso, así que no hay corrección
que hacerle: se conserva íntegro como epígrafe en el README.

## Lo que añade la semilla

Un hecho medido del ecosistema, verificado en vivo el 2026-11-09 por
la API de GitHub (solo lectura) y por programa:

- El listado de `volcado_memoria/lote2/` en
  `Jaime393/miu-memoria-codex`: 17 archivos, 94.368.612 B.
- La suma de la tabla de `LEEME_ABSORCION.md`: 19.595 mensajes, 74
  conversaciones.
- El catálogo: 38.331 expansiones (38.313 + 18).
- La reconciliación exacta entre los dos índices (19.642 = 19.595 +
  1.007 − 976 + 16).
- La discrepancia de 899 B entre la suma en vivo de los 14 volcados
  (94.355.238 B) y el subtotal que escribió la minería ola 6
  (94.354.339 B), registrada como diferencia medida sin explicar.

## Archivos de esta semilla

- `README.md`: el hecho, con el stub como epígrafe y las fuentes.
- `volcado_94mb_repro.py`: reproduce las sumas sin tocar la red.
- `test_volcado_94mb.py`: 10 tests (8 de sumas, 2 de limpieza).
- `HUESO_VOLCADO_94MB.md`: el hueso.
- `EVOLUCION.md`: este archivo.
- `CARENCIAS.md`: 6 huecos con dónde se buscó y fecha.
