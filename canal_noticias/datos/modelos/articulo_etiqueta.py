from peewee import ForeignKeyField, CompositeKey
from datos.modelos.base import BaseModel
from datos.modelos.articulo import Articulo
from datos.modelos.etiqueta import Etiqueta


class ArticuloEtiqueta(BaseModel):
    """Tabla intermedia: un artículo tiene varias etiquetas y una etiqueta, varios artículos."""
    articulo = ForeignKeyField(Articulo, column_name='id_articulo', backref='articulos_etiquetas')
    etiqueta = ForeignKeyField(Etiqueta, column_name='id_etiqueta', backref='articulos_etiquetas')

    class Meta:
        table_name = 'articulos_etiquetas'
        primary_key = CompositeKey('articulo', 'etiqueta')
