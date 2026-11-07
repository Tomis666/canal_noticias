from datos.modelos.usuario import Usuario
from datos.modelos.rol import Rol


def _consulta_base():
    # JOIN con Rol: trae usuario y rol en UNA sola consulta (más eficiente).
    return (Usuario
            .select(Usuario, Rol)
            .join(Rol, on=(Usuario.rol == Rol.id)))


def listado_usuarios():
    return _consulta_base().where(Usuario.habilitado == 1).order_by(Usuario.nombre)


def obtener_usuario(id_usuario):
    return _consulta_base().where((Usuario.id == id_usuario) & (Usuario.habilitado == 1)).first()


def obtener_usuario_correo(correo):
    """Busca por correo incluyendo los deshabilitados (el correo es único)."""
    return _consulta_base().where(Usuario.correo == correo).first()


def guardar_usuario(usuario: Usuario):
    usuario.save()
    return usuario
