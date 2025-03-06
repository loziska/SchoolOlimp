# Склад

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    c = list(map(int, data[idx:idx + n]))
    idx += n
    
    cargo = []
    for i in range(m):
        s = int(data[idx])
        a = int(data[idx + 1])
        d = int(data[idx + 2])
        cargo.append({'id': i + 1, 'size': s, 'arrival': a, 'departure': d})
        idx += 3
    
    # Инициализация отсеков
    cells = [{'id': i + 1, 'capacity': c[i], 'used': 0, 'cargos': []} for i in range(n)]
    
    # Сортировка грузов по времени прибытия
    cargo.sort(key=lambda x: x['arrival'])
    
    # Обработка грузов
    for cg in cargo:
        # Поиск отсека с достаточным свободным местом
        suitable_cells = []
        for cell in cells:
            if cell['capacity'] - cell['used'] >= cg['size']:
                suitable_cells.append(cell)
        
        if suitable_cells:
            # Выбираем отсек с наименьшим свободным местом
            selected_cell = min(suitable_cells, key=lambda x: x['capacity'] - x['used'])
            selected_cell['used'] += cg['size']
            selected_cell['cargos'].append(cg['id'])
            print(f"put cargo {cg['id']} to cell {selected_cell['id']}")
        else:
            # Попытка перемещения грузов
            moved = False
            for cell in cells:
                for cargo_id in cell['cargos']:
                    # Находим груз, который можно переместить
                    cargo_to_move = next((x for x in cargo if x['id'] == cargo_id), None)
                    if cargo_to_move:
                        # Ищем отсек, куда можно переместить этот груз
                        for target_cell in cells:
                            if target_cell['id'] != cell['id'] and target_cell['capacity'] - target_cell['used'] >= cargo_to_move['size']:
                                # Проверяем, освободит ли это место для нового груза
                                if cell['capacity'] - (cell['used'] - cargo_to_move['size']) >= cg['size']:
                                    # Перемещаем груз
                                    cell['used'] -= cargo_to_move['size']
                                    target_cell['used'] += cargo_to_move['size']
                                    cell['cargos'].remove(cargo_to_move['id'])
                                    target_cell['cargos'].append(cargo_to_move['id'])
                                    print(f"move cargo {cargo_to_move['id']} from cell {cell['id']} to cell {target_cell['id']}")
                                    # Размещаем новый груз
                                    cell['used'] += cg['size']
                                    cell['cargos'].append(cg['id'])
                                    print(f"put cargo {cg['id']} to cell {cell['id']}")
                                    moved = True
                                    break
                        if moved:
                            break
                if moved:
                    break
            if not moved:
                print(f"cargo {cg['id']} cannot be stored")
    
    # Удаление грузов по времени
    for cg in cargo:
        for cell in cells:
            if cg['id'] in cell['cargos']:
                cell['used'] -= cg['size']
                cell['cargos'].remove(cg['id'])
                print(f"take cargo {cg['id']} from cell {cell['id']}")

if __name__ == "__main__":
    main()
