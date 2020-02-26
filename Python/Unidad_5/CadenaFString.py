# formato %
# un dato
curso = 'python'
# print('tutoriales de %s'%curso)

# mas de un dato
nombre = 'Alonso'
edad = 21
# print('Hola soy, %s y tengo %s años.'%(nombre,edad))

# --------------------------------------------------------------------------
# formato str.format()
nombre = 'Alonso'
edad = 21
# print('Que tal, soy {} y mi edad es {} años.'.format(nombre,edad))

# --------------------------------------------------------------------------
# formato f-string
nombre = 'Alonso'
edad = 21
# print(f'Hola soy {nombre} y mi edad es {edad} años.')

# --------------------------------------------------------------------------
# ejercicio


class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    # __str__ ejecuta resultados inmediatamente sin ejecutarse en el codigo
    # def __str__(self):
    # __repr__ ejecuta resultados inmediatamente ejecutandose en el codigo
    def __repr__(self):
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}'
nuevoEstudiante = Estudiante('Alonso','Santos',21)
# print(f'{nuevoEstudiante}') # esto es para imprimir desde el metodo __str__
# print(f'{nuevoEstudiante !r}') # esto es para imprimir desde el metodo __repr__