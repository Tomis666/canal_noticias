from datos.modelos.rol import Rol
from datos.repositorios.repo_rol import (
    listado_roles, obtener_rol, obtener_rol_nombre, guardar_rol, contar_usuarios_rol)


def _validar(nombre, permisos):
    nombre = nombre.strip()
    permisos = permisos.strip()
    if len(nombre) < 3:
        raise ValueError('El nombre del rol debe tener al menos 3 caracteres.')
    if permisos == '':
        raise ValueError('Debe indicar los permisos del rol (por ejemplo ALL o LECTURA).')
    return nombre, permisos


def lista_roles():
    return list(listado_roles())


def buscar_rol(id_rol):
    return obtener_rol(id_rol)


def registrar_rol(nombre, permisos):
    nombre, permisos = _validar(nombre, permisos)
    existente = obtener_rol_nombre(nombre)
    if existente is not None:
        if existente.habilitado == 1:
            raise ValueError(f'Ya existe el rol "{nombre}".')
        existente.habilitado = 1
        existente.permisos = permisos
        return guardar_rol(existente)
    rol = Rol()
    rol.nombre = nombre
    rol.permisos = permisos
    return guardar_rol(rol)


def editar_rol(rol: Rol, nombre, permisos):
    nombre, permisos = _validar(nombre, permisos)
    otro = obtener_rol_nombre(nombre)
    if otro is not None and otro.id != rol.id:
        raise ValueError(f'Ya existe otro rol llamado "{nombre}".')
    rol.nombre = nombre
    rol.permisos = permisos
    return guardar_rol(rol)


def deshabilitar_rol(rol: Rol):
    if contar_usuarios_rol(rol.id) > 0:
        raise ValueError('No se puede eliminar: hay usuarios con este rol.')
    rol.habilitado = 0
    guardar_rol(rol)
