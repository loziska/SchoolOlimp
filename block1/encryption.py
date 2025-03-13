pov = int(input('Глубина шифрования: ')) # 2
inp_st = input('Шифруемая строка: ') # BCHAEDFG
lenght = len(inp_st)
k = 0
fib1 = 1
fib2 = 1

while fib2<=lenght:
    fib1, fib2 = fib2, fib1+fib2
    k += 1
    
for i in range(pov):
    temp = inp_st[::-1]
    p = k
    l = 0
    fib1 = 1
    fib2 = 1
    enc_st = ""
    for j in range(lenght):
        if j+1==fib2:
            enc_st+=temp[l]
            fib1, fib2 = fib2, fib1+fib2
            l+=1
        else:
            enc_st+=temp[p]
            p+=1
    inp_st=enc_st

print(enc_st)

