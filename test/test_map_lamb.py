from contextlib import redirect_stdout
from io import StringIO

import pytest


def test_descuento_calculado_correctamente():
    """Verifica que los descuentos se apliquen correctamente."""
    producto = [
        {"nombre": "camisa", "precio": 50000},
        {"nombre": "elden ring", "precio": 120000},
    ]

    aplicar_descuento = map(lambda x: x["precio"] * 0.90, producto)
    descuento = list(aplicar_descuento)

    assert descuento == [45000.0, 108000.0], "El cálculo del descuento es incorrecto"


def test_main_imprime_resultados_correctos():
    """Verifica que la función main imprima los precios esperados."""
    from Datos_map_y_lambda_6 import main

    salida = StringIO()
    with redirect_stdout(salida):
        main()
    output = salida.getvalue()
    precio=2

    assert "Precio: $45,000.00" in output
    assert "Precio: $108,000.00" in output
    assert output.count("Precio:") == precio


def test_funcion_main_no_lanza_excepciones():
    """Prueba que la función main se ejecute sin errores."""
    from Datos_map_y_lambda_6 import main

    try:
        main()
    except Exception as e:
        pytest.fail(f"La función main lanzó una excepción inesperada: {e}")
