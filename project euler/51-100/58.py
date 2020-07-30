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

percentage = 1.0
size = 1
n = 1
c = 0
while percentage > 0.1:
    for j in range(4):
        n += (size) * 2
        if isprime(n) == True:
            c += 1
    #print (c)
    #print (((size * 4) + 1))
    percentage = c / ((size * 4) + 1)
    size += 1
print ((size-1)*2 + 1)
