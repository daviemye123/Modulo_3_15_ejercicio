import os
import pytest
from Gestor_tarea_archivo_txt import (
    agregar_tarea,
    ver_tareas,
    marcar_completada,
    eliminar_tarea,
    limpiar_completadas,
    ARCHIVO_TAREAS
)

@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Limpia o elimina el archivo de tareas antes y después de cada test."""
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)
    yield
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)


def test_agregar_tarea_crea_archivo_y_agrega_linea():
    agregar_tarea("Hacer pytest")
    assert os.path.exists(ARCHIVO_TAREAS)
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
        contenido = f.read().strip()
    assert "[ ] Hacer pytest" in contenido


def test_ver_tareas_devuelve_lista_correcta():
    agregar_tarea("Estudiar Python")
    agregar_tarea("Leer documentación")
    tareas = ver_tareas()
    assert len(tareas) == 2
    assert tareas[0].startswith("[ ]")


def test_marcar_completada_modifica_estado():
    agregar_tarea("Hacer ejercicio")
    marcar_completada(1)
    tareas = ver_tareas()
    assert tareas[0].startswith("[X]") or tareas[0].startswith("[x]")


def test_eliminar_tarea_elimina_linea_correcta():
    agregar_tarea("Tarea 1")
    agregar_tarea("Tarea 2")
    eliminar_tarea(1)
    tareas = ver_tareas()
    assert len(tareas) == 1
    assert "Tarea 2" in tareas[0]


def test_limpiar_completadas_elimina_solo_completadas():
    agregar_tarea("Tarea A")
    agregar_tarea("Tarea B")
    marcar_completada(2)
    limpiar_completadas()
    tareas = ver_tareas()
    assert len(tareas) == 1
    assert tareas[0].endswith("Tarea A")


def test_marcar_completada_fuera_de_rango_no_crashea(capsys):
    agregar_tarea("Tarea X")
    marcar_completada(5)
    salida = capsys.readouterr().out
    assert "inválido" in salida or "Error" in salida


def test_eliminar_tarea_fuera_de_rango_no_crashea(capsys):
    agregar_tarea("Tarea Z")
    eliminar_tarea(10)
    salida = capsys.readouterr().out
    assert "inválido" in salida or "Error" in salida


def test_ver_tareas_con_archivo_vacio_retorna_lista_vacia():
    tareas = ver_tareas()
    assert tareas == []
