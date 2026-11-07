from peewee import CharField, IntegerField
from datos.modelos.base import BaseModel


class Rol(BaseModel):
    nombre = CharField(max_length=50, unique=True)
    permisos = CharField(max_length=255)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'roles'
