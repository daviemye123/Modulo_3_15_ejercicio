def clasificar_riesgo(imc):
    """Clasifica el riesgo de salud según el IMC.

    Args:
        imc: Índice de masa corporal

    Returns:
        str: El nivel de riesgo clasificado.
    """
    if imc < 16.0:
        return "Riesgo muy alto - Delgadez severa"
    elif imc < 17.0:
        return "Riesgo alto - Delgadez moderada"
    elif imc < 18.5:
        return "Riesgo bajo - Delgadez leve"
    elif imc < 25.0:
        return "Riesgo mínimo - Peso normal"
    elif imc < 30.0:
        return "Riesgo aumentado - Sobrepeso"
    elif imc < 35.0:
        return "Riesgo alto - Obesidad clase I"
    elif imc < 40.0:
        return "Riesgo muy alto - Obesidad clase II"
    else:
        return "Riesgo extremo - Obesidad clase III"


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
        return f"IMC {imc:.2f} - Rango normal (peso saludable)"
    elif imc < imc_ideal_min:
        return f"IMC {imc:.2f} - Por debajo del rango normal (bajo peso)"
    elif imc >= imc_sobrepeso:
        return f"IMC {imc:.2f} - Por encima del rango normal (sobrepeso)"


def calcular_peso_ideal(altura: float) -> tuple:
    """Calcula el rango de peso ideal según la altura.

    Args:
        altura: Altura en metros

    Returns:
        tuple: (peso_minimo, peso_maximo) en kg
    """
    peso_min = 18.5 * (altura ** 2)
    peso_max = 24.9 * (altura ** 2)
    return peso_min, peso_max


def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el IMC dado el peso en kg y altura en metros."""
    if peso <= 0 or altura <= 0:
        raise ValueError("El peso y la altura deben ser valores positivos")

    imc = peso / altura ** 2
    return imc


def validar_datos(peso: float, altura: float) -> bool:
    """Valida que los datos sean coherentes."""
    if peso <= 0 or altura <= 0:
        return False
    if altura > 3.0:  # Altura poco realista
        return False
    if peso > 500:  # Peso poco realista
        return False
    return True


def mostrar_tabla_referencia():
    """Muestra una tabla de referencia de clasificación IMC (usando print)."""
    print("\n" + "=" * 40)
    print("Clasificación IMC según la OMS")
    print("=" * 40)
    print("Categoría           | Rango IMC    | Nivel de Riesgo")
    print("-" * 40)
    print("Delgadez severa     | < 16.0       | Muy alto")
    print("Delgadez moderada   | 16.0 - 16.9  | Alto")
    print("Delgadez leve       | 17.0 - 18.4  | Bajo")
    print("Peso normal         | 18.5 - 24.9  | Mínimo")
    print("Sobrepeso           | 25.0 - 29.9  | Aumentado")
    print("Obesidad clase I    | 30.0 - 34.9  | Alto")
    print("Obesidad clase II   | 35.0 - 39.9  | Muy alto")
    print("Obesidad clase III  | ≥ 40.0       | Extremo")
    print("=" * 40)


def main():
    """Función principal para interactuar con el usuario."""
    print("*" * 30)
    print("Calculadora de IMC (Índice de Masa Corporal)")
    print("*" * 30)

    try:
        # Solicitar datos usando input()
        peso_str = input("Ingrese su peso en kilogramos: ")
        altura_str = input("Ingrese su altura en metros: ")

        peso = float(peso_str)
        altura = float(altura_str)

        if not validar_datos(peso, altura):
            print("\n!!! Error: Los valores ingresados no son válidos.")
            print("Deben ser números positivos y realistas.")
            return

        # Calcular IMC
        imc = calcular_imc(peso, altura)
        mensaje = clasificar_imc(imc)
        riesgo = clasificar_riesgo(imc)
        peso_min, peso_max = calcular_peso_ideal(altura)

        print("\n" + "--- Resultados ---")
        print(f"Su IMC es: {imc:.2f}")
        print(f"Clasificación: {mensaje}")
        print(f"Riesgo de Salud: {riesgo}")
        print("-" * 20)

        # Información adicional
        print(f"Rango de peso saludable para su altura:")
        print(f"  Mínimo: {peso_min:.1f} kg")
        print(f"  Máximo: {peso_max:.1f} kg")

        # Calcular diferencia con el peso ideal
        if imc < 18.5:
            dif = peso_min - peso
            print(f"Recomendación: Aumentar aproximadamente {dif:.1f} kg para alcanzar el peso mínimo.")
        elif imc >= 25.0:
            dif = peso - peso_max
            print(f"Recomendación: Reducir aproximadamente {dif:.1f} kg para alcanzar el peso máximo saludable.")
        else:
            print("Estado: Su peso está en el rango ideal.")

        # Mostrar tabla de referencia
        mostrar_tabla_referencia()

        print("\nNota: Esta calculadora es solo una herramienta informativa.")
        print("Consulte con un profesional de la salud para una evaluación completa.")

    except ValueError:
        print("\n!!! Error: Asegúrese de ingresar solo números válidos para peso y altura.")
    except Exception as e:
        print(f"\n!!! Error inesperado: {e}")


if __name__ == "__main__":
    main()