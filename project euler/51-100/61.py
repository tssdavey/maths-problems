global mydict
import math
myset = {}
def tri(n):
    arr = []
    maxi = int((-1 + math.sqrt(1+8*n))//2)
    i = 1
    while i <= maxi:
        arr.append((i)*(i+1)//2)
        i += 1
    return arr
'''
def sqr(n):
    tmpset = set()
    maxi = int(math.sqrt(n))
    i = 1
    while i <= maxi:
        tmpset.add(''.join(sorted(str(i**2))))
        i += 1
    return (tmpset)

def pent(n):
    tmpset = set()
    maxi = int((1+math.sqrt(n))//6)
    i = 1
    while i <= maxi:
        tmpset.add(''.join(sorted(str(i*(3*i - 1)//2))))
        i += 1
    return (tmpset)

val = 1000
myset = {''.join(sorted(str(x))) for x in tri(val)}
myset = myset.intersection(sqr(val))
myset = myset.intersection(pent(val))
print (myset)
'''
def gen(func,ifunc,n):
    myset = set()
    mini = int(ifunc(1001))
    maxi = int(ifunc(n))
    i = mini
    while i <= maxi:
        myset.add(str(func(i)))
        i += 1
    return (myset)

val = 9999
triset = gen(lambda x : (x)*(x+1)//2, lambda x: (-1 + math.sqrt(1+8*x))//2,val)
sqrset = gen(lambda x : (x)**2, lambda x: math.sqrt(x),val)
pntset = gen(lambda x : (x)*(3*x - 1)//2, lambda x: (1+math.sqrt(1+24*x))//6,val)
hexset = gen(lambda x : (x)*(2*x - 1), lambda x: (1+math.sqrt(1+8*x))//4,val)
hepset = gen(lambda x : (x)*(5*x - 3)//2, lambda x: (3+math.sqrt(3+40*x))//10,val)
octset = gen(lambda x : (x)*(3*x - 2), lambda x: (2+math.sqrt(2+12*x))//6,val)
setlist = [triset,sqrset,pntset,hexset,hepset,octset]
#print (setlist)
setdictlist = []
for i,set in enumerate((setlist)):
    setdictlist.append({})
    #print (set)
    for e in set:
        k = e[:2]
        v = e[2:]
        if k in setdictlist[i]:
            setdictlist[i][k].append(v)
        else:
            setdictlist[i][k] = [v]
#print (*setdictlist,sep='\n')

comblist = []
for k,vs in setdictlist[0].items():
    for v in vs:
        comblist.append([(0,k),(0,v)])
#print (comblist)
k = 0
for i in range(5):
    tmpcomblist = comblist.copy()
    for comb in tmpcomblist:
        whole = list(range(0,6))
        #print (whole)
        #print (comb)
        for index,item in comb:
            if index in whole:
                whole.remove(index)
            test = item
        #print (whole)
        for j in whole:
            #print (j)
            if test in setdictlist[j]:
                valid = True
                for v in setdictlist[j][test]:
                    tmpcomb = comb.copy()
                    tmpcomb.append((j,v))
                    #print (tmpcomb)
                    comblist.append(tmpcomb)
        comblist.remove(comb)
#print (*comblist,sep='\n')
print ('-----------------')
for comb in comblist:
    if comb[0][1] == comb[6][1]:
        print (comb)
        print (sum([int(x[1]) + int(x[1])*100 for x in comb[:-1]]))
