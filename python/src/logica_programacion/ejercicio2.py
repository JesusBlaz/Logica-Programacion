# Ejercicio #2:


def es_palindromo(palabra):
    """
    Verifica si la cadena proporcionada es un palíndromo.

    :param palabra: (str), La cadena a verificar.
    :return: (bool), True si la cadena es un palíndromo, False de lo contrario.
    """

    if isinstance(palabra, str):
        palabra = palabra.lower()
        return palabra == ''.join(reversed(palabra))

    return False


# print(es_palindromo("Ana"))
