from datos.repositorios.repo_usuario import listado_usuarios
from datos.repositorios.repo_autor import listado_autores
from datos.repositorios.repo_lector import listado_lectores


def directorio_personas():
    """POLIMORFISMO: usuarios, autores y lectores en una sola lista.

    Cada objeto responde .descripcion() a su manera (ver los modelos).
    """
    personas = []
    personas.extend(listado_usuarios())
    personas.extend(listado_autores())
    personas.extend(listado_lectores())
    return personas
