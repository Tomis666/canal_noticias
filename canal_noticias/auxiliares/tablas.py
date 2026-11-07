from prettytable import PrettyTable


def mostrar_tabla(titulo, columnas, filas, izquierda=()):
    """Imprime una tabla con PrettyTable. 'filas' es una lista de listas."""
    print(f'\n=== {titulo} ===')
    if not filas:
        print('(sin registros)\n')
        return
    tabla = PrettyTable()
    tabla.field_names = columnas
    for columna in izquierda:
        tabla.align[columna] = 'l'
    for fila in filas:
        tabla.add_row(fila)
    print(tabla)
    print()
