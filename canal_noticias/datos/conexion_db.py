from peewee import MySQLDatabase
from decouple import config


def conectar_db():
    """Crea el objeto de conexión a MySQL leyendo los datos del archivo .env"""
    base_datos = MySQLDatabase(config('DB_NAME'), **{
        'charset': 'utf8mb4',
        'host': config('DB_HOST', default='localhost'),
        'port': config('DB_PORT', default=3306, cast=int),
        'user': config('DB_USER'),
        'password': config('DB_PASSWORD')})
    return base_datos
