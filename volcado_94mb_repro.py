#!/usr/bin/env python3
"""volcado_94mb_repro.py — reproduce por programa el hecho de esta semilla.

HECHO: en el repo Jaime393/miu-memoria-codex, el directorio
volcado_memoria/lote2/ tiene 17 archivos que suman 94.368.612 B:
14 volcados de texto (94.355.238 B), más LEEME_ABSORCION.md,
indice_absorcion.json y memories_catalogo.txt. La tabla de LEEME suma
exactamente 19.595 mensajes en 74 conversaciones, y el catálogo dice
38.331 expansiones (38.313 + 18).

Todas las cifras de abajo son literales copiados de la lectura en vivo
por la API de GitHub el 2026-11-09 (listado de lote2/, LEEME_ABSORCION.md,
indice_absorcion.json y memories_catalogo.txt). El script no toca la red
ni lee el contenido de los volcados: solo suma los números ya medidos.

Uso: python3 volcado_94mb_repro.py
"""

# Listado en vivo de volcado_memoria/lote2/ (nombre, bytes), 2026-11-09.
LOTE2 = [
    ("LEEME_ABSORCION.md", 1113),
    ("conversations.txt", 17986876),
    ("conversations0.txt", 4314746),
    ("conversations3.txt", 7179732),
    ("conversations4.txt", 4891081),
    ("conversations_oracle.txt", 6788072),
    ("conversations_pryect.txt", 5620679),
    ("indice_absorcion.json", 12100),
    ("memoria.txt", 14977692),
    ("memories_catalogo.txt", 161),
    ("parte1grande_reparado.txt", 4851811),
    ("parte1v2.txt", 6436767),
    ("parte2.txt", 6239476),
    ("parte2v2.txt", 4592871),
    ("parte3.txt", 3893501),
    ("parte4.txt", 2207424),
    ("proyecto_alma_completo.txt", 4374510),
]

# Los 3 archivos que NO son volcados de texto.
NO_VOLCADOS = {"LEEME_ABSORCION.md", "indice_absorcion.json",
               "memories_catalogo.txt"}

# Tabla de LEEME_ABSORCION.md (fuente, conversaciones, mensajes).
LEEME = [
    ("conversations.json (ago 2026)", 17, 4516),
    ("conversaciones_oracle (2)", 4, 1201),
    ("conversations_pryect", 6, 1139),
    ("parte1v2", 14, 1072),
    ("parte2 / parte2v2", 3, 1946),
    ("memoria.json", 18, 2445),
    ("conversations0 / 3 / 4", 9, 3200),
    ("parte3 / parte4", 2, 1746),
    ("parte1grande (reparado)", 0, 976),
    ("proyecto_alma_completo", 1, 1354),
]

# memories_catalogo.txt: (Aprender del historial, Nuevo recurso).
CATALOGO = (38313, 18)

# total_messages por entrada de indice_absorcion.json (16 entradas).
INDICE_TOTALES = [
    ("conversations0.json", 871),
    ("conversations.json", 4520),
    ("parte2.json", 1040),
    ("memoria.json", 2446),
    ("conversations (4).json", 1007),
    ("conversations_pryect.json", 1139),
    ("conversations_oracle (2).json", 1203),
    ("chat.json", 1007),
    ("parte1 (2).json", 1077),
    ("conversations (3).json", 1325),
    ("proyecto_alma_completo.json", 1355),
    ("parte2 (2).json", 906),
    ("parte4.json", 873),
    ("parte3.json", 873),
    ("memories.json", 0),
    ("parte1.json", 0),
]

# Total del repo según la minería ola 6 (INVENTARIO.md): no re-medido aquí.
REPO_TOTAL_B = 95781877

# Subtotal de los 14 volcados que escribió la minería (INVENTARIO.md).
MINERIA_VOLCADOS_B = 94354339


def suma_lote2():
    return sum(b for _, b in LOTE2)


def suma_volcados():
    return sum(b for n, b in LOTE2 if n not in NO_VOLCADOS)


def suma_leeme_mensajes():
    return sum(m for _, _, m in LEEME)


def suma_leeme_conversaciones():
    return sum(c for _, c, _ in LEEME)


def suma_catalogo():
    return CATALOGO[0] + CATALOGO[1]


def suma_indice():
    return sum(m for _, m in INDICE_TOTALES)


def reconcilia_indice_leeme():
    """19.642 (índice) = 19.595 (LEEME) + 1.007 (chat.json duplicado
    en el índice) - 976 (parte1grande, el índice marca 0) + 16
    (diferencias de 1-5 mensajes en cinco archivos)."""
    diffs = 4 + 2 + 5 + 1 + 3 + 1  # conversations, oracle, parte1v2,
    # memoria, conv0/3/4, proyecto_alma
    return suma_leeme_mensajes() + 1007 - 976 + diffs


def main():
    ok = True

    def check(nombre, medido, esperado):
        nonlocal ok
        marca = "OK  " if medido == esperado else "FALLO"
        if medido != esperado:
            ok = False
        print(f"{marca} {nombre}: medido {medido}, esperado {esperado}")

    check("archivos en lote2/", len(LOTE2), 17)
    check("bytes en lote2/", suma_lote2(), 94368612)
    check("volcados de texto", len(LOTE2) - len(NO_VOLCADOS), 14)
    check("bytes de los 14 volcados", suma_volcados(), 94355238)
    check("mensajes (tabla LEEME)", suma_leeme_mensajes(), 19595)
    check("conversaciones (tabla LEEME)", suma_leeme_conversaciones(), 74)
    check("expansiones (catálogo)", suma_catalogo(), 38331)
    check("total_messages (índice)", suma_indice(), 19642)
    check("reconciliación índice-LEEME", reconcilia_indice_leeme(), 19642)

    # La minería escribió 94.354.339 B para los 14 volcados; la suma en
    # vivo da 94.355.238 B. Diferencia medida, no resuelta: 899 B.
    diff = suma_volcados() - MINERIA_VOLCADOS_B
    print(f"NOTA subtotal minería de los 14 volcados: {MINERIA_VOLCADOS_B} B")
    print(f"NOTA suma en vivo de los 14 volcados: {suma_volcados()} B")
    print(f"NOTA diferencia: {diff} B (sin explicar; ver CARENCIAS.md)")
    if diff != 899:
        ok = False
        print("FALLO la diferencia no es 899 B")

    # El volcado es el 98,5 % del repo (total del repo, cifra de minería).
    share = suma_lote2() / REPO_TOTAL_B
    print(f"NOTA lote2 es el {share:.4f} del repo ({REPO_TOTAL_B} B, minería)")
    if not (0.985 <= share <= 0.986):
        ok = False
        print("FALLO la proporción no está en 98,5 %")

    print("TODO COINCIDE" if ok else "HAY FALLOS")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
