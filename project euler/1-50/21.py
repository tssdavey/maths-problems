import math

def factorsum(n):
    ans = 0
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            ans += i
            ans += n // i
    return ans + 1

mydict = {}

for i in range(1,10000):
    mydict[i] = factorsum(i)

ans = 0
for k in mydict.keys():
    try:
        if mydict[mydict[k]] == k and mydict[k] != k: #remove perfect numbers
            ans += k
    except KeyError:
        pass
print (ans)
