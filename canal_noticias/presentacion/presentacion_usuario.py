import getpass

from auxiliares.entradas import pedir_texto, pedir_entero, elegir_registro, confirmar
from auxiliares.errores import manejar_errores
from auxiliares.tablas import mostrar_tabla
from negocio.negocio_usuarios import (
    lista_usuarios, buscar_usuario, registrar_usuario, editar_usuario,
    deshabilitar_usuario, iniciar_sesion)
from negocio.negocio_roles import lista_roles


def pedir_login(intentos=3):
    """Pide correo y contraseña. Devuelve el Usuario, o None si se agotan los intentos."""
    for restantes in range(intentos - 1, -1, -1):
        correo = input('Correo: ').strip()
        contrasena = getpass.getpass('Contraseña: ')
        try:
            return iniciar_sesion(correo, contrasena)
        except ValueError as error:
            print(f'{error} Intentos restantes: {restantes}\n')
    return None


def _pedir_usuario():
    id_usuario = pedir_entero('Ingrese el id del usuario: ', minimo=1)
    usuario = buscar_usuario(id_usuario)
    if usuario is None:
        raise ValueError('No existe un usuario con ese id.')
    return usuario


@manejar_errores
def mostrar_usuarios():
    filas = [[u.id, u.nombre, u.correo, u.rol.nombre] for u in lista_usuarios()]
    mostrar_tabla('USUARIOS', ['Id', 'Nombre', 'Correo', 'Rol'], filas, izquierda=['Nombre', 'Correo'])


@manejar_errores
def agregar_usuario():
    nombre = pedir_texto('Ingrese el nombre: ', minimo=3)
    correo = pedir_texto('Ingrese el correo: ')
    contrasena = getpass.getpass('Ingrese la contraseña (mínimo 6 caracteres): ')
    id_rol = elegir_registro('Roles', lista_roles(), lambda r: r.nombre)
    usuario = registrar_usuario(nombre, correo, contrasena, id_rol)
    print(f'Usuario guardado con éxito. Id: {usuario.id}\n')


@manejar_errores
def modificar_usuario():
    mostrar_usuarios()
    usuario = _pedir_usuario()
    nombre = pedir_texto(f'Nombre [{usuario.nombre}] (ENTER para conservar): ', minimo=3, conservar=usuario.nombre)
    correo = pedir_texto(f'Correo [{usuario.correo}] (ENTER para conservar): ', conservar=usuario.correo)
    id_rol = elegir_registro('Roles', lista_roles(), lambda r: r.nombre, conservar=usuario.rol_id,
                             mensaje=f'Id del rol [{usuario.rol.nombre}] (ENTER para conservar): ')
    nueva = getpass.getpass('Nueva contraseña (ENTER para conservar la actual): ')
    editar_usuario(usuario, nombre, correo, id_rol, nueva or None)
    print('Usuario actualizado con éxito.\n')


@manejar_errores
def eliminar_usuario():
    mostrar_usuarios()
    usuario = _pedir_usuario()
    if confirmar(f'¿Eliminar al usuario "{usuario.nombre}"?'):
        deshabilitar_usuario(usuario)
        print('Usuario eliminado con éxito.\n')
    else:
        print('Operación cancelada.\n')
