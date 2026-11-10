#!/usr/bin/env python3
"""Tests de volcado_94mb_repro.py.

Solo stdlib. No toca la red ni lee los volcados: comprueba las sumas
sobre las tablas literales del repro y que esta semilla no contenga
literales prohibidos ni valores de claves.
"""

import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import volcado_94mb_repro as R


class TestSumas(unittest.TestCase):
    def test_lote2(self):
        self.assertEqual(len(R.LOTE2), 17)
        self.assertEqual(R.suma_lote2(), 94368612)

    def test_volcados(self):
        self.assertEqual(len(R.LOTE2) - len(R.NO_VOLCADOS), 14)
        self.assertEqual(R.suma_volcados(), 94355238)

    def test_leeme(self):
        self.assertEqual(R.suma_leeme_mensajes(), 19595)
        self.assertEqual(R.suma_leeme_conversaciones(), 74)

    def test_catalogo(self):
        self.assertEqual(R.CATALOGO, (38313, 18))
        self.assertEqual(R.suma_catalogo(), 38331)

    def test_indice_y_reconciliacion(self):
        self.assertEqual(R.suma_indice(), 19642)
        self.assertEqual(R.reconcilia_indice_leeme(), 19642)

    def test_diferencia_899(self):
        # La minería escribió 94.354.339 B; la suma en vivo es 899 B más.
        self.assertEqual(R.suma_volcados() - R.MINERIA_VOLCADOS_B, 899)

    def test_proporcion_repo(self):
        share = R.suma_lote2() / R.REPO_TOTAL_B
        self.assertGreaterEqual(share, 0.985)
        self.assertLessEqual(share, 0.986)

    def test_main_todo_coincide(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            codigo = R.main()
        self.assertEqual(codigo, 0)
        self.assertIn("TODO COINCIDE", buf.getvalue())


class TestLimpieza(unittest.TestCase):
    """Ningún archivo de la semilla trae literales prohibidos ni
    valores de claves: solo conteos, tamaños y nombres de archivo."""

    def test_sin_literales_prohibidos(self):
        base = os.path.dirname(os.path.abspath(__file__))
        propio = os.path.basename(__file__)
        for nombre in sorted(os.listdir(base)):
            if nombre == propio:
                continue  # este archivo nombra los literales al comprobarlos
            if nombre.endswith((".py", ".md")):
                with open(os.path.join(base, nombre),
                          encoding="utf-8") as fh:
                    texto = fh.read()
                self.assertNotIn("16/16", texto, nombre)
                self.assertNotIn("validado", texto, nombre)
                self.assertNotIn("validada", texto, nombre)

    def test_sin_prefijos_de_clave(self):
        base = os.path.dirname(os.path.abspath(__file__))
        propio = os.path.basename(__file__)
        for nombre in sorted(os.listdir(base)):
            if nombre == propio:
                continue  # este archivo nombra los prefijos al comprobarlos
            if nombre.endswith((".py", ".md")):
                with open(os.path.join(base, nombre),
                          encoding="utf-8") as fh:
                    texto = fh.read()
                for prefijo in ("gsk_", "cfk_", "cfut_", "hf_"):
                    self.assertNotIn(prefijo, texto, nombre)


if __name__ == "__main__":
    unittest.main(verbosity=2)
