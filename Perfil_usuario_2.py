from typing import Tuple, Dict


def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genea poerfil de usaurio.

    Esta función crea un perfil formateado que incluye datos básicos del usuario,
    sus pasatiempos favoritos y sus perfiles en redes sociales.

    Args:
        nombre (str): Nombre completo del usuario.
        edad (int): Edad del usuario en años.
        *hobbies (str): Cantidad variable de hobbies o pasatiempos del usuario.
        **redes_sociales (str): Pares clave-valor donde la clave es el nombre de la
                                red social y el valor es el usuario.

    Returns:
        str: Un string formateado con toda la información del perfil.

    """
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser un string")

    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un entero")

    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años")

    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")


    perfil = f"{'=' * 50}\n"
    perfil += f"           PERFIL DE USUARIO\n"
    perfil += f"{'=' * 50}\n\n"


    perfil += f" Nombre: {nombre}\n"
    perfil += f" Edad: {edad} años\n"


    perfil += f"\n{'─' * 50}\n"
    perfil += f" HOBBIES:\n"
    perfil += f"{'─' * 50}\n"

    if hobbies:
        for i, hobby in enumerate(hobbies, 1):
            perfil += f"  {i}. {hobby.capitalize()}\n"
    else:
        perfil += "  (No se especificaron hobbies)\n"


    perfil += f"\n{'─' * 50}\n"
    perfil += f" REDES SOCIALES:\n"
    perfil += f"{'─' * 50}\n"

    if redes_sociales:
        for red, usuario in redes_sociales.items():

            red_formateada = red.replace("_", " ").title()
            perfil += f"  • {red_formateada}: {usuario}\n"
    else:
        perfil += "  (No se especificaron redes sociales)\n"

    perfil += f"\n{'=' * 50}\n"

    return perfil


def obtener_estadisticas_perfil(nombre: str, edad: int, *hobbies: str,
                                **redes_sociales: str) -> Dict[str, int]:
    """
    Obtiene datos del perfil de usaurio.

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
    Extrae y retorna los datos del perfil como una tupla .

    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        *hobbies (str): Hobbies del usuario.
        **redes_sociales (str): Redes sociales del usuario.

    Returns:
        Tuple[str, int, Tuple[str, ...], Dict[str, str]]: Tupla con todos los datos recibidos .
    """
    return nombre, edad, hobbies, redes_sociales



if __name__ == "__main__":
    print("=" * 70)
    print("EJEMPLOS DE USO DE LA FUNCIÓN crear_perfil()")
    print("=" * 70)
    print()


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


    print("\nEJEMPLO 2: Solo información básica (sin hobbies ni redes)")
    print()
    perfil2 = crear_perfil("David Pedraza", 30)
    print(perfil2)


    print("\nEJEMPLO 3: Con hobbies pero sin redes sociales")
    print()
    perfil3 = crear_perfil(
        "Yamith Rosas",
        19,
        "voley",
        "senderismo",
        "pintura"
    )
    print(perfil3)

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
