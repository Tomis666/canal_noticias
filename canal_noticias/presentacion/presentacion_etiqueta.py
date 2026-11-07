from auxiliares.entradas import pedir_texto, pedir_entero, confirmar
from auxiliares.errores import manejar_errores
from auxiliares.tablas import mostrar_tabla
from negocio.negocio_etiquetas import (
    lista_etiquetas, buscar_etiqueta, registrar_etiqueta, editar_etiqueta, deshabilitar_etiqueta)


def _pedir_etiqueta():
    id_etiqueta = pedir_entero('Ingrese el id de la etiqueta: ', minimo=1)
    etiqueta = buscar_etiqueta(id_etiqueta)
    if etiqueta is None:
        raise ValueError('No existe una etiqueta con ese id.')
    return etiqueta


@manejar_errores
def mostrar_etiquetas():
    filas = [[e.id, e.nombre] for e in lista_etiquetas()]
    mostrar_tabla('ETIQUETAS', ['Id', 'Nombre'], filas)


@manejar_errores
def agregar_etiqueta():
    nombre = pedir_texto('Ingrese el nombre de la etiqueta: ', minimo=2)
    etiqueta = registrar_etiqueta(nombre)
    print(f'Etiqueta guardada con éxito. Id: {etiqueta.id}\n')


@manejar_errores
def modificar_etiqueta():
    mostrar_etiquetas()
    etiqueta = _pedir_etiqueta()
    nombre = pedir_texto(f'Nombre [{etiqueta.nombre}] (ENTER para conservar): ',
                         minimo=2, conservar=etiqueta.nombre)
    editar_etiqueta(etiqueta, nombre)
    print('Etiqueta actualizada con éxito.\n')


@manejar_errores
def eliminar_etiqueta():
    mostrar_etiquetas()
    etiqueta = _pedir_etiqueta()
    if confirmar(f'¿Eliminar la etiqueta "{etiqueta.nombre}"?'):
        deshabilitar_etiqueta(etiqueta)
        print('Etiqueta eliminada con éxito.\n')
    else:
        print('Operación cancelada.\n')
