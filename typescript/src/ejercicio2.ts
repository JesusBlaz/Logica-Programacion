// Ejercicio #2:


export default function esPalindromo(palabra:string):boolean {
    /**
     * Verifica si la cadena proporcionada es un palíndromo.
     * @param palabra La cadena a verificar.
     * @return true si la cadena es un palíndromo, false de lo contrario.
     */

    palabra = palabra.toLowerCase()
    return palabra === palabra.split('').reverse().join('')
}


// console.log(esPalindromo("Ana"))
