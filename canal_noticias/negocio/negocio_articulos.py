from datos.modelos.articulo import Articulo
from datos.repositorios.repo_articulo import (
    listado_articulos, buscar_articulos, obtener_articulo, listado_estados, obtener_estado,
    etiquetas_de_articulo, crear_articulo, guardar_articulo)
from datos.repositorios.repo_autor import obtener_autor
from datos.repositorios.repo_categoria import obtener_categoria
from datos.repositorios.repo_etiqueta import obtener_etiqueta
from datos.repositorios.repo_comentario import contar_comentarios
from datos.repositorios.repo_like import contar_likes


def lista_articulos():
    return list(listado_articulos())


def buscar_por_titulo(texto):
    texto = texto.strip()
    if texto == '':
        raise ValueError('Debe ingresar un texto para buscar.')
    return list(buscar_articulos(texto))


def buscar_articulo(id_articulo):
    return obtener_articulo(id_articulo)


def lista_estados():
    return list(listado_estados())


def etiquetas_del_articulo(id_articulo):
    return list(etiquetas_de_articulo(id_articulo))


def detalle_articulo(id_articulo):
    articulo = obtener_articulo(id_articulo)
    if articulo is None:
        raise ValueError('No existe un artículo con ese id.')
    return {
        'articulo': articulo,
        'etiquetas': etiquetas_del_articulo(articulo.id),
        'likes': contar_likes(articulo.id),
        'comentarios': contar_comentarios(articulo.id),
    }


def _validar(titulo, contenido, id_categoria, id_estado, ids_etiquetas):
    titulo = titulo.strip()
    contenido = contenido.strip()
    if len(titulo) < 5:
        raise ValueError('El titular de la noticia debe tener al menos 5 caracteres.')
    if len(titulo) > 150:
        raise ValueError('El titular no puede superar los 150 caracteres.')
    if contenido == '':
        raise ValueError('El cuerpo de la noticia no puede estar vacío.')
    if obtener_categoria(id_categoria) is None:
        raise ValueError('La categoría indicada no existe.')
    if obtener_estado(id_estado) is None:
        raise ValueError('El estado indicado no existe.')
    for id_etiqueta in ids_etiquetas:
        if obtener_etiqueta(id_etiqueta) is None:
            raise ValueError(f'La etiqueta con id {id_etiqueta} no existe.')
    return titulo, contenido


def registrar_articulo(titulo, contenido, id_autor, id_categoria, id_estado, ids_etiquetas):
    titulo, contenido = _validar(titulo, contenido, id_categoria, id_estado, ids_etiquetas)
    if obtener_autor(id_autor) is None:
        raise ValueError('El autor indicado no existe.')
    return crear_articulo(titulo, contenido, id_autor, id_categoria, id_estado, ids_etiquetas)


def editar_articulo(articulo: Articulo, titulo, contenido, id_categoria, id_estado, ids_etiquetas):
    titulo, contenido = _validar(titulo, contenido, id_categoria, id_estado, ids_etiquetas)
    articulo.titulo = titulo
    articulo.contenido = contenido
    articulo.categoria = id_categoria
    articulo.estado = id_estado
    return guardar_articulo(articulo, ids_etiquetas)


def deshabilitar_articulo(articulo: Articulo):
    articulo.habilitado = 0  # borrado LÓGICO: no se pierde el historial de comentarios y likes
    guardar_articulo(articulo)
