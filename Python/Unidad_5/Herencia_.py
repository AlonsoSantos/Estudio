# ----------------------------------------------------------------------------------------
# teoria


class Pokemon:
    pass

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre, self.tipo)


class Pikachu(Pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)


class Charmander(Pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)


# al llamar a una clase hijo toca llenar los datos que el metodo constructor de la clase padre para que sirva
nuevoPokemon = Pikachu('Boby', 'Electrico')
# print(nuevoPokemon.descripcion())
# print(nuevoPokemon.ataque('Impacto trueno'))

# ----------------------------------------------------------------------------------------
# ejercicio


class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresarDato(self):
        self.datos = [int(input('Ingresar dato '+str(i+1)+' = '))
                      for i in range(self.n)]


class OperacionesBasicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a, b, = self.datos
        s = a+b
        print('El resultado es:', s)

    def resta(self):
        a, b, = self.datos
        r = a-b
        print('El resultado es:', r)

    def multiplicacion(self):
        a, b, = self.datos
        m = a*b
        print('El resultado es:', m)

    def division(self):
        a, b, = self.datos
        d = a/b
        print('El resultado es:', d)


class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math
        a, = self.datos
        print('El resultado es:', math.sqrt(a))


objeto = OperacionesBasicas()

# ----------------------------------------------------------------------------------------
# pruebas

# isinstance(obj,class) verifica la herencia
# print(isinstance(objeto,OperacionesBasicas)) #True
# print(isinstance(objeto,Raiz)) #False

# issubclass(class,class) verifica si el primer dato es subclase del segundo dato
# print(issubclass(Calculadora, OperacionesBasicas))  # False
# print(issubclass(OperacionesBasicas, Calculadora))  # True

# ----------------------------------------------------------------------------------------
# herencia multiple


class Telefono:
    def __init__(self):
        pass

    def llamar(self):
        print('LLamando...')

    def ocupado(self):
        print('Ocupado...')


class Camara:
    def __init__(self):
        pass

    def fotografia(self):
        print('Tomando fotos...')


class Reproduccion:
    def __init__(self):
        pass

    def reproduccionDeMusica(self):
        print('Reproduciendo música')

    def reproduccionDeVideo(self):
        print('Reproduciendo video')


class Smartphone(Telefono, Camara, Reproduccion):
    def __del__(self): # este metodo en lugar de ser constructor, es destructor para que se puedan usar las otras clases sin problema
        print('Telefono apagado')


movil = Smartphone()
# dir(obj) revisa que tipo de metodos se puede hacer con el objeto que se creo
# dir(obj) hace lo mismo que __dict__.keys()
print(movil.llamar())