"""
Define una función que reciba una matriz cuadrada y devuelva su traza.

Crea una función generadora que recorra los elementos de la diagonal principal de una matriz.

Escribe una función que calcule el determinante de una matriz 2x2. Devuelve None si no es válida.

Implementa una función recursiva que calcule el producto escalar entre dos vectores de igual longitud.

Diseña una función que devuelva la matriz transpuesta, y otra que la imprima directamente sin devolverla. ¿Cuál es la diferencia entre ambas?

"""

#Define una función que reciba una matriz cuadrada y devuelva su traza.

def traza_matriz(matriz):
    
    es_cuadrada = True
    
    for fila in matriz:
        if len(fila) != len(matriz):
            raise ValueError("La matriz no es cuadrada.")

    filas = len(matriz)
    traza = 0
    
    for i in range(filas):
        traza += matriz[i][i]

    return traza

#Crea una función generadora que recorra los elementos de la diagonal principal de una matriz.

def imprimir_diagonal(matriz):

    for fila in matriz:
        if len(fila) != len(matriz):
            raise ValueError("La matriz no es cuadrada")
    
    filas = len(matriz)
    
    for i in range(filas):
        print(matriz[i][i])


#Escribe una función que calcule el determinante de una matriz 2x2. Devuelve None si no es válida.

def determinante(matriz):

    for fila in matriz:
        
        if len(fila) != len(matriz):
            raise ValueError("No es cuadrada")
    
    det = 0

    for x,y in matriz:
        det = (x1 * x4) + (x2 * x3)

    return det

#Implementa una función recursiva que calcule el producto escalar entre dos vectores de igual longitud.

def producto_escalar(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma longitud")
    
    if not v1: 
        return 0
    else:
        return v1[0] * v2[0] + producto_escalar(v1[1:], v2[1:])


#Diseña una función que devuelva la matriz transpuesta, y otra que la imprima directamente sin devolverla. ¿Cuál es la diferencia entre ambas?

def transpuesta(matriz):
    
    transpuesta = []
    
    columnas = len(matriz[0])
    filas = len(matriz)

    for i in range(columnas):
        fila = []
        for j in range(filas):
             fila.append(matriz[j][i])
        transpuesta.append(fila)

    return transpuesta
        
def imprimir_transpuesta(matriz):

    columnas = len(matriz[0])
    filas = len(matriz)

    for i in range(columnas):
        for j in range(filas):
            print(matriz[j][i], end=" ")
        print()
