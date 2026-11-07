from datos.modelos.autor import Autor
from datos.repositorios.repo_autor import (
    listado_autores, obtener_autor, obtener_autor_de_usuario, guardar_autor, contar_articulos_autor)
from datos.repositorios.repo_usuario import obtener_usuario
from negocio.negocio_usuarios import lista_usuarios


def lista_autores():
    return list(listado_autores())


def buscar_autor(id_autor):
    return obtener_autor(id_autor)


def usuarios_sin_perfil_autor():
    """Usuarios habilitados que todavía no son autores (para elegir al crear uno)."""
    disponibles = []
    for usuario in lista_usuarios():
        perfil = obtener_autor_de_usuario(usuario.id)
        if perfil is None or perfil.habilitado == 0:
            disponibles.append(usuario)
    return disponibles


def registrar_autor(id_usuario, biografia):
    usuario = obtener_usuario(id_usuario)
    if usuario is None:
        raise ValueError('El usuario indicado no existe.')
    existente = obtener_autor_de_usuario(id_usuario)
    if existente is not None and existente.habilitado == 1:
        raise ValueError('Ese usuario ya es autor.')
    autor = existente if existente is not None else Autor()  # reactiva si estaba eliminado
    autor.usuario = id_usuario
    autor.biografia = biografia.strip()
    autor.habilitado = 1
    return guardar_autor(autor)


def editar_autor(autor: Autor, biografia):
    autor.biografia = biografia.strip()
    return guardar_autor(autor)


def deshabilitar_autor(autor: Autor):
    if contar_articulos_autor(autor.id) > 0:
        raise ValueError('No se puede eliminar: el autor tiene artículos publicados.')
    autor.habilitado = 0
    guardar_autor(autor)
