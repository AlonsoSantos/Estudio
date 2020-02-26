class Animal:
    @staticmethod
    def printMensaje():
        print('¿Cual animal eliges?')

    def setEspecie(self, especie):
        self.especie = especie

    def getEspecie(self):
        return f'Elegiste un animal de la especie: {self.especie}'


class Perro(Animal):
    @staticmethod
    def printMensaje():
        pass

    def setRaza(self, raza):
        self.raza = raza

    def getRaza(self):
        return f'Tu nuevo amigo es un perro de la raza {self.raza}'


class Pez(Animal):
    @staticmethod
    def printMensaje():
        pass

    def setAlimentacion(self, comida):
        self.alimentacion = comida

    def getAlimentacion(self):
        return f'Tu nuevo amigo es un pez y elegiste alimentarlo con {self.alimentacion}'


class Serpiente(Animal):
    @staticmethod
    def printMensaje():
        pass

    def setVenenosa(self, venenosa):
        self.venenosa = venenosa

    def isVenenosa(self):
        return 'Tu nuevo amigo es una serpiente sin veneno' if self.venenosa == False else 'Tu nuevo amigo es una serpiente con veneno\n¡Ten mucho cuidado!'

# declaro el objeto a partir de la clase padre
animal = Animal()
# muestro el mensaje para abrir paso a que el usuario ingrese los datos
animal.printMensaje()
opcion = input('1. Perro\n2. Pez\n3. Serpiente\nIngresa tu selección: ')
while opcion == '' or opcion == None or opcion == ' ':
    print('¡Elige una opción válida!')
    opcion = input('1. Perro\n2. Pez\n3. Serpiente\nIngresa tu selección: ')
# segun la opcion seleccionada ingreso la especie pedida por el objeto de la clase principal
if 'perro' in opcion or '1' in opcion or 'Perro' in opcion:
    animal.setEspecie('Perro')
    print(animal.getEspecie())
    # declaro el objeto de la subclase de la seleccion
    seleccion = Perro()
    raza = input('Ingresa la raza del perro: ')
    while raza == '' or raza == None or raza == ' ':
        print('Ingresa una raza válida')
        raza = input('Ingresa la raza del perro: ')
    # ingreso en una variable el dato que la subclase necesita para poder seguir
    seleccion.setRaza(raza)
    print(seleccion.getRaza())
elif 'pez' in opcion or '2' in opcion or 'Pez' in opcion:
    animal.setEspecie('Pez')
    print(animal.getEspecie())
    # declaro el objeto de la subclase de la seleccion
    seleccion = Pez()
    comida = input('Ingresa lo que darías de comer al pez: ')
    while comida == '' or comida == None or comida == ' ':
        print('Ingresa una comida válida')
        comida = input('Ingresa lo que darías de comer al pez: ')
    # ingreso en una variable el dato que la subclase necesita para poder seguir
    seleccion.setAlimentacion(comida)
    print(seleccion.getAlimentacion())
elif 'serpiente' in opcion or '3' in opcion or 'Serpiente' in opcion:
    animal.setEspecie('Serpiente')
    print(animal.getEspecie())
    # declaro el objeto de la subclase de la seleccion
    seleccion = Serpiente()
    veneno = input('¿La serpiente tendrá veneno?')
    while veneno == '' or veneno == None or veneno == ' ':
        print('Ingresa una opción válida')
        veneno = input('¿La serpiente tendrá veneno? ')
    # ingreso en una variable el dato que la subclase necesita para poder seguir
    if 'si' in veneno or 'Si' in veneno or 'Yes' in veneno or 'yes' in veneno or 'y' in veneno or 'Y' in veneno:
        venenosa = True
    else:
        venenosa = False
    seleccion.setVenenosa(venenosa)
    print(seleccion.isVenenosa())
else:
    print('Fin del programa, no ingresaste ninguna de las opciones dadas')
print('Has terminado')