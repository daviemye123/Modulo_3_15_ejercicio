from Contador_llamada_3 import limite_conteo


def test_limite_conteo_alcanza_limite():
    """Prueba que limite_conteo devuelva True al llegar al límite."""
    assert limite_conteo(4) is True


def test_limite_conteo_no_alcanza_limite():
    """Prueba que limite_conteo devuelva False si aún no se alcanza el límite."""
    assert limite_conteo(3) is False
    assert limite_conteo(0) is False
    assert limite_conteo(2, limite=5) is False


