import time

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [int(line.strip()) for line in data if line.strip().isdigit()]

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >=0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def quick_sort(data):
    def _quick_sort(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)
            _quick_sort(items, low, pivot_index)
            _quick_sort(items, pivot_index + 1, high)

    def partition(items, low, high):
        pivot = items[low]
        left = low + 1
        right = high
        done = False
        while not done:
            while left <= right and items[left] <= pivot:
                left = left + 1
            while items[right] >= pivot and right >=left:
                right = right -1
            if right < left:
                done= True
            else:
                items[left], items[right] = items[right], items[left]
        items[low], items[right] = items[right], items[low]
        return right

    _quick_sort(data, 0, len(data) - 1)

def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        L = data[:mid]
        R = data[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1

def measure_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    return time.time() - start_time

# Exemplo de uso
file_path = "testes/teste.txt"
data_original = read_file(file_path)

# Medindo o tempo para Bubble Sort
data = data_original.copy()
time_taken_bubble = measure_time(bubble_sort, data)
print(f"Tempo para Bubble Sort: {time_taken_bubble} segundos")

# Medindo o tempo para Selection Sort
data = data_original.copy()
time_taken_selection = measure_time(selection_sort, data)
print(f"Tempo para Selection Sort: {time_taken_selection} segundos")

# Medindo o tempo para Insertion Sort
data = data_original.copy()
time_taken_insertion = measure_time(insertion_sort, data)
print(f"Tempo para Insertion Sort: {time_taken_insertion} segundos")

# Medindo o tempo para Quick Sort
data = data_original.copy()
time_taken_quick = measure_time(quick_sort, data)
print(f"Tempo para Quick Sort: {time_taken_quick} segundos")

# Medindo o tempo para Merge Sort
data = data_original.copy()
time_taken_merge = measure_time(merge_sort, data)
print(f"Tempo para Merge Sort: {time_taken_merge} segundos")
