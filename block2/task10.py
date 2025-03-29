def best_k_segment(segments, k):
    points = sorted(set(x for l, r in segments for x in (l, r)))  # Уникальные точки
    max_count = 0
    best_start = None

    j = 0  # Второй указатель (для конца окна)
    n = len(points)
    
    for i in range(n):
        start = points[i]
        end = start + k
        
        # Двигаем второй указатель, пока точка входит в [start, start + k]
        while j < n and points[j] < end:
            j += 1
        
        # Считаем, сколько отрезков пересекают этот интервал
        count = sum(1 for l, r in segments if not (r < start or l > end))
        
        if count > max_count:
            max_count = count
            best_start = start

    return best_start, best_start + k, max_count

# Пример теста
segments = [(0, 1), (4, 6), (4, 7), (6, 9), (10, 12)]
k = 4
start, end, count = best_k_segment(segments, k)
print(f"Лучший отрезок: [{start}, {end}], покрывает {count} отрезков")
