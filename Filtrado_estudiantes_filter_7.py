def main():
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9)]
    nota=3.0
    nuw_list = filter(lambda x: x[1] >= nota, estudiantes)
    lista_aprobados = list(nuw_list)
    print(f"Estudiantes: {lista_aprobados}")


if __name__ == "__main__":
    main()
