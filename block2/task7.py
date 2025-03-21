def max_non_overlapping_segments(segments):
    # Сортируем отрезки по правому концу
    segments.sort(key=lambda x: x[1])
    
    for segment in segments:
        if segment[0] > segment[1]:
            return None, segment
    
    result = []  # Список для хранения выбранных отрезков
    last_end = -float('inf')  # Правый конец последнего выбранного отрезка

    for start, end in segments:
        if start >= last_end:  # Если текущий отрезок не пересекается с последним выбранным
            result.append((start, end))
            last_end = end  # Обновляем правый конец последнего выбранного отрезка

    return result, None

segments = [(1, 1), (2, 5), (6, 79), (5, 88), (8, 10), (11, 12), (13, 10)]
result, c = max_non_overlapping_segments(segments)


if result:
    for seg in result:
        print("Максимальное множество непересекающихся отрезков:")
        print(seg)
else:
    print(f'Ошибка. В координатах {c} - a > b.')
