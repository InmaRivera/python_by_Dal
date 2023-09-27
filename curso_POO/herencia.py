class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f'Mi habilidad es: {self.habilidad}')

# ejemplo herencia multiple


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona().__init__(nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa


# hacemos que herede de persona


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, curso, notas):
        super().__init__(nombre, edad, nacionalidad)
        self.curso = curso
        self.notas = notas


roberto = Empleado("Roberto", 43, "argentino", "Programador", 10000)
print(roberto.nombre)

roberto.hablar()
