import math
def isprime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 2
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return i
    return True

m = 1000000
d = dict([(i,1) for i in range(m) if isprime(i) == True])
#print (d)
r = list(d.keys())
#print (r)
a = 0
for i,p in enumerate(r):
    s = 0
    j = 0
    while s < m:
        if s in d and j > a:
            a = j
            print (s)
        s += r[i+j]
        j += 1
print (a)
