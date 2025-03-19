def find_max_difference(arr):
    if len(arr) < 2:
        return None  # Недостаточно элементов для нахождения пары

    min_element = arr[0]
    min_i = 0
    max_difference = 0
    j = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
            min_i = i
        else:
            current_difference = arr[i] - min_element
            if current_difference > max_difference:
                max_difference = current_difference
                j = i
    
    return max_difference, min_element, min_i, j

# Пример использования
arr = [3, 1, 4, 6, 5, 2]
result, min_element, i, j = find_max_difference(arr)
print("Максимальная разница:", result)
print(f'Между значениями a[{i}] = {min_element}, a[{j}] = {arr[j]}')
