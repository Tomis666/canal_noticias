from datos.modelos.usuario import Usuario
from datos.repositorios.repo_usuario import (
    listado_usuarios, obtener_usuario, obtener_usuario_correo, guardar_usuario)
from datos.repositorios.repo_rol import obtener_rol
from datos.repositorios.repo_autor import obtener_autor_de_usuario
from auxiliares.seguridad import hashear_contrasena, verificar_contrasena


def _validar_datos(nombre, correo, id_rol):
    nombre = nombre.strip()
    correo = correo.strip().lower()
    if len(nombre) < 3:
        raise ValueError('El nombre debe tener al menos 3 caracteres.')
    if '@' not in correo or '.' not in correo.split('@')[-1]:
        raise ValueError('El correo no tiene un formato válido.')
    if obtener_rol(id_rol) is None:
        raise ValueError('El rol indicado no existe.')
    return nombre, correo


def _validar_contrasena(contrasena):
    if len(contrasena) < 6:
        raise ValueError('La contraseña debe tener al menos 6 caracteres.')


def lista_usuarios():
    return list(listado_usuarios())


def buscar_usuario(id_usuario):
    return obtener_usuario(id_usuario)


def registrar_usuario(nombre, correo, contrasena, id_rol):
    nombre, correo = _validar_datos(nombre, correo, id_rol)
    _validar_contrasena(contrasena)
    existente = obtener_usuario_correo(correo)
    if existente is not None and existente.habilitado == 1:
        raise ValueError(f'Ya existe un usuario con el correo {correo}.')
    usuario = existente if existente is not None else Usuario()  # reactiva si estaba eliminado
    usuario.nombre = nombre
    usuario.correo = correo
    usuario.contrasena = hashear_contrasena(contrasena)
    usuario.rol = id_rol
    usuario.habilitado = 1
    return guardar_usuario(usuario)


def editar_usuario(usuario: Usuario, nombre, correo, id_rol, contrasena_nueva=None):
    nombre, correo = _validar_datos(nombre, correo, id_rol)
    otro = obtener_usuario_correo(correo)
    if otro is not None and otro.id != usuario.id:
        raise ValueError(f'El correo {correo} ya está en uso.')
    usuario.nombre = nombre
    usuario.correo = correo
    usuario.rol = id_rol
    if contrasena_nueva:
        _validar_contrasena(contrasena_nueva)
        usuario.contrasena = hashear_contrasena(contrasena_nueva)
    return guardar_usuario(usuario)


def deshabilitar_usuario(usuario: Usuario):
    perfil = obtener_autor_de_usuario(usuario.id)
    if perfil is not None and perfil.habilitado == 1:
        raise ValueError('No se puede eliminar: el usuario tiene un perfil de Autor activo. Elimine el autor primero.')
    usuario.habilitado = 0
    guardar_usuario(usuario)


def iniciar_sesion(correo, contrasena):
    """Devuelve el Usuario si las credenciales son correctas; si no, lanza ValueError."""
    usuario = obtener_usuario_correo(correo.strip().lower())
    # Mismo mensaje en todos los casos: no se revela si el correo existe o no.
    if usuario is None or usuario.habilitado != 1 or not verificar_contrasena(contrasena, usuario.contrasena):
        raise ValueError('Correo o contraseña incorrectos.')
    return usuario
