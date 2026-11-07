import datetime

from peewee import CharField, DateField, ForeignKeyField
from datos.modelos.base import BaseModel
from datos.modelos.lector import Lector
from datos.modelos.plan import Plan

ESTADO_ACTIVA = 'ACTIVA'
ESTADO_VENCIDA = 'VENCIDA'
ESTADO_CANCELADA = 'CANCELADA'


class Suscripcion(BaseModel):
    lector = ForeignKeyField(Lector, column_name='id_lector', backref='suscripciones')
    plan = ForeignKeyField(Plan, column_name='id_plan', backref='suscripciones')
    fecha_inicio = DateField(default=datetime.date.today)
    fecha_fin = DateField()
    estado = CharField(max_length=20, default=ESTADO_ACTIVA)  # ACTIVA / VENCIDA / CANCELADA

    class Meta:
        table_name = 'suscripciones'
