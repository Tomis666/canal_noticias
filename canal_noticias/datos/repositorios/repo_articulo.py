from datos.modelos.base import database
from datos.modelos.articulo import Articulo
from datos.modelos.autor import Autor
from datos.modelos.usuario import Usuario
from datos.modelos.categoria import Categoria
from datos.modelos.estado_articulo import EstadoArticulo
from datos.modelos.etiqueta import Etiqueta
from datos.modelos.articulo_etiqueta import ArticuloEtiqueta


def _consulta_base():
    # Un solo SELECT con JOINs trae el artículo + autor + usuario + categoría + estado.
    # Sin esto, mostrar 100 artículos haría ~400 consultas (problema "N+1").
    return (Articulo
            .select(Articulo, Autor, Usuario, Categoria, EstadoArticulo)
            .join(Categoria, on=(Articulo.categoria == Categoria.id))
            .switch(Articulo)
            .join(EstadoArticulo, on=(Articulo.estado == EstadoArticulo.id))
            .switch(Articulo)
            .join(Autor, on=(Articulo.autor == Autor.id))
            .join(Usuario, on=(Autor.usuario == Usuario.id)))


def listado_articulos():
    return (_consulta_base()
            .where(Articulo.habilitado == 1)
            .order_by(Articulo.fecha_publicacion.desc(), Articulo.id.desc()))


def buscar_articulos(texto):
    return (_consulta_base()
            .where((Articulo.habilitado == 1) & (Articulo.titulo.contains(texto)))
            .order_by(Articulo.fecha_publicacion.desc(), Articulo.id.desc()))


def obtener_articulo(id_articulo):
    return _consulta_base().where((Articulo.id == id_articulo) & (Articulo.habilitado == 1)).first()


def listado_estados():
    return EstadoArticulo.select().order_by(EstadoArticulo.id)


def obtener_estado(id_estado):
    return EstadoArticulo.get_or_none(EstadoArticulo.id == id_estado)


def etiquetas_de_articulo(id_articulo):
    return (Etiqueta.select()
            .join(ArticuloEtiqueta, on=(ArticuloEtiqueta.etiqueta == Etiqueta.id))
            .where(ArticuloEtiqueta.articulo == id_articulo)
            .order_by(Etiqueta.nombre))


def _asignar_etiquetas(id_articulo, ids_etiquetas):
    ArticuloEtiqueta.delete().where(ArticuloEtiqueta.articulo == id_articulo).execute()
    filas = [{'articulo': id_articulo, 'etiqueta': id_etiqueta} for id_etiqueta in ids_etiquetas]
    if filas:
        ArticuloEtiqueta.insert_many(filas).execute()


def crear_articulo(titulo, contenido, id_autor, id_categoria, id_estado, ids_etiquetas):
    # atomic(): si algo falla a mitad de camino, no queda nada guardado a medias.
    with database.atomic():
        articulo = Articulo.create(titulo=titulo, contenido=contenido, autor=id_autor,
                                   categoria=id_categoria, estado=id_estado)
        _asignar_etiquetas(articulo.id, ids_etiquetas)
    return articulo


def guardar_articulo(articulo: Articulo, ids_etiquetas=None):
    with database.atomic():
        articulo.save()
        if ids_etiquetas is not None:
            _asignar_etiquetas(articulo.id, ids_etiquetas)
    return articulo
