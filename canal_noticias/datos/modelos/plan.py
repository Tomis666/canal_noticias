from peewee import CharField, DecimalField, IntegerField
from datos.modelos.base import BaseModel


class Plan(BaseModel):
    nombre = CharField(max_length=50)
    precio = DecimalField(max_digits=10, decimal_places=2)
    duracion_dias = IntegerField()
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'planes'
