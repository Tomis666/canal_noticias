from peewee import Model
from datos.conexion_db import conectar_db

database = conectar_db()


class BaseModel(Model):
    """Padre de TODOS los modelos: solo indica a qué base de datos conectarse."""
    class Meta:
        database = database
