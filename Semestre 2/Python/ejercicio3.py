#Caso con match case

print("Bienvenido al programa de comidas")
hora = int(input("Ingrese la hora del día en formato de 24 horas: "))

match hora:
    case 8:
        print("Es hora del desayuno")
    case 14:
        print("Es hora de la comida")
    case 21:
        print("Es hora de la cena")
    case _:
        print("No es hora de comer")