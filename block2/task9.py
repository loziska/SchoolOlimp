def max_segments_cover(segments):
    events = []  
    for l, r in segments:
        events.append((l, 1))   # Начало отрезка
        events.append((r, -1))  # Конец отрезка
    
    # Сортируем: сначала по координате, затем по типу события (начала (+1) раньше, чем концы (-1))
    events.sort(key=lambda x: (x[0], -x[1]))  

    max_count = 0
    current_count = 0
    best_point = None
    
    for point, change in events:
        current_count += change
        if current_count > max_count:
            max_count = current_count
            best_point = point  # Запоминаем лучшую точку
    
    return best_point, max_count

# Пример теста
segments = [(1, 6), (1, 6), (1, 7), (6, 8)]
point, count = max_segments_cover(segments)
print(f"Точка {point} принадлежит {count} отрезкам")
