def find_max_difference(arr, k):
    if len(arr) < 2:
        return None  # Недостаточно элементов для нахождения пары
    max_sum = 0  
    jnd = 0
    ind = 0
    for i in range(len(arr)-1):
        temp_sum = sum(arr[i:i+k])
        if temp_sum > max_sum:
            max_sum = temp_sum
            ind = i
    jnd = ind + k
        
    return max_sum, ind, jnd
# Пример использования
k = 3 # Корректно только для k>0
arr = [15, 1, 4, 6, 5, 3]
result, i, j = find_max_difference(arr, k)
print(f'Максимальная сумма чисел отрезка длиной {k} = {result}')
print(f'На отрезки ({i};{j})')
