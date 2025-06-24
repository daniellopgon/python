"""
Simula un error de tipo ArithmeticError al calcular el inverso multiplicativo de 0, y captura la excepción.

Crea una función que intente acceder a una posición inexistente de un vector. Controla la excepción IndexError.

Simula un diccionario que represente una matriz dispersa. Lanza una excepción KeyError si se accede a una posición no definida.

Crea una función que solo acepte listas como vectores. Si se pasa otro tipo, lanza TypeError.

Diseña una función que convierta elementos de una lista en enteros y capture errores del tipo ValueError al fallar.

"""

#Simula un error de tipo ArithmeticError al calcular el inverso multiplicativo de 0, y captura la excepción.

def inverso_multiplicativo(a):
    if a == 0:
        raise ArithmeticError("No se puede calcular el inverso multiplicativo de 0.")
    return 1 / a

try:
    resultado = inverso_multiplicativo(0)
    print("Inverso:", resultado)
except ArithmeticError as e:
    print("Error atrapado:", e)


#Crea una función que intente acceder a una posición inexistente de un vector. Controla la excepción IndexError.

vector = [1, 2]

def acceder_posicion(indice):
    try:
        return vector[indice]
    except IndexError:
        print("Error: índice fuera de rango.")

acceder_posicion(5)


#Simula un diccionario que represente una matriz dispersa. Lanza una excepción KeyError si se accede a una posición no definida.

# Matriz dispersa representada como diccionario
dic = {
    (0, 3): 5,
    (2, 1): 7
}

def posicion_dic(fila, columna):
    try:
        return dic[(fila, columna)]
    except KeyError:
        print(f"Error: la posición ({fila}, {columna}) no está definida en la matriz.")

print("Valor:", posicion_dic(0, 3))

posicion_dic(1, 1)


#Crea una función que solo acepte listas como vectores. Si se pasa otro tipo, lanza TypeError.

def solo_lista(vector):
    if not isinstance(vector, list):
        raise TypeError("Se esperaba una lista.")
    print("Vector válido:", vector)

try:
    solo_lista((1, 2))  
except TypeError as e:
    print("Error de tipo:", e)


#Diseña una función que convierta elementos de una lista en enteros y capture errores del tipo ValueError al fallar.

def convertir_a_enteros(lista):
    for elemento in lista:
        try:
            numero = int(elemento)
            print(f"Convertido: {numero}")
        except ValueError:
            print(f"Error: '{elemento}' no se puede convertir a entero.")


convertir_a_enteros(["10", "20", "abc", "5.5", "30"])
