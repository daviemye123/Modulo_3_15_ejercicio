import csv
import json
from typing import Dict, List

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def leer_csv(archivo: str) -> List[Dict]:
    """
    Lee un archivo CSV y retorna una lista de diccionarios.

    Args:
        archivo: Ruta del archivo CSV a leer

    Returns:
        Lista de diccionarios con los datos de estudiantes
    """
    estudiantes = []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                estudiantes.append(row)
        console.print(
            f"[green]✓[/green] Archivo CSV leído exitosamente: {len(estudiantes)} "
            f"estudiantes cargados"
        )
    except FileNotFoundError:
        console.print(f"[red]✗[/red] Error: No se encontró el archivo {archivo}")
    except Exception as e:
        console.print(f"[red]✗[/red] Error al leer CSV: {str(e)}")

    return estudiantes


def leer_json(archivo: str) -> List[Dict]:
    """
    Lee un archivo JSON y retorna una lista de diccionarios.

    Args:
        archivo: Ruta del archivo JSON a leer

    Returns:
        Lista de diccionarios con los datos de cursos
    """
    cursos = []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            cursos = json.load(f)
        console.print(
            f"[green]✓[/green] Archivo JSON leído exitosamente: {len(cursos)} "
            f"cursos cargados"
        )
    except FileNotFoundError:
        console.print(f"[red]✗[/red] Error: No se encontró el archivo {archivo}")
    except json.JSONDecodeError as e:
        console.print(f"[red]✗[/red] Error al decodificar JSON: {str(e)}")
    except Exception as e:
        console.print(f"[red]✗[/red] Error al leer JSON: {str(e)}")

    return cursos


def combinar_datos(estudiantes: List[Dict], cursos: List[Dict]) -> Dict[str, Dict]:
    """
    Combina la información de estudiantes y cursos.

    Args:
        estudiantes: Lista de diccionarios con información de estudiantes
        cursos: Lista de diccionarios con información de cursos

    Returns:
        Diccionario con estudiantes y sus cursos asociados
    """
    # Crear un diccionario de cursos por ID para búsqueda rápida
    cursos_dict = {curso["id"]: curso for curso in cursos}

    # Diccionario para almacenar resultado
    reporte_datos = {}

    for estudiante in estudiantes:
        est_id = estudiante["id"]
        est_nombre = estudiante["nombre"]


        cursos_ids = estudiante.get("cursos", "").split(",")
        cursos_ids = [c.strip() for c in cursos_ids if c.strip()]

        # Buscar información de cada curso
        cursos_estudiante = []
        for curso_id in cursos_ids:
            if curso_id in cursos_dict:
                cursos_estudiante.append(cursos_dict[curso_id])

        reporte_datos[est_id] = {
            "nombre": est_nombre,
            "email": estudiante.get("email", "N/A"),
            "cursos": cursos_estudiante,
        }

    console.print("[green]✓[/green] Datos combinados exitosamente")
    return reporte_datos


def mostrar_reporte_rich(reporte_datos: Dict[str, Dict]) -> str:
    """
    Muestra el reporte en consola usando Rich y genera el texto para guardar.

    Args:
        reporte_datos: Diccionario con los datos combinados

    Returns:
        String con el contenido del reporte en formato texto plano
    """
    console.print("\n")
    console.print(
        Panel.fit(
            "[bold cyan]REPORTE DE ESTUDIANTES Y CURSOS[/bold cyan]",
            border_style="cyan",
        )
    )
    console.print("\n")

    # Texto plano para guardar en archivo
    texto_reporte = "=" * 70 + "\n"
    texto_reporte += "REPORTE DE ESTUDIANTES Y CURSOS\n"
    texto_reporte += "=" * 70 + "\n\n"

    for est_id, datos in reporte_datos.items():
        # Mostrar en consola con Rich
        table = Table(
            title=f"[bold]{datos['nombre']}[/bold] (ID: {est_id})",
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
        )

        table.add_column("Curso", style="cyan", width=30)
        table.add_column("Instructor", style="green", width=20)
        table.add_column("Créditos", justify="center", style="yellow", width=10)

        # Agregar al texto plano
        texto_reporte += f"Estudiante: {datos['nombre']}\n"
        texto_reporte += f"ID: {est_id}\n"
        texto_reporte += f"Email: {datos['email']}\n"
        texto_reporte += "-" * 70 + "\n"

        if datos["cursos"]:
            for curso in datos["cursos"]:
                table.add_row(
                    curso.get("nombre", "N/A"),
                    curso.get("instructor", "N/A"),
                    str(curso.get("creditos", "N/A")),
                )

                texto_reporte += f"  • {curso.get('nombre', 'N/A')}\n"
                texto_reporte += f"    Instructor: {curso.get('instructor', 'N/A')}\n"
                texto_reporte += f"    Créditos: {curso.get('creditos', 'N/A')}\n"
        else:
            table.add_row("[dim]Sin cursos asignados[/dim]", "", "")
            texto_reporte += "  Sin cursos asignados\n"

        console.print(table)
        console.print("\n")
        texto_reporte += "\n"

    # Resumen
    total_estudiantes = len(reporte_datos)
    total_cursos = sum(len(datos["cursos"]) for datos in reporte_datos.values())

    resumen = f"[bold green]Total de estudiantes:[/bold green] {total_estudiantes}\n"
    resumen += f"[bold green]Total de inscripciones:[/bold green] {total_cursos}"
    console.print(Panel(resumen, title="[bold]Resumen[/bold]", border_style="green"))

    texto_reporte += "=" * 70 + "\n"
    texto_reporte += f"Total de estudiantes: {total_estudiantes}\n"
    texto_reporte += f"Total de inscripciones: {total_cursos}\n"
    texto_reporte += "=" * 70 + "\n"

    return texto_reporte


def generar_reporte(estudiantes: List[Dict], cursos: List[Dict], archivo_salida: str):
    """
    Genera el reporte final combinando estudiantes y cursos.

    Args:
        estudiantes: Lista de estudiantes
        cursos: Lista de cursos
        archivo_salida: Nombre del archivo donde se guardará el reporte
    """
    if not estudiantes or not cursos:
        console.print(
            "[yellow]⚠[/yellow] No hay datos suficientes para generar el reporte"
        )
        return

    # Combinar datos
    reporte_datos = combinar_datos(estudiantes, cursos)

    # Mostrar en consola con Rich y obtener texto plano
    texto_reporte = mostrar_reporte_rich(reporte_datos)

    # Guardar en archivo
    try:
        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(texto_reporte)
        console.print(
            f"\n[green]✓[/green] Reporte guardado exitosamente en: [bold]{archivo_salida}[/bold]"
        )
    except Exception as e:
        console.print(f"[red]✗[/red] Error al guardar el reporte: {str(e)}")


def main():
    """Función principal que ejecuta el proceso completo."""
    console.print(
        "\n[bold blue]═══════════════════════════════════════════════════════[/bold blue]"
    )
    console.print(
        "[bold blue]    SISTEMA DE REPORTES - ESTUDIANTES Y CURSOS[/bold blue]"
    )
    console.print(
        "[bold blue]═══════════════════════════════════════════════════════[/bold blue]\n"
    )

    # Archivos de entrada y salida
    archivo_csv = "estudiantes.csv"
    archivo_json = "cursos.json"
    archivo_reporte = "reporte.txt"

    console.print("[bold]Paso 1:[/bold] Leyendo datos de estudiantes...")
    estudiantes = leer_csv(archivo_csv)

    console.print("\n[bold]Paso 2:[/bold] Leyendo datos de cursos...")
    cursos = leer_json(archivo_json)

    console.print("\n[bold]Paso 3:[/bold] Generando reporte...")
    generar_reporte(estudiantes, cursos, archivo_reporte)

    console.print("\n[bold green]¡Proceso completado![/bold green]\n")


if __name__ == "__main__":
    main()
