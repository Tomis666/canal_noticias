from auxiliares.entradas import pedir_texto, pedir_entero, confirmar
from auxiliares.errores import manejar_errores
from auxiliares.tablas import mostrar_tabla
from negocio.negocio_roles import (
    lista_roles, buscar_rol, registrar_rol, editar_rol, deshabilitar_rol)


def _pedir_rol():
    id_rol = pedir_entero('Ingrese el id del rol: ', minimo=1)
    rol = buscar_rol(id_rol)
    if rol is None:
        raise ValueError('No existe un rol con ese id.')
    return rol


@manejar_errores
def mostrar_roles():
    filas = [[r.id, r.nombre, r.permisos] for r in lista_roles()]
    mostrar_tabla('ROLES', ['Id', 'Nombre', 'Permisos'], filas)


@manejar_errores
def agregar_rol():
    nombre = pedir_texto('Ingrese el nombre del rol: ', minimo=3)
    permisos = pedir_texto('Ingrese los permisos (ej: ALL, EDICION, LECTURA): ')
    rol = registrar_rol(nombre, permisos)
    print(f'Rol guardado con éxito. Id: {rol.id}\n')


@manejar_errores
def modificar_rol():
    mostrar_roles()
    rol = _pedir_rol()
    nombre = pedir_texto(f'Nombre [{rol.nombre}] (ENTER para conservar): ', minimo=3, conservar=rol.nombre)
    permisos = pedir_texto(f'Permisos [{rol.permisos}] (ENTER para conservar): ', conservar=rol.permisos)
    editar_rol(rol, nombre, permisos)
    print('Rol actualizado con éxito.\n')


@manejar_errores
def eliminar_rol():
    mostrar_roles()
    rol = _pedir_rol()
    if confirmar(f'¿Eliminar el rol "{rol.nombre}"?'):
        deshabilitar_rol(rol)
        print('Rol eliminado con éxito.\n')
    else:
        print('Operación cancelada.\n')
