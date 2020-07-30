import math
def ab(n):
    ans = 0
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            ans += i
            if n //i != i:
                ans += n // i
        if ans > n:
            return True
    return False

mydict = {}
mydict2 = {}
for i in range(1,23124):
    mydict[i] = ab(i)
    mydict2[i] = 1

ks = [k for k,v in mydict.items() if v ==  True]
print (ks[62])
for i in range(len(ks)):
    for j in range(i,len(ks)):
        mydict2[ks[i]+ks[j]] = 0
#print ([k for k,v in mydict2.items() if v == 1])
print (sum([k for k,v in mydict2.items() if v == 1]))
