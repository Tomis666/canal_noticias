from auxiliares.entradas import (
    pedir_texto, pedir_entero, elegir_registro, elegir_varios, confirmar)
from auxiliares.errores import manejar_errores
from auxiliares.tablas import mostrar_tabla
from negocio.negocio_articulos import (
    lista_articulos, buscar_por_titulo, buscar_articulo, detalle_articulo, lista_estados,
    etiquetas_del_articulo, registrar_articulo, editar_articulo, deshabilitar_articulo)
from negocio.negocio_autores import lista_autores
from negocio.negocio_categorias import lista_categorias
from negocio.negocio_etiquetas import lista_etiquetas

_COLUMNAS = ['Id', 'Titular', 'Categoría', 'Autor', 'Estado', 'Fecha']


def _filas(articulos):
    return [[a.id, a.titulo, a.categoria.nombre, a.autor.usuario.nombre, a.estado.estado, a.fecha_publicacion]
            for a in articulos]


def _pedir_articulo():
    id_articulo = pedir_entero('Ingrese el id del artículo: ', minimo=1)
    articulo = buscar_articulo(id_articulo)
    if articulo is None:
        raise ValueError('No existe un artículo con ese id.')
    return articulo


@manejar_errores
def mostrar_articulos():
    mostrar_tabla('ARTÍCULOS PUBLICADOS', _COLUMNAS, _filas(lista_articulos()), izquierda=['Titular'])


@manejar_errores
def ver_articulo():
    id_articulo = pedir_entero('Ingrese el id del artículo: ', minimo=1)
    detalle = detalle_articulo(id_articulo)
    articulo = detalle['articulo']
    etiquetas = ', '.join(e.nombre for e in detalle['etiquetas']) or '(sin etiquetas)'
    print(f'\n{articulo.titulo}')
    print('-' * len(articulo.titulo))
    print(f'Autor: {articulo.autor.usuario.nombre} | Categoría: {articulo.categoria.nombre} | '
          f'Estado: {articulo.estado.estado} | Fecha: {articulo.fecha_publicacion}')
    print(f'Etiquetas: {etiquetas}')
    print(f'Likes: {detalle["likes"]} | Comentarios: {detalle["comentarios"]}\n')
    print(f'{articulo.contenido}\n')


@manejar_errores
def buscar_articulos():
    texto = pedir_texto('Ingrese parte del título a buscar: ')
    mostrar_tabla(f'RESULTADOS PARA "{texto}"', _COLUMNAS, _filas(buscar_por_titulo(texto)), izquierda=['Titular'])


@manejar_errores
def agregar_articulo():
    titulo = pedir_texto('Ingrese el titular (mínimo 5 caracteres): ', minimo=5)
    contenido = pedir_texto('Ingrese el contenido: ')
    id_autor = elegir_registro('Autores', lista_autores(), lambda a: a.nombre, mensaje='Id del autor: ')
    id_categoria = elegir_registro('Categorías', lista_categorias(), lambda c: c.nombre, mensaje='Id de la categoría: ')
    id_estado = elegir_registro('Estados', lista_estados(), lambda e: e.estado, mensaje='Id del estado: ')
    ids_etiquetas = elegir_varios('Etiquetas', lista_etiquetas(), lambda e: e.nombre)
    articulo = registrar_articulo(titulo, contenido, id_autor, id_categoria, id_estado, ids_etiquetas)
    print(f'Artículo guardado con éxito. Id: {articulo.id}\n')


@manejar_errores
def modificar_articulo():
    mostrar_articulos()
    articulo = _pedir_articulo()
    titulo = pedir_texto(f'Titular [{articulo.titulo}] (ENTER para conservar): ',
                         minimo=5, conservar=articulo.titulo)
    contenido = pedir_texto('Contenido (ENTER para conservar): ', conservar=articulo.contenido)
    id_categoria = elegir_registro('Categorías', lista_categorias(), lambda c: c.nombre,
                                   conservar=articulo.categoria_id,
                                   mensaje=f'Id de la categoría [{articulo.categoria.nombre}] (ENTER para conservar): ')
    id_estado = elegir_registro('Estados', lista_estados(), lambda e: e.estado,
                                conservar=articulo.estado_id,
                                mensaje=f'Id del estado [{articulo.estado.estado}] (ENTER para conservar): ')
    actuales = [e.id for e in etiquetas_del_articulo(articulo.id)]
    ids_etiquetas = elegir_varios('Etiquetas', lista_etiquetas(), lambda e: e.nombre, conservar=actuales)
    editar_articulo(articulo, titulo, contenido, id_categoria, id_estado, ids_etiquetas)
    print('Artículo actualizado con éxito.\n')


@manejar_errores
def eliminar_articulo():
    mostrar_articulos()
    articulo = _pedir_articulo()
    if confirmar(f'¿Eliminar el artículo "{articulo.titulo}"?'):
        deshabilitar_articulo(articulo)
        print('Artículo eliminado con éxito.\n')
    else:
        print('Operación cancelada.\n')
