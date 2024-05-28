import unittest
from logica_programacion.ejercicio3 import contar_palabra_en_frase


class TestContarPalabraEnFrase(unittest.TestCase):
    def test_contar_palabra_una(self):
        self.assertEqual(contar_palabra_en_frase("una", "Había una vez una niña"), 2)

    def test_contar_palabra_la(self):
        self.assertEqual(contar_palabra_en_frase("la", "La niña, la Pinta y la Santa María"), 3)

    def test_contar_palabra_una_con_caracteres(self):
        self.assertEqual(contar_palabra_en_frase("una", "Una?, sí, una!!! Había. una. vez una niña!"), 4)

    def test_no_existe_palabra(self):
        self.assertEqual(contar_palabra_en_frase("Hola", "Había una vez una niña"), 0)


if __name__ == '__main__':
    unittest.main()
