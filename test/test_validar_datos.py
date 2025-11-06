import pytest
from Validar_datos_genericos import (
    aplicar_validador, aplicar_validador_con_info,
    es_email_valido, es_email_corporativo,
    es_mayor_a_10, es_numero_positivo, es_numero_par,
    esta_en_rango, es_texto_no_vacio, tiene_longitud_minima,
    contiene_solo_letras, es_lista_no_vacia, tiene_clave,
    combinar_validadores, alguno_valido, negar_validador
)



def test_aplicar_validador_filtra_correctamente():
    datos = [5, 15, 3, 20, 8, 12]
    resultado = aplicar_validador(datos, es_mayor_a_10)
    assert resultado == [15, 20, 12]


def test_aplicar_validador_con_info():
    datos = [5, 15, 3]
    resultado = aplicar_validador_con_info(datos, es_mayor_a_10)
    assert resultado["validos"] == [15]
    assert resultado["invalidos"] == [5, 3]




def test_es_mayor_a_10():
    assert es_mayor_a_10(15) is True
    assert es_mayor_a_10(5) is False
    assert es_mayor_a_10("abc") is False


def test_es_numero_positivo():
    assert es_numero_positivo(5) is True
    assert es_numero_positivo(-3) is False
    assert es_numero_positivo("texto") is False


def test_es_numero_par():
    assert es_numero_par(4) is True
    assert es_numero_par(7) is False
    assert es_numero_par("no_numero") is False


def test_esta_en_rango():
    validador = esta_en_rango(10, 20)
    assert validador(15) is True
    assert validador(25) is False
    assert validador("texto") is False




def test_es_texto_no_vacio():
    assert es_texto_no_vacio("hola") is True
    assert es_texto_no_vacio("   ") is False
    assert es_texto_no_vacio(123) is False


def test_tiene_longitud_minima():
    validador = tiene_longitud_minima(5)
    assert validador("abcdef") is True
    assert validador("abc") is False


def test_contiene_solo_letras():
    assert contiene_solo_letras("Hola") is True
    assert contiene_solo_letras("Hola123") is False
    assert contiene_solo_letras("") is False




def test_es_email_valido():
    assert es_email_valido("usuario@example.com") is True
    assert es_email_valido("correo_invalido") is False
    assert es_email_valido(123) is False


def test_es_email_corporativo():
    assert es_email_corporativo("empleado@empresa.com") is True
    assert es_email_corporativo("usuario@gmail.com") is False
    assert es_email_corporativo("no_valido") is False




def test_es_lista_no_vacia():
    assert es_lista_no_vacia([1, 2]) is True
    assert es_lista_no_vacia([]) is False
    assert es_lista_no_vacia("no_lista") is False


def test_tiene_clave():
    validador = tiene_clave("nombre")
    assert validador({"nombre": "Juan"}) is True
    assert validador({"edad": 30}) is False
    assert validador("no_diccionario") is False




def test_combinar_validadores_AND():
    validador = combinar_validadores(es_mayor_a_10, es_numero_par)
    assert validador(12) is True
    assert validador(15) is False
    assert validador(8) is False


def test_alguno_valido_OR():
    validador = alguno_valido(es_numero_par, es_mayor_a_10)
    assert validador(12) is True
    assert validador(9) is False
    assert validador(11) is True


def test_negar_validador_NOT():
    validador = negar_validador(es_mayor_a_10)
    assert validador(5) is True
    assert validador(15) is False
