"""
Trabaja con cadenas de texto para representar expresiones algebraicas:

a) Declara una cadena que represente una matriz: "[[1, 2], [3, 4]]", y extrae la primera fila.
b) Escribe una fórmula con caracteres especiales como "A = B * C' + D\\E".
c) Crea una cadena multilínea que represente un sistema de ecuaciones lineales.
d) Cuenta cuántas veces aparece la variable "x" en una expresión.
e) Convierte una cadena de números en un vector (lista de enteros).
f) Une una lista de partes de una expresión en una sola cadena.
g) Reemplaza todas las apariciones de "x" por "z" en una expresión algebraica.

"""

import ast

#a) Declara una cadena que represente una matriz: "[[1, 2], [3, 4]]", y extrae la primera fila.

cadena = "[[1,2],[3,4]]"

cadena_nueva = cadena[0:2]

matriz = ast.literal_eval(cadena)

primera_fila = matriz[0]

print("Primera fila:", primera_fila)

#b) Escribe una fórmula con caracteres especiales como "A = B * C' + D\\E".

formula = "A = B * C + D // E"

print(formula)

#c) Crea una cadena multilínea que represente un sistema de ecuaciones lineales.

sistema = """x + 2y + z = 23
2x - y + 3z = 10
-3x + 4y - z = 5"""

print("Sistema de ecuaciones:", sistema)

#d) Cuenta cuántas veces aparece la variable "x" en una expresión.

expresion = "x + x^2 - 3x + y = 0"
contador = expresion.count("x")
print("Cantidad de 'x':", contador)


#e) Convierte una cadena de números en un vector (lista de enteros).

cadena_numeros = "12345"
vector = [int(c) for c in cadena_numeros]
print("Vector:", vector)

#f) Une una lista de partes de una expresión en una sola cadena.

partes = ["3x", "+", "2y", "-", "z"]
expresion_unida = " ".join(partes)
print("Expresión unida:", expresion_unida)

#g) Reemplaza todas las apariciones de "x" por "z" en una expresión algebraica.

expresion = "x + y - 2x + 3"
expresion_modificada = expresion.replace("x", "z")
print("Expresión modificada:", expresion_modificada)