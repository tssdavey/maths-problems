from math import log as l
d = 1
n = 1
c = 0
for i in range(1000):
    if int(l(n,10)) > int(l(d,10)):
        c += 1
    tmp = d
    d  += n
    n += 2 * tmp
print (c)
