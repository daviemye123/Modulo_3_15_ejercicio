from contextlib import redirect_stdout
from io import StringIO

import pytest

import Filtrado_estudiantes_filter_7


def test_filtra_estudiantes_aprobados():
    """Verifica que solo los estudiantes con nota >= 3.0 sean filtrados."""
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9)]

    resultado = list(filter(lambda x: x[1] >= 3.0, estudiantes))

    assert resultado == [("Ana", 4.5), ("Maria", 3.9)]


def test_main_imprime_correctamente():
    """Verifica que main imprima la lista correcta."""
    salida = StringIO()
    with redirect_stdout(salida):
        Filtrado_estudiantes_filter_7.main()

    output = salida.getvalue().strip()

    assert "('Ana', 4.5)" in output
    assert "('Maria', 3.9)" in output

    assert "('Juan', 2.8)" not in output


def test_no_lanza_excepciones():
    """Asegura que la función main se ejecute sin errores."""
    try:
        Filtrado_estudiantes_filter_7.main()
    except Exception as e:
        pytest.fail(f"La función lanzó una excepción inesperada: {e}")
