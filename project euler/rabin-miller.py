import random
def isprime(n):
    k = 2
    d = n-1
    s = 0
    while d % 2 == 0:
        s += 1
        d = d // 2
    print (d,s)
    def comp(x):
        for r in range(1,s):
            x = (x**2) % n
            if x == 1:
                return False
            elif x == n-1:
                return True
        return False
    for i in range(k):
        x = ((random.randint(2,n))**d) % n
        if x == 1 or x == n-1:
            continue
        if comp(x):
            continue
        else:
            return False
    return (True)



print (isprime(31432819))
