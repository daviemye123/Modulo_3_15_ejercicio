"""
Sistema de Gestión de Préstamos de Biblioteca.

Este módulo proporciona una aplicación de consola para gestionar
el préstamo de libros en una biblioteca, con persistencia en JSON
y presentación usando Rich.
"""

import json
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

console = Console()


ARCHIVO_BIBLIOTECA = "biblioteca.json"


def crear_biblioteca_inicial() -> list[dict]:
    """
    Crea una biblioteca inicial con libros de ejemplo.

    Returns:
        Lista de diccionarios con libros de ejemplo
    """
    return [
        {
            "libro_id": "001",
            "titulo": "Cien Años de Soledad",
            "autor": "Gabriel García Márquez",
            "isbn": "978-0307474728",
            "prestado_a": None,
            "fecha_prestamo": None,
        },
        {
            "libro_id": "002",
            "titulo": "Don Quijote de la Mancha",
            "autor": "Miguel de Cervantes",
            "isbn": "978-8424936464",
            "prestado_a": None,
            "fecha_prestamo": None,
        },
        {
            "libro_id": "003",
            "titulo": "1984",
            "autor": "George Orwell",
            "isbn": "978-0451524935",
            "prestado_a": None,
            "fecha_prestamo": None,
        },
        {
            "libro_id": "004",
            "titulo": "El Principito",
            "autor": "Antoine de Saint-Exupéry",
            "isbn": "978-0156012195",
            "prestado_a": None,
            "fecha_prestamo": None,
        },
        {
            "libro_id": "005",
            "titulo": "Orgullo y Prejuicio",
            "autor": "Jane Austen",
            "isbn": "978-0141439518",
            "prestado_a": None,
            "fecha_prestamo": None,
        },
    ]


def cargar_datos(archivo: str = ARCHIVO_BIBLIOTECA) -> list[dict]:
    """
    Carga los datos de la biblioteca desde el archivo JSON.

    Args:
        archivo: Nombre del archivo JSON con los datos de la biblioteca

    Returns:
        Lista de diccionarios con los libros de la biblioteca
    """
    archivo_path = Path(archivo)

    try:
        if archivo_path.exists():
            with open(archivo_path, encoding="utf-8") as f:
                libros = json.load(f)
            console.print(
                f"[green]✓[/green] Biblioteca cargada: {len(libros)} libros"
            )
            return libros
        else:
            libros = crear_biblioteca_inicial()
            guardar_datos(libros, archivo)
            console.print(
                "[yellow]⚠[/yellow] Archivo no encontrado. "
                "Se creó una biblioteca inicial."
            )
            return libros
    except json.JSONDecodeError as e:
        console.print(f"[red]✗[/red] Error al leer el archivo JSON: {e}")
        return []
    except Exception as e:
        console.print(f"[red]✗[/red] Error inesperado: {e}")
        return []


def guardar_datos(libros: list[dict], archivo: str = ARCHIVO_BIBLIOTECA) -> None:
    """
    Guarda los datos actuales de la biblioteca en el archivo JSON.

    Args:
        libros: Lista de libros a guardar
        archivo: Nombre del archivo JSON donde guardar los datos
    """
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(libros, f, ensure_ascii=False, indent=2)
    except Exception as e:
        console.print(f"[red]✗[/red] Error al guardar datos: {e}")


def buscar_libro_por_id(libros: list[dict], libro_id: str) -> dict | None:
    """
    Busca un libro por su ID.

    Args:
        libros: Lista de libros en la biblioteca
        libro_id: ID del libro a buscar

    Returns:
        Diccionario del libro si se encuentra, None en caso contrario
    """
    for libro in libros:
        if libro["libro_id"] == libro_id:
            return libro
    return None


def prestar_libro(
    libros: list[dict], libro_id: str, nombre_aprendiz: str, archivo: str = ARCHIVO_BIBLIOTECA
) -> bool:
    """
    Marca un libro como prestado a un aprendiz.

    Args:
        libros: Lista de libros en la biblioteca
        libro_id: ID del libro a prestar
        nombre_aprendiz: Nombre de la persona que toma prestado el libro
        archivo: Nombre del archivo para persistir los cambios

    Returns:
        True si el préstamo fue exitoso, False en caso contrario
    """
    libro = buscar_libro_por_id(libros, libro_id)

    if libro is None:
        console.print(f"[red]✗[/red] Libro con ID '{libro_id}' no encontrado.")
        return False

    if libro["prestado_a"] is not None:
        console.print(
            f"[yellow]⚠[/yellow] El libro '{libro['titulo']}' ya está "
            f"prestado a: {libro['prestado_a']}"
        )
        return False

    libro["prestado_a"] = nombre_aprendiz
    libro["fecha_prestamo"] = datetime.now().isoformat()
    guardar_datos(libros, archivo)

    console.print(
        f"[green]✓[/green] Libro '{libro['titulo']}' prestado "
        f"exitosamente a {nombre_aprendiz}"
    )
    return True


def devolver_libro(
    libros: list[dict], libro_id: str, archivo: str = ARCHIVO_BIBLIOTECA
) -> bool:
    """
    Marca un libro como disponible (no prestado).

    Args:
        libros: Lista de libros en la biblioteca
        libro_id: ID del libro a devolver
        archivo: Nombre del archivo para persistir los cambios

    Returns:
        True si la devolución fue exitosa, False en caso contrario
    """
    libro = buscar_libro_por_id(libros, libro_id)

    if libro is None:
        console.print(f"[red]✗[/red] Libro con ID '{libro_id}' no encontrado.")
        return False

    if libro["prestado_a"] is None:
        console.print(
            f"[yellow]⚠[/yellow] El libro '{libro['titulo']}' "
            "no está prestado."
        )
        return False

    prestado_a = libro["prestado_a"]
    libro["prestado_a"] = None
    libro["fecha_prestamo"] = None
    guardar_datos(libros, archivo)

    console.print(
        f"[green]✓[/green] Libro '{libro['titulo']}' devuelto "
        f"exitosamente por {prestado_a}"
    )
    return True


def buscar_libro(libros: list[dict], query: str) -> list[dict]:
    """
    Busca libros por título o autor (búsqueda insensible a mayúsculas).

    Args:
        libros: Lista de libros en la biblioteca
        query: Término de búsqueda

    Returns:
        Lista de diccionarios con los libros encontrados
    """
    query_lower = query.lower()
    resultados = [
        libro
        for libro in libros
        if query_lower in libro["titulo"].lower()
        or query_lower in libro.get("autor", "").lower()
    ]

    if not resultados:
        console.print(
            f"[yellow]⚠[/yellow] No se encontraron libros con: '{query}'"
        )
        return []

    mostrar_libros(resultados, f"Resultados de búsqueda: '{query}'")
    return resultados


def ver_libros_prestados(libros: list[dict]) -> list[dict]:
    """
    Muestra todos los libros que están prestados actualmente.

    Args:
        libros: Lista de libros en la biblioteca

    Returns:
        Lista de diccionarios con los libros prestados
    """
    prestados = [libro for libro in libros if libro["prestado_a"] is not None]

    if not prestados:
        console.print("[cyan]ℹ[/cyan] No hay libros prestados actualmente.")
        return []

    mostrar_libros(prestados, "Libros Prestados", mostrar_prestamo=True)
    return prestados


def ver_todos_los_libros(libros: list[dict]) -> None:
    """
    Muestra todos los libros de la biblioteca.

    Args:
        libros: Lista de libros en la biblioteca
    """
    if not libros:
        console.print("[yellow]⚠[/yellow] La biblioteca está vacía.")
        return

    mostrar_libros(libros, "Catálogo Completo de la Biblioteca", mostrar_prestamo=True)


def mostrar_libros(
    libros: list[dict], titulo: str, mostrar_prestamo: bool = False
) -> None:
    """
    Muestra una tabla de libros usando Rich.

    Args:
        libros: Lista de libros a mostrar
        titulo: Título de la tabla
        mostrar_prestamo: Si se debe mostrar información de préstamo
    """
    table = Table(
        title=titulo,
        show_header=True,
        header_style="bold magenta",
        border_style="cyan",
    )

    table.add_column("ID", style="cyan", width=6)
    table.add_column("Título", style="green", width=30)
    table.add_column("Autor", style="yellow", width=25)

    if mostrar_prestamo:
        table.add_column("Estado", style="blue", width=15)
        table.add_column("Prestado a", style="magenta", width=20)

    for libro in libros:
        if mostrar_prestamo:
            estado = (
                "[red]Prestado[/red]"
                if libro["prestado_a"]
                else "[green]Disponible[/green]"
            )
            prestado = libro["prestado_a"] or "-"
            table.add_row(
                libro["libro_id"],
                libro["titulo"],
                libro.get("autor", "Desconocido"),
                estado,
                prestado,
            )
        else:
            table.add_row(
                libro["libro_id"],
                libro["titulo"],
                libro.get("autor", "Desconocido"),
            )

    console.print("\n")
    console.print(table)
    console.print("\n")


def mostrar_menu() -> None:
    """Muestra el menú principal de la aplicación."""
    console.print("\n")
    panel = Panel(
        "[bold cyan]1.[/bold cyan] Prestar libro\n"
        "[bold cyan]2.[/bold cyan] Devolver libro\n"
        "[bold cyan]3.[/bold cyan] Buscar libro\n"
        "[bold cyan]4.[/bold cyan] Ver libros prestados\n"
        "[bold cyan]5.[/bold cyan] Ver todos los libros\n"
        "[bold cyan]6.[/bold cyan] Salir",
        title="[bold blue] MENÚ PRINCIPAL[/bold blue]",
        border_style="blue",
    )
    console.print(panel)


def main() -> None:
    """Función principal que ejecuta la aplicación."""
    console.clear()
    console.print(
        Panel.fit(
            "[bold yellow]🏛️  SISTEMA DE GESTIÓN DE BIBLIOTECA  🏛️[/bold yellow]",
            border_style="yellow",
        )
    )
    console.print("\n")

    # Cargar datos al inicio
    libros = cargar_datos()

    while True:
        mostrar_menu()
        opcion = Prompt.ask(
            "[bold]Seleccione una opción[/bold]",
            choices=["1", "2", "3", "4", "5", "6"],
        )

        if opcion == "1":
            # Prestar libro
            console.print("\n[bold cyan]═══ Prestar Libro ═══[/bold cyan]")
            libro_id = Prompt.ask("Ingrese el ID del libro")
            nombre = Prompt.ask("Ingrese el nombre del aprendiz")
            prestar_libro(libros, libro_id, nombre)

        elif opcion == "2":
            # Devolver libro
            console.print("\n[bold cyan]═══ Devolver Libro ═══[/bold cyan]")
            libro_id = Prompt.ask("Ingrese el ID del libro")
            devolver_libro(libros, libro_id)

        elif opcion == "3":
            # Buscar libro
            console.print("\n[bold cyan]═══ Buscar Libro ═══[/bold cyan]")
            query = Prompt.ask("Ingrese el título o autor a buscar")
            buscar_libro(libros, query)

        elif opcion == "4":
            # Ver libros prestados
            console.print("\n")
            ver_libros_prestados(libros)

        elif opcion == "5":
            # Ver todos los libros
            console.print("\n")
            ver_todos_los_libros(libros)

        elif opcion == "6":
            if Confirm.ask("\n¿Está seguro que desea salir?"):
                console.print(
                    "\n[bold green]¡Gracias por usar el sistema de biblioteca![/bold green]\n"
                )
                break

        if opcion != "6":
            Prompt.ask("\n[dim]Presione Enter para continuar[/dim]", default="")


if __name__ == "__main__":
    main()