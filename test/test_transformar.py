from Transformar_8 import analizar_texto


def test_palabras_mayusculas_correctas():
    texto = "Piratear juegos de NINTENDO es moralmente etico apoyado por GAMERS"
    resultado = analizar_texto(texto)
    total=2

    assert "NINTENDO" in resultado["palabras_filtradas"]
    assert "GAMERS" in resultado["palabras_filtradas"]
    assert resultado["resumen"]["total"] == total


def test_diccionario_longitudes():
    texto = "HOLA UNIVERSO PYTHON CODIGO"
    resultado = analizar_texto(texto)

    esperado = {"UNIVERSO": 8, "PYTHON": 6, "CODIGO": 6}
    assert resultado["diccionario_longitudes"] == esperado


def test_resumen_palabras_larga_y_corta():
    texto = "UNO DOS TRES CUATRO CINCO SEIS SIETE OCHO"
    resultado = analizar_texto(texto)

    assert resultado["resumen"]["mas_larga"][0] == "CUATRO"
    assert (
        resultado["resumen"]["mas_corta"][0] == "CUATRO"
    )  # solo una palabra de más de 5 letras
    assert resultado["resumen"]["total"] == 1


def test_texto_sin_palabras_mayusculas():
    texto = "Este texto no tiene palabras en MAYUSCULAS largas"
    resultado = analizar_texto(texto)

    assert resultado["resumen"]["total"] == 1
    assert "MAYUSCULAS" in resultado["diccionario_longitudes"]


def test_texto_vacio():
    resultado = analizar_texto("")
    assert resultado["palabras_filtradas"] == []
    assert resultado["diccionario_longitudes"] == {}
    assert resultado["resumen"]["total"] == 0
    assert resultado["resumen"]["mas_larga"] is None
    assert resultado["resumen"]["mas_corta"] is None
