from Contador_llamada_3 import crear_contador, limite_conteo



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
