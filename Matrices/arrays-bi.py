matriz = [
        [1, 2, 3],
        [4, 5, 6]
        ]

## Mostrar matriz con print solo
print (matriz)

## Mostar matriz con for usando unicamente fila
for fila in matriz:
    print(fila)



## Mostar unicamente una fila de matriz
print(matriz[0])

## Mostrar ultimo valor de matrz
print(matriz[1][2])

## Agregar fila a la matriz
matriz.append([7, 8, 9])
print(matriz)

## Eliminar un valor de la matriz
matriz.pop(matriz[0][2])
print(matriz)
