# Идея в том, чтобы проверить, можно ли получить отсортированную последовательность, используя только стек как вспомогательное хранилище. 
# Это аналог классической задачи "можно ли получить перестановку с помощью стека". 
# Мы сравниваем контейнеры в порядке поступления с ожидаемой (отсортированной) последовательностью и "выгружаем" контейнеры из стека, если они совпадают с ожидаемыми.

def can_sort_containers(test_cases):
    results = []  # Список для хранения результатов каждого теста

    for case in test_cases:
        k, *containers = case  # k — количество контейнеров, containers — список степеней срочности
        stack = []  # Стек (склад) для временного хранения контейнеров
        expected = sorted(containers)  # Ожидаемый порядок контейнеров — отсортированный список
        index = 0  # Индекс текущего ожидаемого контейнера для выхода в цех B

        # Перебираем контейнеры в порядке их поступления
        for container in containers:
            stack.append(container)  # Перемещаем контейнер на склад (в стек)

            # Пока верхний контейнер на складе совпадает с ожидаемым, выгружаем его в цех B
            while stack and stack[-1] == expected[index]:
                stack.pop()  # Удаляем верхний контейнер со склада (он уходит в цех B)
                index += 1  # Переходим к следующему ожидаемому контейнеру

        # Если после всех операций склад пуст — удалось отсортировать, иначе — нет
        results.append(1 if not stack else 0)

    return results  # Возвращаем список результатов для всех тестов


# 1 тестовый пример
input_data = """2
2 2.9 2.1
3 5.6 9.0 2.0""".strip().split('\n')
N = int(input_data[0])  # Количество тестов
# Преобразуем строки тестов в список чисел
test_cases = [list(map(float, line.split())) for line in input_data[1:N+1]]

# 2 тестовый пример
input_data2 = """3
3 1.2 3.4 2.5
4 5.0 4.2 6.1 3.3
2 7.7 7.7""".strip().split('\n')
N2 = int(input_data2[0])
test_cases2 = [list(map(float, line.split())) for line in input_data2[1:N2+1]]

# Вывод результатов
# print('test1')
# for result in can_sort_containers(test_cases):
#     print(result)

# print('test2')
# for result in can_sort_containers(test_cases2):
#     print(result)

# Дополнительные тесты

input_data3 = """4
3 3.0 2.0 1.0        
3 1.0 2.0 3.0       
3 2.0 1.0 3.0
3 2.0 3.0 1.0
""".strip().split('\n')
    # 1 — контейнеры уже в обратном порядке, можно выгрузить через стек
    # 1 — контейнеры уже отсортированы, проходят напрямую
    # 1 — можно: 2 -> склад, 1 -> цех, затем 2 -> цех, потом 3
    # 0 — нельзя: 2 окажется под 3 на складе и не сможет выйти раньше
N3 = int(input_data3[0])
test_cases3 = [list(map(float, line.split())) for line in input_data3[1:N3+1]]

print('test3')
for result in can_sort_containers(test_cases3):
    print(result)

input_data4 = """6
1 42.0               
2 5.5 5.5            
3 3.0 3.0 3.0                  
5 1.0 2.0 3.0 4.0 5.0         
5 5.0 4.0 3.0 2.0 1.0          
5 3.0 1.0 2.0 5.0 4.0
""".strip().split('\n')
    # 1 — всего один контейнер, всегда можно
    # 1 — одинаковые, порядок уже "отсортирован"
    # 1 — все одинаковые, допускается
    # 1 — уже отсортированы
    # 1 — в обратном порядке, стек справится

N4 = int(input_data4[0])
test_cases4 = [list(map(float, line.split())) for line in input_data4[1:N4+1]]

print('test4')
for result in can_sort_containers(test_cases4):
    print(result)
