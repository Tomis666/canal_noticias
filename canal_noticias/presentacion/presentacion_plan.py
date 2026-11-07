from auxiliares.entradas import pedir_texto, pedir_entero, pedir_decimal, confirmar
from auxiliares.errores import manejar_errores
from auxiliares.tablas import mostrar_tabla
from negocio.negocio_planes import (
    lista_planes, buscar_plan, registrar_plan, editar_plan, deshabilitar_plan)


def _pedir_plan():
    id_plan = pedir_entero('Ingrese el id del plan: ', minimo=1)
    plan = buscar_plan(id_plan)
    if plan is None:
        raise ValueError('No existe un plan con ese id.')
    return plan


@manejar_errores
def mostrar_planes():
    filas = [[p.id, p.nombre, f'${p.precio:,.0f}', p.duracion_dias] for p in lista_planes()]
    mostrar_tabla('PLANES', ['Id', 'Nombre', 'Precio', 'Duración (días)'], filas, izquierda=['Nombre'])


@manejar_errores
def agregar_plan():
    nombre = pedir_texto('Ingrese el nombre del plan: ', minimo=3)
    precio = pedir_decimal('Ingrese el precio: ')
    duracion = pedir_entero('Ingrese la duración en días: ', minimo=1)
    plan = registrar_plan(nombre, precio, duracion)
    print(f'Plan guardado con éxito. Id: {plan.id}\n')


@manejar_errores
def modificar_plan():
    mostrar_planes()
    plan = _pedir_plan()
    nombre = pedir_texto(f'Nombre [{plan.nombre}] (ENTER para conservar): ', minimo=3, conservar=plan.nombre)
    precio = pedir_decimal(f'Precio [{plan.precio}] (ENTER para conservar): ', conservar=plan.precio)
    duracion = pedir_entero(f'Duración en días [{plan.duracion_dias}] (ENTER para conservar): ',
                            minimo=1, conservar=plan.duracion_dias)
    editar_plan(plan, nombre, precio, duracion)
    print('Plan actualizado con éxito.\n')


@manejar_errores
def eliminar_plan():
    mostrar_planes()
    plan = _pedir_plan()
    if confirmar(f'¿Eliminar el plan "{plan.nombre}"?'):
        deshabilitar_plan(plan)
        print('Plan eliminado con éxito.\n')
    else:
        print('Operación cancelada.\n')
