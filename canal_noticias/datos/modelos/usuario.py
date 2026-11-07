from peewee import CharField, ForeignKeyField
from datos.modelos.persona import Persona
from datos.modelos.rol import Rol


class Usuario(Persona):
    """Hija de Persona: agrega contraseña y rol."""
    contrasena = CharField(max_length=255)  # se guarda el HASH, no el texto
    rol = ForeignKeyField(Rol, column_name='id_rol', backref='usuarios')

    class Meta:
        table_name = 'usuarios'

    def descripcion(self):
        return f'Usuario {self.nombre} (rol: {self.rol.nombre})'
