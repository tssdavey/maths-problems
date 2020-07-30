import math
#PRIME FACTORISER
#---------------------------
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
#---------------------------

l = 4
n = 10
while True:
    if len([1 for j in range(l) if len(set(recur(n+j))) == l]) == l:
        print (n)
        break
    n += 1
