"""
Usa diccionarios para representar matrices, vectores y sus propiedades en álgebra lineal:

a) Crea un diccionario con nombres de matrices y su traza.
b) Agrega una nueva entrada con el determinante de una matriz.
c) Elimina una clave que representa una matriz singular.
d) Itera por un diccionario de vectores y muestra su norma.
e) Verifica si un vector dado está como clave en el diccionario.
f) Usa los métodos .keys(), .values() y .items() para recorrer un diccionario de matrices y sus rangos.
g) Muestra solo los vectores cuya norma sea mayor que 5.

"""

import math

# a) Crea un diccionario con nombres de matrices y su traza.

matrices = {
    "matriz1": 6,
    "matriz2": 8,
    "matriz3": 4
}

# b) Agrega una nueva entrada con el determinante de una matriz.
# Suponemos que "matriz2" tiene determinante 16, lo añadimos a otro diccionario para no sobrescribir la traza

determinantes = {
    "matriz2": 16
}

# c) Elimina una clave que representa una matriz singular (una matriz con determinante 0)
# Supongamos que "matriz3" es singular

del matrices["matriz3"]

# d) Itera por un diccionario de vectores y muestra su norma.
# Representamos vectores como tuplas (x, y): por ejemplo, (2, 3) tiene norma sqrt(2² + 3²)

vectores = {
    "v1": (2, 3),
    "v2": (4, 5),
    "v3": (3, 2)
}

for nombre, coordenadas in vectores.items():
    x, y = coordenadas
    norma = math.sqrt(x**2 + y**2)
    print(norma)

# e) Verifica si un vector dado está como clave en el diccionario.

vector_dado = (2, 3)

encontrado = False
for nombre, coords in vectores.items():
    if coords == vector_dado:
        encontrado = True
        print("El vector está en el diccionario con nombre")
        break

if not encontrado:
    print("El vector no está como valor en el diccionario")

# f) Usa .keys(), .values() y .items() en un diccionario de matrices y sus rangos

rangos = {
    "matriz1": 2,
    "matriz2": 3
}

print("Claves (nombres):", list(rangos.keys()))
print("Valores (rangos):", list(rangos.values()))
print("Items (pares):")
for nombre, rango in rangos.items():
    print(f"{nombre}: rango = {rango}")

# g) Muestra solo los vectores cuya norma sea mayor que 5

print("Vectores con norma > 5:")
for nombre, (x, y) in vectores.items():
    norma = math.sqrt(x**2 + y**2)
    if norma > 5:
        print(f"{nombre}: {x, y}, norma = {norma:.2f}")


