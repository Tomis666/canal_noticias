from auxiliares.entradas import elegir_registro, pedir_entero, pedir_texto
from auxiliares.errores import manejar_errores
from negocio.negocio_articulos import lista_articulos
from negocio.negocio_lectores import lista_lectores
from negocio.negocio_interacciones import interacciones_de_articulo
from negocio.negocio_comentarios import (
    comentarios_del_articulo, registrar_comentario, deshabilitar_comentario)
from negocio.negocio_likes import dar_like, quitar_like


def _elegir_articulo():
    return elegir_registro('Artículos', lista_articulos(), lambda a: a.titulo, mensaje='Id del artículo: ')


def _elegir_lector():
    return elegir_registro('Lectores', lista_lectores(), lambda l: f'{l.nombre} <{l.correo}>',
                           mensaje='Id del lector: ')


@manejar_errores
def mostrar_interacciones():
    id_articulo = _elegir_articulo()
    interacciones = interacciones_de_articulo(id_articulo)
    print(f'\n=== INTERACCIONES DEL ARTÍCULO {id_articulo} ===')
    if not interacciones:
        print('(sin comentarios ni likes)\n')
        return
    for interaccion in interacciones:
        # POLIMORFISMO: mismo método, resultado distinto según sea Comentario o Like.
        print(f'{interaccion.fecha} | {interaccion.lector.nombre}: {interaccion.resumen()}')
    print()


@manejar_errores
def agregar_comentario():
    id_articulo = _elegir_articulo()
    id_lector = _elegir_lector()
    contenido = pedir_texto('Escriba el comentario: ', minimo=3)
    comentario = registrar_comentario(id_lector, id_articulo, contenido)
    print(f'Comentario guardado con éxito. Id: {comentario.id}\n')


@manejar_errores
def eliminar_comentario():
    id_articulo = _elegir_articulo()
    comentarios = comentarios_del_articulo(id_articulo)
    id_comentario = elegir_registro('Comentarios del artículo', comentarios,
                                    lambda c: f'{c.lector.nombre}: {c.resumen()}',
                                    mensaje='Id del comentario: ')
    deshabilitar_comentario(id_comentario)
    print('Comentario eliminado con éxito.\n')


@manejar_errores
def agregar_like():
    id_articulo = _elegir_articulo()
    id_lector = _elegir_lector()
    dar_like(id_lector, id_articulo)
    print('Like registrado con éxito.\n')


@manejar_errores
def eliminar_like():
    id_articulo = _elegir_articulo()
    id_lector = _elegir_lector()
    quitar_like(id_lector, id_articulo)
    print('Like eliminado con éxito.\n')
