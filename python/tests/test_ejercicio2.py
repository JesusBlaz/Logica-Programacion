import unittest
from logica_programacion.ejercicio2 import es_palindromo


class TestPalindromo(unittest.TestCase):
    def test_es_palindromo_ana(self):
        self.assertEqual(es_palindromo("Ana"), True)

    def test_es_palindromo_otto(self):
        self.assertEqual(es_palindromo("otto"), True)

    def test_es_palindromo_carlos(self):
        self.assertEqual(es_palindromo("carlos"), False)


if __name__ == '__main__':
    unittest.main()
