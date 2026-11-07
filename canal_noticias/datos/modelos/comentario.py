from peewee import TextField, IntegerField
from datos.modelos.interaccion import Interaccion


class Comentario(Interaccion):
    contenido = TextField()
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'comentarios'

    def resumen(self):
        texto = self.contenido if len(self.contenido) <= 60 else self.contenido[:57] + '...'
        return f'Comentó: "{texto}"'
