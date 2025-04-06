def can_fill_exact_volume(volumes, target):
    n = len(volumes)
    for mask in range(1 << n):  # перебираем все подмножества
        total = 0
        for i in range(n):
            if mask & (1 << i):
                total += volumes[i]
        if total == target:
            return "да"
    return "нет"

# Считываем ввод
n = int(input())
volumes = [int(input()) for _ in range(n)]
target = int(input())

print(can_fill_exact_volume(volumes, target))

# 3
# 1
# 3
# 4
# 5
