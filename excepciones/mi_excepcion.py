# creando mi propia excepcion
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f'Impresionante cometiste el siguiente error: {err}')

        # Lanzando mi propia excepcion
        # raise MiExcepcion("jajajaja, persona poco culta")


        # manejandola
try:
    raise MiExcepcion("jajajaja, persona poco culta")
except:
    print("como vas a crear ese error?")
