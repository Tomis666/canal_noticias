from decimal import Decimal, InvalidOperation


def pedir_texto(mensaje, minimo=1, conservar=None, obligatorio=True):
    """Pide un texto. Si 'conservar' tiene valor, ENTER devuelve ese valor."""
    while True:
        valor = input(mensaje).strip()
        if valor == '':
            if conservar is not None:
                return conservar
            if not obligatorio:
                return ''
        elif len(valor) >= minimo:
            return valor
        print(f'Debe ingresar un texto de al menos {minimo} carácter(es).')


def pedir_entero(mensaje, minimo=None, conservar=None):
    while True:
        valor = input(mensaje).strip()
        if valor == '' and conservar is not None:
            return conservar
        try:
            numero = int(valor)
        except ValueError:
            print('Debe ingresar un número entero.')
            continue
        if minimo is not None and numero < minimo:
            print(f'El número debe ser mayor o igual a {minimo}.')
            continue
        return numero


def pedir_decimal(mensaje, minimo=0, conservar=None):
    while True:
        valor = input(mensaje).strip().replace(',', '.')
        if valor == '' and conservar is not None:
            return conservar
        try:
            numero = Decimal(valor)
        except InvalidOperation:
            print('Debe ingresar un número (por ejemplo 4990 o 4990.50).')
            continue
        if numero < minimo:
            print(f'El número debe ser mayor o igual a {minimo}.')
            continue
        return numero


def pedir_id(mensaje, ids_validos, conservar=None):
    """Pide un id y repite hasta que sea uno de los ids de la lista."""
    while True:
        numero = pedir_entero(mensaje, conservar=conservar)
        if numero in ids_validos:
            return numero
        print('Ese id no está en la lista. Intente nuevamente.')


def confirmar(mensaje):
    return input(f'{mensaje} (s/n): ').strip().lower() in ('s', 'si', 'sí')


def elegir_registro(titulo, registros, describir, conservar=None, mensaje='Ingrese el id: '):
    """Muestra una lista numerada por id y devuelve el id elegido.

    registros: lista de modelos (cada uno con .id)
    describir: función que recibe un modelo y devuelve el texto a mostrar
    """
    if not registros:
        raise ValueError(f'No hay registros en "{titulo}". Agregue uno primero.')
    print(f'\n{titulo}:')
    for registro in registros:
        print(f'  [{registro.id}] {describir(registro)}')
    ids = {registro.id for registro in registros}
    return pedir_id(mensaje, ids, conservar)


def elegir_varios(titulo, registros, describir, conservar=None):
    """Igual que elegir_registro, pero acepta varios ids separados por coma.

    ENTER -> conserva 'conservar' (o ninguno si es None). Escribir 0 -> ninguno.
    """
    if not registros:
        return list(conservar or [])
    print(f'\n{titulo}:')
    for registro in registros:
        print(f'  [{registro.id}] {describir(registro)}')
    ids = {registro.id for registro in registros}
    while True:
        texto = input('Ids separados por coma (0 = ninguno, ENTER = conservar/ninguno): ').strip()
        if texto == '':
            return list(conservar or [])
        if texto == '0':
            return []
        try:
            elegidos = [int(parte) for parte in texto.split(',') if parte.strip() != '']
        except ValueError:
            print('Use solo números separados por coma. Ejemplo: 1,3')
            continue
        if all(numero in ids for numero in elegidos):
            return sorted(set(elegidos))
        print('Alguno de los ids no está en la lista. Intente nuevamente.')
