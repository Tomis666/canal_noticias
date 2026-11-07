from datos.modelos.etiqueta import Etiqueta
from datos.repositorios.repo_etiqueta import (
    listado_etiquetas, obtener_etiqueta, obtener_etiqueta_nombre,
    guardar_etiqueta, contar_articulos_etiqueta)


def _validar_nombre(nombre):
    nombre = nombre.strip()
    if len(nombre) < 2:
        raise ValueError('El nombre de la etiqueta debe tener al menos 2 caracteres.')
    return nombre


def lista_etiquetas():
    return list(listado_etiquetas())


def buscar_etiqueta(id_etiqueta):
    return obtener_etiqueta(id_etiqueta)


def registrar_etiqueta(nombre):
    nombre = _validar_nombre(nombre)
    existente = obtener_etiqueta_nombre(nombre)
    if existente is not None:
        if existente.habilitado == 1:
            raise ValueError(f'Ya existe la etiqueta "{nombre}".')
        existente.habilitado = 1
        return guardar_etiqueta(existente)
    etiqueta = Etiqueta()
    etiqueta.nombre = nombre
    return guardar_etiqueta(etiqueta)


def editar_etiqueta(etiqueta: Etiqueta, nombre):
    nombre = _validar_nombre(nombre)
    otra = obtener_etiqueta_nombre(nombre)
    if otra is not None and otra.id != etiqueta.id:
        raise ValueError(f'Ya existe otra etiqueta llamada "{nombre}".')
    etiqueta.nombre = nombre
    return guardar_etiqueta(etiqueta)


def deshabilitar_etiqueta(etiqueta: Etiqueta):
    if contar_articulos_etiqueta(etiqueta.id) > 0:
        raise ValueError('No se puede eliminar: la etiqueta está usada en artículos.')
    etiqueta.habilitado = 0
    guardar_etiqueta(etiqueta)
