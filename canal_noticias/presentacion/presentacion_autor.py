from auxiliares.entradas import pedir_texto, pedir_entero, elegir_registro, confirmar
from auxiliares.errores import manejar_errores
from auxiliares.tablas import mostrar_tabla
from negocio.negocio_autores import (
    lista_autores, buscar_autor, usuarios_sin_perfil_autor, registrar_autor,
    editar_autor, deshabilitar_autor)


def _pedir_autor():
    id_autor = pedir_entero('Ingrese el id del autor: ', minimo=1)
    autor = buscar_autor(id_autor)
    if autor is None:
        raise ValueError('No existe un autor con ese id.')
    return autor


@manejar_errores
def mostrar_autores():
    filas = []
    for autor in lista_autores():
        biografia = autor.biografia or ''
        resumen = biografia if len(biografia) <= 60 else biografia[:57] + '...'
        filas.append([autor.id, autor.nombre, autor.usuario.correo, resumen])
    mostrar_tabla('AUTORES (PERIODISTAS)', ['Id', 'Nombre', 'Correo', 'Biografía'], filas,
                  izquierda=['Nombre', 'Correo', 'Biografía'])


@manejar_errores
def agregar_autor():
    id_usuario = elegir_registro('Usuarios que aún no son autores', usuarios_sin_perfil_autor(),
                                 lambda u: f'{u.nombre} <{u.correo}>', mensaje='Id del usuario: ')
    biografia = pedir_texto('Ingrese la biografía (opcional): ', obligatorio=False)
    autor = registrar_autor(id_usuario, biografia)
    print(f'Autor guardado con éxito. Id: {autor.id}\n')


@manejar_errores
def modificar_autor():
    mostrar_autores()
    autor = _pedir_autor()
    biografia = pedir_texto('Nueva biografía (ENTER para conservar): ',
                            conservar=autor.biografia or '', obligatorio=False)
    editar_autor(autor, biografia)
    print('Autor actualizado con éxito.\n')


@manejar_errores
def eliminar_autor():
    mostrar_autores()
    autor = _pedir_autor()
    if confirmar(f'¿Eliminar al autor "{autor.nombre}"?'):
        deshabilitar_autor(autor)
        print('Autor eliminado con éxito.\n')
    else:
        print('Operación cancelada.\n')
