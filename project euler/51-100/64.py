import math
def sim(x,y,n):
    #print ('---------------')
    #print (x,y,n)
    z = int(x / ((math.sqrt(n)-y)))
    #print (z)
    if (n - y **2) % x != 0:
        print ('major malfunction')
    return -1*((x*y)-(z*(n-y**2)))//x,(n-y**2)//x,z

print (sim(3,2,13))
#print (sim(1,4,23))
c = 0

for i in range(2,10001):
    #print ('------------------')
    #print (i)
    #print (math.sqrt(i)**2)
    if int(math.sqrt(i))**2 == i:
        print ('continueing')
        #print ('perfect square')
        continue

    x,y,z = 1,int(math.sqrt(i)),4
    t = (x,y,z)
    t = (0,0,0)
    #print (int(math.sqrt(i)))
    myset = set()
    #print (myset)
    #print (t)
    while t not in myset:
        myset.add(t)
        y,x,z = sim(x,y,i)
        t = (x,y,z)
        #print (x,y,z)
    #print (len(myset)-1)
    if (len(myset)-1) % 2 == 1:
        #print (i)
        c += 1
print (c)
