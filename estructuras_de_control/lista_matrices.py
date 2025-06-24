"""
Crea un programa que recorra una lista de matrices 2x2 (predefinida o ingresada por el usuario).

Si alguna matriz tiene un determinante igual a 0, usa continue para saltarla.

Si una matriz tiene todos sus elementos mayores que 10, usa break y detén el programa.

Si ninguna condición se cumple, imprime la inversa (puedes simplemente imprimir "Inversa calculada" como mensaje simulado).

"""
matriz1 = [[1,2],[2,3]]
matriz2 = [[2,3],[4,5]]
matriz3 = [[6,5],[13,14]]

lista_matrices = [matriz1,matriz2,matriz3]

for matriz in lista_matrices:
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]
    determinante = a * d - b * c

    if determinante == 0:
        print("Determinante 0, se salta la matriz.")
        continue

    if all(element > 10 for fila in matriz for element in fila):
        print("Todos los elementos > 10. Se detiene el programa.")
        break

    print("Inversa calculada para la matriz:", matriz)