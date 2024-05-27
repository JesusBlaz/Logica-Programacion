import unittest
from logica_programacion.ejercicio1 import tabla_de_multiplicar


class TestTablaDeMultiplicar(unittest.TestCase):
    def test_tabla_del_dos(self):
        resultado_esperado = (
            "Tabla del #2 \n"
            "2 x 0 = 0 \n"
            "2 x 1 = 2 \n"
            "2 x 2 = 4 \n"
            "2 x 3 = 6 \n"
            "2 x 4 = 8 \n"
            "2 x 5 = 10 \n"
            "2 x 6 = 12 \n"
            "2 x 7 = 14 \n"
            "2 x 8 = 16 \n"
            "2 x 9 = 18 \n"
            "2 x 10 = 20 \n"
        )
        self.assertEqual(tabla_de_multiplicar(2), resultado_esperado)

    def test_tabla_del_tres(self):
        resultado_esperado = (
            "Tabla del #3 \n"
            "3 x 0 = 0 \n"
            "3 x 1 = 3 \n"
            "3 x 2 = 6 \n"
            "3 x 3 = 9 \n"
            "3 x 4 = 12 \n"
            "3 x 5 = 15 \n"
            "3 x 6 = 18 \n"
            "3 x 7 = 21 \n"
            "3 x 8 = 24 \n"
            "3 x 9 = 27 \n"
            "3 x 10 = 30 \n"
        )
        self.assertEqual(tabla_de_multiplicar(3), resultado_esperado)


if __name__ == '__main__':
    unittest.main()
