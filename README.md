# Taller 15 ejercicios
ejercicios resueltos con sus respectivos test 
# nota
cuando vaya a ejecutar los test hacerlo de manera se parada o bn en mi caso me toco ejecutarlos asi 

#  Sistema de Gestión de Biblioteca

Sistema profesional de consola para gestionar préstamos de libros en una biblioteca, desarrollado con las mejores prácticas de Python.

##  Características

- **Calcular imc **:Segun peso y altura
- **Generador de pefiles de usuario
- **Contadopr de llamada
- **Validacion de datos genericos 
- **Procesamiento de datos 
- **Filtrado de estudiantes
- **Transformacion de datos con list
- **Sumatoria con reduce 
- **Explorador de datos
- **Gestor tareas com txt
- **Analizador de datos con csv
- **Inventario con json
- **Generador de reportes con archivos multiples
- **Sistema de biblioteca 
- **Préstamo de libros
- **Devolución de libros
- **Búsqueda avanzada
- **Visualización de prestados
- **Catálogo completo
- **Persistencia en JSON
- **Interfaz atractiva

## ️ Tecnologías y Herramientas

- **Python **: Lenguaje de programación
- **Rich**: Interfaz de consola elegante
- **uv**: Gestor de paquetes rápido
- **Ruff**: Linter y formateador
- **pytest**: Framework de testing


## 📦 Instalación

### Con uv (Recomendado)

```bash
uv venv
source .venv/bin/activate  
uv pip install -e ".[dev]"
```

### Con pip 

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -e ".[dev]"
```
### Como ejecutar la aplicación

```bash
python biblioteca.py
```

### Menú principal

1. **Prestar libro**: Ingresa el ID del libro y nombre del aprendiz
2. **Devolver libro**: Ingresa el ID del libro a devolver
3. **Buscar libro**: Busca por título o autor
4. **Ver libros prestados**: Muestra todos los libros actualmente prestados
5. **Ver todos los libros**: Muestra el catálogo completo
6. **Salir**: Cierra la aplicación

##  Testing

```bash

pytest

```

## 🔍 Linting y Formateo

```bash

ruff check .
```


### Docstrings Completos
Todas las funciones y clases incluyen docstrings en formato Google Style.

###  Type Hints
Todo el código usa anotaciones de tipo para mayor seguridad.

###  Tests Exhaustivos
Más de 20 tests unitarios con cobertura superior al 90%.

###  Manejo de Errores
Manejo robusto de excepciones y casos edge.

###  Código Limpio
Cumple con PEP 8 y las mejores prácticas de Python.


### Configuración de Pytest

- Cobertura de código automática
- Tests verbosos por defecto

##  Contribución

1. Asegúrate de que todos los tests pasen: `pytest`
2. Verifica el código con Ruff: `ruff check .`
3. Formatea el código: `ruff format .`
4. Agrega tests para nuevas funcionalidades

##  Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

##  Autor

David Leonardo Pedraza Bello.