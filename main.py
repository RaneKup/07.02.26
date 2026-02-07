import random
import time

# задача 1
list = []
for _ in range(15):
    list.append(random.randint(1,100))
print(f'лист для сортировки: {list}')
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

start = time.time()
print(f'отсортированый лист: {bubble_sort(list)}')
end = time.time()
start_time = time.time()
list.sort()
end_time = time.time()
print(f'Время пузырьковой сортировки: {end - start}')
print(f'Время .sort(): {end_time - start_time}')
# задача 2
matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]
'''
если указать отрицательное число в переменную shift_num то сдвиг произойдёт влево,
если указать положительное число то сдвиг произойдёт вправо
'''
shift_num = int(input('На сколько хотите выполнить сдвиг: '))
def shift(matrix, n):
    new = []
    for arr in matrix:
        l = len(arr)
        n = n % l
        if n == 0:
            new.append(arr)
        new.append(arr[-n:] + arr[:-n])
    for row in new:
        for el in row:
            print(el, end=" ")
        print()

shift(matrix, shift_num)
# задача 3
# быстрая сортировка лучше для матриц потому что она выполняется "на месте" и имеет высокую скорость
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]

        return quicksort(less) + middle + quicksort(greater)


matrix = [[3, 4, 7], [6, 9, 2], [9, 8, 5]]
print(matrix)
flat_list = [item for row in matrix for item in row]
sorted_list = quicksort(flat_list)
sorted_matrix = [sorted_list[i:i + 3] for i in range(0, len(sorted_list), 3)]

print(sorted_matrix)
# задача 4
def line(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

test_data = [random.randint(0, 100000) for _ in range(100)]

start_time = time.time()
max_lin = line(test_data)
end_time = time.time()
linear_duration = end_time - start_time
print(f"Время: {linear_duration}")

start_time = time.time()
max_bub = bubble_sort(test_data)
end_time = time.time()
bubble_duration = end_time - start_time
print(f"Время: {bubble_duration}")

print(f"\nЛинейный поиск быстрее пузырьковой сортировки в {bubble_duration / linear_duration} раз")