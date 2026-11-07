from datos.repositorios.repo_like import obtener_like, crear_like, eliminar_like
from datos.repositorios.repo_lector import obtener_lector
from datos.repositorios.repo_articulo import obtener_articulo


def dar_like(id_lector, id_articulo):
    if obtener_lector(id_lector) is None:
        raise ValueError('El lector indicado no existe.')
    if obtener_articulo(id_articulo) is None:
        raise ValueError('El artículo indicado no existe.')
    if obtener_like(id_lector, id_articulo) is not None:
        raise ValueError('Ese lector ya le dio like a este artículo.')
    return crear_like(id_lector, id_articulo)


def quitar_like(id_lector, id_articulo):
    like = obtener_like(id_lector, id_articulo)
    if like is None:
        raise ValueError('Ese lector no le había dado like a este artículo.')
    eliminar_like(like)
