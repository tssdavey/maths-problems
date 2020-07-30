p = []
v = 100000
for n in range(1,v+1):
    p.append(n*(3*n -1)//2)
#print (p)

for i in range(v):
    for j in range(i,v):
        #print (i,j)
        #if p[i] + p[j] in p:
            #print ('1',p[i] + p[j])
        #if p[i] - p[j] in p:
            #print ('2,',p[j] - p[i])
        if p[i] + p[j] in p and p[j] - p[i] in p:
            print (i,j)
