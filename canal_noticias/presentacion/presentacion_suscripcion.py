from auxiliares.entradas import elegir_registro, pedir_entero, confirmar
from auxiliares.errores import manejar_errores
from auxiliares.tablas import mostrar_tabla
from negocio.negocio_suscripciones import (
    lista_suscripciones, suscripciones_activas, suscribir_lector, cancelar_suscripcion)
from negocio.negocio_lectores import lista_lectores
from negocio.negocio_planes import lista_planes


@manejar_errores
def mostrar_suscripciones():
    filas = [[s.id, s.lector.nombre, s.plan.nombre, s.fecha_inicio, s.fecha_fin, s.estado]
             for s in lista_suscripciones()]
    mostrar_tabla('SUSCRIPCIONES', ['Id', 'Lector', 'Plan', 'Inicio', 'Fin', 'Estado'], filas,
                  izquierda=['Lector', 'Plan'])


@manejar_errores
def agregar_suscripcion():
    id_lector = elegir_registro('Lectores', lista_lectores(), lambda l: f'{l.nombre} <{l.correo}>',
                                mensaje='Id del lector: ')
    id_plan = elegir_registro('Planes', lista_planes(),
                              lambda p: f'{p.nombre} - ${p.precio:,.0f} por {p.duracion_dias} días',
                              mensaje='Id del plan: ')
    suscripcion = suscribir_lector(id_lector, id_plan)
    print(f'Suscripción creada con éxito. Id: {suscripcion.id} (vence el {suscripcion.fecha_fin})\n')


@manejar_errores
def anular_suscripcion():
    activas = suscripciones_activas()
    id_suscripcion = elegir_registro('Suscripciones activas', activas,
                                     lambda s: f'{s.lector.nombre} - {s.plan.nombre} (vence {s.fecha_fin})',
                                     mensaje='Id de la suscripción: ')
    if confirmar('¿Cancelar esta suscripción?'):
        cancelar_suscripcion(id_suscripcion)
        print('Suscripción cancelada con éxito.\n')
    else:
        print('Operación cancelada.\n')
