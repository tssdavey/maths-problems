maxval = 0
for i in range(2,1000):
    j = 1
    if i % 2 == 0 or i % 5 == 0:
        #print ('fac')
        pass
    else:
        while (10 ** j) % i != 1:
            j += 1
    if j > maxval:
        print (i,j)
        maxval = j

print (maxval)
