# metodo de clase
import math


class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'Pastel({self.ingredientes !r})'
    # cuando se usa @classmethod el metodo no lleva self, en su lugar lleva cls
    @classmethod  # Esto dice que los valores del metodo son independientes
    def PastelChocolate(cls):
        return cls(['Harina', 'Leche', 'Chocolate'])

    @classmethod
    def PastelVainilla(cls):
        return cls(['Harina', 'Leche', 'Vainilla'])
# print(Pastel.PastelChocolate())


# ---------------------------------------------------------------------------------------
# metodo estatico


class Pastel:
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño

    def __repr__(self):
        return f'Pastel({self.ingredientes}, 'f'{self.tamaño})'

    def area(self):
        return self.tamañoArea(self.tamaño)
    # el staticmethod es independiente, no necesita self ni cls
    @staticmethod
    def tamañoArea(A):
        return A ** 2 * math.pi


nuevoPastel = Pastel(['Harina','Azucar','Leche','Crema'],4)
print(nuevoPastel.tamañoArea(4)) # Los datos que se mandan a algun metodo estatico son unicos, no se usan en ninguna orta parte