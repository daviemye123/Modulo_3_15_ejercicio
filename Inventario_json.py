import json
import os

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import FloatPrompt, IntPrompt, Prompt
from rich.table import Table

console = Console()


def cargar_inventario(archivo="inventario.json"):
    """
    Carga el inventario desde un archivo JSON.
    Si no existe, retorna una lista vacía.
    """
    if os.path.exists(archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                inventario = json.load(f)
            console.print(
                f"[green]✓[/green] Inventario cargado: {len(inventario)} productos",
                style="dim",
            )
            return inventario
        except json.JSONDecodeError:
            console.print(
                "[yellow]⚠[/yellow] Archivo corrupto. Creando nuevo inventario.",
                style="dim",
            )
            return []
    else:
        console.print(
            "[yellow]⚠[/yellow] Archivo no encontrado. Creando nuevo inventario.",
            style="dim",
        )
        return []


def guardar_inventario(inventario, archivo="inventario.json"):
    """
    Guarda el inventario en un archivo JSON con formato legible.
    """
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(inventario, f, indent=4, ensure_ascii=False)
        console.print("[green]✓[/green] Inventario guardado exitosamente", style="dim")
        return True
    except Exception as e:
        console.print(f"[red]✗[/red] Error al guardar: {e}", style="bold red")
        return False


def agregar_producto(inventario):
    """
    Agrega un nuevo producto al inventario.
    """
    console.print("\n[bold cyan]➕ AGREGAR PRODUCTO[/bold cyan]")

    nombre = Prompt.ask("Nombre del producto")
    cantidad = IntPrompt.ask("Cantidad inicial", default=0)
    precio = FloatPrompt.ask("Precio unitario", default=0.0)
    categoria = Prompt.ask("Categoría", default="General")

    if inventario:
        nuevo_id = max(p.get("id", 0) for p in inventario) + 1
    else:
        nuevo_id = 1

    producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "categoria": categoria,
    }

    inventario.append(producto)
    guardar_inventario(inventario)

    console.print(
        f"\n[green]✓[/green] Producto '{nombre}' agregado con ID: {nuevo_id}",
        style="bold green",
    )
    return inventario


def vender_producto(inventario):
    """
    Realiza una venta disminuyendo el stock de un producto.
    """
    if not inventario:
        console.print(
            "[yellow]⚠[/yellow] No hay productos en el inventario", style="bold yellow"
        )
        return inventario

    console.print("\n[bold magenta] REGISTRAR VENTA[/bold magenta]")
    mostrar_inventario(inventario, resumido=True)

    producto_id = IntPrompt.ask("\nID del producto a vender")

    producto = None
    for p in inventario:
        if p["id"] == producto_id:
            producto = p
            break

    if not producto:
        console.print("[red]✗[/red] Producto no encontrado", style="bold red")
        return inventario

    console.print(f"\nProducto: [cyan]{producto['nombre']}[/cyan]")
    console.print(f"Stock disponible: [yellow]{producto['cantidad']}[/yellow]")

    cantidad_venta = IntPrompt.ask("Cantidad a vender", default=1)

    if cantidad_venta > producto["cantidad"]:
        console.print("[red]✗[/red] Stock insuficiente", style="bold red")
        return inventario

    producto["cantidad"] -= cantidad_venta
    total = cantidad_venta * producto["precio"]

    guardar_inventario(inventario)

    console.print("\n[green]✓[/green] Venta registrada:", style="bold green")
    console.print(f"  • Cantidad: {cantidad_venta} unidades")
    console.print(f"  • Total: ${total:,.2f}")
    console.print(f"  • Stock restante: {producto['cantidad']}")

    return inventario


def mostrar_inventario(inventario, resumido=False):
    """
    Muestra el inventario en una tabla formateada con Rich.
    """
    if not inventario:
        console.print("\n[yellow] El inventario está vacío[/yellow]", style="bold")
        return

    tabla = Table(
        title=" INVENTARIO DE PRODUCTOS",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
        title_style="bold white on blue",
    )

    tabla.add_column("ID", justify="center", style="dim")
    tabla.add_column("Producto", style="cyan")
    if not resumido:
        tabla.add_column("Categoría", style="magenta")
    tabla.add_column("Stock", justify="right", style="yellow")
    tabla.add_column("Precio", justify="right", style="green")
    if not resumido:
        tabla.add_column("Valor Total", justify="right", style="bold green")

    total_productos = 0
    valor_total = 0

    for p in inventario:
        valor_producto = p["cantidad"] * p["precio"]
        total_productos += p["cantidad"]
        valor_total += valor_producto
        cantidades=10

        stock_style = "bold red" if p["cantidad"] < cantidades else "yellow"

        if resumido:
            tabla.add_row(
                str(p["id"]),
                p["nombre"],
                f"[{stock_style}]{p['cantidad']}[/{stock_style}]",
                f"${p['precio']:,.2f}",
            )
        else:
            tabla.add_row(
                str(p["id"]),
                p["nombre"],
                p["categoria"],
                f"[{stock_style}]{p['cantidad']}[/{stock_style}]",
                f"${p['precio']:,.2f}",
                f"${valor_producto:,.2f}",
            )

    console.print()
    console.print(tabla)

    if not resumido:
        resumen = f"[bold]Total productos:[/bold] {len(inventario)} | "
        resumen += f"[bold]Unidades totales:[/bold] {total_productos} | "
        resumen += f"[bold]Valor inventario:[/bold] ${valor_total:,.2f}"

        console.print(Panel(resumen, style="cyan", box=box.ROUNDED))


def buscar_producto(inventario):
    """
    Busca productos por nombre o categoría.
    """
    console.print("\n[bold yellow] BUSCAR PRODUCTO[/bold yellow]")
    termino = Prompt.ask("Término de búsqueda (nombre o categoría)").lower()

    resultados = [
        p
        for p in inventario
        if termino in p["nombre"].lower() or termino in p["categoria"].lower()
    ]

    if resultados:
        console.print(f"\n[green]Se encontraron {len(resultados)} resultado(s)[/green]")
        mostrar_inventario(resultados)
    else:
        console.print("[yellow]No se encontraron resultados[/yellow]")


def editar_producto(inventario):
    """
    Permite editar los datos de un producto existente.
    """
    if not inventario:
        console.print(
            "[yellow]⚠[/yellow] No hay productos en el inventario", style="bold yellow"
        )
        return inventario

    console.print("\n[bold blue]✏️  EDITAR PRODUCTO[/bold blue]")
    mostrar_inventario(inventario, resumido=True)

    producto_id = IntPrompt.ask("\nID del producto a editar")

    producto = None
    for p in inventario:
        if p["id"] == producto_id:
            producto = p
            break

    if not producto:
        console.print("[red]✗[/red] Producto no encontrado", style="bold red")
        return inventario

    console.print(f"\n[cyan]Editando: {producto['nombre']}[/cyan]")
    console.print("[dim](Presiona Enter para mantener el valor actual)[/dim]\n")

    nuevo_nombre = Prompt.ask("Nombre", default=producto["nombre"])
    nueva_cantidad = IntPrompt.ask("Cantidad", default=producto["cantidad"])
    nuevo_precio = FloatPrompt.ask("Precio", default=producto["precio"])
    nueva_categoria = Prompt.ask("Categoría", default=producto["categoria"])

    producto["nombre"] = nuevo_nombre
    producto["cantidad"] = nueva_cantidad
    producto["precio"] = nuevo_precio
    producto["categoria"] = nueva_categoria

    guardar_inventario(inventario)
    console.print(
        "[green]✓[/green] Producto actualizado exitosamente", style="bold green"
    )

    return inventario


def mostrar_menu():
    """
    Muestra el menú principal con Rich.
    """
    menu = """
[bold cyan]1.[/bold cyan] Agregar producto
[bold magenta]2.[/bold magenta] Vender producto
[bold yellow]3.[/bold yellow] Mostrar inventario
[bold blue]4.[/bold blue] Buscar producto
[bold green]5.[/bold green] Editar producto
[bold red]6.[/bold red] Salir
    """
    console.print(
        Panel(
            menu,
            title="[bold white]MENÚ PRINCIPAL[/bold white]",
            border_style="cyan",
            box=box.DOUBLE,
        )
    )


def main():
    """
    Función principal del programa.
    """
    console.clear()
    console.print(
        Panel.fit(
            "[bold white] SISTEMA DE INVENTARIO [/bold white]\n"
            "[dim]Con persistencia JSON y Rich[/dim]",
            border_style="cyan",
            box=box.DOUBLE,
        )
    )

    inventario = cargar_inventario()

    while True:
        mostrar_menu()
        opcion = Prompt.ask(
            "\n[bold]Selecciona una opción[/bold]",
            choices=["1", "2", "3", "4", "5", "6"],
        )

        if opcion == "1":
            inventario = agregar_producto(inventario)
        elif opcion == "2":
            inventario = vender_producto(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            buscar_producto(inventario)
        elif opcion == "5":
            inventario = editar_producto(inventario)
        elif opcion == "6":
            console.print("\n[bold green] by [/bold green]\n")
            break

        if opcion != "6":
            Prompt.ask("\n[dim]Presiona Enter para continuar[/dim]", default="")
            console.clear()


if __name__ == "__main__":
    main()
