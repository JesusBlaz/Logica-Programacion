// Resultado ejercicio #1:


export let tablaDeMultiplicar = (tabla: number, rango=10) => {
    /**
     * Genera la tabla de multiplicar para un número dado hasta el rango especificado.
     * @param tabla: number, La tabla de multiplicar a generar.
     * @param rango: number (opcional), hasta qué número se debe multiplicar la 'tabla'.
     * @return: string, la tabla de multiplicar como un string formateado.
     */

    let tablaMultiplicar = `Tabla del #${tabla} \n`

    for (let i:number = 0; i <= rango; i++) {
        let resultado = tabla * i
        tablaMultiplicar += `${tabla} x ${i} = ${resultado} \n`
    }

    return tablaMultiplicar
}

// console.log(tablaDeMultiplicar(2))
