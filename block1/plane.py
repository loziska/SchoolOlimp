imp = False

# всё хорошо
# count_row = 8
# count_passengers = 15
# plane = [[0,0,0,0,1,0],
#        [0,1,0,0,1,1],
#        [0,0,1,1,0,1],
#        [0,1,0,0,0,0],
#        [1,1,0,0,0,0],
#        [1,0,0,0,1,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,1,0]]

# Начётное кол-во людей в итоге
# count_row = 8
# count_passengers = 16
# plane = [[0,0,0,0,1,0],
#        [0,1,0,0,1,1],
#        [0,0,1,1,0,1],
#        [0,1,0,0,0,0],
#        [1,1,0,0,0,0],
#        [1,0,0,0,1,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,1,0]]

# Самолёт переполнен, чётное кол-во человек
# count_row = 8
# count_passengers = 305
# plane = [[0,0,0,0,1,0],
#        [0,1,0,0,1,1],
#        [0,0,1,1,0,1],
#        [0,1,0,0,0,0],
#        [1,1,0,0,0,0],
#        [1,0,0,0,1,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,1,0]]

# Недостаточно пассажиров на стойке регистрации для семетричной расскадки
# count_row = 8
# count_passengers = 1
# plane = [[0,0,0,0,1,0],
#        [0,1,0,0,1,1],
#        [0,0,1,1,0,1],
#        [0,1,0,0,0,0],
#        [1,1,0,0,0,0],
#        [1,0,0,0,1,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,1,0]]

# Пустой самолёт. По условию задачи - полетит. Симметрично же.
# count_row = 8
# count_passengers = 0
# plane = [[0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]

# Полностью забитый самолёт. Симметрично. Летит.
count_row = 8
count_passengers = 48
plane = [[0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0]]

online_registred = sum([sum(row) for row in plane])
free_space = count_row * 6 - online_registred

if count_passengers + online_registred > 6 * count_row:
    imp = True
else:
    for row in range(count_row):
        for place in range(3):
            if (plane[row][place] == 1 or plane[row][5-place] == 1) and plane[row][place] != plane[row][5-place]:
                plane[row][place], plane[row][5-place] = 1, 1
                count_passengers -= 1
    if count_passengers < 0:
        imp = True
    if count_passengers % 2 == 1:
        imp = True
    else:
        for row in range(count_row):
            for place in range(3):
                if count_passengers > 0:
                    if plane[row][place] == 0 and plane[row][5-place] == 0:
                        plane[row][place], plane[row][5-place] = 1, 1
                        count_passengers -= 2
            

if imp:
    print('Impossible')

if not imp:
    for row in plane:
        print(row)  
                   
