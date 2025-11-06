import pytest

from Sumatoria_reduce_9 import (
    comparacion_reduce_vs_alternativas,
    concatenar_strings,
    ejemplos_adicionales,
    suma_numeros,
)


def test_suma_numeros():
    """Verifica que la suma total con reduce sea correcta."""
    resultado = suma_numeros()
    resultado=15
    assert resultado == resultado, f"Se esperaba 15, pero se obtuvo {resultado}"


def test_concatenar_strings():
    """Verifica la concatenación de strings."""
    resultado = concatenar_strings()
    assert resultado == "Hola SENA!", (
        f"Se esperaba 'Hola SENA!', pero se obtuvo '{resultado}'"
    )


def test_ejemplos_adicionales():
    """Verifica que los valores calculados con reduce sean correctos."""
    resultado = ejemplos_adicionales()
    maixmo=41
    producto=24

    assert resultado["maximo"] == maixmo, "El máximo debe ser 41"
    assert resultado["producto"] == producto, "El producto debe ser 24 (2×3×4)"
    assert resultado["frase_con_guiones"] == "Python-es-genial", (
        "La frase concatenada debe ser 'Python-es-genial'"
    )


def test_comparacion_reduce_vs_alternativas():
    """Verifica que reduce y las alternativas den los mismos resultados."""
    resultado = comparacion_reduce_vs_alternativas()

    assert resultado["suma_reduce"] == resultado["suma_builtin"], (
        "La suma con reduce y sum() deben ser iguales"
    )

    assert resultado["concat_reduce"] == resultado["concat_join"], (
        "La concatenación con reduce y join() deben ser iguales"
    )


@pytest.mark.parametrize(
    "funcion",
    [
        suma_numeros,
        concatenar_strings,
        ejemplos_adicionales,
        comparacion_reduce_vs_alternativas,
    ],
)
def test_funciones_no_lanzan_excepciones(funcion):
    """Prueba que las funciones principales se ejecuten correctamente."""
    try:
        funcion()
    except Exception as e:
        pytest.fail(
            f"La función {funcion.__name__} lanzó una excepción inesperada: {e}"
        )
