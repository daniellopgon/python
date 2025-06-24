"""
1. if, if-else, if-elif, if-elif-else

Enunciado:
Crea un programa que calcule el determinante de una matriz 2x2.
Pide al usuario los 4 elementos de la matriz (a, b, c, d) y calcula el determinante con la fórmula:
det = a * d - b * c

Si el determinante es 0, imprime "La matriz es singular (no invertible)"

Si es diferente de 0, imprime "La matriz es regular (invertible)"

"""

a = (int(input(" Introduce el valor de a: ")))
b = (int(input(" Introduce el valor de b: ")))
c = (int(input(" Introduce el valor de c: ")))
d = (int(input(" Introduce el valor de d: ")))

determinante = a * d - b * c

if determinante == 0:
    print(" La matriz es singular no invertible ")
else:
    print( " La matriz es regular no se puede invertir ")
    

