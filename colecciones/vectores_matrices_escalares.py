"""
Crea una serie de listas en Python para representar vectores, matrices y escalares. Realiza las siguientes operaciones:

a) Representa los vectores [1, 0], [0, 1] y [1, 1] en una lista y muestra el segundo vector.
b) Construye una lista con los escalares del 1 al 10 y extrae los impares.
c) Añade nuevos vectores usando append e insert, luego elimina uno con del.
d) Calcula la norma (módulo) de cada vector en una lista y crea una lista de normas.
e) Comprueba si el vector [0, 0] está en la lista.
f) Genera por comprensión todos los vectores [x, y] tales que x + y = 3 con x, y en 0..3.
g) Declara una matriz 2x2 como lista de listas, accede y modifica un elemento.
h) Clona una lista de vectores y demuestra que son independientes.

"""

import copy
import math

#a) Representa los vectores [1, 0], [0, 1] y [1, 1] en una lista y muestra el segundo vector.

vector1=[1,0]
vector2=[0,1]
vector3=[1,1]

lista_vectores = [vector1,vector2,vector3]

print(lista_vectores[1])

#b) Construye una lista con los escalares del 1 al 10 y extrae los impares.

vectores_resultantes = []

for escalar in range(1,11): 
    for v in lista_vectores:
        resultado = [escalar * a for a in v]
        if all(b % 2 != 0 for b in resultado):
            vectores_resultantes.append(resultado)

print(vectores_resultantes)

#c) Añade nuevos vectores usando append e insert, luego elimina uno con del.

x = int(input(" introduce la x "))
y = int(input(" introduce la y "))

nuevo_vector = [x,y]

lista_vectores.append(nuevo_vector)

print(lista_vectores)

lista_vectores.remove(nuevo_vector)

print(lista_vectores)

#d) Calcula la norma (módulo) de cada vector en una lista y crea una lista de normas.

lista_normas = []

for (x,y) in lista_vectores:
    norma = math.sqrt(x**2 + y**2)
    lista_normas.append(norma)

#e) Comprueba si el vector [0, 0] está en la lista.

if [0][0] in lista_vectores:
    print("Existe")
else:
    print("No existe")

#f) Genera por comprensión todos los vectores [x, y] tales que x + y = 3 con x, y en 0..3.

lista_comprension_vectores=[[x,y] for x in range(4) for y in range(4) if x + y == 3]

print(lista_comprension_vectores)

#g) Declara una matriz 2x2 como lista de listas, accede y modifica un elemento.

matriz = [
        [1,2],
        [5,6]
        ]

print(matriz)

for i in matriz:
    for j in i:
        if(matriz[i][j] == 2):
            matriz[i][j] = 3

print(matriz)

#h) Clona una lista de vectores y demuestra que son independientes.

vectores = [[1, 0], [0, 1]]

copia_vectores = copy.deepcopy(vectores)

print("Original:", vectores)
print("Clonada: ", copia_vectores)

copia_vectores[0][0] = 99

print("Después de modificar la copia:")
print("Original:", vectores)
print("Clonada: ", copia_vectores)