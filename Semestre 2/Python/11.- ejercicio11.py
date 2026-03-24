fila = int(input('Ingrese el numero de filas que desa imprimir: '))

for i in range(fila, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()