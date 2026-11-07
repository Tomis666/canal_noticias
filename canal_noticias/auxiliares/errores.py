import functools

from auxiliares.info_app import mensaje_error


def manejar_errores(funcion):
    """Decorador: es un try/except reutilizable para las funciones de presentación.

    - ValueError  -> errores de validación que lanza la capa de negocio (mensaje claro).
    - Exception   -> cualquier otro fallo (por ejemplo, la base de datos).
    """
    @functools.wraps(funcion)
    def envoltura(*args, **kwargs):
        try:
            return funcion(*args, **kwargs)
        except (EOFError, KeyboardInterrupt):
            raise  # lo captura main.py para salir limpio
        except ValueError as error:
            print(f'\nNo se pudo completar la operación: {error}\n')
        except Exception as error:
            print(f'\n{mensaje_error}{error}\n')
    return envoltura
