from datos.modelos.rol import Rol
from datos.modelos.usuario import Usuario


def listado_roles():
    return Rol.select().where(Rol.habilitado == 1).order_by(Rol.nombre)


def obtener_rol(id_rol):
    return Rol.get_or_none((Rol.id == id_rol) & (Rol.habilitado == 1))


def obtener_rol_nombre(nombre):
    return Rol.get_or_none(Rol.nombre == nombre)


def guardar_rol(rol: Rol):
    rol.save()
    return rol


def contar_usuarios_rol(id_rol):
    return Usuario.select().where((Usuario.rol == id_rol) & (Usuario.habilitado == 1)).count()
