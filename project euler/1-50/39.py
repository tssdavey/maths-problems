maxc = 0
for p in range(10,1000):
    c = 0
    for i in range(1,p):
        for j in range(i,p):
            if i ** 2 + j ** 2 == (p - i - j) ** 2:
                c += 1
                #print (i,j,p-i-j)
    if c > maxc:
        maxc = c
        print (p)
print ('yeet')
