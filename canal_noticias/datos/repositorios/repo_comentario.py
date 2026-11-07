from datos.modelos.comentario import Comentario
from datos.modelos.lector import Lector


def comentarios_de_articulo(id_articulo):
    return (Comentario
            .select(Comentario, Lector)
            .join(Lector, on=(Comentario.lector == Lector.id))
            .where((Comentario.articulo == id_articulo) & (Comentario.habilitado == 1))
            .order_by(Comentario.fecha, Comentario.id))


def obtener_comentario(id_comentario):
    return Comentario.get_or_none((Comentario.id == id_comentario) & (Comentario.habilitado == 1))


def crear_comentario(id_lector, id_articulo, contenido):
    return Comentario.create(lector=id_lector, articulo=id_articulo, contenido=contenido)


def guardar_comentario(comentario: Comentario):
    comentario.save()
    return comentario


def contar_comentarios(id_articulo):
    return Comentario.select().where((Comentario.articulo == id_articulo) & (Comentario.habilitado == 1)).count()
