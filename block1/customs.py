import heapq

def min_machines(N, cargoes):
    if N == 0:
        return 0
    
    # Сортируем грузы по времени прибытия
    cargoes.sort()
    
    # Минимальная куча для хранения времени окончания обработки
    heap = []
    
    for Ti, Li in cargoes:
        if heap and heap[0] <= Ti:
            # Освобождаем аппарат и используем его для текущего груза
            heapq.heappop(heap)
        # Добавляем время окончания обработки текущего груза
        heapq.heappush(heap, Ti + Li)
    
    # Количество аппаратов равно размеру кучи
    return len(heap)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    cargoes = []
    index = 1
    for _ in range(N):
        Ti = int(data[index])
        Li = int(data[index + 1])
        cargoes.append((Ti, Li))
        index += 2
    
    result = min_machines(N, cargoes)
    print(result)

if __name__ == "__main__":
    main()
