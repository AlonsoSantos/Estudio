import math
numero = int(input('Digite un número: '))
while numero < 0:
    print('Error: El número debe ser positivo')
    numero = int(input('Digite un número: '))
print(f'\nSu raíz cuadrada es: {(math.sqrt(numero)):.2f}')
'''
    math.sqrt(x) saca la raiz cuadrada del numero
    .2f es para que el resultado sea de solo 2 decimales
'''
i = 0
while i < 10:
    print(i+1)
    i += 1
