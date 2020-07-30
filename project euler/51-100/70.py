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

minval  = -1
for n in range(2,10000000):
#for n in range(87109,87110):
    x = np.prod([1 - 1/x for x in set(recur(n))])
    #print (1/x)
    if x > minval and sorted(str(int(n*x))) == sorted(str(n)):
        minval = x
        print (n)
        print(int(n*x))
        print(1/x)
    #print (int(n*np.prod([1 - 1/x for x in set(recur(n))])))
