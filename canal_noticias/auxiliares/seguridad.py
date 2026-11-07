import hashlib
import hmac
import os

_ITERACIONES = 100_000


def hashear_contrasena(contrasena: str) -> str:
    """Devuelve 'sal$hash'. Nunca se guarda la contraseña en texto plano."""
    sal = os.urandom(16)
    hash_bytes = hashlib.pbkdf2_hmac('sha256', contrasena.encode('utf-8'), sal, _ITERACIONES)
    return f'{sal.hex()}${hash_bytes.hex()}'


def verificar_contrasena(contrasena: str, guardada: str) -> bool:
    """Compara la contraseña escrita con la guardada ('sal$hash')."""
    try:
        sal_hex, hash_hex = guardada.split('$')
        sal = bytes.fromhex(sal_hex)
    except ValueError:
        return False
    hash_bytes = hashlib.pbkdf2_hmac('sha256', contrasena.encode('utf-8'), sal, _ITERACIONES)
    return hmac.compare_digest(hash_bytes.hex(), hash_hex)
