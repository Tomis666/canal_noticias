from datos.modelos.categoria import Categoria
from datos.repositorios.repo_categoria import (
    listado_categorias, obtener_categoria, obtener_categoria_nombre,
    guardar_categoria, contar_articulos_categoria)


def _validar_nombre(nombre):
    nombre = nombre.strip()
    if len(nombre) < 3:
        raise ValueError('El nombre de la categoría debe tener al menos 3 caracteres.')
    return nombre


def lista_categorias():
    return list(listado_categorias())


def buscar_categoria(id_categoria):
    return obtener_categoria(id_categoria)


def registrar_categoria(nombre):
    nombre = _validar_nombre(nombre)
    existente = obtener_categoria_nombre(nombre)
    if existente is not None:
        if existente.habilitado == 1:
            raise ValueError(f'Ya existe la categoría "{nombre}".')
        existente.habilitado = 1  # estaba "eliminada": se reactiva
        return guardar_categoria(existente)
    categoria = Categoria()
    categoria.nombre = nombre
    return guardar_categoria(categoria)


def editar_categoria(categoria: Categoria, nombre):
    nombre = _validar_nombre(nombre)
    otra = obtener_categoria_nombre(nombre)
    if otra is not None and otra.id != categoria.id:
        raise ValueError(f'Ya existe otra categoría llamada "{nombre}".')
    categoria.nombre = nombre
    return guardar_categoria(categoria)


def deshabilitar_categoria(categoria: Categoria):
    if contar_articulos_categoria(categoria.id) > 0:
        raise ValueError('No se puede eliminar: la categoría tiene artículos asociados.')
    categoria.habilitado = 0  # borrado LÓGICO: la fila sigue en la base de datos
    guardar_categoria(categoria)
