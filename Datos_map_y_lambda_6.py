def main ():
    producto = [{"nombre": "camisa", "precio": 50000},
                {"nombre": "elden ring", "precio": 120000}]

    aplicar_descuento = map(lambda x: x["precio"] * 0.90, producto)

    descuento = list(aplicar_descuento)

    for precio in descuento:
        print(f"Precio: ${precio:,.2f}")
if __name__ == "__main__":
    main()