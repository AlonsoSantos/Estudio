ErrorDetail = 'Debe digitar una operación válida'
num1 = float(input('Digite primer número: '))
num2 = float(input('Digite segundo número: '))
opcion = input('Digite el número correspondiente o el símbolo de la operación a realizar:\n1: Sumar(+)\n2: Restar(-)\n3: Multiplicar(*)\n4: Dividir(/)\nOperación a realizar: ')
if '1' in opcion or 'Sumar' in opcion or 'sumar' in opcion or '+' in opcion:
    error = False
    resultado = num1+num2
elif '2' in opcion or 'Restar' in opcion or 'restar' in opcion or '-' in opcion:
    error = False
    resultado = num1-num2
elif '3' in opcion or 'Multiplicar' in opcion or 'multiplicar' in opcion or '*' in opcion or 'x' in opcion:
    error = False
    resultado = num1*num2
elif '4' in opcion or 'Dividir' in opcion or 'dividir' in opcion or '/' in opcion:
    if num2 != 0:
        error = False
        resultado = num1/num2
    else:
        error = True
        ErrorDetail = 'No se puede dividir entre cero'
else:
    error = True
if error == False:
    if resultado == int(resultado):
        print('Resultado: ', int(resultado))
    else:
        print('Resultado: ', resultado)
else:
    print(ErrorDetail)
