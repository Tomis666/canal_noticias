from datos.modelos.interaccion import Interaccion


class Like(Interaccion):

    class Meta:
        table_name = 'likes'

    def resumen(self):
        return 'Le dio like al artículo'
