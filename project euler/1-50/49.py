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

d = {}
for i in range(1001,10000):
    if isprime(i) == True:
        d[i] = 1

l = len(d.keys())
k = list(d.keys())
for i,ni in enumerate(k):
    for j,nj in enumerate(k[:i]):
        nk = 2 * nj - ni
        if nk in d and sorted(str(nk)) == sorted(str(ni)) and sorted(str(ni)) == sorted(str(nj)):
            print (ni,nj,nk)
