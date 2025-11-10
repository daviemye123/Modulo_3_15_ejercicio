import pytest

from Imc_1 import (
    calcular_imc,
    calcular_peso_ideal,
    clasificar_imc,
    clasificar_riesgo,
)


def test_clasificar_riesgo_limites():
    """Prueba los límites de las clasificaciones de riesgo."""

    assert clasificar_riesgo(15.9) == " Delgadez severa"
    assert clasificar_riesgo(16.0) == " Delgadez moderada"

    assert clasificar_riesgo(16.99) == " Delgadez moderada"
    assert clasificar_riesgo(17.0) == " Delgadez leve"

    assert clasificar_riesgo(18.49) == " Delgadez leve"
    assert clasificar_riesgo(18.5) == " Peso normal"

    assert clasificar_riesgo(24.99) == " Peso normal"
    assert clasificar_riesgo(25.0) == " Sobrepeso"

    assert clasificar_riesgo(29.99) == " Sobrepeso"
    assert clasificar_riesgo(30.0) == " Obesidad clase 1"

    assert clasificar_riesgo(34.99) == " Obesidad clase 1"
    assert clasificar_riesgo(35.0) == "R Obesidad clase 2"

    assert clasificar_riesgo(39.99) == "R Obesidad clase 2"
    assert clasificar_riesgo(40.0) == "Obesidad clase 3"

    assert clasificar_riesgo(40.0) == "Obesidad clase 3"
    assert clasificar_riesgo(50.0) == "Obesidad clase 3"


def test_clasificar_imc_peso_saludable():
    """Prueba el rango de peso saludable (18.5 - 24.9)."""
    assert clasificar_imc(18.5) == "IMC 18.50 ,peso saludabel"
    assert clasificar_imc(24.9) == "IMC 24.90 ,peso saludabel"
    assert clasificar_imc(22.0) == "IMC 22.00 ,peso saludabel"


def test_clasificar_imc_bajo_peso():
    """Prueba el rango de bajo peso (< 18.5)."""
    assert clasificar_imc(18.49) == "IMC 18.49 , tiene bajo peso"
    assert clasificar_imc(15.0) == "IMC 15.00 , tiene bajo peso"


def test_clasificar_imc_sobre_peso():
    """Prueba el rango de sobrepeso (>= 25.0)."""
    assert clasificar_imc(25.0) == "IMC 25.00 , sobre peso"
    assert clasificar_imc(35.0) == "IMC 35.00 , sobre peso"


def test_calcular_peso_ideal_ejemplo():
    """Prueba el cálculo con una altura estándar (e.g., 1.75m)."""
    altura = 1.75
    peso_min_esperado = 18.5 * (altura**2)
    peso_max_esperado = 24.9 * (altura**2)

    peso_min, peso_max = calcular_peso_ideal(altura)

    assert peso_min == pytest.approx(peso_min_esperado)
    assert peso_max == pytest.approx(peso_max_esperado)


def test_calcular_peso_ideal_limite():
    """Prueba el cálculo con una altura diferente."""
    altura = 1.50
    peso_min, peso_max = calcular_peso_ideal(altura)
    assert peso_min == pytest.approx(41.625)
    assert peso_max == pytest.approx(55.025)


def test_calcular_imc_normal():
    """Prueba el cálculo del IMC con valores válidos."""

    peso = 70.0
    altura = 1.75
    imc_esperado = 70.0 / (1.75**2)
    assert calcular_imc(peso, altura) == pytest.approx(imc_esperado)


def test_calcular_imc_valores_cero_o_negativos():
    """Prueba que se lance ValueError con datos no positivos."""

    with pytest.raises(ValueError) as excinfo:
        calcular_imc(0.0, 1.75)
    assert "positivos" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        calcular_imc(70.0, 0.0)
    assert "positivos" in str(excinfo.value)

    with pytest.raises(ValueError):
        calcular_imc(-70.0, 1.75)
    with pytest.raises(ValueError):
        calcular_imc(70.0, -1.75)



