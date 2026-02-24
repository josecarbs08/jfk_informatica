#Caso de If-elif-else

print("Bienvenido al programa de comidas")
hora = int(input("Introduce la hora (en formato 24 horas): "))

if hora == 8:
    print("Es hora del desayuno")
elif hora == 14:
    print("Es hora de comer")
elif hora == 21:
    print("Es hora de cenar")
else:
    print("No es hora de comer")