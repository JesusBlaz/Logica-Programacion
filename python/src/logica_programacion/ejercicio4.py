# Ejercicio #4:


def invertir_texto(texto) -> str:
    """
    Función que invierte cualquier texto sin métodos propios del lenguaje.
    :param (string) texto: El texto que se invertirá.
    :return: (string) nuevo_texto: El texto generado, es decir, el texto invertido.
    """

    nuevo_texto = ''
    for letra in texto:
        nuevo_texto = letra + nuevo_texto

    return nuevo_texto


# print(invertir_texto('Hola mundo!'))
