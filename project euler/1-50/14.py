mydict = {1:0}
resdict = {}

for i in range(1,1000001):
    num = i
    prev = 0
    c = 0
    while num not in mydict:
        prev = num
        if num % 2 != 0:
            num = num * 3 + 1
        else:
            num = num // 2
        c += 1


    mydict[prev] = mydict[num] + 1
    resdict[i] = c + mydict[num]

maxv = 0
for k,v in resdict.items():
    if v > maxv:
        print (k)
        maxv = v
