import math
import numpy as np
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


def recur(n):
    #print (n)
    p = isprime(n)
    #print (p)
    if p == True:
        yield n
    else:
        yield from recur(p)
        yield from recur(n//p)

minval = 100
print (set(recur(36)))
for n in range(2,1000001):
    #print (np.prod([1 - 1/x for x in set(recur(n))]))
    x = np.prod([1 - 1/x for x in set(recur(n))])
    if x < minval:
        minval = x
        print (n)
