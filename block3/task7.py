def count_cutting_ways(n, m):
    if m > n:
        return 0
    if m == 1:
        return n  # можно выбрать любое одно дерево

    count = 0
    max_d = (n - 1) // (m - 1)

    for d in range(1, max_d + 1):
        max_start = n - (m - 1) * d
        count += max_start

    return count


# Пример:
n = 10  # всего деревьев
m = 4   # нужно оставить

result = count_cutting_ways(n, m)
print(f"Количество способов вырубки: {result}")
