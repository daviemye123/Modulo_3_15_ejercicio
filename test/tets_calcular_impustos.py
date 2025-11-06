import pytest

from Calculadora_impuesto import actualizar_iva, calcular_iva


@pytest.fixture(autouse=True)
def tasa_iva_restaurada():
    """
    Asegura que la TASA_IVA comience en 0.19 antes de cada prueba
    y se restaure al finalizar.
    """
    from Calculadora_impuesto import TASA_IVA

    tasa_inicial = TASA_IVA
    actualizar_iva(0.19)
    yield
    actualizar_iva(tasa_inicial)


def test_calcular_iva_valor_cero():
    assert calcular_iva(0.0) == 0.0


def test_calcular_iva_valor_cien():
    assert calcular_iva(100.00) == pytest.approx(19.00)


def test_calcular_iva_valor_flotante():
    assert calcular_iva(55.50) == pytest.approx(10.545)
