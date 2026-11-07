from peewee import CharField, IntegerField
from datos.modelos.base import BaseModel


class Etiqueta(BaseModel):
    nombre = CharField(max_length=50, unique=True)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'etiquetas'
