import esPalindromo from '../src/ejercicio2'


test('Test es palíndromo Ana', () => {
    expect(esPalindromo('Ana')).toBe(true)
})

test('Test es palíndromo otto', () => {
    expect(esPalindromo('otto')).toBe(true)
})

test('Test es palíndromo carlos', () => {
    expect(esPalindromo('carlos')).toBe(false)
})
