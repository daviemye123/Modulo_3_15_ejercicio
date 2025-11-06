"""
funcion anidada
agr:varibale inicial de conteo estando en 0
Returns: retonando la funcion unterna que es incrementar
"""
def crear_contador():
    conteo = 0
    """
    incrementa el conteo 
    agr:varibale inicial de conteo estando en 0
    returns: retonando la funcion unterna que es incrementar
    """
    def incrementar():

        nonlocal conteo
        conteo += 1

        return conteo
    return incrementar
"""
limita el conteo hasta que llegue a 4 
arg:limite=4
returns: retonando la funcion unterna que es incrementar
"""

def limite_conteo(valor, limite=4):
    return valor == limite
"""
inicio del programa
con un bucle while para poder obtener el valor actual del conteo hasta llegar a 4
imprime valor actual
"""

def main():
    contador1 = crear_contador()

    print("Iniciando contador hasta 4:")

    while True:
        valor_actual = contador1()

        print(f"El contador actual es: {valor_actual}")

        if limite_conteo(valor_actual, limite=4):
            print("límite de 4 alcanzado")
            break

if __name__ == "__main__":
    main()