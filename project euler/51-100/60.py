def genprime(n):
    primes = [3]
    for i in range(3,n,2):
        p = 1
        for j in primes:
            if i % j == 0:
                p = 0
                break
        if p == 1:
            primes.append(i)
    return primes
import math
def isprime(n):
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True
def checkprime(n):
    if n > max:
        return isprime(n)
    else:
        return n in primedict

global max
global primedict
max  = 1000000
primes = genprime(max)
primedict = {p:1 for p in primes}
del primes [0] #get rid of 3 - assume it will be in the solution
primes1 = []
primes2 = []
print ('here')
for prime in primes:
    if prime % 3 == 1:
        primes1.append(prime)
    else:
        primes2.append(prime)


minval = 100000000
#print (primes1,primes2)
from itertools import combinations as comb
for i in comb(primes1,3):
    valid = 1
    for n1,n2 in comb((*i,3),2):
        if checkprime(int(str(n1) + str(n2))) == False:
            valid = 0
            break
        if checkprime(int(str(n2) + str(n1))) == False:
            valid = 0
            break
    if valid == 1:
        if sum(i) < minval:
            minval = sum(i)
        print (i)

for i in comb(primes2,3):
    valid = 1
    for n1,n2 in comb((*i,3),2):
        if checkprime(int(str(n1) + str(n2))) == False:
            valid = 0
            break
        if checkprime(int(str(n2) + str(n1))) == False:
            valid = 0
            break
    if valid == 1:
        if sum(i) < minval:
            minval = sum(i)
        print (i)
print (minval+3)
