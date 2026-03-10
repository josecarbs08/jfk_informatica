print('Conozca si un año es bisiesto o no')
year = int(input('Ingrese el año: '))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('El año es bisiesto')
else:
    print('El año ingresado no es bisiesto')

