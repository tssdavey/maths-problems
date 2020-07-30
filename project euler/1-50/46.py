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
#primes = {2:1}
#maxprime = 2
primes = {}
f = 0
i = 3
#for i in range(3,31,2):
while True:
    #print (i)
    if isprime(i) == True:
        primes[i] = 1
    else:
        #print (primes)
        for p in primes.keys():
            f = 0
            t = math.sqrt((i-p) // 2)
            if int(t + 0.5) ** 2 == (i - p) // 2:
                #print (p)
                f = 1
                break
        if f == 0:
            print ('found')
            print (i)
            break
    i += 2
    print ('')
    
