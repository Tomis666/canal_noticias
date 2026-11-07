from datos.modelos.autor import Autor
from datos.modelos.usuario import Usuario
from datos.modelos.articulo import Articulo


def _consulta_base():
    return (Autor
            .select(Autor, Usuario)
            .join(Usuario, on=(Autor.usuario == Usuario.id)))


def listado_autores():
    return _consulta_base().where(Autor.habilitado == 1).order_by(Usuario.nombre)


def obtener_autor(id_autor):
    return _consulta_base().where((Autor.id == id_autor) & (Autor.habilitado == 1)).first()


def obtener_autor_de_usuario(id_usuario):
    """Incluye autores deshabilitados (cada usuario tiene como máximo un perfil)."""
    return _consulta_base().where(Autor.usuario == id_usuario).first()


def guardar_autor(autor: Autor):
    autor.save()
    return autor


def contar_articulos_autor(id_autor):
    return Articulo.select().where((Articulo.autor == id_autor) & (Articulo.habilitado == 1)).count()
