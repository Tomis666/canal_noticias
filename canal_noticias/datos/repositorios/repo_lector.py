from datos.modelos.lector import Lector
from datos.modelos.suscripcion import Suscripcion, ESTADO_ACTIVA


def listado_lectores():
    return Lector.select().where(Lector.habilitado == 1).order_by(Lector.nombre)


def obtener_lector(id_lector):
    return Lector.get_or_none((Lector.id == id_lector) & (Lector.habilitado == 1))


def obtener_lector_correo(correo):
    return Lector.get_or_none(Lector.correo == correo)


def guardar_lector(lector: Lector):
    lector.save()
    return lector


def contar_suscripciones_activas_lector(id_lector):
    return (Suscripcion.select()
            .where((Suscripcion.lector == id_lector) & (Suscripcion.estado == ESTADO_ACTIVA))
            .count())
