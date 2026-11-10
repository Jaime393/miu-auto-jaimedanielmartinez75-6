# CARENCIAS — lo que esta semilla no sabe

Fecha de búsqueda: 2026-11-09. Todo lo de abajo es NO SÉ con su
lugar de búsqueda: huecos locales, no huecos del ecosistema.

1. **Qué hay dentro de los 14 volcados de texto.** No se leyeron
   enteros por tamaño (94.355.238 B en total). Solo se leyeron nombre,
   tamaño, `LEEME_ABSORCION.md`, `indice_absorcion.json` y
   `memories_catalogo.txt`. Lo que afirman los volcados más allá de
   sus índices no se verificó aquí. Buscado: listado en vivo de
   `volcado_memoria/lote2/` y lectura de los 3 archivos pequeños,
   2026-11-09.

2. **Si la redacción de secretos que LEEME afirma es completa.**
   `LEEME_ABSORCION.md` dice que se redactaron las claves de Groq,
   los tokens de Telegram, las claves de Cloudflare y las direcciones
   0x. No se verificó por lectura de los volcados (ver punto 1), así
   que la redacción es una afirmación del archivo, no un hecho
   comprobado por esta semilla. Buscado: el texto de LEEME, leído
   entero, 2026-11-09.

3. **Por qué la minería sumó 94.354.339 B para los 14 volcados.**
   La suma en vivo de los mismos 14 archivos da 94.355.238 B: 899 B
   más. El total de lote2 (94.368.612 B) coincide exacto entre la
   minería y la lectura en vivo, y los tamaños por archivo de la tabla
   de la minería coinciden con el listado en vivo. La diferencia está
   solo en el subtotal escrito. NO SÉ si es un error de suma de la
   minería o una agrupación distinta de archivos. Buscado: listado en
   vivo de lote2/ y tabla de `INVENTARIO.md` de la minería ola 6,
   2026-11-09.

4. **Por qué el índice y la tabla LEEME difieren en 1–5 mensajes en
   cinco archivos.** `conversations.json` 4.520 vs 4.516, oracle 1.203
   vs 1.201, `parte1v2` 1.077 vs 1.072, `memoria.json` 2.446 vs 2.445,
   `conversations0/3/4` 3.203 vs 3.200, `proyecto_alma_completo`
   1.355 vs 1.354. La reconciliación total es exacta (19.642 =
   19.595 + 1.007 − 976 + 16), pero la causa de cada diferencia
   pequeña no está escrita en ningún archivo leído. Buscado: tabla
   LEEME y `total_messages` de `indice_absorcion.json`, 2026-11-09.

5. **Si las 38.331 expansiones corresponden a conversaciones reales
   o a generaciones automáticas.** El índice las lista como 38.331
   filas de tipo "expansion" con 0 mensajes cada una, y el catálogo
   las divide en 38.313× "Aprender del historial de conversaciones"
   y 18× "Nuevo recurso descubierto". Qué es una expansión —un
   registro, un resumen, una ejecución— no lo dice ningún archivo
   leído. Buscado: `memories_catalogo.txt` e `indice_absorcion.json`,
   2026-11-09.

6. **Si los 24 commits del 2026-08-29 son toda la historia del repo
   `miu-memoria-codex` o si hubo historia anterior.** El commit más
   viejo devuelto por la API es `cf1b0412…` ("Memoria absorbida
   Codex 2026-08-29 (redactada)", 01:34:16Z) y la cabeza es
   `e284ad31…` (11:36:02Z), todo en un solo día. No se buscó fuera
   de la API de commits. Buscado: `list_commits` del repo,
   2026-11-09.
