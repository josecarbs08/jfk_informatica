import random

num = random.randint(0, 9)

print(num)

numin = 0

while numin != num:
    numin = int(input("Ingrese un el numero secreto: "))
    if numin != num:
        print('Incorrecto, vuelva a intentar' )
    else:
        print("")

print("Excelente! Encontraste el numero secreto.")