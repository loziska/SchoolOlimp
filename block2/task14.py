def find_nearest_non_overlapping_right(segments):
    n = len(segments)
    # Добавляем индексы к отрезкам, чтобы после сортировки знать их исходные позиции
    indexed_segments = [(start, end, idx) for idx, (start, end) in enumerate(segments)]
    # Сортируем отрезки по левому концу
    sorted_segments = sorted(indexed_segments, key=lambda x: x[0])
    
    starts = [seg[0] for seg in sorted_segments]
    ends = [seg[1] for seg in sorted_segments]
    indices = [seg[2] for seg in sorted_segments]
    
    answer = [-1] * n
    
    for i in range(n):
        current_start, current_end, original_idx = sorted_segments[i]
        # Ищем самый левый отрезок, у которого start >= current_end
        left = i + 1
        right = n - 1
        best_j = -1
        while left <= right:
            mid = (left + right) // 2
            if starts[mid] >= current_end:
                best_j = mid
                right = mid - 1
            else:
                left = mid + 1
        if best_j != -1:
            answer[original_idx] = indices[best_j]
    
    return answer

segments = [(1, 3), (-10, -5), (2, 5), (4, 6), (7, 9)]
result = find_nearest_non_overlapping_right(segments)
print(result)
