'''
    And (Conjunción) --> and
    Or (Disyunción) --> or
    Negación --> not
'''

'''
    Prioridad
    1- NOT
    2- AND
    3- OR
'''

# a = 10
# b = 12
# c = 13
# d = 10
# print(((a > b)or(a < c)) and ((a == c) or (a >= b)))

'''
    Prioridad general
    1- ()
    2- **
    3- *,/,%,not
    4- +,-,and
    5- >,<,==,>=,<=,!=,or
'''

a = 10
b = 15
c =20
resultado1 = ((a<b) and (b<c))
resultado2 = ((a>b) and (b<c))
resultado3 = ((a>b) or (b<c))
resultado4 = not((a>b) or (b<c))
print(resultado4)