from typing import Tuple, Dict


def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera un perfil de usuario con información personal, hobbies y redes sociales.

    Esta función crea un perfil formateado que incluye datos básicos del usuario,
    sus pasatiempos favoritos y sus perfiles en redes sociales.

    Args:
        nombre (str): Nombre completo del usuario.
        edad (int): Edad del usuario en años.
        *hobbies (str): Cantidad variable de hobbies o pasatiempos del usuario.
        **redes_sociales (str): Pares clave-valor donde la clave es el nombre de la
                                red social y el valor es el usuario/handle.

    Returns:
        str: Un string formateado con toda la información del perfil.

    Examples:
        >>> crear_perfil("Ana García", 25, "lectura", "yoga", instagram="@ana_g", twitter="@anagarcia")

        >>> crear_perfil("Carlos Ruiz", 30)

        >>> crear_perfil("María López", 28, "fotografía", "viajes", "cocina",
        ...              linkedin="maria-lopez", github="mlopez")

    Raises:
        ValueError: Si la edad es negativa o mayor a 150.
        TypeError: Si nombre no es string o edad no es entero.
    """
    # Validaciones
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser un string")

    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un entero")

    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años")

    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    # Construcción del perfil
    perfil = f"{'=' * 50}\n"
    perfil += f"           PERFIL DE USUARIO\n"
    perfil += f"{'=' * 50}\n\n"

    # Información básica
    perfil += f"📝 Nombre: {nombre}\n"
    perfil += f"🎂 Edad: {edad} años\n"

    # Hobbies
    perfil += f"\n{'─' * 50}\n"
    perfil += f"🎯 HOBBIES:\n"
    perfil += f"{'─' * 50}\n"

    if hobbies:
        for i, hobby in enumerate(hobbies, 1):
            perfil += f"  {i}. {hobby.capitalize()}\n"
    else:
        perfil += "  (No se especificaron hobbies)\n"

    # Redes sociales
    perfil += f"\n{'─' * 50}\n"
    perfil += f"🌐 REDES SOCIALES:\n"
    perfil += f"{'─' * 50}\n"

    if redes_sociales:
        for red, usuario in redes_sociales.items():
            # Formatear el nombre de la red social
            red_formateada = red.replace("_", " ").title()
            perfil += f"  • {red_formateada}: {usuario}\n"
    else:
        perfil += "  (No se especificaron redes sociales)\n"

    perfil += f"\n{'=' * 50}\n"

    return perfil


def obtener_estadisticas_perfil(nombre: str, edad: int, *hobbies: str,
                                **redes_sociales: str) -> Dict[str, int]:
    """
    Obtiene estadísticas sobre el perfil del usuario.

    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        *hobbies (str): Hobbies del usuario.
        **redes_sociales (str): Redes sociales del usuario.

    Returns:
        Dict[str, int]: Diccionario con estadísticas del perfil.
    """
    return {
        "longitud_nombre": len(nombre),
        "cantidad_hobbies": len(hobbies),
        "cantidad_redes": len(redes_sociales),
        "edad": edad
    }


def extraer_datos_perfil(nombre: str, edad: int, *hobbies: str,
                         **redes_sociales: str) -> Tuple[str, int, Tuple[str, ...], Dict[str, str]]:
    """
    Extrae y retorna los datos del perfil como una tupla estructurada.

    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        *hobbies (str): Hobbies del usuario.
        **redes_sociales (str): Redes sociales del usuario.

    Returns:
        Tuple[str, int, Tuple[str, ...], Dict[str, str]]: Tupla con todos los datos.
    """
    return nombre, edad, hobbies, redes_sociales


# Ejemplos de uso
if __name__ == "__main__":
    print("=" * 70)
    print("EJEMPLOS DE USO DE LA FUNCIÓN crear_perfil()")
    print("=" * 70)
    print()

    # Ejemplo 1: Perfil completo
    print("EJEMPLO 1: Perfil completo con hobbies y redes sociales")
    print()
    perfil1 = crear_perfil(
        "Ana García",
        25,
        "lectura",
        "yoga",
        "fotografía",
        instagram="@ana_garcia",
        twitter="@anag",
        linkedin="ana-garcia-dev"
    )
    print(perfil1)

    # Ejemplo 2: Solo información básica
    print("\nEJEMPLO 2: Solo información básica (sin hobbies ni redes)")
    print()
    perfil2 = crear_perfil("Carlos Ruiz", 30)
    print(perfil2)

    # Ejemplo 3: Con hobbies pero sin redes sociales
    print("\nEJEMPLO 3: Con hobbies pero sin redes sociales")
    print()
    perfil3 = crear_perfil(
        "María López",
        28,
        "cocina",
        "senderismo",
        "pintura"
    )
    print(perfil3)

    # Ejemplo 4: Sin hobbies pero con redes sociales
    print("\nEJEMPLO 4: Sin hobbies pero con redes sociales")
    print()
    perfil4 = crear_perfil(
        "Pedro Martínez",
        35,
        github="pmartinez",
        stackoverflow="pedro_m",
        twitter="@pedrom"
    )
    print(perfil4)

    # Ejemplo 5: Uso de función auxiliar de estadísticas
    print("\nEJEMPLO 5: Estadísticas del perfil")
    print()
    stats = obtener_estadisticas_perfil(
        "Laura Fernández",
        27,
        "natación",
        "música",
        facebook="laura.fernandez",
        instagram="@lau_fer"
    )
    print(f"Estadísticas: {stats}")

    # Ejemplo 6: Extracción de datos
    print("\nEJEMPLO 6: Extracción estructurada de datos")
    print()
    nombre, edad, hobbies, redes = extraer_datos_perfil(
        "Jorge Silva",
        32,
        "programación",
        "gaming",
        github="jsilva",
        linkedin="jorge-silva-dev"
    )
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Hobbies: {hobbies}")
    print(f"Redes: {redes}")

    # Ejemplo 7: Manejo de errores
    print("\n\nEJEMPLO 7: Manejo de errores")
    print()
    try:
        perfil_error = crear_perfil("", 25)
    except ValueError as e:
        print(f" Error capturado: {e}")

    try:
        perfil_error = crear_perfil("Juan", -5)
    except ValueError as e:
        print(f" Error capturado: {e}")

    try:
        perfil_error = crear_perfil("Juan", "25")  # Edad como string
    except TypeError as e:
        print(f" Error capturado: {e}")
