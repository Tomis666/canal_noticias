from datos.repositorios.repo_comentario import (
    comentarios_de_articulo, obtener_comentario, crear_comentario, guardar_comentario)
from datos.repositorios.repo_lector import obtener_lector
from datos.repositorios.repo_articulo import obtener_articulo


def comentarios_del_articulo(id_articulo):
    return list(comentarios_de_articulo(id_articulo))


def registrar_comentario(id_lector, id_articulo, contenido):
    contenido = contenido.strip()
    if len(contenido) < 3:
        raise ValueError('El comentario debe tener al menos 3 caracteres.')
    if obtener_lector(id_lector) is None:
        raise ValueError('El lector indicado no existe.')
    if obtener_articulo(id_articulo) is None:
        raise ValueError('El artículo indicado no existe.')
    return crear_comentario(id_lector, id_articulo, contenido)


def deshabilitar_comentario(id_comentario):
    comentario = obtener_comentario(id_comentario)
    if comentario is None:
        raise ValueError('No existe un comentario con ese id.')
    comentario.habilitado = 0
    guardar_comentario(comentario)
