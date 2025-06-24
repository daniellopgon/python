"""
Escribe un programa que intente calcular la inversa de una matriz cuadrada. Usa try-except para manejar errores si la matriz es singular.

Crea una función que contenga un bloque try-except con varias ramas ordenadas (por ejemplo: ZeroDivisionError, ValueError, Exception).

Haz una función que llame a otra, la cual lanza una excepción. Muestra cómo la excepción se propaga entre funciones.

Desarrolla una función que delegue el manejo de errores a una función externa.

Crea un programa que permita ingresar datos de una matriz desde consola y maneje cualquier excepción que ocurra en el proceso de entrada.

"""

#Escribe un programa que intente calcular la inversa de una matriz cuadrada. Usa try-except para manejar errores si la matriz es singular.

import numpy as np

def calcular_inversa(matriz):
    try:
        inversa = np.linalg.inv(matriz)
        print("Inversa de la matriz:")
        print(inversa)
    except np.linalg.LinAlgError:
        print("Error: La matriz es singular y no tiene inversa.")
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

if __name__ == "__main__":
    
    A = np.array([
        [2, 1],
        [5, 3]
    ])

    calcular_inversa(A)



#Crea una función que contenga un bloque try-except con varias ramas ordenadas (por ejemplo: ZeroDivisionError, ValueError, Exception).

def manejo_de_errores(valor):
    try:
        resultado = 10 / int(valor)
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Error: División por cero.")
    except ValueError:
        print("Error: Valor inválido. Se esperaba un número.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

manejo_de_errores("0")    
manejo_de_errores("abc")  


#Haz una función que llame a otra, la cual lanza una excepción. Muestra cómo la excepción se propaga entre funciones.

def funcion_interna():
    raise ValueError("¡Ocurrió un error en la función interna!")

def funcion_externa():
    try:
        funcion_interna()
    except ValueError as e:
        print("Excepción capturada en la función externa:", e)

funcion_externa()


#Desarrolla una función que delegue el manejo de errores a una función externa.

def manejar_error(e):
    print(f"Manejo externo del error: {e}")

def funcion_con_error():
    try:
        x = 1 / 0
    except Exception as e:
        manejar_error(e)

funcion_con_error()


#Crea un programa que permita ingresar datos de una matriz desde consola y maneje cualquier excepción que ocurra en el proceso de entrada.

def pedir_entero(mensaje):

    entrada = input(mensaje)
    return int(entrada)

def pedir_fila(numero_fila, columnas):
   
    entrada = input(f"Ingrese {columnas} valores para la fila {numero_fila} (separados por espacios): ")

    entrada_limpia = entrada.strip()
    partes = entrada_limpia.split()

    if len(partes) != columnas:
        raise ValueError(f"Se esperaban {columnas} valores, pero se recibieron {len(partes)}.")

    elementos = []
    for parte in partes:
        elementos.append(int(parte))

    return elementos

def ingresar_datos():
    
    matriz = []
    try:
        filas = pedir_entero("Ingrese el número de filas: ")
        columnas = pedir_entero("Ingrese el número de columnas: ")

        for i in range(filas):
            fila = pedir_fila(i + 1, columnas)
            matriz.append(fila)

        print("\nMatriz ingresada correctamente:")
        for fila in matriz:
            print(fila)

        return matriz

    except ValueError as e:
        print("Error de valor:", e)
    except Exception as e:
        print("Ocurrió un error inesperado:", e)


if __name__ == "__main__":
    ingresar_datos()

