from peewee import CharField
from datos.modelos.base import BaseModel


class EstadoArticulo(BaseModel):
    estado = CharField(max_length=30, unique=True)

    class Meta:
        table_name = 'estados_articulo'
