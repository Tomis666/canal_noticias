from datos.modelos.plan import Plan
from datos.modelos.suscripcion import Suscripcion, ESTADO_ACTIVA


def listado_planes():
    return Plan.select().where(Plan.habilitado == 1).order_by(Plan.precio)


def obtener_plan(id_plan):
    return Plan.get_or_none((Plan.id == id_plan) & (Plan.habilitado == 1))


def guardar_plan(plan: Plan):
    plan.save()
    return plan


def contar_suscripciones_activas_plan(id_plan):
    return (Suscripcion.select()
            .where((Suscripcion.plan == id_plan) & (Suscripcion.estado == ESTADO_ACTIVA))
            .count())
