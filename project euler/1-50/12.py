import math
def getdiv(n):
    divs = 0
    for i in range(1,int(math.sqrt(n)+1)):
        if n % i == 0:
            divs += 1
    return divs

c = 1
n = 1
maxval = 0
while maxval < 250:
    x = getdiv(n)
    if x > maxval:
        maxval = x
        print (n,maxval,sep=':')
    c += 1
    n += c
