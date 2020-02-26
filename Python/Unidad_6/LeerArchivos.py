# r = read(solo lectura)
# w = write(realmente crea el archivo, si ya existe uno con el mismo nombre lo sobreescribe eliminando el anterior)
# a = append(agregar elementos o informacion)
# r+ = read/write(lectura y escritura)
variable = open("D:/Estudio/Python/Unidad_6/prueba.txt", "r") # abrir archivo
# print(variable.read()) # lee todo el archivo
# print(variable.readline()) #lee la primera linea
# print(variable.readlines()) # muestra todo el documento como una lista en array segun cada salto de linea
# for datos in variable:
#     print(datos)
# python solo utiliza el .read .readline .readlines una vez porque internamente vacia el archivo(solo para el uso de esto, en el documento no lo elimina)
variable.close() # cerrar archivo