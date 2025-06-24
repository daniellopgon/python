"""
Define una función que reciba una matriz y un escalar, y devuelva la matriz resultante de multiplicar cada elemento por ese escalar.
Usa argumentos posicionales y por palabra clave.

Crea una función con un parámetro por defecto que calcule la norma de un vector. Si no se indica el orden, calcula la norma euclídea.

Declara una variable global que represente el número de operaciones realizadas y actualízala desde varias funciones.

Crea dos funciones: una con una variable local llamada matriz, y otra con una global del mismo nombre. Muestra el efecto del name shadowing.

Implementa una función que acepte cualquier número de vectores (como tuplas) y devuelva una lista con sus dimensiones. Usa *args.

"""


"""Define una función que reciba una matriz y un escalar, y devuelva la matriz resultante de multiplicar cada elemento por ese escalar.
Usa argumentos posicionales y por palabra clave."""

def matriz_por_escalar(matriz, escalar=1):
    
    resultado = []
    for fila in matriz:
        nueva_fila = [escalar * elemento for elemento in fila]
        resultado.append(nueva_fila)
    return resultado


matriz = [[1, 2], [3, 4]]
print(matriz_por_escalar(matriz))            
print(matriz_por_escalar(matriz, escalar=3)) 

#Crea una función con un parámetro por defecto que calcule la norma de un vector. Si no se indica el orden, calcula la norma euclídea.

def norma_vector(vector, orden=2):
   
    if orden == 1:
        return sum(abs(x) for x in vector)
    elif orden == 2:
        return sum(x**2 for x in vector) ** 0.5
    else:
        return sum(abs(x)**orden for x in vector) ** (1/orden)


print(norma_vector([3, 4]))         
print(norma_vector([3, 4], orden=1)) 


#Declara una variable global que represente el número de operaciones realizadas y actualízala desde varias funciones.

operaciones_realizadas = 0  

def suma(a, b):
    global operaciones_realizadas
    operaciones_realizadas += 1
    return a + b

def resta(a, b):
    global operaciones_realizadas
    operaciones_realizadas += 1
    return a - b


suma(1, 2)
resta(5, 3)
print("Operaciones realizadas:", operaciones_realizadas)


#Crea dos funciones: una con una variable local llamada matriz, y otra con una global del mismo nombre. Muestra el efecto del name shadowing.

matriz = [[1, 2], [3, 4]] 

def funcion_con_local():
    matriz = [[9, 9]]  
    print("Matriz local:", matriz)

def funcion_con_global():
    print("Matriz global:", matriz)

funcion_con_local()  
funcion_con_global()  

#Implementa una función que acepte cualquier número de vectores (como tuplas) y devuelva una lista con sus dimensiones. Usa *args.

def dimensiones_vectores(*vectores):
    
    return [len(v) for v in vectores]


print(dimensiones_vectores((1, 2), (3, 4, 5), ()))  # [2, 3, 0]
