def union_length(segments):
    events = []  # Список событий
    
    for l, r in segments:
        events.append((l, 1))   # Начало отрезка
        events.append((r, -1))  # Конец отрезка

    events.sort()  # Сортируем по координате (если равны — сначала -1, потом +1)

    active_segments = 0
    prev_x = None
    total_length = 0

    for x, event in events:
        if active_segments > 0 and prev_x is not None:
            total_length += x - prev_x  # Добавляем длину активного интервала

        active_segments += event  # Обновляем количество активных отрезков
        prev_x = x  # Запоминаем текущую координату

    return total_length

# Пример теста
segments = [(1, 5), (2, 6), (8, 10), (12, 13)]
print("Длина объединения отрезков:", union_length(segments))
