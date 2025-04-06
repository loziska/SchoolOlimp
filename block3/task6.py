def knapsack(weights, costs, max_weight):
    n = len(weights)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    # dp[i][j] — максимальная стоимость при рассмотрении первых i предметов и весе j
    for i in range(1, n + 1):
        for j in range(max_weight + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + costs[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    # Восстановление выбранных предметов
    res_weight = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][res_weight] != dp[i - 1][res_weight]:
            selected_items.append(i - 1)  # Индексация с нуля
            res_weight -= weights[i - 1]

    selected_items.reverse()
    return dp[n][max_weight], selected_items


# Пример:
weights = [3, 2, 1, 4]
costs = [5, 3, 2, 7]
max_weight = 5

max_cost, items = knapsack(weights, costs, max_weight)

print("Максимальная стоимость:", max_cost)
print("Выбранные предметы (индексы):", items)
