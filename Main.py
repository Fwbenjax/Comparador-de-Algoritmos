import random
import time

def bubble_sort(arr):
    n = len(arr)
    steps = 0
    data = list(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return steps

def selection_sort(arr):
    n = len(arr)
    steps = 0
    data = list(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return steps

def insertion_sort(arr):
    steps = 0
    data = list(arr)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            steps += 1
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        steps += 1
    return steps

def shell_sort(arr):
    steps = 0
    data = list(arr)
    n = len(data)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                steps += 1
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
            steps += 1
        gap //= 2
    return steps

def quick_sort_wrapper(arr):
    steps = [0]
    data = list(arr)
    
    def quick_sort(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)
            quick_sort(items, low, pivot_index)
            quick_sort(items, pivot_index + 1, high)

    def partition(items, low, high):
        pivot = items[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while items[i] < pivot:
                i += 1
                steps[0] += 1
            j -= 1
            while items[j] > pivot:
                j -= 1
                steps[0] += 1
            if i >= j:
                return j
            items[i], items[j] = items[j], items[i]
            steps[0] += 1

    quick_sort(data, 0, len(data) - 1)
    return steps[0]

def main():
    try:
        n = int(input("Cantidad de números a generar: "))
        min_val = int(input("Rango inicial: "))
        max_val = int(input("Rango final: "))
    except ValueError:
        print("Error: Ingrese solo números enteros.")
        return

    # Generación de Array
    original_array = [random.randint(min_val, max_val) for _ in range(n)]
    print(f"\nArray generado: {original_array}")

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("shell Sort", shell_sort),
        ("Quick Sort", quick_sort_wrapper),
    ]

    results = []

    for name, func in algorithms:
        start_time = time.perf_counter_ns()
        steps = func(original_array)
        end_time = time.perf_counter_ns()
        
        execution_time = end_time - start_time
        results.append({
            "nombre": name,
            "pasos": steps,
            "tiempo": execution_time
        })

    # Ordenar resultados por tiempo (menor a mayor)
    results.sort(key=lambda x: x["tiempo"])

    # Salida de resultados
    print("\nResultados de la comparación (Ordenados por tiempo):")
    print(f"{'Pos':<5} | {'Algoritmo':<20} | {'Pasos':<12} | {'Tiempo (ns)':<15}")
    print("-" * 60)
    for idx, res in enumerate(results, 1):
        print(f"{idx:<5} | {res['nombre']:<20} | {res['pasos']:<12} | {res['tiempo']:<15}")

if __name__ == "__main__":
    main()