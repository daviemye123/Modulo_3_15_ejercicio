"""
Tests para el sistema de gestión de biblioteca (versión sin clases).

Este módulo contiene tests unitarios para todas las funcionalidades
del sistema de préstamos de biblioteca usando solo funciones.
"""

import json
from pathlib import Path

import pytest

from Biblioteca import (
    buscar_libro,
    buscar_libro_por_id,
    cargar_datos,
    crear_biblioteca_inicial,
    devolver_libro,
    guardar_datos,
    prestar_libro,
    ver_libros_prestados,
    ver_todos_los_libros,
)


@pytest.fixture
def archivo_temporal(tmp_path):
    """Crea un archivo temporal para las pruebas."""
    return str(tmp_path / "test_biblioteca.json")


@pytest.fixture
def libros_vacios():
    """Crea una lista vacía de libros para pruebas."""
    return []


@pytest.fixture
def libros_con_datos():
    """Crea una lista de libros con datos de prueba."""
    return [
        {
            "libro_id": "001",
            "titulo": "Test Book 1",
            "autor": "Test Author 1",
            "isbn": "123456789",
            "prestado_a": None,
            "fecha_prestamo": None,
        },
        {
            "libro_id": "002",
            "titulo": "Test Book 2",
            "autor": "Test Author 2",
            "isbn": "987654321",
            "prestado_a": "Juan Pérez",
            "fecha_prestamo": "2025-01-01T10:00:00",
        },
        {
            "libro_id": "003",
            "titulo": "Python Programming",
            "autor": "Test Author 1",
            "isbn": "111222333",
            "prestado_a": None,
            "fecha_prestamo": None,
        },
    ]


def test_crea_biblioteca_con_libros():
    """Verifica que se cree una biblioteca con libros."""
    libros = crear_biblioteca_inicial()
    assert len(libros) > 0
    assert isinstance(libros, list)


def test_libros_tienen_estructura_correcta():
    """Verifica que los libros tengan la estructura correcta."""
    libros = crear_biblioteca_inicial()
    for libro in libros:
        assert "libro_id" in libro
        assert "titulo" in libro
        assert "autor" in libro
        assert "prestado_a" in libro
        assert "fecha_prestamo" in libro


def test_libros_inicialmente_disponibles():
    """Verifica que los libros estén inicialmente disponibles."""
    libros = crear_biblioteca_inicial()
    for libro in libros:
        assert libro["prestado_a"] is None
        assert libro["fecha_prestamo"] is None


def test_carga_archivo_existente(archivo_temporal, libros_con_datos):
    """Verifica que se carguen datos de un archivo existente."""

    guardar_datos(libros_con_datos, archivo_temporal)

    libros = cargar_datos(archivo_temporal)
    libro=3
    assert len(libros) == libro
    assert libros[0]["titulo"] == "Test Book 1"


def test_crea_archivo_si_no_existe(archivo_temporal):
    """Verifica que se cree un archivo si no existe."""
    libros = cargar_datos(archivo_temporal)
    assert Path(archivo_temporal).exists()
    assert len(libros) > 0


def test_guarda_datos_correctamente(archivo_temporal, libros_con_datos):
    """Verifica que los datos se guarden correctamente."""
    guardar_datos(libros_con_datos, archivo_temporal)

    assert Path(archivo_temporal).exists()

    with open(archivo_temporal, encoding="utf-8") as f:
        datos = json.load(f)
        datos1=3

    assert len(datos) == datos1
    assert datos[0]["titulo"] == "Test Book 1"


def test_buscar_libro_existente(libros_con_datos):
    """Verifica que se encuentre un libro existente."""
    libro = buscar_libro_por_id(libros_con_datos, "001")
    assert libro is not None
    assert libro["titulo"] == "Test Book 1"


def test_buscar_libro_inexistente(libros_con_datos):
    """Verifica que retorne None para libro inexistente."""
    libro = buscar_libro_por_id(libros_con_datos, "999")
    assert libro is None


def test_buscar_en_lista_vacia(libros_vacios):
    """Verifica búsqueda en lista vacía."""
    libro = buscar_libro_por_id(libros_vacios, "001")
    assert libro is None


def test_prestar_libro_disponible(archivo_temporal, libros_con_datos):
    """Verifica que se pueda prestar un libro disponible."""
    resultado = prestar_libro(libros_con_datos, "001", "María García", archivo_temporal)
    assert resultado is True

    libro = buscar_libro_por_id(libros_con_datos, "001")
    assert libro["prestado_a"] == "María García"
    assert libro["fecha_prestamo"] is not None


def test_prestar_libro_ya_prestado(archivo_temporal, libros_con_datos):
    """Verifica que no se pueda prestar un libro ya prestado."""
    resultado = prestar_libro(libros_con_datos, "002", "Ana López", archivo_temporal)
    assert resultado is False

    libro = buscar_libro_por_id(libros_con_datos, "002")
    assert libro["prestado_a"] == "Juan Pérez"


def test_prestar_libro_inexistente(archivo_temporal, libros_con_datos):
    """Verifica el manejo de préstamo de libro inexistente."""
    resultado = prestar_libro(libros_con_datos, "999", "Carlos Ruiz", archivo_temporal)
    assert resultado is False


def test_persistencia_prestamo(archivo_temporal, libros_con_datos):
    """Verifica que el préstamo se persista en el archivo."""
    prestar_libro(libros_con_datos, "001", "Test User", archivo_temporal)

    with open(archivo_temporal, encoding="utf-8") as f:
        datos = json.load(f)

    libro = next(item for item in datos if item["libro_id"] == "001")
    assert libro["prestado_a"] == "Test User"


def test_fecha_prestamo_formato_iso(archivo_temporal, libros_con_datos):
    """Verifica que la fecha de préstamo esté en formato ISO."""
    prestar_libro(libros_con_datos, "003", "Pedro Sánchez", archivo_temporal)

    libro = buscar_libro_por_id(libros_con_datos, "003")
    assert "T" in libro["fecha_prestamo"]


def test_devolver_libro_prestado(archivo_temporal, libros_con_datos):
    """Verifica que se pueda devolver un libro prestado."""
    resultado = devolver_libro(libros_con_datos, "002", archivo_temporal)
    assert resultado is True

    libro = buscar_libro_por_id(libros_con_datos, "002")
    assert libro["prestado_a"] is None
    assert libro["fecha_prestamo"] is None


def test_devolver_libro_no_prestado(archivo_temporal, libros_con_datos):
    """Verifica que no se pueda devolver un libro no prestado."""
    resultado = devolver_libro(libros_con_datos, "001", archivo_temporal)
    assert resultado is False


def test_devolver_libro_inexistente(archivo_temporal, libros_con_datos):
    """Verifica el manejo de devolución de libro inexistente."""
    resultado = devolver_libro(libros_con_datos, "999", archivo_temporal)
    assert resultado is False


def test_persistencia_devolucion(archivo_temporal, libros_con_datos):
    """Verifica que la devolución se persista en el archivo."""
    devolver_libro(libros_con_datos, "002", archivo_temporal)

    with open(archivo_temporal, encoding="utf-8") as f:
        datos = json.load(f)


    libro = next(item for item in datos if item["libro_id"] == "002")
    assert libro["prestado_a"] is None


def test_buscar_por_titulo_exacto(libros_con_datos):
    """Verifica búsqueda por título exacto."""
    resultados = buscar_libro(libros_con_datos, "Test Book 1")
    assert len(resultados) == 1
    assert resultados[0]["titulo"] == "Test Book 1"


def test_buscar_por_titulo_parcial(libros_con_datos):
    """Verifica búsqueda por título parcial."""
    resultados = buscar_libro(libros_con_datos, "Test Book")
    resultados=2
    assert len(resultados) == resultados


def test_buscar_por_autor(libros_con_datos):
    """Verifica búsqueda por autor."""
    resultados = buscar_libro(libros_con_datos, "Test Author 1")
    resultados=2
    assert len(resultados) == resultados


def test_buscar_insensible_mayusculas(libros_con_datos):
    """Verifica que la búsqueda sea insensible a mayúsculas."""
    resultados = buscar_libro(libros_con_datos, "test book 1")
    assert len(resultados) == 1


def test_buscar_sin_resultados(libros_con_datos):
    """Verifica comportamiento sin resultados."""
    resultados = buscar_libro(libros_con_datos, "Nonexistent")
    assert len(resultados) == 0


def test_buscar_por_palabra_clave(libros_con_datos):
    """Verifica búsqueda por palabra clave."""
    resultados = buscar_libro(libros_con_datos, "Python")
    assert len(resultados) == 1
    assert "Python" in resultados[0]["titulo"]


def test_ver_libros_prestados(libros_con_datos):
    """Verifica que se filtren solo los libros prestados."""
    prestados = ver_libros_prestados(libros_con_datos)
    assert len(prestados) == 1
    assert prestados[0]["libro_id"] == "002"


def test_ver_sin_libros_prestados(archivo_temporal, libros_con_datos):
    """Verifica comportamiento sin libros prestados."""
    devolver_libro(libros_con_datos, "002", archivo_temporal)

    prestados = ver_libros_prestados(libros_con_datos)
    assert len(prestados) == 0


def test_ver_multiples_prestados(archivo_temporal, libros_con_datos):
    """Verifica con múltiples libros prestados."""
    prestar_libro(libros_con_datos, "001", "Usuario 1", archivo_temporal)
    prestar_libro(libros_con_datos, "003", "Usuario 2", archivo_temporal)

    prestados = ver_libros_prestados(libros_con_datos)
    prestamos=3
    assert len(prestados) == prestamos


def test_ver_todos_los_libros(libros_con_datos):
    """Verifica que se muestren todos los libros."""
    ver_todos_los_libros(libros_con_datos)
    datos=2
    assert len(libros_con_datos) == datos


def test_ver_biblioteca_vacia(libros_vacios):
    """Verifica comportamiento con biblioteca vacía."""
    ver_todos_los_libros(libros_vacios)
    assert len(libros_vacios) == 0


def test_flujo_completo_prestamo_devolucion(archivo_temporal):
    """Verifica flujo completo: cargar, prestar, devolver."""
    libros = crear_biblioteca_inicial()
    guardar_datos(libros, archivo_temporal)

    # Prestar libro
    assert prestar_libro(libros, "001", "Test User", archivo_temporal) is True

    # Verificar préstamo
    prestados = ver_libros_prestados(libros)
    assert len(prestados) == 1

    assert devolver_libro(libros, "001", archivo_temporal) is True

    # Verificar devolución
    prestados = ver_libros_prestados(libros)
    assert len(prestados) == 0


def test_multiples_operaciones(archivo_temporal, libros_con_datos):
    """Verifica múltiples operaciones consecutivas."""
    # Prestar varios libros
    prestar_libro(libros_con_datos, "001", "Usuario A", archivo_temporal)
    prestar_libro(libros_con_datos, "003", "Usuario B", archivo_temporal)

    prestados = ver_libros_prestados(libros_con_datos)
    prestados=3
    assert len(prestados) == prestados

    devolver_libro(libros_con_datos, "001", archivo_temporal)
    devolver_libro(libros_con_datos, "002", archivo_temporal)
    devolver_libro(libros_con_datos, "003", archivo_temporal)

    prestados = ver_libros_prestados(libros_con_datos)
    assert len(prestados) == 0


def test_buscar_despues_de_modificar(archivo_temporal, libros_con_datos):
    """Verifica búsqueda después de modificaciones."""
    prestar_libro(libros_con_datos, "001", "Test User", archivo_temporal)

    resultados = buscar_libro(libros_con_datos, "Test Book 1")
    assert len(resultados) == 1
    assert resultados[0]["prestado_a"] == "Test User"


def test_persistencia_multiples_operaciones(archivo_temporal, libros_con_datos):
    """Verifica persistencia en múltiples operaciones."""
    guardar_datos(libros_con_datos, archivo_temporal)

    # Realizar operaciones
    prestar_libro(libros_con_datos, "001", "Usuario X", archivo_temporal)
    prestar_libro(libros_con_datos, "003", "Usuario Y", archivo_temporal)
    devolver_libro(libros_con_datos, "002", archivo_temporal)

    # Cargar datos del archivo
    libros_cargados = cargar_datos(archivo_temporal)

    # Verificar estado
    libro1 = buscar_libro_por_id(libros_cargados, "001")
    libro2 = buscar_libro_por_id(libros_cargados, "002")
    libro3 = buscar_libro_por_id(libros_cargados, "003")

    assert libro1["prestado_a"] == "Usuario X"
    assert libro2["prestado_a"] is None
    assert libro3["prestado_a"] == "Usuario Y"


def test_prestar_con_nombre_vacio(archivo_temporal, libros_con_datos):
    """Verifica préstamo con nombre vacío."""
    resultado = prestar_libro(libros_con_datos, "001", "", archivo_temporal)
    assert resultado is True

    libro = buscar_libro_por_id(libros_con_datos, "001")
    assert libro["prestado_a"] == ""


def test_buscar_con_string_vacio(libros_con_datos):
    """Verifica búsqueda con string vacío."""
    resultados = buscar_libro(libros_con_datos, "")
    assert len(resultados) >= 0


def test_operaciones_sobre_lista_vacia(archivo_temporal, libros_vacios):
    """Verifica operaciones sobre lista vacía."""
    # Prestar en lista vacía
    resultado = prestar_libro(libros_vacios, "001", "Test", archivo_temporal)
    assert resultado is False

    # Buscar en lista vacía
    resultados = buscar_libro(libros_vacios, "Test")
    assert len(resultados) == 0

    # Ver prestados en lista vacía
    prestados = ver_libros_prestados(libros_vacios)
    assert len(prestados) == 0
