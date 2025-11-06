TASA_IVA = 0.19


def calcular_iva(precio_base: float) -> float:
    return precio_base * TASA_IVA


def actualizar_iva(nueva_tasa: float):
    global TASA_IVA
    TASA_IVA = nueva_tasa


if __name__ == "__main__":
    precio_base = 100.00
    print(f"Tasa de IVA global inicial: {TASA_IVA}")
    print(f"Precio Base: ${precio_base:.2f}")

    iva_inicial = calcular_iva(precio_base)
    print(f"Cálculo inicial (Tasa {TASA_IVA * 100:.0f}%): ${iva_inicial:.2f}")

    actualizar_iva(0.21)
    print(f"Tasa de IVA global después de actualizar: {TASA_IVA}")
    iva_actualizado = calcular_iva(precio_base)
    print(f"Cálculo actualizado (Tasa {TASA_IVA * 100:.0f}%): ${iva_actualizado:.2f}")
