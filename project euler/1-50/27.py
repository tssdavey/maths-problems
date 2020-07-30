def isprime(num):
    prime = True
    if num < 0:
        return False
    if num % 2 == 0:
        return False
    for i in range(3,num // 2,2):
        if num % i == 0:
            return (False)
    return (True)


maxval = 0
for i in range(-1000,1001):
    for j in range(-1000,1001):
        c = 1
        while isprime(c**2 + i * c + j) == True:
            c += 1
        if c > maxval:
            maxval = c
            print (i,j,maxval,i*j)

print ('done')
'''
print (isprime(61))

for i in range(10):
    print (i ** 2 + i * -999 + 61)
'''
