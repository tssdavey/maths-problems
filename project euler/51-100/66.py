import math
#this solution was sponsered by wikipedia's explanatoin of pell equations
#and also the previous two problems
def sim(x,y,n):
    #print ('---------------')
    #print (x,y,n)
    z = int(x / ((math.sqrt(n)-y)))
    #print (z)
    if (n - y **2) % x != 0: #good sanity check
        print ('major malfunction')
    return -1*((x*y)-(z*(n-y**2)))//x,(n-y**2)//x,z

def add (i,n,d): #iteger numerator, denominator
    return (i * d + n, d) #numerator, demoinator

c = 0
maxval = 0
for i in range(2,1001):
    #print (i)
    flrroot = int(math.sqrt(i))
    if int(flrroot)**2 == i:
        continue
    x,y,z = 1,int(math.sqrt(i)),4
    t = (x,y,z)
    t = (0,0,0)
    myset = set()
    mylist = []
    while t not in myset:
        myset.add(t)
        y,x,z = sim(x,y,i)
        mylist.append(z)
        t = (x,y,z)
        #print (t)
    '''
    if (len(myset)-1) % 2 == 1:
        c += 1
    '''
    del mylist[-1:] #remove extra element from list which matches first element
    #print (mylist)
    mylist = mylist + mylist #i dont know why you have to repeat the list, but it does not pick up big numbers unless you do
    for j in range(1,len(mylist)+1):
        fracreplist = mylist[:j]
        fracreplist.reverse() #reve
        n = 1
        d = fracreplist[0]
        del fracreplist [0]
        #print (fracreplist)
        for k in fracreplist:
            d,n = add(k,n,d)
        n,d = add(flrroot,n,d)
        if (n**2) - (i*(d**2)) == 1:
            #print (n,d)
            if n > maxval:
                print (i,n,d)
                maxval = n
            break
print (c)
