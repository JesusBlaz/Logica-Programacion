import {textoEnReversa} from '../src/ejercicio4'


test('Test invertir texto 1', () => {
    expect(textoEnReversa('Hola mundo!')).toBe('!odnum aloH')
})

test('Test invertir texto 2', () => {
    expect(
        textoEnReversa('Programando con Python y Typescript')
    ).toBe('tpircsepyT y nohtyP noc odnamargorP')
})
