from peewee import CharField, IntegerField
from datos.modelos.base import BaseModel


class Categoria(BaseModel):
    nombre = CharField(max_length=100, unique=True)
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'categorias'
