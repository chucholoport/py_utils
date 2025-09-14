# py_utils

Colección de utilidades Python reutilizables.

## Paquetes implementados

- `logger`: utilidades para logging y mensajes de consola coloreados.

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

- 2025-09-13: Primera versión pública. Incluye el paquete `logger` con funciones de logging y mensajes de consola coloreados.
