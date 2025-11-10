def clasificar_riesgo(imc):
    """Clasifica el riesgo de salud según el IMC.

    Args:
        imc: Índice de masa corporal

    Returns:
        str: El nivel de riesgo clasificado.
    """
    rangos = [
        (16.0, "Delgadez severa"),
        (17.0, "Delgadez moderada"),
        (18.5, "Delgadez leve"),
        (25.0, "Peso normal"),
        (30.0, "Sobrepeso"),
        (35.0, "Obesidad clase 1"),
        (40.0, "Obesidad clase 2"),
    ]

    for limite, clasificacion in rangos:
        if imc < limite:
            return clasificacion

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
    altura1=3.0
    peso1=500
    if peso <= 0 or altura <= 0:
        return False
    if altura > altura1:
        return False
    if peso > peso1:
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
