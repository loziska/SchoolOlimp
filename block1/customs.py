n = 5
mas =[[13,4],
      [15,1],
      [11,5],
      [12,3],
      [10,3]]

mas_sort = sorted(mas) 

mas_t = []

for i in range(n):

    fl = True

    for j in range(len(mas_t)):
        if mas_sort[i][0] >= mas_t[j]:
            mas_t[j] = mas_sort[i][0] + mas_sort[i][1]
            fl = False
            break

    if fl:
        mas_t.append(mas_sort[i][0] + mas_sort[i][1])

print(len(mas_t))
print(mas_t)
