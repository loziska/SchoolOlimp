def main():
    data = []
    test_input = (
            "3 5\n"      # 3 отсека, 5 грузов
            "3 2 10\n" # Вместимости отсеков
            "1 1 6\n"   # Груз 1
            "3 2 8\n"  
            "9 3 5\n"    
            "2 4 9\n"  
            "12 7 10\n"   
    )
    data = test_input.strip().split()
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    capacities = [int(next(it)) for _ in range(n)]
    free = capacities[:]  # Копия свободного пространства
    cells = [[] for _ in range(n)]
    cargo_placement = {}
    
    events = []
    for cargo_num in range(1, m+1):
        size = int(next(it))
        a = int(next(it))
        d = int(next(it))
        events.append((a, 'arrive', cargo_num, size, d))
        events.append((d, 'depart', cargo_num))
    events.sort(key=lambda x: x[0])
    
    actions = []
    
    for event in events:
        time = event[0]
        etype = event[1]
        if etype == 'depart':
            cargo_num = event[2]
            if cargo_num in cargo_placement:
                cell_index, size = cargo_placement[cargo_num]
                cells[cell_index].remove((cargo_num, size))
                free[cell_index] += size
                del cargo_placement[cargo_num]
                actions.append(f"take cargo {cargo_num} from cell {cell_index+1}")
        elif etype == 'arrive':
            cargo_num, size, d = event[2], event[3], event[4]
            best_cell = None
            best_free = None
            for i in range(n):
                if free[i] >= size:
                    if best_cell is None or free[i] < best_free or (free[i] == best_free and i < best_cell):
                        best_cell = i
                        best_free = free[i]
            if best_cell is not None:
                free[best_cell] -= size
                cells[best_cell].append((cargo_num, size))
                cargo_placement[cargo_num] = (best_cell, size)
                actions.append(f"put cargo {cargo_num} to cell {best_cell+1}")
            else:
                candidate = None
                for src in range(n):
                    for (cnum, csize) in cells[src]:
                        if free[src] + csize >= size:
                            for dest in range(n):
                                if dest == src:
                                    continue
                                if free[dest] >= csize:
                                    new_free_source = free[src] + csize
                                    new_free_dest = free[dest] - csize
                                    candidate_tuple = (csize, new_free_source, new_free_dest, cnum, dest, src)
                                    if candidate is None or candidate_tuple < candidate[0]:
                                        candidate = (candidate_tuple, cnum, src, dest, csize)
                if candidate is not None:
                    _, moved_cargo, src, dest, moved_size = candidate
                    cells[src].remove((moved_cargo, moved_size))
                    free[src] += moved_size
                    cells[dest].append((moved_cargo, moved_size))
                    free[dest] -= moved_size
                    cargo_placement[moved_cargo] = (dest, moved_size)
                    actions.append(f"move cargo {moved_cargo} from cell {src+1} to cell {dest+1}")
                    free[src] -= size
                    cells[src].append((cargo_num, size))
                    cargo_placement[cargo_num] = (src, size)
                    actions.append(f"put cargo {cargo_num} to cell {src+1}")
                else:
                    actions.append(f"cargo {cargo_num} cannot be stored")
    
    for act in actions:
        print(act)

if __name__ == '__main__':
    main()

