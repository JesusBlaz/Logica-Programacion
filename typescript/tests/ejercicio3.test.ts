import contarPalabraEnFrase from '../src/ejercicio3'


test('Test contar palabra una', () => {
    expect(contarPalabraEnFrase("una", "Había una vez una niña")).toBe(2)
})

test('Test contar palabra la', () => {
    expect(contarPalabraEnFrase("la", "La niña, la Pinta y la Santa María")).toBe(3)
})

test('Test contar palabra una con caracteres', () => {
    expect(contarPalabraEnFrase("una", "Una?, sí, una!!! Había. una. vez una niña!")).toBe(4)
})

test('Test no existe palabra', () => {
    expect(contarPalabraEnFrase("Hola", "Había una vez una niña")).toBe(0)
})
