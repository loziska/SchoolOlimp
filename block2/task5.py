def find_subarray_with_sum(arr, k):
    n = len(arr)
    sum_dict = {}  # Словарь для хранения промежуточных сумм
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]

        # Если текущая сумма равна k, возвращаем границы [0, i]
        if current_sum == k:
            return (0, i)

        # Если (current_sum - k) есть в словаре, возвращаем границы [sum_dict[current_sum - k] + 1, i]
        if (current_sum - k) in sum_dict:
            return (sum_dict[current_sum - k] + 1, i)

        # Сохраняем текущую сумму в словаре
        sum_dict[current_sum] = i

    return None  # Если подмассив с суммой k не найден

# Пример использования
arr = [10, 2, -2, -20, -5, 5, 40]
k = 20

result = find_subarray_with_sum(arr, k)

if result:
    print(f"Фрагмент с суммой {k} находится на отрезке ({result[0]}; {result[1]})")
else:
    print(f"Фрагмент с суммой {k} не найден")
