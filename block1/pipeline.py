def can_sort_containers(test_case):
    k, containers = test_case
    stack = []
    expected = 1  # Ожидаемый минимальный элемент (индекс для упрощения)
    
    for container in containers:
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1
        
        if container == expected:
            expected += 1
        else:
            stack.append(container)
    
    while stack:
        if stack[-1] == expected:
            stack.pop()
            expected += 1
        else:
            return 0
    
    return 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    index = 1
    results = []
    
    for _ in range(N):
        K = int(data[index])
        containers = list(map(float, data[index + 1: index + 1 + K]))
        index += 1 + K
        
        result = can_sort_containers((K, containers))
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
