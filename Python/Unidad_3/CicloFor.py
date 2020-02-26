lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)

lista2 = {1, 2, 3, 4, 5}
for i in lista2:
    print(i)

coleccion = {'Alonso': 21, 'Alison': 18, 'Daniela': 20}
# forma 1
for i in coleccion:
    print(f'Elemento: {i} -> {coleccion[i]}')
# forma 2
for clave, valor in coleccion.items():
    print(f'Elemento: {clave} -> {valor}')

cadena = "Alonso"
for i in cadena:
    print(f'{i}', end=" ")
# end sirve para reemplazar el enter por cada print y poner el caracter que yo mismo coloque
