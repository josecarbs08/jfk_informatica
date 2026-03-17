print('Conocer la solucion de una ecuacion de primer grado')
print('La base de la ecuacion es ax + b = 0')

a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))

x = -b / a


if a == 0 and b != 0:
    print('La ecuacion no tiene solucion')

elif a == 0 and b == 0:
    print('La ecuacion tiene infinitas soluciones')
else:
    print('La ecuacion tiene una solucion unica')
    print('La solucion de la ecuacion es x =', x)

