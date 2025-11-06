import pytest

from Perfil_usuario_2 import (
    crear_perfil,
    extraer_datos_perfil,
    obtener_estadisticas_perfil,
)


@pytest.fixture
def perfil_completo():
    """Fixture que crea un perfil completo."""
    return crear_perfil(
        "Usuario Test",
        30,
        "hobby1",
        "hobby2",
        "hobby3",
        red1="@usuario",
        red2="usuario_test",
    )


def test_perfil_solo_datos_basicos():
    """Test con solo nombre y edad."""
    perfil = crear_perfil("Juan Pérez", 30)
    assert "Juan Pérez" in perfil
    assert "30 años" in perfil
    assert "PERFIL DE USUARIO" in perfil


def test_perfil_con_un_hobby():
    """Test con un solo hobby."""
    perfil = crear_perfil("María García", 25, "lectura")
    assert "María García" in perfil
    assert "Lectura" in perfil.title()


def test_perfil_con_multiples_hobbies():
    """Test con múltiples hobbies."""
    perfil = crear_perfil("Carlos López", 28, "fútbol", "música", "cocina")
    assert "Fútbol" in perfil.title()
    assert "Música" in perfil.title()
    assert "Cocina" in perfil.title()


def test_perfil_con_multiples_redes_sociales():
    """Test con múltiples redes sociales."""
    perfil = crear_perfil(
        "Pedro Martínez",
        32,
        instagram="@pedro_m",
        twitter="@pedrom",
        linkedin="pedro-martinez",
    )
    assert "@pedro_m" in perfil
    assert "@pedrom" in perfil
    assert "pedro-martinez" in perfil


def test_nombre_solo_espacios_lanza_error():
    """Test que verifica que nombre con solo espacios lanza ValueError."""
    with pytest.raises(ValueError, match="vacío"):
        crear_perfil("   ", 25)


def test_edad_negativa_lanza_error():
    """Test que verifica que edad negativa lanza ValueError."""
    with pytest.raises(ValueError, match="entre 0 y 150"):
        crear_perfil("Juan", -1)


def test_edad_flotante_lanza_error():
    """Test que verifica que edad como float lanza TypeError."""
    with pytest.raises(TypeError, match="entero"):
        crear_perfil("Juan", 25.5)


def test_edad_cero():
    """Test con edad cero (bebé)."""
    perfil = crear_perfil("Bebé López", 0)
    assert "0 años" in perfil


def test_nombre_con_caracteres_especiales():
    """Test con caracteres especiales en el nombre."""
    perfil = crear_perfil("José María Ñoño", 30)
    assert "José María Ñoño" in perfil


def test_red_social_con_guion_bajo():
    """Test que verifica que guiones bajos se formatean correctamente."""
    perfil = crear_perfil("Juan", 25, red_social_personalizada="@juan")

    assert "red social personalizada" in perfil.lower()


def test_retorno_es_string():
    """Test que verifica que el retorno es un string."""
    perfil = crear_perfil("Juan", 25)
    assert isinstance(perfil, str)


def test_perfil_contiene_seccion_redes(perfil_completo):
    """Test usando fixture para verificar sección de redes."""
    assert "REDES SOCIALES" in perfil_completo


def test_estadisticas_basicas():
    """Test estadísticas con datos básicos."""
    stats = obtener_estadisticas_perfil("Juan Pérez", 30)
    edad=30
    assert stats["cantidad_hobbies"] == 0
    assert stats["cantidad_redes"] == 0
    assert stats["edad"] == edad


def test_estadisticas_con_hobbies():
    """Test estadísticas con hobbies."""
    stats = obtener_estadisticas_perfil("María", 25, "lectura", "yoga")
    cantidad=2
    assert stats["cantidad_hobbies"] == cantidad



def test_extraer_con_hobbies():
    """Test extracción con hobbies."""
    nombre, edad, hobbies, redes = extraer_datos_perfil("María", 25, "lectura", "yoga")
    assert hobbies == ("lectura", "yoga")


def test_extraer_con_redes():
    """Test extracción con redes sociales."""
    nombre, edad, hobbies, redes = extraer_datos_perfil(
        "Carlos", 28, twitter="@carlos", github="carlos"
    )
    assert redes["twitter"] == "@carlos"
    assert redes["github"] == "carlos"


@pytest.mark.parametrize(
    "nombre,edad",
    [
        ("Juan Pérez", 25),
        ("María García", 30),
    ],
)
def test_crear_perfil_parametrizado(nombre, edad):
    """Test parametrizado con diferentes nombres y edades."""
    perfil = crear_perfil(nombre, edad)
    assert nombre in perfil
    assert str(edad) in perfil


@pytest.mark.parametrize("edad_invalida", [-1, 151])
def test_edades_invalidas_parametrizado(edad_invalida):
    """Test parametrizado con edades inválidas."""
    with pytest.raises(ValueError):
        crear_perfil("Juan", edad_invalida)


@pytest.mark.parametrize("nombre_invalido", ["", "   "])
def test_nombres_invalidos_parametrizado(nombre_invalido):
    """Test parametrizado con nombres inválidos."""
    with pytest.raises(ValueError):
        crear_perfil(nombre_invalido, 25)
