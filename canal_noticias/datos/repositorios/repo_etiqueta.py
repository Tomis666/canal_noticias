from datos.modelos.etiqueta import Etiqueta
from datos.modelos.articulo import Articulo
from datos.modelos.articulo_etiqueta import ArticuloEtiqueta


def listado_etiquetas():
    return Etiqueta.select().where(Etiqueta.habilitado == 1).order_by(Etiqueta.nombre)


def obtener_etiqueta(id_etiqueta):
    return Etiqueta.get_or_none((Etiqueta.id == id_etiqueta) & (Etiqueta.habilitado == 1))


def obtener_etiqueta_nombre(nombre):
    return Etiqueta.get_or_none(Etiqueta.nombre == nombre)


def guardar_etiqueta(etiqueta: Etiqueta):
    etiqueta.save()
    return etiqueta


def contar_articulos_etiqueta(id_etiqueta):
    return (ArticuloEtiqueta.select()
            .join(Articulo, on=(ArticuloEtiqueta.articulo == Articulo.id))
            .where((ArticuloEtiqueta.etiqueta == id_etiqueta) & (Articulo.habilitado == 1))
            .count())
