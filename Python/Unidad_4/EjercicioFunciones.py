def ejercicio1():
    def coordenadaZ(x, y):
        x = x+10
        y = y+15
        return x+y
    # programa principal
    x = int(input('Coordenada eje x: '))
    y = int(input('Coordenada eje y: '))
    for i in range(3):
        z = coordenadaZ(x, y)
        x += 1
        y += 1
    print(x, ".", y)


def ejercicio2():
    def maximo(a, b):
        if a > b:
            return a
        else:
            return b

    def minimo(a, b):
        if a < b:
            return a
        else:
            return b
    # programa principal
    x = int(input('Un número: '))
    y = int(input('Otro número: '))
    print(maximo(x-3, minimo(x+2, y-5)))

'''
    NOTA: si en una funcion no se usan las variables que estan dentro de la funcion Python busca tales variables en el global haciendo que tire un resultado erroneo
    RECOMENDACION: usar funciones en archivos diferentes para evitar errores como lo de la nota anterior y se importa para poder usarlas sin problema (from funciones import *)
    http://pythontutor.com/visualize.html#mode=edit
    sirve para ver linea a linea lo que hace el fragmento de código
'''
