def main() -> int:
    # Los imports van aquí dentro a propósito: si falta el archivo .env o la
    # librería, podemos mostrar un mensaje claro en vez de un error largo.
    try:
        from datos.modelos.base import database
    except Exception as error:
        print('No se pudo leer la configuración de la base de datos.')
        print('Revise que exista el archivo .env (copie .env.example) y que haya instalado')
        print('las librerías:  pip install -r requirements.txt')
        print(f'Detalle: {error}')
        return 1

    try:
        database.connect(reuse_if_open=True)
    except Exception as error:
        print('No se pudo conectar a MySQL. Revise que:')
        print('  1) MySQL esté encendido (en XAMPP: botón Start de MySQL).')
        print('  2) El usuario, la clave, el puerto y el nombre de la base del .env sean correctos.')
        print(f'Detalle: {error}')
        return 1

    try:
        from presentacion.menu import menu_principal
        from presentacion.presentacion_usuario import pedir_login

        print('Canal de Noticias - Inicio de sesión')
        usuario = pedir_login()
        if usuario is None:
            print('Demasiados intentos fallidos. Saliendo...')
            return 1
        menu_principal(usuario)
    except (EOFError, KeyboardInterrupt):
        print('\nSaliendo...')
    finally:
        if not database.is_closed():
            database.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
