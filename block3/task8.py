def count_mowed_and_watered(x1, y1, x2, y2, x3, y3, r):
    r2 = r * r
    count = 0

    for x in range(x1, x2 + 1):
        dx2 = (x - x3) ** 2
        if dx2 > r2:
            continue  # Нет смысла проверять по y, слишком далеко по x
        dy_limit = int((r2 - dx2) ** 0.5)
        y_start = max(y1, y3 - dy_limit)
        y_end = min(y2, y3 + dy_limit)
        count += max(0, y_end - y_start + 1)

    return count


# Пример ввода:
x1, y1, x2, y2 = map(int, input().split())
x3, y3, r = map(int, input().split())

result = count_mowed_and_watered(x1, y1, x2, y2, x3, y3, r)
print(result)

# 0 0 5 4
# 4 0 3
