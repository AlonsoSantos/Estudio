class Persona:
    pass

    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año

    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre, self.año)

    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre, frase)


doctor = Persona('Alonso', 21)
# print(doctor.descripcion())
# print(doctor.comentario('Hola que tal'))

# modificar atributo


class Email:
    def __init__(self):
        self.enviado = False

    def EnviarCorreo(self):
        self.enviado = True


MiCorreo = Email()
print(MiCorreo.enviado)
MiCorreo.EnviarCorreo()
print(MiCorreo.enviado)
