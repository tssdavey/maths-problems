from itertools import combinations as comb
from itertools import permutations as perm
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
#to have a familly og 8 primes it must have 3 asterixis
#the last digit cannot be repeater

digits = map(str,range(10))

two_digit_comb = list(map(list,comb(digits,2)))
three_digit_comb = list(map(list,comb(digits,3)))

possibilities = [
['n','*','n','*','*','n'],
['n','*','*','n','*','n'],
['n','*','*','*','n','n'],
['n','n','*','*','*','n'],
['*','*','*','n','n','n'],
['*','*','n','*','n','n'],
['*','*','n','n','*','n'],
['*','n','*','n','*','n'],
['*','n','*','*','n','n'],
['*','n','n','*','*','n'],
]

for poss in possibilities:
    iindex = poss.index('n')
    jindex = poss.index('n',iindex+1)
    kindex = poss.index('n',jindex+1)
    #print (iindex,jindex,kindex)
    for i in range(10):
        poss[iindex] = i
        for j in range(10):
            poss[jindex] = j
            for k in range(10):
                poss[kindex] = k
                count = 0
                for l in range(10):
                    #print ([x if x != '*' else l for x in poss])
                    if isprime(int(''.join((map(str,[x if x != '*' else l for x in poss]))))) == True:
                        count += 1
                #print (count)
                if count == 8:
                    print (poss)
