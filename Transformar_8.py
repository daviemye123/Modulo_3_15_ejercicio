def analizar_texto(texto: str) -> dict:
    """
    Analiza un texto y devuelve información sobre palabras en MAYÚSCULAS
    con más de 5 letras.

    Args:
        texto (str): Texto a analizar.

    Returns:
        dict: Contiene las palabras filtradas, un diccionario con longitudes
              y resumen de estadísticas.
    """

    palabras_filtradas = [
        palabra for palabra in texto.split()
        if len(palabra) > 5 and palabra.isupper()
    ]

    diccionario_longitudes = {
        palabra: len(palabra)
        for palabra in palabras_filtradas
    }

    if not diccionario_longitudes:
        resumen = {
            "total": 0,
            "mas_larga": None,
            "mas_corta": None
        }
    else:
        palabra_larga = max(diccionario_longitudes, key=diccionario_longitudes.get)
        palabra_corta = min(diccionario_longitudes, key=diccionario_longitudes.get)

        resumen = {
            "total": len(palabras_filtradas),
            "mas_larga": (palabra_larga, diccionario_longitudes[palabra_larga]),
            "mas_corta": (palabra_corta, diccionario_longitudes[palabra_corta])
        }

    return {
        "palabras_filtradas": palabras_filtradas,
        "diccionario_longitudes": diccionario_longitudes,
        "resumen": resumen
    }



if __name__ == "__main__":
    texto = """
    Piratear juegos de NINTENDO es moralmente etico
    apoyado por todos los GAMERS
    """
    resultado = analizar_texto(texto)
    print(resultado)
