def find_max_difference(arr, k):
    if len(arr) < 2:
        return None  
    max_diff = 0  
    jnd = 0
    ind = 0
  
    for i in range(len(arr)-1):
        if i + k - 1 > len(arr):
            k -= 1
        diff = arr[i] - max(arr[i+1:i+k])
        if diff < max_diff:
            max_diff = diff
            ind = i
    
    for i in range(1,k):
        if arr[ind] - arr[ind+i] == max_diff:
            jnd = ind+i
        
    return max_diff, ind, jnd

k = 3
arr = [3, 1, 4, 6, 5, 3]
result, i, j = find_max_difference(arr, k)
print("Максимальная разница:", result)
print(f'Между значениями a[{i}] = {arr[i]}, a[{j}] = {arr[j]}')
