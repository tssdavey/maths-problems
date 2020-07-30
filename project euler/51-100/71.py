from math import factorial as f
import numpy as np
from fractions import Fraction

print(Fraction(3,7)-Fraction(2,5))

m = 1000000

target = (f(6)*np.prod(range(8,m+1))*3)
print (target)
mindiff = 10000000
'''
for i in range(2,m+1):
    for j in range(2,i):
        x = (f(i - 1)*np.prod(range(i+1,m+1))*j)
        if x > target:
            break
        elif (target - x) < mindiff:
            mindiff = target - x
            print (i,j)
'''
target = Fraction(3,7)
preval = 1
mindiff = 1

for i in range(2,m+1):
    curval = preval
    curfrac = Fraction(curval,i)
    while Fraction(curval,i) < target:
        if target - curfrac < mindiff:
            mindiff = target - curfrac
            #print (curfrac)
        #print (Fraction(curval,i))
        curval += 1
        curfrac = Fraction(curval,i)
    preval = curval - 1
print (target - mindiff)
