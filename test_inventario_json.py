import os
from contextlib import redirect_stdout
from io import StringIO

import pytest

import Inventario_json


@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Elimina el archivo JSON antes y después de cada test."""
    archivo = "inventario.json"
    if os.path.exists(archivo):
        os.remove(archivo)
    yield
    if os.path.exists(archivo):
        os.remove(archivo)


def test_cargar_inventario_nuevo():
    """Debe crear un inventario vacío si no existe el archivo."""
    inventario_data = Inventario_json.cargar_inventario()
    assert inventario_data == []


def test_guardar_y_cargar_inventario(tmp_path):
    """Guarda y carga correctamente el archivo JSON."""
    archivo = tmp_path / "inventario.json"
    data = [
        {"id": 1, "nombre": "Flor", "cantidad": 5, "precio": 3000, "categoria": "Rosas"}
    ]

    resultado = Inventario_json.guardar_inventario(data, archivo)
    assert resultado is True

    cargado = Inventario_json.cargar_inventario(archivo)
    assert cargado == data


def test_agregar_producto(monkeypatch):
    """Agrega un producto correctamente con valores simulados."""
    inputs = iter(["Lirio", "10", "2500", "Flores"])
    monkeypatch.setattr("rich.prompt.Prompt.ask", lambda *a, **kw: next(inputs))
    monkeypatch.setattr("rich.prompt.IntPrompt.ask", lambda *a, **kw: int(next(inputs)))
    monkeypatch.setattr(
        "rich.prompt.FloatPrompt.ask", lambda *a, **kw: float(next(inputs))
    )

    inventario_actual = []
    resultado = Inventario_json.agregar_producto(inventario_actual)
    precio = 2500.0
    cantidad = 10

    assert len(resultado) == 1
    assert resultado[0]["nombre"] == "Lirio"
    assert resultado[0]["cantidad"] == cantidad
    assert resultado[0]["precio"] == precio
    assert resultado[0]["categoria"] == "Flores"


def test_vender_producto(monkeypatch):
    """Simula una venta y reduce correctamente el stock."""
    inventario_actual = [
        {
            "id": 1,
            "nombre": "Tulipán",
            "cantidad": 5,
            "precio": 2000,
            "categoria": "Flores",
        }
    ]

    inputs = iter(["1", "2"])
    monkeypatch.setattr("rich.prompt.IntPrompt.ask", lambda *a, **kw: int(next(inputs)))

    resultado = Inventario_json.vender_producto(inventario_actual)
    cantidad = 3

    assert resultado[0]["cantidad"] == cantidad
    assert os.path.exists("inventario.json")


def test_vender_producto_stock_insuficiente(monkeypatch):
    """Debe evitar vender más de lo disponible."""
    inventario_actual = [
        {
            "id": 1,
            "nombre": "Rosa",
            "cantidad": 2,
            "precio": 1000,
            "categoria": "Flores",
        }
    ]

    inputs = iter(["1", "5"])  # intenta vender más de lo que hay
    monkeypatch.setattr("rich.prompt.IntPrompt.ask", lambda *a, **kw: int(next(inputs)))

    resultado = Inventario_json.vender_producto(inventario_actual)
    cantidad = 2

    assert resultado[0]["cantidad"] == cantidad


def test_editar_producto(monkeypatch):
    """Edita correctamente los datos de un producto."""
    inventario_actual = [
        {
            "id": 1,
            "nombre": "Rosa",
            "cantidad": 10,
            "precio": 1000,
            "categoria": "Flores",
        }
    ]

    inputs = iter(["1", "Rosa Blanca", "20", "1200", "Decorativas"])
    monkeypatch.setattr("rich.prompt.IntPrompt.ask", lambda *a, **kw: int(next(inputs)))
    monkeypatch.setattr("rich.prompt.Prompt.ask", lambda *a, **kw: next(inputs))
    monkeypatch.setattr(
        "rich.prompt.FloatPrompt.ask", lambda *a, **kw: float(next(inputs))
    )

    resultado = Inventario_json.editar_producto(inventario_actual)
    cantidad = 20
    precio = 1200.0

    p = resultado[0]
    assert p["nombre"] == "Rosa Blanca"
    assert p["cantidad"] == cantidad
    assert p["precio"] == precio
    assert p["categoria"] == "Decorativas"


def test_buscar_producto(monkeypatch):
    """Busca productos por nombre o categoría."""
    inventario_actual = [
        {
            "id": 1,
            "nombre": "Rosa",
            "cantidad": 5,
            "precio": 1000,
            "categoria": "Flores",
        },
        {
            "id": 2,
            "nombre": "Maceta",
            "cantidad": 3,
            "precio": 5000,
            "categoria": "Decoración",
        },
    ]

    monkeypatch.setattr("rich.prompt.Prompt.ask", lambda *a, **kw: "rosa")

    salida = StringIO()
    with redirect_stdout(salida):
        Inventario_json.buscar_producto(inventario_actual)
    output = salida.getvalue()

    assert "Rosa" in output or "Se encontraron" in output


def test_mostrar_inventario_vacio(capsys):
    """Debe imprimir mensaje de inventario vacío."""
    Inventario_json.mostrar_inventario([])
    salida = capsys.readouterr().out
    assert "vacío" in salida
