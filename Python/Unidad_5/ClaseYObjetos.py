# parte 1
# clase: modelo para crear objetos


class Auto:
    marca = ''
    modelo = 0
    placa = ''


taxi = Auto()
# print(taxi.modelo)


# parte 2
class Persona:
    doctor = 'Alonso'
# print(Persona.doctor)


class JugadoresA:
    j1 = 'Messi'
    j2 = 'C.Ronaldo'


class JugadoresB:
    j3 = 'Marcelo'
    j1 = 'Falcao'


# print(JugadoresB.j1)
# ----------------------------------------------------------------------------
class Nombre:
    pass


Alonso = Nombre()
Maria = Nombre()

# objeto.atributo = valor
Alonso.edad = 21
Alonso.sexo = 'Masculino'
Alonso.pais = 'Colombia'

Maria.edad = 20
Maria.sexo = 'Femenino'
Maria.pais = 'Bolivia'

print(Alonso.edad)
print(Maria.edad)
