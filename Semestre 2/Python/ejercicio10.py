filas = int(input("Ingrese el número de filas que desea que su piramide tenga: "))

for i in range(1, filas + 1, 1):
    for j in range(1, i + 1, 1):
        print("*", end="")
    print()

