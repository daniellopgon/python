"""
Utiliza tuplas para representar elementos constantes del álgebra lineal y compáralas con listas:

a) Crea una tupla con los vectores base (1, 0) y (0, 1). Muestra el primero y el último.
b) Usa slicing para extraer los escalares positivos de una tupla (-2, -1, 0, 1, 2).
c) Intenta modificar un elemento en una lista y en una tupla, y explica la diferencia.
d) Crea una tupla que contenga una lista representando una matriz 2x2. Modifica la lista interna.
e) Crea una lista de tuplas, donde cada tupla representa un vector 2D. Imprime solo los valores de x.

"""

#a) Crea una tupla con los vectores base (1, 0) y (0, 1). Muestra el primero y el último.

tupla = ((1,0),(0,1))

print(tupla[0])

print(tupla[1])

#b) Usa slicing para extraer los escalares positivos de una tupla (-2, -1, 0, 1, 2).

tupla_negativos = ((-2,-1),(0,1),(1,2))

tupla_positivos = tupla_negativos[3:]

print(tupla_positivos)

#c) Intenta modificar un elemento en una lista y en una tupla, y explica la diferencia.

lista = [1,2,3,4,5]
tupla_prueba = ((3,4),(8,9))

lista[2]=4

#La tupla no se puede es inmutable

print(lista)

#d) Crea una tupla que contenga una lista representando una matriz 2x2. Modifica la lista interna.

matriz = [[1,2],[2,3],[6,7],[8,9]]
tupla_matriz = (matriz,)

tupla_matriz[0][0][1] = 99

print(tupla_matriz)

# e) Crea una lista de tuplas, donde cada tupla representa un vector 2D. Imprime solo los valores de x.

tupla_lista_x = [(1,2),(6,7)]

for vector in tupla_lista_x:
    print(vector[0])