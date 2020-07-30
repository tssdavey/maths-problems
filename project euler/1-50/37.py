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

import math
c = 0
a = 0
arr = []
#arr = [113, 131, 137, 173, 197, 311, 313, 317, 373, 797, 1373, 1997, 3137, 3797, 7331, 73331]
#arr = [113]
for i in range(11,1000000,2):
#for i in arr:
    #print (i)
    istr = str(i)
    if isprime(i) == True:
        trunc = True
        for j in range(1,int(math.log(i,10))+1):
            #print (j)
            #print (istr[j:],istr[:-j])
            #print (isprime(int(istr[j:])),isprime(int(istr[:-j]))==1)
            if isprime(int(istr[j:])) != True or isprime(int(istr[:-j])) != True:
                #print ('breaking')
                trunc = False
                break
        if trunc == True:
            print (i)
            c += 1
            a += i
            #arr.append(i)

print (c)
print (a)
print (arr)
print (len(arr))
print (isprime(1))
