# creamos objetos
class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
# creando metodos

    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.modelo}')

    def colgar(self):
        print(f'Estas colgando una llamada desde un: {self.modelo}')


# instanciamos objetos
celular1 = Celular("Samsung", "s23", "48MP")
celular2 = Celular("Apple", "Iphone 15", "96MP")

# print(celular1.marca)
# print(celular2.marca)

# mostramos resultado
celular1.llamar()
