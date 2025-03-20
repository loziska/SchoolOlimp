def find_max_subarray(arr):
    if not arr:
        return None  

    max_sum = float('-inf') 
    current_sum = 0  
    start = 0  
    end = 0  
    temp_start = 0  
    
    if max(arr) < 0:
        max_element = max(arr)
        index = arr.index(max_element)
        return (index, index, max_element)
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        # Если текущая сумма больше максимальной, обновляем максимальную сумму и границы
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        # Если текущая сумма становится отрицательной, сбрасываем её и начинаем новый фрагмент
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return (start, end, max_sum)

arr = [-2, -4, -3, -114, -1, -2, -6, -3, -6]
result = find_max_subarray(arr)
print("Границы фрагмента:", result[0], "до", result[1])
print("Максимальная сумма:", result[2])
