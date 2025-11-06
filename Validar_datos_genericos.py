"""
Funciones de Orden Superior para Validación de Datos.

Este módulo implementa funciones de orden superior (Higher-Order Functions)
que permiten aplicar validaciones personalizadas a colecciones de datos.

Conceptos aplicados:
- Higher-Order Functions (funciones de orden superior)
- Type Hinting con Callable
- Composición de funciones
- Reutilización de código
"""

import re
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def aplicar_validador(datos: list, validador: Callable[[Any], bool]) -> list:
    """
    Función de orden superior que aplica un validador a cada elemento de una lista.

    Esta función recibe una lista de datos y una función validadora,
    y retorna una nueva lista conteniendo solo los elementos que
    pasaron la validación (aquellos para los que el validador retorna True).

    Args:
        datos (list): Lista de elementos a validar.
        validador (Callable[[Any], bool]): Función que toma un elemento
            y retorna True si es válido, False en caso contrario.

    Returns:
        list: Nueva lista con solo los elementos que pasaron la validación.

    Example:
        >>> numeros = [5, 15, 3, 20, 8, 12]
        >>> mayores = aplicar_validador(numeros, es_mayor_a_10)
        >>> print(mayores)
        [15, 20, 12]
    """
    return [elemento for elemento in datos if validador(elemento)]


def aplicar_validador_con_info(datos: list, validador: Callable[[Any], bool]) -> dict:
    """
    Versión extendida que retorna tanto los válidos como los inválidos.

    Args:
        datos (list): Lista de elementos a validar.
        validador (Callable[[Any], bool]): Función validadora.

    Returns:
        dict: Diccionario con claves 'validos' e 'invalidos'.

    Example:
        >>> resultado = aplicar_validador_con_info([5, 15, 3], es_mayor_a_10)
        >>> print(resultado['validos'])
        [15]
        >>> print(resultado['invalidos'])
        [5, 3]
    """
    validos = []
    invalidos = []

    for elemento in datos:
        if validador(elemento):
            validos.append(elemento)
        else:
            invalidos.append(elemento)

    return {"validos": validos, "invalidos": invalidos}


# ==================== VALIDADORES DE EMAIL ====================


def es_email_valido(email: str) -> bool:
    """
    Valida si un string tiene formato de email válido.

    Utiliza una expresión regular para verificar el formato básico
    de un email: usuario@dominio.extension

    Args:
        email (str): String a validar como email.

    Returns:
        bool: True si el email es válido, False en caso contrario.

    Example:
        >>> es_email_valido("usuario@example.com")
        True
        >>> es_email_valido("email_invalido")
        False
    """
    if not isinstance(email, str):
        return False

    # Patrón básico de email
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, email) is not None


def es_email_corporativo(email: str) -> bool:
    """
    Valida si un email es corporativo (no de dominios públicos).

    Args:
        email (str): Email a validar.

    Returns:
        bool: True si es email corporativo, False en caso contrario.
    """
    if not es_email_valido(email):
        return False

    dominios_publicos = [
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com",
        "live.com",
        "icloud.com",
    ]

    dominio = email.split("@")[1].lower()
    return dominio not in dominios_publicos


def es_mayor_a_10(numero: int) -> bool:
    """
    Valida si un número es mayor a 10.

    Args:
        numero (int): Número a validar.

    Returns:
        bool: True si el número es mayor a 10, False en caso contrario.

    Example:
         es_mayor_a_10(15)
        True
         es_mayor_a_10(5)
        False
    """
    try:
        maxim=10
        return float(numero) > maxim
    except (TypeError, ValueError):
        return False


def es_numero_positivo(numero: float) -> bool:
    """
    Valida si un número es positivo.

    Args:
        numero (float): Número a validar.

    Returns:
        bool: True si es positivo, False en caso contrario.
    """
    try:
        return float(numero) > 0
    except (TypeError, ValueError):
        return False


def es_numero_par(numero: int) -> bool:
    """
    Valida si un número es par.

    Args:
        numero (int): Número a validar.

    Returns:
        bool: True si es par, False en caso contrario.
    """
    try:
        return int(numero) % 2 == 0
    except (TypeError, ValueError):
        return False


def esta_en_rango(minimo: float, maximo: float) -> Callable[[float], bool]:
    """
    Genera un validador que verifica si un número está en un rango.

    Esta es una función de orden superior que RETORNA un validador.

    Args:
        minimo (float): Valor mínimo del rango (inclusivo).
        maximo (float): Valor máximo del rango (inclusivo).

    Returns:
        Callable[[float], bool]: Función validadora para el rango especificado.

    Example:
         validador_edad = esta_en_rango(18, 65)
         validador_edad(25)
        True
         validador_edad(70)
        False
    """

    def validador(numero: float) -> bool:
        try:
            valor = float(numero)
            return minimo <= valor <= maximo
        except (TypeError, ValueError):
            return False

    return validador


def es_texto_no_vacio(texto: str) -> bool:
    """
    Valida que un texto no esté vacío (después de eliminar espacios).

    Args:
        texto (str): Texto a validar.

    Returns:
        bool: True si no está vacío, False en caso contrario.
    """
    return isinstance(texto, str) and texto.strip() != ""


def tiene_longitud_minima(minimo: int) -> Callable[[str], bool]:
    """
    Genera un validador que verifica longitud mínima de texto.

    Args:
        minimo (int): Longitud mínima requerida.

    Returns:
        Callable[[str], bool]: Función validadora de longitud.

    Example:
         validador_password = tiene_longitud_minima(8)
         validador_password("secreto123")
        True
         validador_password("corta")
        False
    """

    def validador(texto: str) -> bool:
        return isinstance(texto, str) and len(texto) >= minimo

    return validador


def contiene_solo_letras(texto: str) -> bool:
    """
    Valida que un texto contenga solo letras (sin números ni símbolos).

    Args:
        texto (str): Texto a validar.

    Returns:
        bool: True si contiene solo letras, False en caso contrario.
    """
    return isinstance(texto, str) and texto.isalpha()


def es_lista_no_vacia(elemento: list) -> bool:
    """
    Valida que un elemento sea una lista no vacía.

    Args:
        elemento: Elemento a validar.

    Returns:
        bool: True si es lista no vacía, False en caso contrario.
    """
    return isinstance(elemento, list) and len(elemento) > 0


def tiene_clave(clave: str) -> Callable[[dict], bool]:
    """
    Genera un validador que verifica si un diccionario tiene una clave.

    Args:
        clave (str): Clave a buscar.

    Returns:
        Callable[[dict], bool]: Función validadora.

    Example:
         validador = tiene_clave('email')
         validador({'nombre': 'Juan', 'email': 'juan@example.com'})
        True
    """

    def validador(diccionario: dict) -> bool:
        return isinstance(diccionario, dict) and clave in diccionario

    return validador


def combinar_validadores(*validadores: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """
    Combina múltiples validadores en uno solo (operación AND).

    El elemento debe pasar TODOS los validadores para ser considerado válido.

    Args:
        *validadores: Funciones validadoras a combinar.

    Returns:
        Callable[[Any], bool]: Validador combinado.

    Example:
         validador_completo = combinar_validadores(
             es_mayor_a_10,
             es_numero_par
         )
         validador_completo(12)  # Mayor a 10 Y par
        True
         validador_completo(15)  # Mayor a 10 pero NO par
        False
    """

    def validador_combinado(elemento: Any) -> bool:
        return all(validador(elemento) for validador in validadores)

    return validador_combinado


def alguno_valido(*validadores: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """
    Combina múltiples validadores con operación OR.

    El elemento debe pasar AL MENOS UN validador para ser considerado válido.

    Args:
        *validadores: Funciones validadoras a combinar.

    Returns:
        Callable[[Any], bool]: Validador combinado.
    """

    def validador_combinado(elemento: Any) -> bool:
        return any(validador(elemento) for validador in validadores)

    return validador_combinado


def negar_validador(validador: Callable[[Any], bool]) -> Callable[[Any], bool]:
    """
    Invierte un validador (operación NOT).

    Args:
        validador: Función validadora a invertir.

    Returns:
        Callable[[Any], bool]: Validador invertido.

    Example:
        validador_menor_o_igual_10 = negar_validador(es_mayor_a_10)
        validador_menor_o_igual_10(5)
        True
         validador_menor_o_igual_10(15)
        False
    """

    def validador_invertido(elemento: Any) -> bool:
        return not validador(elemento)

    return validador_invertido


if __name__ == "__main__":
    print("=== Demostración de Funciones de Orden Superior ===\n")

    print("1. Validación de emails:")
    emails = [
        "usuario@example.com",
        "email_invalido",
        "contacto@empresa.org",
        "sin_arroba.com",
        "valido@dominio.co",
    ]
    emails_validos = aplicar_validador(emails, es_email_valido)
    print(f"Emails originales: {emails}")
    print(f"Emails válidos: {emails_validos}\n")

    print("2. Números mayores a 10:")
    numeros = [5, 15, 3, 20, 8, 12, 10, 25]
    mayores = aplicar_validador(numeros, es_mayor_a_10)
    print(f"Números originales: {numeros}")
    print(f"Mayores a 10: {mayores}\n")

    print("3. Edades válidas (18-65):")
    edades = [15, 25, 30, 70, 45, 12, 60, 80]
    validador_edad = esta_en_rango(18, 65)
    edades_validas = aplicar_validador(edades, validador_edad)
    print(f"Edades originales: {edades}")
    print(f"Edades válidas: {edades_validas}\n")

    print("4. Números pares:")
    numeros_pares = aplicar_validador(numeros, es_numero_par)
    print(f"Números originales: {numeros}")
    print(f"Números pares: {numeros_pares}\n")

    print("5. Números mayores a 10 Y pares:")
    validador_combinado = combinar_validadores(es_mayor_a_10, es_numero_par)
    mayores_pares = aplicar_validador(numeros, validador_combinado)
    print(f"Números originales: {numeros}")
    print(f"Mayores a 10 Y pares: {mayores_pares}\n")

    print("6. Validación con información detallada:")
    resultado = aplicar_validador_con_info(numeros, es_mayor_a_10)
    print(f"Válidos: {resultado['validos']}")
    print(f"Inválidos: {resultado['invalidos']}\n")

    print("7. Emails corporativos:")
    todos_emails = [
        "el_rosas@gmail.com",
        "david@empresa.com",
        "personal@yahoo.com",
        "trabajo@miempresa.org",
    ]
    emails_corp = aplicar_validador(todos_emails, es_email_corporativo)
    print(f"Todos los emails: {todos_emails}")
    print(f"Emails corporativos: {emails_corp}")
