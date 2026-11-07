from datos.modelos.plan import Plan
from datos.repositorios.repo_plan import (
    listado_planes, obtener_plan, guardar_plan, contar_suscripciones_activas_plan)


def _validar(nombre, precio, duracion_dias):
    nombre = nombre.strip()
    if len(nombre) < 3:
        raise ValueError('El nombre del plan debe tener al menos 3 caracteres.')
    if precio < 0:
        raise ValueError('El precio no puede ser negativo.')
    if duracion_dias < 1:
        raise ValueError('La duración debe ser de al menos 1 día.')
    return nombre


def lista_planes():
    return list(listado_planes())


def buscar_plan(id_plan):
    return obtener_plan(id_plan)


def registrar_plan(nombre, precio, duracion_dias):
    nombre = _validar(nombre, precio, duracion_dias)
    plan = Plan()
    plan.nombre = nombre
    plan.precio = precio
    plan.duracion_dias = duracion_dias
    return guardar_plan(plan)


def editar_plan(plan: Plan, nombre, precio, duracion_dias):
    nombre = _validar(nombre, precio, duracion_dias)
    plan.nombre = nombre
    plan.precio = precio
    plan.duracion_dias = duracion_dias
    return guardar_plan(plan)


def deshabilitar_plan(plan: Plan):
    if contar_suscripciones_activas_plan(plan.id) > 0:
        raise ValueError('No se puede eliminar: hay suscripciones activas con este plan.')
    plan.habilitado = 0
    guardar_plan(plan)
