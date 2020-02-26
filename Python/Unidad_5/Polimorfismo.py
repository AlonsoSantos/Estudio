# teoria
# metodos u objetos con mismo nombre pero que cumplen diferentes funciones
class Auto:
    rueda = 4

    def desplazamiento(self):
        print('el auto se esta desplazando sobre 4 ruedas')


class Moto:
    rueda = 2

    def desplazamiento(self):
        print('la moto se esta desplazando sobre 2 ruedas')


# ejercicio
class Animales:
    def __init__(self, nombre):
        self.nombre = nombre

    def tipoAnimal(self):
        pass


class Leon(Animales):
    def tipoAnimal(self):
        print('Animal salvaje')


class Perro(Animales):
    def tipoAnimal(self):
        print('Animal domestico')


nuevoAnimal = Leon('SIMBA')
nuevoAnimal.tipoAnimal()
nuevoAnimal = Perro('REX')
nuevoAnimal.tipoAnimal()
