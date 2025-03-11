def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    seats = []
    index = 2
    for _ in range(n):
        row = data[index]
        seats.append(list(row))
        index += 1
    
    total = 0
    for row in seats:
        if row[0] == 'X' and row[5] == '.':
            row[5] = 'X'
            total += 1
        elif row[0] == '.' and row[5] == 'X':
            row[0] = 'X'
            total += 1
        if row[1] == 'X' and row[4] == '.':
            row[4] = 'X'
            total += 1
        elif row[1] == '.' and row[4] == 'X':
            row[1] = 'X'
            total += 1
        if row[2] == 'X' and row[3] == '.':
            row[3] = 'X'
            total += 1
        elif row[2] == '.' and row[3] == 'X':
            row[2] = 'X'
            total += 1
    
    if total < m:
        print("Impossible")
        return
    
    for row in seats:
        for i in range(6):
            if row[i] == '.' and m > 0:
                row[i] = 'X'
                m -= 1
    
    for row in seats:
        print(''.join(row))

if __name__ == "__main__":
    main()
