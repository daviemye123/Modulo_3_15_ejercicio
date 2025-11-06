import os
import pytest
from io import StringIO
from contextlib import redirect_stdout

import Gestor_tarea_archivo_txt


@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Limpia el archivo de tareas antes y después de cada test."""
    if os.path.exists(Gestor_tarea_archivo_txt  .ARCHIVO_TAREAS):
        os.remove(Gestor_tarea_archivo_txt  .ARCHIVO_TAREAS)
    yield
    if os.path.exists(Gestor_tarea_archivo_txt  .ARCHIVO_TAREAS):
        os.remove(Gestor_tarea_archivo_txt  .ARCHIVO_TAREAS)


def test_agregar_y_ver_tareas():
    """Verifica que las tareas se agreguen correctamente al archivo."""
    Gestor_tarea_archivo_txt  .agregar_tarea("Estudiar Python")
    Gestor_tarea_archivo_txt  .agregar_tarea("Hacer pytest")

    tareas = Gestor_tarea_archivo_txt  .ver_tareas()
    assert "[ ] Estudiar Python" in tareas
    assert "[ ] Hacer pytest" in tareas
    assert len(tareas) == 2


def test_eliminar_tarea():
    """Prueba que eliminar_tarea borra la línea correcta."""
    Gestor_tarea_archivo_txt  .agregar_tarea("Tarea 1")
    Gestor_tarea_archivo_txt  .agregar_tarea("Tarea 2")
    Gestor_tarea_archivo_txt  .eliminar_tarea(1)

    tareas = Gestor_tarea_archivo_txt  .ver_tareas()
    assert len(tareas) == 1
    assert "[ ] Tarea 2" in tareas


def test_marcar_completada():
    """Verifica que se marque correctamente una tarea."""
    Gestor_tarea_archivo_txt  .agregar_tarea("Aprender Pytest")
    Gestor_tarea_archivo_txt  .marcar_completada(1)

    tareas = Gestor_tarea_archivo_txt  .ver_tareas()
    assert tareas[0].startswith("[X]"), "La tarea debe marcarse como completada"


def test_limpiar_completadas():
    """Prueba que se eliminen las tareas completadas."""
    Gestor_tarea_archivo_txt  .agregar_tarea("Tarea 1")
    Gestor_tarea_archivo_txt  .agregar_tarea("Tarea 2")
    Gestor_tarea_archivo_txt  .marcar_completada(1)

    Gestor_tarea_archivo_txt  .limpiar_completadas()
    tareas = Gestor_tarea_archivo_txt  .ver_tareas()

    assert len(tareas) == 1
    assert tareas[0].startswith("[ ]"), "Solo deben quedar pendientes"


def test_mostrar_tareas_sin_tareas():
    """Verifica que mostrar_tareas no falle con lista vacía."""
    salida = StringIO()
    with redirect_stdout(salida):
        Gestor_tarea_archivo_txt  .mostrar_tareas()
    output = salida.getvalue()

    assert "No hay tareas registradas" in output


def test_ver_tareas_archivo_inexistente():
    """Debe retornar una lista vacía si el archivo no existe."""
    if os.path.exists(Gestor_tarea_archivo_txt  .ARCHIVO_TAREAS):
        os.remove(Gestor_tarea_archivo_txt  .ARCHIVO_TAREAS)
    assert Gestor_tarea_archivo_txt  .ver_tareas() == []