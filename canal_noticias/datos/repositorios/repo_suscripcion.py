from datos.modelos.suscripcion import Suscripcion, ESTADO_ACTIVA, ESTADO_VENCIDA
from datos.modelos.lector import Lector
from datos.modelos.plan import Plan


def listado_suscripciones():
    return (Suscripcion
            .select(Suscripcion, Lector, Plan)
            .join(Lector, on=(Suscripcion.lector == Lector.id))
            .switch(Suscripcion)
            .join(Plan, on=(Suscripcion.plan == Plan.id))
            .order_by(Suscripcion.fecha_fin.desc()))


def obtener_suscripcion(id_suscripcion):
    return Suscripcion.get_or_none(Suscripcion.id == id_suscripcion)


def suscripcion_activa_de(id_lector):
    return (Suscripcion.select()
            .where((Suscripcion.lector == id_lector) & (Suscripcion.estado == ESTADO_ACTIVA))
            .first())


def crear_suscripcion(id_lector, id_plan, fecha_inicio, fecha_fin):
    return Suscripcion.create(lector=id_lector, plan=id_plan,
                              fecha_inicio=fecha_inicio, fecha_fin=fecha_fin,
                              estado=ESTADO_ACTIVA)


def guardar_suscripcion(suscripcion: Suscripcion):
    suscripcion.save()
    return suscripcion


def marcar_vencidas(hoy):
    """Pasa a VENCIDA todas las suscripciones ACTIVAS cuya fecha de fin ya pasó."""
    (Suscripcion.update(estado=ESTADO_VENCIDA)
     .where((Suscripcion.estado == ESTADO_ACTIVA) & (Suscripcion.fecha_fin < hoy))
     .execute())
