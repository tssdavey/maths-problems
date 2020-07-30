import math
from collections import deque

def isprime(n):
    if n % 2 == 0:
        return 2
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return i
    return True

mydict = {}
for i in range(1000000):
    if isprime(i) == True:
        if ''.join(sorted(str(i))) in mydict:
            #print (i)
            continue
        circ = True
        i = deque(str(i))
        arr = []
        for _ in range(len(i)):
            if isprime(int(''.join(i))) != True:
                circ = False
                break
            d = i.copy()
            arr.append(d)
            i.rotate(1)
        if circ == True:
            for j in arr:
                print (j)
                mydict[''.join(j)] = 1

print (*mydict.items(),sep='\n')
print (sum(mydict.values()))
#11 reversed is 11
#2 should replace 1, but doent not matter for the count
