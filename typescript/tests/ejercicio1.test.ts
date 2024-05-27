import {tablaDeMultiplicar} from "../src/ejercicio1"


test('Test Tabla de multiplicar del 2', () => {
    let resultado_esperado = 'Tabla del #2 \n' +
                             '2 x 0 = 0 \n' +
                             '2 x 1 = 2 \n' +
                             '2 x 2 = 4 \n' +
                             '2 x 3 = 6 \n' +
                             '2 x 4 = 8 \n' +
                             '2 x 5 = 10 \n' +
                             '2 x 6 = 12 \n' +
                             '2 x 7 = 14 \n' +
                             '2 x 8 = 16 \n' +
                             '2 x 9 = 18 \n' +
                             '2 x 10 = 20 \n';
    expect(tablaDeMultiplicar(2)).toBe(resultado_esperado)
})
