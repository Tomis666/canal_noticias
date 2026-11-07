from datos.repositorios.repo_comentario import comentarios_de_articulo
from datos.repositorios.repo_like import likes_de_articulo


def interacciones_de_articulo(id_articulo):
    """POLIMORFISMO en acción: mezcla comentarios y likes en UNA lista.

    Comentario y Like son hijas de Interaccion, así que todos los elementos
    tienen .lector, .fecha y .resumen(); quien use la lista no necesita saber
    de qué clase es cada uno.
    """
    interacciones = list(comentarios_de_articulo(id_articulo)) + list(likes_de_articulo(id_articulo))
    return sorted(interacciones, key=lambda interaccion: interaccion.fecha)
