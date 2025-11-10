from Explorar_datos_10 import explorar_estructura


def test_explorar_numero_simple(capsys):
    """Prueba con un número entero simple (Profundidad 1)."""
    explorar_estructura(100)
    captura = capsys.readouterr()
    assert "Valor: 100, Profundidad: 1" in captura.out.strip()


def test_explorar_string_simple(capsys):
    """Prueba con un string simple (Profundidad 1)."""
    explorar_estructura("Test String")
    captura = capsys.readouterr()
    assert "Valor: Test String, Profundidad: 1" in captura.out.strip()


def test_explorar_valor_none(capsys):
    """Prueba con el valor None (Profundidad 1)."""
    explorar_estructura(None)
    captura = capsys.readouterr()
    assert "Valor: None, Profundidad: 1" in captura.out.strip()


def test_explorar_lista_plana(capsys):
    """Prueba con una lista plana, verificando Profundidad 2."""
    estructura = [1, 2]
    explorar_estructura(estructura)
    captura = capsys.readouterr()
    output = captura.out.strip().split("\n")
    assert "Valor: 1, Profundidad: 2" in output
    assert "Valor: 2, Profundidad: 2" in output


def test_explorar_lista_anidada(capsys):
    """Prueba con anidamiento profundo."""
    estructura = [1, [2, [3]]]
    explorar_estructura(estructura)
    captura = capsys.readouterr()
    output = captura.out.strip().split("\n")

    assert "Valor: 1, Profundidad: 2" in output
    assert "Valor: 2, Profundidad: 3" in output
    assert "Valor: 3, Profundidad: 4" in output


def test_explorar_diccionario_plano(capsys):
    """Prueba con un diccionario plano, verificando clave y valor (Profundidad 2)."""
    estructura = {"a": 1, "b": "dos"}
    explorar_estructura(estructura)
    captura = capsys.readouterr()
    output = captura.out.strip().split("\n")

    assert "Clave: a, Profundidad: 2" in output
    assert "Valor: 1, Profundidad: 2" in output
    assert "Clave: b, Profundidad: 2" in output
    assert "Valor: dos, Profundidad: 2" in output


def test_explorar_diccionario_anidado(capsys):
    """Prueba con un diccionario que contiene una lista."""
    estructura = {"config": [True, False]}
    explorar_estructura(estructura)
    captura = capsys.readouterr()
    output = captura.out.strip().split("\n")

    assert "Clave: config, Profundidad: 2" in output

    assert "Valor: True, Profundidad: 3" in output
    assert "Valor: False, Profundidad: 3" in output


