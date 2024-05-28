// Ejercicio #3:


export default function contarPalabraEnFrase(palabra:string, frase:string): number {
    /**
     * Cuenta las apariciones de una palabra específica dentro de una frase dada.
     * La función ignora mayúsculas y minúsculas y no cuenta palabras con puntuación.
     *
     * @param {string} palabra - La palabra a buscar dentro de la frase.
     * @param {string} frase - La frase donde buscar la palabra.
     * @return {number} El número de veces que la palabra aparece en la frase.
     */

    let textoLimpio: string[] = frase.toLowerCase().replace(/[.,¡!¿?_-]/gi, "").split(" ")

    let conteo = 0
    for (const palabraEnFrase of textoLimpio) {
        if (palabra.toLowerCase() === palabraEnFrase) {
            conteo ++
        }
    }

    return conteo
}


// console.log(contarPalabraEnFrase("una", "Una. noche había una vez una niña!"))
