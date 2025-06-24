"""
Pide al usuario una lista de 3 vectores en ℝ².

Verifica con un bucle for si todos son linealmente independientes (usa determinantes de pares para comprobarlo).

Si detectas dependencia lineal en algún par, usa break y muestra "Hay dependencia"

Si el bucle termina sin break, muestra con else "Son independientes entre sí"

"""

vectores = []

for i in range(3):
    x = int(input("Introduce el eje x: "))
    y = int(input("Introduce el eje y: "))
    vectores.append((x, y))

for i in range(3):
    for j in range(i + 1, 3):
        x1, y1 = vectores[i]
        x2, y2 = vectores[j]
        det = x1 * y2 - y1 * x2
        if det == 0:
            print("Hay dependencia")
            break
    else:
        continue  
    break  
else:
    print("Son independientes entre sí")


