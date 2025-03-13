def can_sort_containers(test_cases):
    results = []
    for case in test_cases:
        k, *containers = case
        stack = []
        expected = sorted(containers)  # Ожидаемый порядок контейнеров
        index = 0

        for container in containers:
            stack.append(container)
            while stack and stack[-1] == expected[index]:
                stack.pop()
                index += 1

        results.append(1 if not stack else 0)
    
    return results

# 1 тестовый пример
input_data = """2
2 2.9 2.1
3 5.6 9.0 2.0""".strip().split('\n')
N = int(input_data[0])
test_cases = [list(map(float, line.split())) for line in input_data[1:N+1]]

# 2 тестовый пример
input_data2 = """3
3 1.2 3.4 2.5
4 5.0 4.2 6.1 3.3
2 7.7 7.7""".strip().split('\n')
N2 = int(input_data2[0])
test_cases2 = [list(map(float, line.split())) for line in input_data2[1:N2+1]]

# Вывод результатов
print('test1')
for result in can_sort_containers(test_cases):
    print(result)
  
print('test2')
for result in can_sort_containers(test_cases2):
    print(result)
