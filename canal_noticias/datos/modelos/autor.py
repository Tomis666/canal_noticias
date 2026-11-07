from peewee import TextField, IntegerField, ForeignKeyField
from datos.modelos.base import BaseModel
from datos.modelos.usuario import Usuario


class Autor(BaseModel):
    """Un Autor es el perfil de periodista de un Usuario (relación 1 a 1)."""
    biografia = TextField(null=True)
    usuario = ForeignKeyField(Usuario, column_name='id_usuario', unique=True,
                              backref='perfil_autor')
    habilitado = IntegerField(default=1)

    class Meta:
        table_name = 'autores'

    @property
    def nombre(self):
        # El nombre vive en Usuario: así no se guarda dos veces.
        return self.usuario.nombre

    def descripcion(self):
        return f'Autor {self.nombre}'
