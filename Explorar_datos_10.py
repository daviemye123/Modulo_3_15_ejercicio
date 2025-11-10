from typing import Any, Iterable


def explorar_estructura(elemento: Any, profundidad: int = 1) -> None:
    """
    Explora recursivamente estructuras de datos anidadas (listas, tuplas, diccionarios)
    e imprime los valores no-iterables (números, strings, booleanos, None)
    con su profundidad.

    Args:
        elemento: La estructura de datos a explorar (lista, dict, o un valor simple).
        profundidad: Nivel de anidamiento actual (comienza en 1 por defecto).
    """

    if not isinstance(elemento, Iterable) or isinstance(elemento, (str, bytes)):
        # Si es un valor simple (número, string, bool, None), lo imprimimos.
        print(f"Valor: {elemento}, Profundidad: {profundidad}")
        return

    if isinstance(elemento, (list, tuple)):
        for item in elemento:
            explorar_estructura(item, profundidad + 1)

    elif isinstance(elemento, dict):
        for key, value in elemento.items():
            print(f"Clave: {key}, Profundidad: {profundidad + 1}")

            explorar_estructura(value, profundidad + 1)


estructura_anidada = [1, [2, 3, "Hola"], {"a": 4, "b": (5.5, None)}, [{"clave": [6]}]]

print("Exploración de Estructura Anidada ")
explorar_estructura(estructura_anidada)


estructura_simple = (100, 200)
print("\n Exploración de Tupla Simple ")
explorar_estructura(estructura_simple)
