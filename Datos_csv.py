"""
Analizador de archivos CSV - Estadísticas de columnas numéricas
Calcula promedio, máximo y mínimo de columnas especificadas
"""

import csv
import os

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def analizar_csv(nombre_archivo: str, columna: str) -> dict:
    """
    Lee un archivo CSV y calcula estadísticas de una columna numérica.

    Args:
        nombre_archivo (str): Ruta del archivo CSV.
        columna (str): Nombre de la columna a analizar.

    Returns:
        dict: Diccionario con promedio, máximo, mínimo y total de registros.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si la columna no existe o no contiene valores numéricos.
    """

    if not os.path.exists(nombre_archivo):
        raise FileNotFoundError(f"El archivo '{nombre_archivo}' no existe.")

    valores = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        if lector.fieldnames is None:
            raise ValueError(
                f"El archivo '{nombre_archivo}"
                f"' está vacío o mal formado (no tiene encabezados)."
            )

        if columna not in lector.fieldnames:
            raise ValueError(
                f"La columna '{columna}' no existe. "
                f"Columnas disponibles: {', '.join(lector.fieldnames)}"
            )

        for fila in lector:
            valor_celda = fila.get(columna, None)
            try:
                valor = float(valor_celda)
                valores.append(valor)
            except (ValueError, TypeError):
                console.print(
                    f"[yellow]⚠ Advertencia: Valor no numérico ignorado: '"
                    f"{valor_celda}'[/yellow]"
                )

    if not valores:
        raise ValueError(
            f"No se encontraron valores numéricos en la columna '{columna}'"
        )

    promedio = sum(valores) / len(valores)
    maximo = max(valores)
    minimo = min(valores)

    return {
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo,
        "total_registros": len(valores),
    }


def mostrar_resultados(resultados: dict, columna: str, archivo: str) -> None:
    """
    Muestra los resultados del análisis en una tabla formateada con Rich.
    """
    tabla = Table(
        title=f" Análisis de la columna: [cyan]{columna}[/cyan]",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
    )

    tabla.add_column("Estadística", style="cyan bold", width=20)
    tabla.add_column("Valor", style="green", justify="right", width=15)

    tabla.add_row("Promedio", f"{resultados['promedio']:.2f}")
    tabla.add_row("Máximo", f"{resultados['maximo']:.2f}")
    tabla.add_row("Mínimo", f"{resultados['minimo']:.2f}")
    tabla.add_row("Total registros", str(resultados["total_registros"]))

    console.print()
    console.print(tabla)
    console.print(f"\n[dim]Archivo analizado: {archivo}[/dim]")


def mostrar_datos_csv(nombre_archivo: str) -> None:
    """
    Muestra todos los datos del archivo CSV en una tabla.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            filas = list(lector)

            if not filas:
                console.print("[yellow]El archivo está vacío[/yellow]")
                return

            tabla = Table(
                title=f" Datos de: {nombre_archivo}",
                box=box.SIMPLE,
                show_header=True,
                header_style="bold cyan",
            )

            for columna in lector.fieldnames:
                tabla.add_column(columna, style="white")

            for fila in filas:
                tabla.add_row(*[fila[col] for col in lector.fieldnames])

            console.print()
            console.print(tabla)

    except Exception as e:
        console.print(f"[bold red]✗ Error al mostrar datos: {e}[/bold red]")


def crear_csv_ejemplo() -> None:
    """
    Crea un archivo CSV de ejemplo con datos de estudiantes.
    """
    nombre_archivo = "estudiantes.csv"
    datos = [
        {"nombre": "Ana García", "edad": "20", "calificacion": "8.5"},
        {"nombre": "Carlos López", "edad": "22", "calificacion": "7.8"},
        {"nombre": "María Rodríguez", "edad": "19", "calificacion": "9.2"},
        {"nombre": "Juan Martínez", "edad": "21", "calificacion": "6.5"},
        {"nombre": "Laura Sánchez", "edad": "20", "calificacion": "8.9"},
        {"nombre": "Pedro Gómez", "edad": "23", "calificacion": "7.3"},
        {"nombre": "Sofía Torres", "edad": "19", "calificacion": "9.5"},
        {"nombre": "Diego Ramírez", "edad": "22", "calificacion": "8.1"},
        {"nombre": "Valentina Cruz", "edad": "21", "calificacion": "8.7"},
        {"nombre": "Andrés Morales", "edad": "20", "calificacion": "7.9"},
    ]

    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "edad", "calificacion"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(datos)

        console.print(
            f"[green]✓ Archivo '{nombre_archivo}' creado exitosamente[/green]"
        )

    except Exception as e:
        console.print(f"[bold red]✗ Error al crear archivo: {e}[/bold red]")


def main() -> None:
    """
    Función principal que demuestra el uso del analizador de CSV.
    """
    console.clear()

    titulo = Panel(
        "[bold cyan]Analizador de Archivos CSV[/bold cyan]\n"
        "[dim]Calcula estadísticas de columnas numéricas[/dim]",
        border_style="cyan",
        box=box.DOUBLE,
    )
    console.print(titulo)
    console.print()

    archivo = "estudiantes.csv"
    if not os.path.exists(archivo):
        console.print(
            "[yellow]⚠ No se encontró el archivo de ejemplo. Creando...[/yellow]\n"
        )
        crear_csv_ejemplo()
        console.print()

    console.print("[bold]Datos del archivo:[/bold]")
    mostrar_datos_csv(archivo)
    console.print()

    columnas_a_analizar = ["calificacion", "edad"]

    for columna in columnas_a_analizar:
        try:
            console.print(
                f"\n[bold magenta]→ Analizando columna: {columna}[/bold magenta]"
            )
            resultados = analizar_csv(archivo, columna)
            mostrar_resultados(resultados, columna, archivo)

        except Exception as e:
            console.print(
                f"[bold red]✗ No se pudo analizar '{columna}': {e}[/bold red]"
            )

    console.print("\n" + "=" * 70)
    console.print("[bold yellow]Ejemplo de manejo de errores:[/bold yellow]\n")

    try:
        analizar_csv(archivo, "columna_inexistente")
    except ValueError as e:
        console.print(f"[red]✗ Error capturado: {e}[/red]")

    console.print("\n" + "=" * 70)
    console.print("\n[bold green]✓ Análisis completado[/bold green]\n")

    conceptos = Panel(
        """[cyan]✓ Módulo csv (DictReader, DictWriter)[/cyan]
[cyan]✓ Conversión de tipos (str → float)[/cyan]
[cyan]✓ Manejo de archivos (with open)[/cyan]
[cyan]✓ Funciones con type hints[/cyan]
[cyan]✓ Manejo de excepciones[/cyan]
[cyan]✓ Rich para visualización[/cyan]""",
        title="[bold] Conceptos Aplicados[/bold]",
        border_style="green",
    )
    console.print(conceptos)


if __name__ == "__main__":
    main()
