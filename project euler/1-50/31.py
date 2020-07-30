'''two = [1,1]
five = [2,2,1]
ten = [5,5]
twenty = [10,10]
fifty = [20,20,10]
pound = [50,50]
twopound = [100,100]
from collections import defaultdict

n = 20
arr = [n]
ending = [1]*n

def reduce(arr):
    print ('------')
    mydict = {2:[1,1],5:[2,2,1],10:[5,5],20:[10,10],50:[20,20,10],100:[50,50],200:[100,100]}

    for i,item in enumerate(arr):
        if item in mydict:
            tmp = arr[:]
            del tmp[i]
            tmp += mydict[item]
            print (tmp)
            yield (tmp)

while arr != ending:
    countdict = defaultdict(list)
    masterarrlist = []
    arrlist = [arr]
    while len(arrlist) > 1 or arrlist[0] != ending:
        for arr in arrlist:
            if arr not in masterarrlist:
                masterarrlist.append(arr)
            arrlist = list(reduce(arr))
    break
print (len(masterarrlist)+1)
'''
'''
n = 20
start = {1:n,2:0,5:0,10:0,20:0}

def reduce(d):
    if d[1] >= 2:
        tmp = d.copy()
        tmp[1] -= 2
        tmp[2] += 1
        yield tmp
    if d[1] >= 5:
        tmp = d.copy()
        tmp[1] -= 5
        tmp[5] += 1
        yield tmp
    if d[1] >= 10:
        tmp = d.copy()
        tmp[1] -= 10
        tmp[10] += 1
        yield tmp
    if d[1] >= 20:
        tmp = d.copy()
        tmp[1] -= 20
        tmp[20] += 1
        yield tmp
    if d[1] >= 50:
        tmp = d.copy()
        tmp[1] -= 50
        tmp[50] += 1
        yield tmp
    if d[1] >= 100:
        tmp = d.copy()
        tmp[1] -= 100
        tmp[100] += 1
        yield tmp
    if d[1] >= 200:
        tmp = d.copy()
        tmp[1] -= 200
        tmp[200] += 1
        yield tmp
    if d[2] >= 2 and d[1] >= 1:
        tmp = d.copy()
        tmp[1] -= 1
        tmp[2] -= 2
        tmp[5] += 1
        yield tmp
    if d[2] >= 5:
        tmp = d.copy()
        tmp[2] -= 5
        tmp[10] += 1
    if d[2] >= 10:
        tmp = d.copy()
        tmp[2] -= 10
        tmp[20] += 1
    if d[2] >= 25:
        tmp = d.copy()
        tmp[2] -= 25
        tmp[50] += 1
    if d[2] >= 50:
        tmp = d.copy()
        tmp[2] -= 50
        tmp[100] += 1
    if d[2] >= 100:
        tmp = d.copy()
        tmp[2] -= 100
        tmp[200] += 1
    if d[5] >=
print (*reduce(start))
'''
'''
import itertools
list1 = [1] * 200
list2 = [2] * 100
list5 = [5] * 40
list10 = [10] * 20
list20 = [20] * 10
list50 = [50] * 4
list100 = [100] * 2
list200 = [200]
mylist = list1 + list2 + list5 + list10 + list20 + list50 + list100 + list200
c = 0
print (len(list(itertools.combinations(mylist,200))))
for mylist in list(itertools.combinations(mylist,200)):
    if sum(mylist) == 200:
        c += 1
print (c)
'''
max = 200
cs = [1, 2, 5, 10, 20, 50, 100, 200]
x = [1] + [0]*max

for c in cs:
    #print (c)
    for i in range(c, max+1):
        #print (i)
        #print ('there are ',x[i-c],'ways of making',i-c,'\n')
        x[i] += x[i-c]
    print (*enumerate(x))
print (x[max])
