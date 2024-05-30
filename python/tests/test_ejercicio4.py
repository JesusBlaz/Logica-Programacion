import unittest
from logica_programacion.ejercicio4 import invertir_texto


class TestInvertirTexto(unittest.TestCase):
    def test_invertir_texto_1(self):
        texto = 'Hola mundo!'
        texto_invertido = '!odnum aloH'
        self.assertEqual(invertir_texto(texto), texto_invertido)

    def test_invertir_texto_2(self):
        texto = 'Programando con Python y Typescript'
        texto_invertido = 'tpircsepyT y nohtyP noc odnamargorP'
        self.assertEqual(invertir_texto(texto), texto_invertido)


if __name__ == '__main__':
    unittest.main()
