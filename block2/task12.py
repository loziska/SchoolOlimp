def full_intersection_length(arcs):
    events = []  # События (угол, +1/-1)

    for start, end in arcs:
        if start <= end:
            events.append((start, 1))   # Начало дуги
            events.append((end, -1))    # Конец дуги
        else:
            # Разбиваем на две части (одна до 360°, другая после 0°)
            events.append((start, 1))   
            events.append((360, -1))    
            events.append((0, 1))       
            events.append((end, -1))    

    events.sort()  # Сортируем по углу

    active_arcs = 0
    prev_angle = None
    total_length = 0

    for angle, change in events:
        if active_arcs == len(arcs) and prev_angle is not None:
            total_length += (angle - prev_angle) % 360  # Добавляем длину пересечения

        active_arcs += change  # Обновляем активные дуги
        prev_angle = angle

    return total_length

# Пример теста
arcs = [(10, 120), (50, 150), (0, 200)]
print("Длина пересечения всех дуг:", full_intersection_length(arcs))
