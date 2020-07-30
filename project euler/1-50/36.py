from itertools import combinations as c
from itertools import permutations as p

#PALINDROME GENERATOR
n = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]
pals = []
for i in range(1,4):
    #print (i)
    #print (*c(n,i))
    pals += [x[:-1]+x[::-1] for x in c(n,i) if x[0] != 0]
    pals += [x+x[::-1] for x in c(n,i) if x[0] != 0]
a = 0
pals = []
for i in map(str,range(1,1000)):
    pals.append(i[:-1]+i[::-1])
    pals.append(i+i[::-1])
mydict = {}
for pal in pals:
    x = str(bin(int(''.join([str(x) for x in pal]))))[2:]
    if x == x[::-1] and x not in mydict:
        mydict[x] = 1
        #print (pal)
        #print (x)
        a += int(pal)
print (a)
a = 0
for i in range(1,1000000):
    stri = str(i)
    x = bin(i)[2:]
    if stri == stri[::-1] and x == x[::-1]:
        #print (i)
        #print (x)
        a += i
print (a)
