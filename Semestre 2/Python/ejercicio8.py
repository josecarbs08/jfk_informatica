
destino = input("Ingrese el destino (Monterrey, Guadalajara, Cancún): ")
edad = int(input("Ingrese su edad: "))
if destino == "Monterrey":
    pasaje = 950
elif destino == "Guadalajara":
    pasaje = 850    
elif destino == "Cancún":
    pasaje = 1200
else:    print("Destino no válido.")


if edad >= 0 and edad <= 3:
    descuento = 1
elif edad >= 4 and edad <= 11:
    descuento = 0.5
elif edad >= 12 and edad <= 17:
    descuento = 0.7
elif edad >= 18 and edad <= 59:
    descuento = 1
elif edad >= 60:
    descuento = 0.2
else:  
    print("Edad no válida.")
    
total = pasaje * descuento
print(f"El total a pagar por el pasaje a {destino} es: ${total:.2f}")
