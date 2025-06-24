"""
Enunciado:
Pide al usuario el número de filas y columnas de una matriz y crea una matriz de ceros con esas dimensiones.
Usa un bucle for anidado para pedir al usuario cada uno de los elementos (fila por fila) y almacenarlos.
Al final, imprime la matriz.

"""

filas=int(input(" Introduce el número de filas"))
columnas=int(input(" Introduce el número de columnas"))

matriz=[[0 for _ in range(columnas)]for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = int(input(" Introduce al elemento [{i}],[{j}]: "))

for fila in matriz:
    print(fila)