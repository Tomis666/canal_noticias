from auxiliares.entradas import pedir_texto, pedir_entero, confirmar
from auxiliares.errores import manejar_errores
from auxiliares.tablas import mostrar_tabla
from negocio.negocio_lectores import (
    lista_lectores, buscar_lector, registrar_lector, editar_lector, deshabilitar_lector)


def _pedir_lector():
    id_lector = pedir_entero('Ingrese el id del lector: ', minimo=1)
    lector = buscar_lector(id_lector)
    if lector is None:
        raise ValueError('No existe un lector con ese id.')
    return lector


@manejar_errores
def mostrar_lectores():
    filas = [[l.id, l.nombre, l.correo] for l in lista_lectores()]
    mostrar_tabla('LECTORES', ['Id', 'Nombre', 'Correo'], filas, izquierda=['Nombre', 'Correo'])


@manejar_errores
def agregar_lector():
    nombre = pedir_texto('Ingrese el nombre: ', minimo=3)
    correo = pedir_texto('Ingrese el correo: ')
    lector = registrar_lector(nombre, correo)
    print(f'Lector guardado con éxito. Id: {lector.id}\n')


@manejar_errores
def modificar_lector():
    mostrar_lectores()
    lector = _pedir_lector()
    nombre = pedir_texto(f'Nombre [{lector.nombre}] (ENTER para conservar): ', minimo=3, conservar=lector.nombre)
    correo = pedir_texto(f'Correo [{lector.correo}] (ENTER para conservar): ', conservar=lector.correo)
    editar_lector(lector, nombre, correo)
    print('Lector actualizado con éxito.\n')


@manejar_errores
def eliminar_lector():
    mostrar_lectores()
    lector = _pedir_lector()
    if confirmar(f'¿Eliminar al lector "{lector.nombre}"?'):
        deshabilitar_lector(lector)
        print('Lector eliminado con éxito.\n')
    else:
        print('Operación cancelada.\n')
