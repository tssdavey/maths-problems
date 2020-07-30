from math import log as l
i = 1
c = 0
while True:
    d = 1
    for j in range(1,10):
        if int(l(j**i,10))+1 == i:
            c += 1
            d = 0
            print (j,i)
    if d == 1:
        break
    i += 1
print (c)
