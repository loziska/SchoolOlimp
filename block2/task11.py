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

# # Пример теста
# segments = [(1, 5), (2, 6), (8, 10), (12, 13)]
# print("Длина объединения отрезков:", union_length(segments))

# Граничные тесты для функции union_length

# 1. Пустой список отрезков
segments1 = []
print("test1:", union_length(segments1))  # Ожидаемый результат: 0

# 2. Один отрезок
segments2 = [(3, 7)]
print("test2:", union_length(segments2))  # Ожидаемый результат: 4

# 3. Несколько непересекающихся отрезков
segments3 = [(1, 3), (5, 8), (10, 12)]
print("test3:", union_length(segments3))  # Ожидаемый результат: 2 + 3 + 2 = 7

# 4. Полное перекрытие — вложенные отрезки
segments4 = [(1, 10), (2, 5), (3, 4)]
print("test4:", union_length(segments4))  # Ожидаемый результат: 9

# 5. Частичные перекрытия
segments5 = [(1, 5), (3, 7), (6, 9)]
print("test5:", union_length(segments5))  # Ожидаемый результат: от 1 до 9 => 8

# 6. Совпадающие отрезки
segments6 = [(2, 6), (2, 6), (2, 6)]
print("test6:", union_length(segments6))  # Ожидаемый результат: 4

# 7. Отрезки длиной 0 (точки)
segments7 = [(1, 1), (2, 2), (3, 3)]
print("test7:", union_length(segments7))  # Ожидаемый результат: 0

# 8. Отрезки с "обратным" порядком (если разрешено)
segments8 = [(5, 1), (7, 3)]  # Интерпретируем как (1,5) и (3,7)
segments8_fixed = [(min(l, r), max(l, r)) for l, r in segments8]
print("test8:", union_length(segments8_fixed))  # Ожидаемый результат: от 1 до 7 => 6

# 9. Максимально длинный отрезок и куча коротких внутри
segments9 = [(0, 1000000)] + [(i, i + 1) for i in range(0, 1000000, 2)]
print("test9:", union_length(segments9))  # Ожидаемый результат: 1000000

# 10. Очень большое количество маленьких непересекающихся отрезков
segments10 = [(i * 2, i * 2 + 1) for i in range(100000)]
print("test10:", union_length(segments10))  # Ожидаемый результат: 100000

# 11. Отрезки с отрицательными координатами
segments11 = [(-10, -5), (-6, -2), (-3, 0)]
print("test11:", union_length(segments11))  # Ожидаемый результат: от -10 до 0 => 10

# 12. Отрезки с дробными координатами
segments12 = [(1.1, 2.2), (2.0, 3.5)]
print("test12:", union_length(segments12))  # Ожидаемый результат: от 1.1 до 3.5 => 2.4

# 13. Налегающие отрезки (без пропуска между ними)
segments13 = [(0, 2), (2, 4), (4, 6)]
print("test13:", union_length(segments13))  # Ожидаемый результат: от 0 до 6 => 6
