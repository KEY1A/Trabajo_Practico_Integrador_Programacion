import time
import random


# Algoritmos de Búsqueda

# Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Búsqueda binaria (requiere lista ordenada)
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Algoritmos de Ordenamiento

# Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Quick Sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quick_sort(izquierda) + centro + quick_sort(derecha)

# Función auxiliar para medir tiempos

def medir_tiempo(funcion, *args):
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()
    return resultado, fin - inicio

# Programa principal de prueba

if __name__ == "__main__":
    # Crear una lista grande con 10,000 números aleatorios
    tamano = 10_000
    lista_original = [random.randint(1, 100_000) for _ in range(tamano)]
    objetivo = lista_original[tamano // 2]  # Usamos un número que sabemos que está

    print("\nORDENAMIENTO")

    # Bubble Sort 
    lista_copia = lista_original.copy()
    _, tiempo_bubble = medir_tiempo(bubble_sort, lista_copia)
    print(f"Bubble Sort: {tiempo_bubble:.4f} segundos")

    # Quick Sort
    lista_copia = lista_original.copy()
    lista_ordenada, tiempo_quick = medir_tiempo(quick_sort, lista_copia)
    print(f"Quick Sort: {tiempo_quick:.4f} segundos")

    print("\nBÚSQUEDA")

    # Búsqueda Lineal
    _, tiempo_lineal = medir_tiempo(busqueda_lineal, lista_original, objetivo)
    print(f"Búsqueda Lineal: {tiempo_lineal:.6f} segundos")

    # Búsqueda Binaria 
    _, tiempo_binaria = medir_tiempo(busqueda_binaria, lista_ordenada, objetivo)
    print(f"Búsqueda Binaria: {tiempo_binaria:.6f} segundos")

    print("\nCONCLUSIÓN")
    print("• Quick Sort fue más eficiente que Bubble Sort.")
    print("• Búsqueda Binaria fue más rápida que la lineal, pero requiere una lista ordenada.")