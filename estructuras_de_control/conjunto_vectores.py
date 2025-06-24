"""
Dado un conjunto de vectores en ℝ² (lista de tuplas como [(1,2), (3,4), (0,0)]), itera sobre ellos y calcula su norma.
Imprime el vector con mayor norma y su valor.
Usa la fórmula: norma = sqrt(x² + y²)

"""

import math


vectores = [(1,2),(3,4),(0,0)]

vector_mayor = (0,0)
mayor_norma = 0

for x, y in vectores:
    norma = math.sqrt(x**2 + y**2)
    print(f"Vector: ({x}, {y}) - Norma: {norma:.2f}")
    if norma > mayor_norma:
        mayor_norma = norma
        vector_mayor = (x, y)

print(f"Vector con mayor norma: {vector_mayor} (Norma: {mayor_norma:.2f})")