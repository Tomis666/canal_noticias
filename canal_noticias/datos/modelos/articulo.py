import datetime

from peewee import CharField, TextField, DateField, IntegerField, ForeignKeyField
from datos.modelos.base import BaseModel
from datos.modelos.autor import Autor
from datos.modelos.categoria import Categoria
from datos.modelos.estado_articulo import EstadoArticulo


class Articulo(BaseModel):
    titulo = CharField(max_length=150)
    contenido = TextField()
    fecha_publicacion = DateField(default=datetime.date.today)
    autor = ForeignKeyField(Autor, column_name='id_autor', backref='articulos')
    categoria = ForeignKeyField(Categoria, column_name='id_categoria', backref='articulos')
    estado = ForeignKeyField(EstadoArticulo, column_name='id_estado', backref='articulos')
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'articulos'
