print("Bienvenido al programa de signos zodiacales")
dia = int(input("Ingrese el día de su nacimiento (1-31): "))
mes = int(input("Ingrese el mes de su nacimiento (1-12): "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    print("Tu signo zodiacal es Aries")
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    print("Tu signo zodiacal es Tauro")
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    print("Tu signo zodiacal es Géminis")
elif (mes == 6 and dia >= 21) or (mes == 7 and
        dia <= 22):
        print("Tu signo zodiacal es Cáncer")    

elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    print("Tu signo zodiacal es Leo")
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    print("Tu signo zodiacal es Virgo")
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    print("Tu signo zodiacal es Libra")
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    print("Tu signo zodiacal es Escorpio")
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    print("Tu signo zodiacal es Sagitario")
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    print("Tu signo zodiacal es Capricornio")
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    print("Tu signo zodiacal es Acuario")
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    print("Tu signo zodiacal es Piscis")
else:
    print("Fecha de nacimiento no válida. Por favor, ingrese una fecha correcta.")

