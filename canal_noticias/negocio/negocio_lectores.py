from datos.modelos.lector import Lector
from datos.repositorios.repo_lector import (
    listado_lectores, obtener_lector, obtener_lector_correo, guardar_lector,
    contar_suscripciones_activas_lector)


def _validar(nombre, correo):
    nombre = nombre.strip()
    correo = correo.strip().lower()
    if len(nombre) < 3:
        raise ValueError('El nombre debe tener al menos 3 caracteres.')
    if '@' not in correo or '.' not in correo.split('@')[-1]:
        raise ValueError('El correo no tiene un formato válido.')
    return nombre, correo


def lista_lectores():
    return list(listado_lectores())


def buscar_lector(id_lector):
    return obtener_lector(id_lector)


def registrar_lector(nombre, correo):
    nombre, correo = _validar(nombre, correo)
    existente = obtener_lector_correo(correo)
    if existente is not None and existente.habilitado == 1:
        raise ValueError(f'Ya existe un lector con el correo {correo}.')
    lector = existente if existente is not None else Lector()  # reactiva si estaba eliminado
    lector.nombre = nombre
    lector.correo = correo
    lector.habilitado = 1
    return guardar_lector(lector)


def editar_lector(lector: Lector, nombre, correo):
    nombre, correo = _validar(nombre, correo)
    otro = obtener_lector_correo(correo)
    if otro is not None and otro.id != lector.id:
        raise ValueError(f'El correo {correo} ya está en uso.')
    lector.nombre = nombre
    lector.correo = correo
    return guardar_lector(lector)


def deshabilitar_lector(lector: Lector):
    if contar_suscripciones_activas_lector(lector.id) > 0:
        raise ValueError('No se puede eliminar: el lector tiene una suscripción activa. Cancélela primero.')
    lector.habilitado = 0
    guardar_lector(lector)
