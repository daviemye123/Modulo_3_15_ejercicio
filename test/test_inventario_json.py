import os
import json
import pytest
from unittest.mock import patch

from Inventario_json import (
    cargar_inventario,
    guardar_inventario,
    agregar_producto,
    vender_producto,
    mostrar_inventario,
    buscar_producto,
    editar_producto
)


ARCHIVO_TEST = "inventario.json"


@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Borra el archivo de inventario antes y después de cada prueba."""
    if os.path.exists(ARCHIVO_TEST):
        os.remove(ARCHIVO_TEST)
    yield
    if os.path.exists(ARCHIVO_TEST):
        os.remove(ARCHIVO_TEST)


def test_cargar_inventario_retorna_lista_vacia_si_no_existe():
    if os.path.exists(ARCHIVO_TEST):
        os.remove(ARCHIVO_TEST)
    data = cargar_inventario(ARCHIVO_TEST)
    assert data == []


def test_guardar_y_cargar_inventario(tmp_path):
    archivo = tmp_path / "inv.json"
    inventario = [{"id": 1, "nombre": "Flor", "cantidad": 10, "precio": 5.0, "categoria": "Rosas"}]
    assert guardar_inventario(inventario, archivo)
    cargado = cargar_inventario(archivo)
    assert cargado == inventario


@patch("inventario.Prompt.ask", side_effect=["Rosa"])
@patch("inventario.IntPrompt.ask", side_effect=[10])
@patch("inventario.FloatPrompt.ask", side_effect=[5.0])
@patch("inventario.Prompt.ask", side_effect=["Flores"])
def test_agregar_producto_agrega_un_item(mock_cat, mock_precio, mock_cant, mock_nombre):
    inventario = []
    with patch("inventario.guardar_inventario", return_value=True):
        result = agregar_producto(inventario)
    assert len(result) == 1
    assert result[0]["nombre"] == "Rosa"
    assert result[0]["cantidad"] == 10
    assert result[0]["precio"] == 5.0


@patch("inventario.IntPrompt.ask", side_effect=[1, 3])
def test_vender_producto_resta_stock(mock_prompt):
    inventario = [{"id": 1, "nombre": "Tulipán", "cantidad": 10, "precio": 2.5, "categoria": "Flores"}]
    with patch("inventario.guardar_inventario", return_value=True):
        actualizado = vender_producto(inventario)
    assert actualizado[0]["cantidad"] == 7


@patch("inventario.IntPrompt.ask", side_effect=[1, 15])
def test_vender_producto_stock_insuficiente(mock_prompt, capsys):
    inventario = [{"id": 1, "nombre": "Lirio", "cantidad": 5, "precio": 2.5, "categoria": "Flores"}]
    vender_producto(inventario)
    salida = capsys.readouterr().out
    assert "Stock insuficiente" in salida


def test_mostrar_inventario_vacio(capsys):
    mostrar_inventario([])
    salida = capsys.readouterr().out
    assert "vacío" in salida


def test_mostrar_inventario_tabla(capsys):
    inventario = [{"id": 1, "nombre": "Rosa", "cantidad": 5, "precio": 10.0, "categoria": "Flores"}]
    mostrar_inventario(inventario)
    salida = capsys.readouterr().out
    assert "Rosa" in salida


@patch("inventario.Prompt.ask", return_value="rosa")
def test_buscar_producto_encontrado(mock_prompt, capsys):
    inventario = [{"id": 1, "nombre": "Rosa", "cantidad": 10, "precio": 5.0, "categoria": "Flores"}]
    buscar_producto(inventario)
    salida = capsys.readouterr().out
    assert "resultado" in salida.lower()


@patch("inventario.Prompt.ask", return_value="nada")
def test_buscar_producto_no_encontrado(mock_prompt, capsys):
    inventario = [{"id": 1, "nombre": "Rosa", "cantidad": 10, "precio": 5.0, "categoria": "Flores"}]
    buscar_producto(inventario)
    salida = capsys.readouterr().out
    assert "No se encontraron" in salida

@patch("inventario.IntPrompt.ask", side_effect=[1])
@patch("inventario.Prompt.ask", side_effect=["Rosa Editada", "Flores"])
@patch("inventario.FloatPrompt.ask", return_value=7.5)
@patch("inventario.IntPrompt.ask", side_effect=[1, 20])
def test_editar_producto_actualiza(mock_int1, mock_float, mock_prompt, mock_id):
    inventario = [{"id": 1, "nombre": "Rosa", "cantidad": 10, "precio": 5.0, "categoria": "Flores"}]
    with patch("inventario.guardar_inventario", return_value=True):
        actualizado = editar_producto(inventario)
    assert actualizado[0]["nombre"] == "Rosa Editada"
    assert actualizado[0]["precio"] == 7.5
    assert actualizado[0]["cantidad"] == 20
