"""
Enunciado:

Pide al usuario un vector en ℝ³ (3 componentes) y determina si:

El vector es nulo (todos sus componentes son 0)

El vector es unitario (su norma es 1)

El vector tiene al menos un componente negativo

Usa operadores lógicos como and, or y not en tus condiciones.

"""

x = int(input(" Introduce el elemento x del vector"))
y = int(input(" Introduce el elemento y del vector"))
z = int(input(" Introduce el elemento z del vector"))

if x == 0 and y == 0 and z == 0:
    print(" El vector es nulo ")
elif x**2 + y**2 + z**2 == 1:
    print(" El vector es unitario ")
elif x < 0 or y < 0 or z < 0:
    print(" El vector tiene un componente negativo ")
else:
    print(" No cumple ninguna condición ")
    
