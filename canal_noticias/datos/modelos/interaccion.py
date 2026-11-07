import datetime

from peewee import DateField, ForeignKeyField
from datos.modelos.base import BaseModel
from datos.modelos.lector import Lector
from datos.modelos.articulo import Articulo


class Interaccion(BaseModel):
    """HERENCIA: clase padre de Comentario y Like.

    Un lector interactúa con un artículo en una fecha. Eso es común a
    comentarios y likes. Tampoco tiene tabla propia.
    (backref='+' significa "no crear acceso inverso"; las consultas se hacen
    directamente sobre Comentario o Like.)
    """
    lector = ForeignKeyField(Lector, column_name='id_lector', backref='+')
    articulo = ForeignKeyField(Articulo, column_name='id_articulo', backref='+')
    fecha = DateField(default=datetime.date.today)

    def resumen(self):
        """POLIMORFISMO: cada hija lo redefine."""
        return 'Interacción'
