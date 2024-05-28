# Ejercicio #3:
import re


def contar_palabra_en_frase(palabra, frase) -> int:
    """
    Cuenta las apariciones de una palabra específica dentro de una frase.

    :param palabra: (str), la palabra que se desea contar dentro de la frase.
    :param frase: (str), la frase donde se busca la palabra.
    :return: (int), el número de veces que la palabra aparece en la frase.
    """

    texto_limpio = re.sub(r'[.,¡!¿?_-]', "", frase)

    contador = 0
    for palabra_en_frase in texto_limpio.lower().split():
        if palabra_en_frase == palabra.lower():
            contador += 1

    return contador


# print(contar_palabra_en_frase("una", "Una?, sí, ¡una! había. una. vez una ¡niña!"))
