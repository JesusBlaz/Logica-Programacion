# Resultado ejercicio #1:


def tabla_de_multiplicar(tabla, rango=10):
    """
    Genera la tabla de multiplicar para un número dado hasta el rango especificado.

    :param tabla: int, La tabla de multiplicar a generar.
    :param rango: int (opcional), hasta qué número se debe multiplicar la 'tabla'.
    :return: str, la tabla de multiplicar como un string formateado.
    """

    tabla_multiplicar = f"Tabla del #{tabla} \n"
    for numero in range(0, rango + 1):
        resultado = tabla * numero
        tabla_multiplicar += f'{tabla} x {numero} = {resultado} \n'

    return tabla_multiplicar


# print(tabla_de_multiplicar(2))
