# funcion
class Tomate:
    def tipo(self):
        print('Vegetal')

    def color(self):
        print('Rojo')


class Manzana:
    def tipo(self):
        print('Fruta')

    def color(self):
        print('Verde')


def funcion(objeto):
    objeto.tipo()
    objeto.color()


nuevoTomate = Tomate()
# funcion(nuevoTomate)

nuevaManzana = Manzana()
# funcion(nuevaManzana)


# --------------------------------------------------------------------------
# metodos
class Colombia:
    def capital(self):
        print('Bogotá')

    def idioma(self):
        print('Español')


class Francia:
    def capital(self):
        print('Paris')

    def idioma(self):
        print('Frances')


# toca con 2 objetos para que funcione bien
colombiano = Colombia()
frances = Francia()
# for pais in (colombiano, frances):
#     pais.capital()
#     pais.idioma()


# --------------------------------------------------------------------------
# herencia
class Aves:
    def volar(self):
        print('La mayoria de las aves pueden volar pero algunas no')


class Aguila(Aves):
    def volar(self):
        print('Las aguilas pueden volar')


class Gallina(Aves):
    def volar(self):
        print('Las gallinas no pueden volar')


objAve = Aves()
objAguila = Aguila()
objGallina = Gallina()
objAve.volar()
objAguila.volar()
objGallina.volar()