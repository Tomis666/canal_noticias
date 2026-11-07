from peewee import CharField, IntegerField
from datos.modelos.base import BaseModel


class Persona(BaseModel):
    """HERENCIA: clase padre de Usuario y Lector.

    Contiene lo que tienen en común (nombre, correo, habilitado), así no se
    repite en cada clase hija. Persona NO tiene tabla propia: cada hija crea
    la suya (usuarios, lectores) con estos campos incluidos.
    """
    nombre = CharField(max_length=100)
    correo = CharField(max_length=100, unique=True)
    habilitado = IntegerField(default=1)

    def descripcion(self):
        """POLIMORFISMO: cada hija redefine este método a su manera."""
        return f'Persona {self.nombre} <{self.correo}>'
