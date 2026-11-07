from datos.modelos.like import Like
from datos.modelos.lector import Lector


def likes_de_articulo(id_articulo):
    return (Like
            .select(Like, Lector)
            .join(Lector, on=(Like.lector == Lector.id))
            .where(Like.articulo == id_articulo)
            .order_by(Like.fecha, Like.id))


def obtener_like(id_lector, id_articulo):
    return Like.select().where((Like.lector == id_lector) & (Like.articulo == id_articulo)).first()


def crear_like(id_lector, id_articulo):
    return Like.create(lector=id_lector, articulo=id_articulo)


def eliminar_like(like: Like):
    like.delete_instance()


def contar_likes(id_articulo):
    return Like.select().where(Like.articulo == id_articulo).count()
