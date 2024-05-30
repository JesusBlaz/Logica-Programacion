// Ejercicio #4:


export let textoEnReversa: (texto:string) => string = (texto:string) => {
    /**
     * Función que invierte un texto sin usar métodos propios del lenguaje.
     *
     * @param {string} texto -El texto que se invertirá.
     * @return {string} El texto invertido.
     */

    let nuevoTexto = ''
    for (let letra of texto) {
        nuevoTexto = letra + nuevoTexto
    }

    return nuevoTexto
}


// console.log(textoEnReversa("Hola mundo!"))
