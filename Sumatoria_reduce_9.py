from functools import reduce


def suma_numeros():
    """Ejercicio 1: Suma de números usando reduce."""
    print("=" * 70)
    print("EJERCICIO 1: SUMA DE NÚMEROS CON REDUCE")
    print("=" * 70)

    numeros = [1, 2, 3, 4, 5]
    suma_total = reduce(lambda x, y: x + y, numeros)

    print(f"\nLista de números: {numeros}")
    print(f"Suma total usando reduce: {suma_total}")

    print("\nProceso paso a paso:")
    print("  1 + 2 = 3")
    print("  3 + 3 = 6")
    print("  6 + 4 = 10")
    print("  10 + 5 = 15")

    return suma_total


def concatenar_strings():
    """Ejercicio 2: Concatenar strings usando reduce."""
    print("\n" + "=" * 70)
    print("EJERCICIO 2: CONCATENAR STRINGS CON REDUCE")
    print("=" * 70)

    palabras = ["Hola", " ", "SENA", "!"]
    frase_completa = reduce(lambda x, y: x + y, palabras)

    print(f"\nLista de strings: {palabras}")
    print(f"Frase concatenada: '{frase_completa}'")

    print("\nProceso paso a paso:")
    print("  'Hola' + ' ' = 'Hola '")
    print("  'Hola ' + 'SENA' = 'Hola SENA'")
    print("  'Hola SENA' + '!' = 'Hola SENA!'")

    return frase_completa


def ejemplos_adicionales():
    """Ejemplos adicionales con reduce: máximo, producto y concatenación."""
    print("\n" + "=" * 70)
    print("EJEMPLOS ADICIONALES")
    print("=" * 70)

    numeros2 = [15, 3, 27, 9, 41, 8]
    maximo = reduce(lambda x, y: x if x > y else y, numeros2)
    print(f"\nEncontrar el máximo en {numeros2}")
    print(f"Máximo: {maximo}")

    numeros3 = [2, 3, 4]
    producto = reduce(lambda x, y: x * y, numeros3)
    print(f"\nMultiplicar todos los números en {numeros3}")
    print(f"Producto: {producto} (2 × 3 × 4)")

    palabras2 = ["Python", "es", "genial"]
    frase_con_guiones = reduce(lambda x, y: x + "-" + y, palabras2)
    print(f"\nConcatenar con guiones: {palabras2}")
    print(f"Resultado: '{frase_con_guiones}'")

    return {
        "maximo": maximo,
        "producto": producto,
        "frase_con_guiones": frase_con_guiones,
    }


def comparacion_reduce_vs_alternativas():
    """Comparación entre reduce() y funciones integradas."""
    print("\n" + "=" * 70)
    print("COMPARACIÓN: reduce vs alternativas")
    print("=" * 70)

    numeros = [1, 2, 3, 4, 5]
    palabras = ["Hola", " ", "SENA", "!"]

    suma_reduce = reduce(lambda x, y: x + y, numeros)
    suma_builtin = sum(numeros)
    concat_reduce = reduce(lambda x, y: x + y, palabras)
    concat_join = "".join(palabras)

    print(f"\nSuma con reduce: {suma_reduce}")
    print(f"Suma con sum():  {suma_builtin}")
    print(f"\nConcatenar con reduce: '{concat_reduce}'")
    print(f"Concatenar con join():  '{concat_join}'")

    return {
        "suma_reduce": suma_reduce,
        "suma_builtin": suma_builtin,
        "concat_reduce": concat_reduce,
        "concat_join": concat_join,
    }


def conclusion():
    """Imprime la conclusión sobre reduce()."""
    print("\n" + "=" * 70)
    print("CONCLUSIÓN")
    print("=" * 70)
    print("""
reduce() aplica una función acumulativa de izquierda a derecha:
- La función lambda toma 2 parámetros (acumulador y valor actual)
- El resultado se usa como acumulador para la siguiente iteración
- Es útil cuando necesitas reducir una secuencia a un solo valor
""")


def main():
    """Ejecuta todos los ejercicios de demostración."""
    suma_numeros()
    concatenar_strings()
    ejemplos_adicionales()
    comparacion_reduce_vs_alternativas()
    conclusion()


if __name__ == "__main__":
    main()
