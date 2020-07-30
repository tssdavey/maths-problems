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

from itertools import combinations as c
from itertools import permutations as p
n = ['1','2','3','4','5','6','7','8','9']
for i in range(1,10):
    for tuple in p(n[:i],i):
        #print (tuple)
        #print (int(''.join(tuple)))
        if isprime(int(''.join(tuple))) == True:
            print (''.join(tuple))
