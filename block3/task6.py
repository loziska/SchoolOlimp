def knapsack(weights, costs, max_weight):
    n = len(weights)  # Количество предметов

    # Создаем двумерный массив dp размером (n+1) x (max_weight+1),
    # где dp[i][j] будет хранить максимальную стоимость при выборе из первых i предметов и вместимости рюкзака j
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    # Заполнение таблицы динамического программирования
    for i in range(1, n + 1):  # Перебираем предметы
        for j in range(max_weight + 1):  # Перебираем возможные веса от 0 до max_weight
            if weights[i - 1] <= j:
                # Если текущий предмет можно положить в рюкзак (по весу),
                # то выбираем максимум между:
                # 1. Не брать этот предмет: dp[i-1][j]
                # 2. Взять этот предмет: dp[i-1][j - вес предмета] + его стоимость
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + costs[i - 1])
            else:
                # Иначе, предмет слишком тяжелый и мы не можем его взять
                dp[i][j] = dp[i - 1][j]

    # Восстановление оптимального набора предметов по таблице dp
    res_weight = max_weight  # Начинаем с полной вместимости рюкзака
    selected_items = []  # Список выбранных предметов (индексы)

    # Идем в обратном порядке, чтобы выяснить, какие предметы были выбраны
    for i in range(n, 0, -1):
        # Если значение изменилось — предмет был выбран
        if dp[i][res_weight] != dp[i - 1][res_weight]:
            selected_items.append(i - 1)  # Добавляем индекс предмета (индексация с 0)
            res_weight -= weights[i - 1]  # Уменьшаем оставшийся вес рюкзака

    selected_items.reverse()  # Переворачиваем список, чтобы получить порядок выбора

    return dp[n][max_weight], selected_items  # Возвращаем максимальную стоимость и список предметов


# Пример использования:
weights = [3, 2, 1, 4]      # Веса предметов
costs = [5, 3, 2, 7]        # Стоимости предметов
max_weight = 5             # Максимальный допустимый вес рюкзака

max_cost, items = knapsack(weights, costs, max_weight)

print("Максимальная стоимость:", max_cost)
print("Выбранные предметы (индексы):", items)


test_num = 0
test_num += 1
print(f'Test {test_num}:')
# 1. Пустой рюкзак (нет предметов)
weights = []  
costs = []  
max_weight = 10  

max_cost, items = knapsack(weights, costs, max_weight)  

print("Максимальная стоимость:", max_cost)  # Ожидаем 0  
print("Выбранные предметы (индексы):", items)  # Ожидаем []  

test_num += 1
print(f'Test {test_num}:')
# 2. Нулевая вместимость рюкзака
weights = [1, 2, 3]  
costs = [10, 20, 30]  
max_weight = 0  

max_cost, items = knapsack(weights, costs, max_weight)  

print("Максимальная стоимость:", max_cost)  # Ожидаем 0  
print("Выбранные предметы (индексы):", items)  # Ожидаем []  

test_num += 1
print(f'Test {test_num}:')
# 3. Один предмет, который можно взять
weights = [5]  
costs = [10]  
max_weight = 5  

max_cost, items = knapsack(weights, costs, max_weight)  

print("Максимальная стоимость:", max_cost)  # Ожидаем 10  
print("Выбранные предметы (индексы):", items)  # Ожидаем [0]

test_num += 1
print(f'Test {test_num}:')
# 4. Один предмет, который нельзя взять (слишком тяжелый)
weights = [6]  
costs = [10]  
max_weight = 5  

max_cost, items = knapsack(weights, costs, max_weight)  

print("Максимальная стоимость:", max_cost)  # Ожидаем 0  
print("Выбранные предметы (индексы):", items)  # Ожидаем []  

test_num += 1
print(f'Test {test_num}:')
# 5. Все предметы имеют одинаковый вес и стоимость (проверка выбора максимального количества)
weights = [2, 2, 2, 2]  
costs = [5, 5, 5, 5]  
max_weight = 6  

max_cost, items = knapsack(weights, costs, max_weight)  

print("Максимальная стоимость:", max_cost)  # Ожидаем 15 (3 предмета)  
print("Выбранные предметы (индексы):", items)  # Ожидаем [0, 1, 2] или любые 3 из 4

test_num += 1
print(f'Test {test_num}:')
# 6. Предмет с нулевой стоимостью (должен игнорироваться, если не помогает)
weights = [1, 2, 3]  
costs = [0, 5, 0]  
max_weight = 3  

max_cost, items = knapsack(weights, costs, max_weight)  

print("Максимальная стоимость:", max_cost)  # Ожидаем 5 (предмет с весом 2)  
print("Выбранные предметы (индексы):", items)  # Ожидаем [1]  

test_num += 1
print(f'Test {test_num}:')
# 7. Предмет с нулевым весом (должен браться, если стоимость > 0)
weights = [0, 2, 3]  
costs = [10, 5, 6]  
max_weight = 3  

max_cost, items = knapsack(weights, costs, max_weight)  

print("Максимальная стоимость:", max_cost)  # Ожидаем 15 (0-вес + 2 или 3)  
print("Выбранные предметы (индексы):", items)  # Ожидаем [0, 1] или [0, 2]

test_num += 1
print(f'Test {test_num}:')
# 8. Оптимальный выбор между дорогим тяжелым и дешевыми легкими предметами
weights = [4, 3, 2, 1]  
costs = [10, 8, 5, 1]  
max_weight = 5  

max_cost, items = knapsack(weights, costs, max_weight)  

print("Максимальная стоимость:", max_cost)  # Ожидаем 13 (3 + 2)  
print("Выбранные предметы (индексы):", items)  # Ожидаем [1, 2] 

test_num += 1
print(f'Test {test_num}:')
# 9. Все предметы можно взять (суммарный вес ≤ max_weight)
weights = [1, 2, 3]  
costs = [5, 10, 15]  
max_weight = 10  

max_cost, items = knapsack(weights, costs, max_weight)  

print("Максимальная стоимость:", max_cost)  # Ожидаем 30  
print("Выбранные предметы (индексы):", items)  # Ожидаем [0, 1, 2]  
