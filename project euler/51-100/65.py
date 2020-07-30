## construct seqeunce
import math
var = 99
arr = []
for i in range(1,var//3 + 1):
    arr += [1,2*i,1]
arr += [1,2* (var//3) + 2,1][:var%3]
#print (len(arr))
#print (arr)
arr.reverse()
#print (arr)

def add (i,n,d): #iteger numerator, denominator
    return (i * d + n, d) #numerator, demoinator
arr = [1,1,1]
#print (add(1,1,3))
n = 1
d = arr[0]
del arr[0]

for i in arr:
    d,n = add(i,n,d)
    #print (n,d)
#print (add(2,n,d))
n,d = (add(2,n,d))
print (n,d)
#print ([int(x) for x in str(n)])
#print (sum([int(x) for x in str(n)]))
