#NOTE THIS FUNCTION DOES NOT WORK FOR 3
'''
def primefac(n,fax):
    if n % 2 == 0:
        if 2 in fax:
            fax[2] += 1
        else:
            fax[2] = 1
        primefac(n//2, fax)
    for i in range(3,n // 3 + 2,2):
        if n % i == 0:
            if i in fax:
                fax[i] += 1
            else:
                fax[i] = 1
            primefac(n//i,fax)
    return fax


print (primefac(27,{}))
'''
'''
'''
'''
#PRIME FACTOR GENERATOR HERE
import math
from collections import Counter
def isprime(n):
    if n % 2 == 0:
        return 2
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return i
    return True

def fac(num):
    x = isprime(num)
    if x != True:
        yield (x)
        yield from fac(num//x)
    elif num != 1:
        yield num

print (Counter(list(fac(3125))))
'''
mydict = {}
for a in range(2,101):
    for b in range(2,101):
        x = pow(a,b)
        if x not in mydict:
            mydict[x] = 1
print (len(mydict.keys()))


'''
def create_thing(n):
    yield n
    print ('banana')
    create_thing(n)
print (*create_thing(15))
'''
