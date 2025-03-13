count_row = 8
count_passengers = 15
imp = False

plane = [[0,0,0,0,1,0],
       [0,1,0,0,1,1],
       [0,0,1,1,0,1],
       [0,1,0,0,0,0],
       [1,1,0,0,0,0],
       [1,0,0,0,1,0],
       [0,0,0,1,1,0],
       [0,0,0,0,1,0]]

online_registred = sum([sum(row) for row in plane])
free_space = count_row * 6 - online_registred

if count_passengers + online_registred > 6 * count_row:
    print("Impossible")
    imp = True
else:
    for row in range(count_row):
        for place in range(3):
            if (plane[row][place] == 1 or plane[row][5-place] == 1) and plane[row][place] != plane[row][5-place]:
                plane[row][place], plane[row][5-place] = 1, 1
                count_passengers -= 1
    if count_passengers % 2 == 1:
        print('Impossible')
        imp = True
    else:
        for row in range(count_row):
            for place in range(3):
                if count_passengers > 0:
                    if plane[row][place] == 0 and plane[row][5-place] == 0:
                        plane[row][place], plane[row][5-place] = 1, 1
                        count_passengers -= 2

if not imp:
    for row in plane:
        print(row)  
                   
