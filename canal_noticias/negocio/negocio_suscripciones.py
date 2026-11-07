import datetime

from datos.repositorios.repo_suscripcion import (
    listado_suscripciones, obtener_suscripcion, suscripcion_activa_de,
    crear_suscripcion, guardar_suscripcion, marcar_vencidas)
from datos.repositorios.repo_lector import obtener_lector
from datos.repositorios.repo_plan import obtener_plan
from datos.modelos.suscripcion import ESTADO_ACTIVA, ESTADO_CANCELADA


def lista_suscripciones():
    marcar_vencidas(datetime.date.today())  # antes de mostrar, actualiza las que ya vencieron
    return list(listado_suscripciones())


def suscribir_lector(id_lector, id_plan):
    if obtener_lector(id_lector) is None:
        raise ValueError('El lector indicado no existe.')
    plan = obtener_plan(id_plan)
    if plan is None:
        raise ValueError('El plan indicado no existe.')
    hoy = datetime.date.today()
    marcar_vencidas(hoy)
    if suscripcion_activa_de(id_lector) is not None:
        raise ValueError('El lector ya tiene una suscripción activa.')
    fin = hoy + datetime.timedelta(days=plan.duracion_dias)
    return crear_suscripcion(id_lector, id_plan, hoy, fin)


def suscripciones_activas():
    return [s for s in lista_suscripciones() if s.estado == ESTADO_ACTIVA]


def cancelar_suscripcion(id_suscripcion):
    suscripcion = obtener_suscripcion(id_suscripcion)
    if suscripcion is None:
        raise ValueError('No existe una suscripción con ese id.')
    if suscripcion.estado != ESTADO_ACTIVA:
        raise ValueError(f'Solo se pueden cancelar suscripciones activas (esta está {suscripcion.estado}).')
    suscripcion.estado = ESTADO_CANCELADA
    return guardar_suscripcion(suscripcion)
