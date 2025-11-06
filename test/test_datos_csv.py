import csv

import pytest

from Datos_csv import analizar_csv, crear_csv_ejemplo


@pytest.fixture
def archivo_ejemplo(tmp_path):
    """Crea un CSV temporal para pruebas."""
    archivo = tmp_path / "test_estudiantes.csv"
    datos = [
        {"nombre": "Ana", "edad": "20", "calificacion": "8.5"},
        {"nombre": "Carlos", "edad": "22", "calificacion": "7.8"},
        {"nombre": "María", "edad": "19", "calificacion": "9.2"},
        {"nombre": "Juan", "edad": "21", "calificacion": "6.5"},
    ]

    with open(archivo, "w", newline="", encoding="utf-8") as f:
        campos = ["nombre", "edad", "calificacion"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)

    return archivo


def test_analizar_csv_calificacion(archivo_ejemplo):
    """Verifica el cálculo de estadísticas en una columna numérica."""
    resultados = analizar_csv(str(archivo_ejemplo), "calificacion")
    maximo=9.2
    minimo=6.5
    registro=4
    promedio=8.0

    assert pytest.approx(resultados["promedio"], 0.01) == promedio
    assert resultados["maximo"] == maximo
    assert resultados["minimo"] == minimo
    assert resultados["total_registros"] == registro


def test_analizar_csv_edad(archivo_ejemplo):
    """Verifica el cálculo de estadísticas de la columna edad."""
    resultados = analizar_csv(str(archivo_ejemplo), "edad")
    promedio=20.5
    maximo=22
    minimo=19
    registro=4

    assert pytest.approx(resultados["promedio"], 0.01) == promedio
    assert resultados["maximo"] == maximo
    assert resultados["minimo"] == minimo
    assert resultados["total_registros"] == registro


def test_columna_inexistente(archivo_ejemplo):
    """Debe lanzar error si la columna no existe."""
    with pytest.raises(ValueError, match="no existe"):
        analizar_csv(str(archivo_ejemplo), "nota_final")


def test_archivo_inexistente():
    """Debe lanzar error si el archivo no existe."""
    with pytest.raises(FileNotFoundError):
        analizar_csv("archivo_que_no_existe.csv", "edad")


def test_valores_no_numericos(tmp_path):
    """Debe ignorar valores no numéricos y lanzar error si no hay ninguno válido."""
    archivo = tmp_path / "test_invalidos.csv"
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["nombre", "edad"])
        escritor.writeheader()
        escritor.writerow({"nombre": "Ana", "edad": "abc"})  # no numérico
        escritor.writerow({"nombre": "Carlos", "edad": "xyz"})  # no numérico

    with pytest.raises(ValueError, match="No se encontraron valores numéricos"):
        analizar_csv(str(archivo), "edad")


def test_crear_csv_ejemplo(tmp_path, monkeypatch):
    """Verifica que crear_csv_ejemplo cree correctamente el archivo de ejemplo."""
    ruta = tmp_path / "estudiantes.csv"

    monkeypatch.chdir(tmp_path)
    crear_csv_ejemplo()

    assert ruta.exists()

    with open(ruta, encoding="utf-8") as f:
        contenido = f.read()
        assert "nombre" in contenido
        assert "calificacion" in contenido
