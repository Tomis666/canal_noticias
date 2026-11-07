from auxiliares.errores import manejar_errores
from negocio.negocio_personas import directorio_personas


@manejar_errores
def mostrar_directorio():
    personas = directorio_personas()
    print('\n=== DIRECTORIO DE PERSONAS ===')
    if not personas:
        print('(sin registros)\n')
        return
    for persona in personas:
        # POLIMORFISMO: Usuario, Autor y Lector responden .descripcion() cada uno a su manera.
        print(f' - {persona.descripcion()}')
    print()
