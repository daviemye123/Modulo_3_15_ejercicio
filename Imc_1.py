def clasificar_riesgo(imc):
    """Clasifica el riesgo de salud según el IMC.

    Args:
        imc: Índice de masa corporal

    Returns:
        str: El nivel de riesgo clasificado.
    """
    if imc < 16.0:
        return " Delgadez severa"
    elif imc < 17.0:
        return " Delgadez moderada"
    elif imc < 18.5:
        return " Delgadez leve"
    elif imc < 25.0:
        return " Peso normal"
    elif imc < 30.0:
        return " Sobrepeso"
    elif imc < 35.0:
        return " Obesidad clase 1"
    elif imc < 40.0:
        return "R Obesidad clase 2"
    else:
        return "Obesidad clase 3"


def clasificar_imc(imc):
    """Clasifica el IMC según los datos de la persona.

    Args:
        imc: Índice de masa corporal

    Returns:
        str: La clasificación del IMC.
    """
    imc_ideal_min = 18.5
    imc_ideal_max = 24.9
    imc_sobrepeso = 25.0

    if imc >= imc_ideal_min and imc <= imc_ideal_max:
        return f"IMC {imc:.2f} ,peso saludabel"
    elif imc < imc_ideal_min:
        return f"IMC {imc:.2f} , tiene bajo peso"
    elif imc >= imc_sobrepeso:
        return f"IMC {imc:.2f} , sobre peso"


def calcular_peso_ideal(altura: float) -> tuple:
    """Calcula el rango de peso ideal según la altura.

    Args:
        altura: Altura en metros

    Returns:
        tuple: (peso_minimo, peso_maximo) en kg
    """
    peso_min = 18.5 * (altura**2)
    peso_max = 24.9 * (altura**2)
    return peso_min, peso_max


def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el IMC dado el peso en kg y altura en metros."""
    if peso <= 0 or altura <= 0:
        raise ValueError("El peso y la altura deben ser valores positivos")

    imc = peso / altura**2
    return imc


def validar_datos(peso: float, altura: float) -> bool:
    """Valida que los datos sean coherentes."""
    if peso <= 0 or altura <= 0:
        return False
    if altura > 3.0:
        return False
    if peso > 500:
        return False
    return True


def main():
    """Función principal para interactuar con el usuario."""
    print("Calculadora de IMC (Índice de Masa Corporal)")

    try:
        peso_str = input("Ingrese su peso en kilogramos: ")
        altura_str = input("Ingrese su altura en metros: ")

        peso = float(peso_str)
        altura = float(altura_str)

        if not validar_datos(peso, altura):
            print("\n Error valores no validos.")
            print("Deben ser números positivos y realistas.")
            return

        imc = calcular_imc(peso, altura)
        mensaje = clasificar_imc(imc)
        riesgo = clasificar_riesgo(imc)
        peso_min, peso_max = calcular_peso_ideal(altura)

        print("\n" + " Resultados ")
        print(f"Su IMC es: {imc:.2f}")
        print(f"estado: {mensaje}")
        print(f"Riesgo de Salud: {riesgo}")

        print("Rango de peso saludable para su altura:")
        print(f"  Mínimo: {peso_min:.1f} kg")
        print(f"  Máximo: {peso_max:.1f} kg")

    except ValueError:
        print("\n Error datos invalido, validar peso y altura sean validos.")


if __name__ == "__main__":
    main()
