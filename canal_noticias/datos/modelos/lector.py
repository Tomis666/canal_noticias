from datos.modelos.persona import Persona


class Lector(Persona):
    """Hija de Persona: no agrega campos, pero sí su propia descripción."""

    class Meta:
        table_name = 'lectores'

    def descripcion(self):
        return f'Lector {self.nombre} <{self.correo}>'
