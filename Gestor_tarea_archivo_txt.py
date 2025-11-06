"""
Gestor de Tareas - Aplicación de Consola
Permite agregar, ver, eliminar y marcar tareas como completadas
"""

import os

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

# Inicializar consola de Rich
console = Console()

# Nombre del archivo donde se guardan las tareas
ARCHIVO_TAREAS = "tareas.txt"


def agregar_tarea(tarea: str) -> None:
    """
    Añade una nueva tarea al final del archivo.

    Args:
        tarea: Texto de la tarea a agregar
    """
    try:
        with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
            # Agregar la tarea con un salto de línea
            archivo.write(f"[ ] {tarea}\n")
        console.print("✓ Tarea agregada exitosamente", style="bold green")
    except Exception as e:
        console.print(f"✗ Error al agregar tarea: {e}", style="bold red")


def ver_tareas() -> list[str]:
    """
    Lee todas las tareas del archivo y las devuelve como una lista.

    Returns:
        Lista de tareas (strings)
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(ARCHIVO_TAREAS):
            return []

        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            # Leer todas las líneas y eliminar espacios en blanco
            tareas = [linea.strip() for linea in archivo.readlines()]
            # Filtrar líneas vacías
            return [tarea for tarea in tareas if tarea]
    except Exception as e:
        console.print(f"✗ Error al leer tareas: {e}", style="bold red")
        return []


def mostrar_tareas() -> None:
    """
    Muestra todas las tareas en una tabla formateada con Rich.
    """
    tareas = ver_tareas()

    if not tareas:
        console.print(
            Panel(
                "[yellow]No hay tareas registradas[/yellow]",
                title="📋 Lista de Tareas",
                border_style="yellow",
            )
        )
        return

    tabla = Table(
        title="📋 Lista de Tareas",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
    )

    tabla.add_column("#", style="dim", width=6, justify="center")
    tabla.add_column("Estado", width=10, justify="center")
    tabla.add_column("Tarea", style="white")

    for i, tarea in enumerate(tareas, 1):
        # Determinar si está completada
        if tarea.startswith("[X]") or tarea.startswith("[x]"):
            estado = "[green]✓ Completada[/green]"
            estilo_tarea = "dim strike"
        else:
            estado = "[yellow]○ Pendiente[/yellow]"
            estilo_tarea = "white"

        # Extraer el texto de la tarea (sin el [ ] o [X])
        texto_tarea = tarea[3:].strip()

        tabla.add_row(str(i), estado, f"[{estilo_tarea}]{texto_tarea}[/{estilo_tarea}]")

    console.print(tabla)
    console.print(f"\n[dim]Total de tareas: {len(tareas)}[/dim]")


def eliminar_tarea(numero: int) -> None:
    """
    Elimina una tarea específica por su número.

    Args:
        numero: Número de la tarea a eliminar (1-indexed)
    """
    tareas = ver_tareas()

    if not tareas:
        console.print("✗ No hay tareas para eliminar", style="bold red")
        return

    if numero < 1 or numero > len(tareas):
        console.print(
            f"✗ Número de tarea inválido. Debe ser entre 1 y {len(tareas)}",
            style="bold red",
        )
        return

    try:
        # Eliminar la tarea de la lista
        tarea_eliminada = tareas.pop(numero - 1)

        # Reescribir el archivo con las tareas restantes
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            for tarea in tareas:
                archivo.write(f"{tarea}\n")

        console.print(
            f"✓ Tarea eliminada: {tarea_eliminada[3:].strip()}", style="bold green"
        )
    except Exception as e:
        console.print(f"✗ Error al eliminar tarea: {e}", style="bold red")


def marcar_completada(numero: int) -> None:
    """
    Marca una tarea como completada.

    Args:
        numero: Número de la tarea a marcar (1-indexed)
    """
    tareas = ver_tareas()

    if not tareas:
        console.print("✗ No hay tareas para marcar", style="bold red")
        return

    if numero < 1 or numero > len(tareas):
        console.print(
            f"✗ Número de tarea inválido. Debe ser entre 1 y {len(tareas)}",
            style="bold red",
        )
        return

    try:
        # Cambiar [ ] por [X]
        tarea_actual = tareas[numero - 1]
        if tarea_actual.startswith("[ ]"):
            tareas[numero - 1] = tarea_actual.replace("[ ]", "[X]", 1)

            # Reescribir el archivo
            with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
                for tarea in tareas:
                    archivo.write(f"{tarea}\n")

            console.print("✓ Tarea marcada como completada", style="bold green")
        else:
            console.print("⚠ La tarea ya está completada", style="bold yellow")
    except Exception as e:
        console.print(f"✗ Error al marcar tarea: {e}", style="bold red")


def limpiar_completadas() -> None:
    """
    Elimina todas las tareas marcadas como completadas.
    """
    tareas = ver_tareas()
    tareas_pendientes = [
        t for t in tareas if not (t.startswith("[X]") or t.startswith("[x]"))
    ]

    cantidad_eliminadas = len(tareas) - len(tareas_pendientes)

    if cantidad_eliminadas == 0:
        console.print("⚠ No hay tareas completadas para limpiar", style="bold yellow")
        return

    try:
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            for tarea in tareas_pendientes:
                archivo.write(f"{tarea}\n")

        console.print(
            f"✓ Se eliminaron {cantidad_eliminadas} tarea(s) completada(s)",
            style="bold green",
        )
    except Exception as e:
        console.print(f"✗ Error al limpiar tareas: {e}", style="bold red")


def mostrar_menu() -> None:
    """
    Muestra el menú principal con opciones disponibles.
    """
    menu = Panel(
        """[cyan bold]1.[/cyan bold] Agregar tarea
[cyan bold]2.[/cyan bold] Ver todas las tareas
[cyan bold]3.[/cyan bold] Marcar tarea como completada
[cyan bold]4.[/cyan bold] Eliminar tarea
[cyan bold]5.[/cyan bold] Limpiar tareas completadas
[cyan bold]6.[/cyan bold] Salir""",
        title="[bold magenta]📝 GESTOR DE TAREAS[/bold magenta]",
        border_style="magenta",
        box=box.DOUBLE,
    )
    console.print(menu)


def main() -> None:
    """
    Función principal que gestiona el menú y las llamadas a funciones.
    """
    console.clear()
    console.print("[bold green]¡Bienvenido al Gestor de Tareas![/bold green]\n")

    while True:
        mostrar_menu()

        opcion = Prompt.ask(
            "\n[bold cyan]Selecciona una opción[/bold cyan]",
            choices=["1", "2", "3", "4", "5", "6"],
            default="2",
        )

        console.print()  # Línea en blanco

        if opcion == "1":
            tarea = Prompt.ask("[bold]Ingresa la nueva tarea[/bold]")
            if tarea.strip():
                agregar_tarea(tarea.strip())
            else:
                console.print("✗ La tarea no puede estar vacía", style="bold red")

        elif opcion == "2":
            mostrar_tareas()

        elif opcion == "3":
            mostrar_tareas()
            try:
                numero = int(Prompt.ask("\n[bold]Número de tarea a marcar[/bold]"))
                marcar_completada(numero)
            except ValueError:
                console.print("✗ Debes ingresar un número válido", style="bold red")

        elif opcion == "4":
            mostrar_tareas()
            try:
                numero = int(Prompt.ask("\n[bold]Número de tarea a eliminar[/bold]"))
                marcar_completada(numero)
                eliminar_tarea(numero)
            except ValueError:
                console.print("✗ Debes ingresar un número válido", style="bold red")

        elif opcion == "5":
            limpiar_completadas()

        elif opcion == "6":
            console.print("\n[bold green]¡Hasta luego! 👋[/bold green]\n")
            break

        # Pausa antes de continuar
        if opcion != "6":
            console.print()
            Prompt.ask("\n[dim]Presiona Enter para continuar[/dim]", default="")
            console.clear()


if __name__ == "__main__":
    main()
