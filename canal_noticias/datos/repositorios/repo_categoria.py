from datos.modelos.categoria import Categoria
from datos.modelos.articulo import Articulo


def listado_categorias():
    return Categoria.select().where(Categoria.habilitado == 1).order_by(Categoria.nombre)


def obtener_categoria(id_categoria):
    return Categoria.get_or_none((Categoria.id == id_categoria) & (Categoria.habilitado == 1))


def obtener_categoria_nombre(nombre):
    """Busca por nombre incluyendo las deshabilitadas (el nombre es único)."""
    return Categoria.get_or_none(Categoria.nombre == nombre)


def guardar_categoria(categoria: Categoria):
    categoria.save()
    return categoria


def contar_articulos_categoria(id_categoria):
    return (Articulo.select()
            .where((Articulo.categoria == id_categoria) & (Articulo.habilitado == 1))
            .count())
