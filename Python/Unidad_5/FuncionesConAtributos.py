class Persona:
    edad = 21
    nombre = 'Alonso'
    pais = 'Colombia'


doctor = Persona()
# print('La edad es:',doctor.edad)
# print('La edad es:',getattr(doctor,'edad')) # getattr(obj,atr) muestra el atributo especifico que se ingrese
# print('¿El doctor tiene una edad?', hasattr(doctor,'edad')) # hasattr(obj,atr) comprueba la existencia de un atributo
# ----------------------------------------------------------------------------------------------------
# print(doctor.nombre)
# setattr(doctor,'nombre','Odair') # setattr(obj, atr, val) sirve para cambiar el valor de un atributo
# print(doctor.nombre)
# ----------------------------------------------------------------------------------------------------
# delattr(Persona,'pais') # delattr(class,atr) elimina un atributo de la clase
# print(doctor.pais)
