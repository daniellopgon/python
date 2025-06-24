"""
Enunciado:

Pide al usuario los coeficientes de una ecuación lineal en dos variables:

ax + by = c

Luego pide un punto (x, y) y determina:

Si el punto satisface la ecuación

Si además x = 0 y y = 0, di "El punto es el origen y satisface la ecuación"

Si no es el origen, di "El punto satisface la ecuación pero no es el origen"

Si no la satisface, imprime "El punto no pertenece a la recta"

"""

a = int(input(" Introduce el valor de a "))
b = int(input(" Introduce el valor de b "))
c = int(input(" Introduce el valor de c "))

x = int(input(" Introduce el valor de x "))
y = int(input(" Introduce el valor de y "))

if a * x + b * y == c:
    print(" El punto satisface la ecuación ")
    if x == 0 and y == 0:
        print(" El punto es el origen y satisface la ecuación ")
    else:
        print(" El punto satisface la ecuación pero no es el origen ")
else:
    print(" El punto no pertenece a la recta ")