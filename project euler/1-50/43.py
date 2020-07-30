from itertools import combinations as c
from itertools import permutations as p
n = ['0','1','2','3','4','5','6','7','8','9']
ar = [2,3,5,7,11,13,17]
a = 0
for tuple in p(n,10):
    #print (tuple)
    #break
#for tuple in [('1','4','0','6','3','5','7','2','8','9')]:
    t = 1
    for i in range(7):
        #print (int(''.join(tuple[(1+i):(4+i)])))
        #print (ar[i])
        #print (int(''.join(tuple[(2+i):(5+i)])) % (ar[i]))
        if int(''.join(tuple[(1+i):(4+i)])) % ar[i] != 0:
            t = 0
            break
    if t == 1:
        print(tuple)
        a += int(''.join(tuple))
    #print (tuple[2:5])
    #''.join(tuple)

print (406%2)
print (a)
