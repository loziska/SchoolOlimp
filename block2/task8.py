def min_segments_to_cover(a, b, segments):
    # Сортируем отрезки по левому концу
    segments.sort()
    
    result = []  # Список для хранения выбранных отрезков
    current_position = a  # Текущая позиция, которую нужно покрыть
    n = len(segments)
    i = 0

    while current_position < b and i < n:
        # Выбираем отрезок, который начинается до current_position и заканчивается как можно дальше
        farthest_end = current_position
        best_segment = None
        while i < n and segments[i][0] <= current_position:
            if segments[i][1] > farthest_end:
                farthest_end = segments[i][1]
                best_segment = segments[i]
            i += 1
        
        # Если не нашли подходящий отрезок, выходим
        if best_segment is None:
            return None  # Невозможно покрыть отрезок [a; b]
        
        # Добавляем выбранный отрезок в результат
        result.append(best_segment)
        # Перемещаем текущую позицию на конец выбранного отрезка
        current_position = farthest_end

    # Проверяем, покрыли ли весь отрезок [a; b]
    if current_position < b:
        return None  # Невозможно покрыть отрезок [a; b]
    
    return result

a, b = 1, 10
segments = [(1, 4), (-1, 9), (3, 6), (5, 8), (7, 10)]
result = min_segments_to_cover(a, b, segments)

if result:
    print("Минимальное количество отрезков для покрытия [a; b]:", len(result))
    for seg in result:
        print(seg)
else:
    print("Невозможно покрыть отрезок [a; b] данными отрезками.")
