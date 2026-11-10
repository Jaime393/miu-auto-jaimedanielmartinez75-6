# miu-auto-jaimedanielmartinez75-6

## Epígrafe: lo que la cáscara era

El stub original, íntegro (README.md, 32 B, blob SHA `3e7f0c0f…`):

```
# miu-auto-jaimedanielmartinez75-6
```

El título no afirma nada falso: es solo el nombre. No hay nada que corregir en él.

La cáscara tenía 2 commits (autor FranBot-Evolucion, 2026-08-25): `Initial commit`
`6e18deae…` (17:30:22Z) y la cabeza `3fff0bc9…` ("polen v133 - suelo que
sostiene a otros", 17:42:19Z). El segundo commit añadió `polen_v133.html`
(844 B, SHA `47717d47…`), el mismo archivo byte a byte que en las cáscaras
#6–8: una página con un fragmento de worker de JSON fijo y una promesa de
"Endpoints vivos: 24 Pages + 40 CF + R2 100GB" sin lista que la respalde.
Esa promesa no se verifica aquí: es una afirmación de la plantilla, no
un hecho medido (ver EVOLUCION.md).

## El hecho: el volcado es casi todo el repo

En el repo `Jaime393/miu-memoria-codex` (cabeza `e284ad31`, 24 commits en
un solo día, 2026-08-29 01:34Z → 11:36Z), el directorio
`volcado_memoria/lote2/` tiene **17 archivos que suman 94.368.612 B**:
14 volcados de texto (94.355.238 B) más `LEEME_ABSORCION.md`,
`indice_absorcion.json` y `memories_catalogo.txt`.

El repo entero pesa 95.781.877 B en 202 archivos (minería ola 6,
`~/workspace/mineria/miu-memoria-codex/INVENTARIO.md`). El volcado es
el **98,5 %** del repo. Dicho de otro modo: el repo no es un proyecto
con un volcado dentro; es un volcado con un proyecto alrededor.

Dentro del volcado, lo que dicen sus dos índices pequeños (leídos
enteros; los 14 volcados no se leyeron por tamaño, solo nombre y tamaño):

- **19.595 mensajes en 74 conversaciones.** La tabla de
  `LEEME_ABSORCION.md` suma exactamente 19.595 (4.516 + 1.201 + 1.139 +
  1.072 + 1.946 + 2.445 + 3.200 + 1.746 + 976 + 1.354) y 74
  conversaciones (17 + 4 + 6 + 14 + 3 + 18 + 9 + 2 + 1).
- **38.331 expansiones.** `memories_catalogo.txt` (161 B, 3 líneas):
  38.313× "Aprender del historial de conversaciones" y 18× "Nuevo
  recurso descubierto"; rango 2026-07-23T14:55:45 → 2026-08-06T23:27:49.
- **Los dos índices no cuadran entre sí, y cuadran al céntimo cuando
  se cuenta el duplicado.** `indice_absorcion.json` suma 19.642
  mensajes en sus `total_messages`, 47 más que la tabla LEEME. La
  diferencia se reconcilia exactamente: 19.595 + 1.007 (`chat.json`,
  duplicado en el índice de `conversations (4).json`) − 976
  (`parte1grande`, que el índice marca con 0 mensajes tras la
  reparación) + 16 (diferencias de 1–5 mensajes en cinco archivos) =
  19.642. La reconciliación es aritmética; la causa de las diferencias
  de 1–5 no se sabe (ver CARENCIAS.md).

## Cómo se verificó

Listado en vivo del directorio `volcado_memoria/lote2/` por la API de
GitHub el 2026-11-09 (17 archivos, suma por programa: 94.368.612 B),
lectura entera de `LEEME_ABSORCION.md`, `indice_absorcion.json` y
`memories_catalogo.txt`, y suma de la tabla LEEME y de los
`total_messages` del índice. El contenido de los 14 volcados no se
leyó: esta semilla solo afirma conteos y tamaños, nunca contenido.

## Reproducir

```sh
python3 volcado_94mb_repro.py
python3 test_volcado_94mb.py
```

El repro no toca la red: suma las tablas literales copiadas de la
lectura en vivo e imprime `TODO COINCIDE` si todo cuadra.

## Fuentes

- Jaime393/miu-memoria-codex, `volcado_memoria/lote2/` (listado en vivo,
  2026-11-09): 17 archivos, 94.368.612 B.
- Jaime393/miu-memoria-codex, `volcado_memoria/lote2/LEEME_ABSORCION.md`
  (1.113 B, leído entero, 2026-11-09): tabla de 10 fuentes, total
  "~74 conversaciones / ~19.595 mensajes / ~95 MB".
- Jaime393/miu-memoria-codex, `volcado_memoria/lote2/indice_absorcion.json`
  (12.100 B, leído entero, 2026-11-09): 16 entradas, `total_messages`
  suman 19.642.
- Jaime393/miu-memoria-codex, `volcado_memoria/lote2/memories_catalogo.txt`
  (161 B, leído entero, 2026-11-09): 38.331 expansiones.
- Minería ola 6, `~/workspace/mineria/miu-memoria-codex/INVENTARIO.md` y
  `CONTENIDO.md` (2026-11-09): repo 202 archivos, 95.781.877 B; lote2
  94.368.612 B, 17 archivos.
- Jaime393/miu-auto-jaimedanielmartinez75-6 (cáscara): cabeza
  `3fff0bc9…`, README 32 B, `polen_v133.html` SHA `47717d47…`
  (lectura en vivo, 2026-11-09).
