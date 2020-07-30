from math import factorial as f

c = 0
mydict = []
for num in map(str,range(0,1000001)):
    seen = set()
    #print (num)
    mysum = sum([f(int(dig)) for dig in num])
    while mysum not in seen:
        seen.add(mysum)
        num = str(mysum)
        mysum = sum([f(int(dig)) for dig in num])
    #print (len(seen))
    if len(seen) +1 == 60:
        c += 1
        #print (num)
print (c)
