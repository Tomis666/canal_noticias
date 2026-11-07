from auxiliares.entradas import pedir_texto, pedir_entero, confirmar
from auxiliares.errores import manejar_errores
from auxiliares.tablas import mostrar_tabla
from negocio.negocio_categorias import (
    lista_categorias, buscar_categoria, registrar_categoria, editar_categoria, deshabilitar_categoria)


def _pedir_categoria():
    id_categoria = pedir_entero('Ingrese el id de la categoría: ', minimo=1)
    categoria = buscar_categoria(id_categoria)
    if categoria is None:
        raise ValueError('No existe una categoría con ese id.')
    return categoria


@manejar_errores
def mostrar_categorias():
    filas = [[c.id, c.nombre] for c in lista_categorias()]
    mostrar_tabla('CATEGORÍAS', ['Id', 'Nombre'], filas)


@manejar_errores
def agregar_categoria():
    nombre = pedir_texto('Ingrese el nombre de la categoría: ', minimo=3)
    categoria = registrar_categoria(nombre)
    print(f'Categoría guardada con éxito. Id: {categoria.id}\n')


@manejar_errores
def modificar_categoria():
    mostrar_categorias()
    categoria = _pedir_categoria()
    nombre = pedir_texto(f'Nombre [{categoria.nombre}] (ENTER para conservar): ',
                         minimo=3, conservar=categoria.nombre)
    editar_categoria(categoria, nombre)
    print('Categoría actualizada con éxito.\n')


@manejar_errores
def eliminar_categoria():
    mostrar_categorias()
    categoria = _pedir_categoria()
    if confirmar(f'¿Eliminar la categoría "{categoria.nombre}"?'):
        deshabilitar_categoria(categoria)
        print('Categoría eliminada con éxito.\n')
    else:
        print('Operación cancelada.\n')
