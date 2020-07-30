from itertools import combinations as c
from itertools import permutations as p
from itertools import product as prod
import math
def isprime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 2
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return i
    return True
'''
#this way using permutations is super stupid
#well i guess I'm just calling lists tuples now
nodigits = 7
maxcount = 0
for tuple in map(list,p(['*'] * nodigits + ['1','2','3','4','5','6','7','8','9'],nodigits)):
#for tuple in [['5','6','*','*','3']]:
    if '*' in tuple and tuple[0] != '*':
        #print (tuple)
        count = 0
        for i in range(10):
            #print ([str(i) for x in tuple if x == '*'])
            #print (''.join([str(i) if x == '*' else x for x in tuple]))
            if isprime (int(''.join([str(i) if x == '*' else x for x in tuple]))) == True:
                count += 1
        #print (count)
        if count == 8:
            #maxcount = count
            print (tuple)

print (maxcount)
'''
'''
# ***857
# *4*6*9
tuple = ['5', '*', '7', '4', '*', '*', '9']

#tuple = ['*', '4', '*', '6', '*', '9']
#tuple = ['*', '*', '*', '8', '5', '7']
minval = 100000000
for i in range(10):
    print (int(''.join([str(i) if x == '*' else x for x in tuple])))
    if isprime (int(''.join([str(i) if x == '*' else x for x in tuple]))) == True:
        if int(''.join([str(i) if x == '*' else x for x in tuple])) < minval:
            minval = int(''.join([str(i) if x == '*' else x for x in tuple]))
print (minval)
'''

#print (*p(['1','2','3']))

arr = []
'''
for l in map(list,p(['1','2','3','4'],3)):
    print (l)
    for i in range(1,4):
        print (l[:i] + ['*'] + l[i:])
        arr.append(l[:i] + ['*'] + l[i:])
'''

'''
no_ast = 2
for l in map(list,p(['1','2','3','4'],2)):
    print (l)
    for tuple in map(list,c(['1','2','3'],no_ast)):
        to_app = list(p(tuple+['*']*no_ast))
        if to_app[0] != '*':
            arr += (to_app)
    pass
'''
'''
digits = 6
for i in range(1,digits):
    no_ast = i
    no_num = digits - i
    for tuple in map(list,c(['0','1','2','3','4','5','6','7','8','9'],no_num)):
        to_app = list(p(tuple+['*']*no_ast))
        if to_app[0] != '*':
            arr += (to_app)

#print (arr)
#print (arr.index(('5','6','*','*','3')))
#print (arr[36033])
target = 8
for array in arr:
#for array in [('5', '6', '*', '*', '3')]:
    c = 0
    for i in range(10):
        #print (''.join([str(i) if x == '*' else x for x in array]))
        if isprime((int(''.join([str(i) if x == '*' else x for x in array])))) == True:
            c += 1
        #print (c)
    if c == target:
        print (array)
'''


minval = 10000000000
tuple = ['5', '*', '7', '4', '*', '*', '9']
tuple = ['5', '*', '8', '*', '0', '*', '9']
tuple = ['*', '*', '*', '1', '0', '9']
tuple = ['*', '4', '*', '6', '*', '9']
#tuple = ['*', '*', '*', '8', '5', '7']
for i in range(10):
    if isprime (int(''.join([str(i) if x == '*' else x for x in tuple]))) == True:
        print (int(''.join([str(i) if x == '*' else x for x in tuple])))
        if int(''.join([str(i) if x == '*' else x for x in tuple])) < minval:
            minval = int(''.join([str(i) if x == '*' else x for x in tuple]))
print (minval)




'''
print (*c([0,1,2,3],2))
'''
#print (arr)

#for i in range()
