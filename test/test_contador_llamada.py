from Contador_llamada_3 import crear_contador, limite_conteo

# --- Pruebas para crear_contador --- #


def test_crear_contador_incrementa_correctamente():
    """Prueba que el contador incremente correctamente en cada llamada."""
    contador = crear_contador()

    # Primer llamado -> 1
    assert contador() == 1
    # Segundo llamado -> 2
    assert contador() == 2
    # Tercer llamado -> 3
    assert contador() == 3


def test_crear_contador_es_independiente():
    """Prueba que dos contadores diferentes mantengan su propio conteo."""
    contador_a = crear_contador()
    contador_b = crear_contador()

    # Cada uno debe iniciar desde 1 independientemente
    assert contador_a() == 1
    assert contador_a() == 2

    assert contador_b() == 1
    assert contador_b() == 2


# --- Pruebas para limite_conteo --- #


def test_limite_conteo_alcanza_limite():
    """Prueba que limite_conteo devuelva True al llegar al límite."""
    assert limite_conteo(4) is True


def test_limite_conteo_no_alcanza_limite():
    """Prueba que limite_conteo devuelva False si aún no se alcanza el límite."""
    assert limite_conteo(3) is False
    assert limite_conteo(0) is False
    assert limite_conteo(2, limite=5) is False


def test_limite_conteo_con_valor_personalizado():
    """Prueba que se pueda usar un límite distinto de 4."""
    assert limite_conteo(5, limite=5) is True
    assert limite_conteo(4, limite=5) is False
