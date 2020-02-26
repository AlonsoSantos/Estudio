# la mejor opcion es usar el a (append) para que agregue lo nuevo al final y ya, los demas sobreescriben lo ya existente
variable = open("D:/Estudio/Python/Unidad_6/prueba.txt", "a")
variable.write('\nCarolina - ReactJS')
variable.close()