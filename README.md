# Encontrara 
ejercicios resueltos con sus respectivos test 
# nota
cuando vaya a ejecutar los test hacerlo de manera se parada o bn en mi caso me toco ejecutarlos asi 

#  Sistema de Gestión de Biblioteca

Sistema profesional de consola para gestionar préstamos de libros en una biblioteca, desarrollado con las mejores prácticas de Python.

## ✨ Características

- **Préstamo de libros**: Asignar libros a aprendices
- **Devolución de libros**: Marcar libros como disponibles
- **Búsqueda avanzada**: Buscar por título o autor
- **Visualización de prestados**: Ver todos los libros prestados actualmente
- **Catálogo completo**: Consultar todos los libros disponibles
- **Persistencia en JSON**: Los datos se guardan automáticamente
- **Interfaz atractiva**: Tablas y menús coloridos con Rich

## 🛠️ Tecnologías y Herramientas

- **Python 3.10+**: Lenguaje de programación
- **Rich**: Interfaz de consola elegante
- **uv**: Gestor de paquetes rápido
- **Ruff**: Linter y formateador
- **pytest**: Framework de testing
- **Type Hints**: Tipado estático para mejor calidad

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

## 🧪 Testing

```bash

pytest


pytest --cov


```

## 🔍 Linting y Formateo

```bash

ruff check .


ruff format .


ruff check --fix .
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

## 🤝 Contribución

1. Asegúrate de que todos los tests pasen: `pytest`
2. Verifica el código con Ruff: `ruff check .`
3. Formatea el código: `ruff format .`
4. Agrega tests para nuevas funcionalidades

##  Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

##  Autor

David Leonardo Pedraza Bello.