# Ejemplo de Programación Imperativa
# Algoritmo: Ordenamiento Burbuja

# Lista de números que queremos ordenar
numeros = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:")
print(numeros)

# Recorremos la lista varias veces
for i in range(len(numeros)):

    # Comparamos elementos consecutivos
    for j in range(0, len(numeros) - i - 1):

        # Si el elemento actual es mayor que el siguiente,
        # intercambiamos sus posiciones
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Mostramos la lista después del ordenamiento
print("\nLista ordenada:")
print(numeros)
