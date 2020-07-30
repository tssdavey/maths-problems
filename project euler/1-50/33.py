from fractions import Fraction
import numpy as np
'''
for i in range(1,100):
    istr = str(i)
    for j in range(1,100):
        print ('---------------------')
        print (i,j)
        tmpistr = istr[:]
        jstr =  str(j)
        try:
            matchdig = str([digit for digit in istr if digit in jstr and digit != 0][0])
            x = float(i/j)
            print (x)
            tmpistr = tmpistr.replace(matchdig,'')
            jstr = jstr.replace(matchdig,'')
            try:
                print (matchdig,tmpistr,jstr)
                y = float(int(tmpistr)/int(jstr))
                print (y)
                if x == y:
                    print (i,j)
            except (ZeroDivisionError,ValueError):
                pass
        except IndexError:
            pass
'''

for i in range(1,100):
    istr = str(i)
    for j in range(i,100):
        if j == i:
            continue
        jstr = str(j)
        tmpistr = istr[:]
        try:
            matchdig = str([digit for digit in istr if (digit in jstr and digit != '0')][0])
            tmpistr = tmpistr.replace(matchdig,'')
            jstr = jstr.replace(matchdig,'')
            try:
                if len(tmpistr) > 0 and len(jstr) > 0:
                    if Fraction(i,j) == Fraction(int(tmpistr),int(jstr)):
                        #print ('-------------------------')
                        #print (matchdig)
                        #print (i,j)
                        print (tmpistr,jstr)
            except ZeroDivisionError:
                pass
        except IndexError:
            pass
print (5*5*4)
