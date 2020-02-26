def suma(num1, num2, num3):
    return num1+num2+num3


def division(num1, num2):
    return num1/num2


def multiplicacion(num1, num2):
    return num1*num2


def multiplesValores():
    return 'String', 1, True, 25.6


def mostrarResultado(funcion):
    print(funcion(6, 8))


resultado1 = suma(10, 20, 30)
# forma 1
resultado2 = division(num2=10, num1=100)
# forma 2
resultado2 = division(100, 10)
resultado3 = multiplicacion(6, 10)
resultado4 = multiplesValores()
# Python asigna a las variables en el orden que retornan los valores
string, entero, bol, floa = multiplesValores()

miVariable = multiplicacion
mostrarResultado(miVariable)
