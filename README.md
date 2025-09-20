# py_utils

Colección de utilidades Python reutilizables.

## Paquetes implementados

- `logger`: utilidades para logging y mensajes de consola coloreados.
- `data_generator`: utilidad para generar archivos de datos aleatorios.

## API de `logger`

### logger.set_logging(log_file="exercise.log")
Configura el sistema de logging global para mostrar mensajes de nivel INFO o superior y suprime la verbosidad de librerías externas (matplotlib, PIL, tensorflow, torch, sklearn). Guarda los logs en el archivo especificado.

**Parámetros:**
- `log_file` (str): nombre del archivo de log. Por defecto "exercise.log".

### logger.plog(message, level=logging.INFO, eol=False)
Imprime mensajes de log en consola con colores según el nivel de severidad y los registra usando el sistema de logging.

**Parámetros:**
- `message` (str): mensaje a imprimir.
- `level` (int): nivel de severidad (`logging.DEBUG`, `logging.INFO`, `logging.WARNING`, `logging.ERROR`). Por defecto `logging.INFO`.
- `eol` (bool): si es True, añade una línea extra tras el mensaje. Por defecto False.

### logger.clog(name)
Muestra en consola la estructura pública de una clase o instancia, excluyendo atributos y métodos especiales (__dunder__). Ideal para inspección didáctica y depuración estructural.

**Parámetros:**
- name (type or object): clase o instancia a inspeccionar. Por ejemplo, Perceptron.

**Comportamiento:**
- Filtra todos los miembros cuyo nombre comienza con __.
- Imprime cada atributo o método público con indentación y formato tipo árbol (├─, └─).
- Si no se encuentran miembros públicos, muestra un mensaje de error.


## API de `data_generator`

### DataGenerator(file="data")
Objeto generador de base de datos de estudiantes aleatoria. Maneja archivos de salida en formato CSV, JSON & YAML.

> Nota: Al crear una nueva instancia, se invocan todos los métodos de la API. 

**Parámetros:**
- `data` (str): nombre de los archivos de salida. Por defecto "data".
  
### data_generator.set_logging(log_file="data_generator.log")
Configura el sistema de logging global para mostrar mensajes de nivel INFO o superior y suprime la verbosidad de librerías externas (matplotlib, PIL, tensorflow, torch, sklearn). Guarda los logs en el archivo especificado.

**Parámetros:**
- `log_file` (str): nombre del archivo de log. Por defecto "data_generator.log".
  
### data_generator.generate_data()
Genera los archivos de salida en formato CSV, JSON & YAML con la información generada aleatoriamente.

## Uso como submódulo

Puedes añadir este repositorio como submódulo en tu proyecto:

```bash
git submodule add <URL_DEL_REPO> py_utils
```

Luego puedes importar los paquetes desde tu código Python:

```python
from py_utils.logger import set_logging, plog
```

Asegúrate de que el directorio `py_utils` esté en tu `PYTHONPATH` o en la raíz de tu proyecto.

---

**Autor:** Jesús Salvador López Ortega  
[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport)

Actualizado: septiembre 2025

## Change Log

- 2025-09-20: Actualización del paquete `logger` con funcion clog para desplegar estructuras de clases.
- 2025-09-18: Inclusión del paquete `data_generator` para generación de archivos de datos (CSV, JSON & YAML).
- 2025-09-13: Primera versión pública. Incluye el paquete `logger` con funciones de logging y mensajes de consola coloreados.

