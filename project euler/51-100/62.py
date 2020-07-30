mydict = {}
mydict2 = {}
i = 1
testval = 5
while True:
    cubestr = str(sorted(str(i ** 3)))
    if cubestr in mydict:
        if mydict[cubestr] == testval - 1:
            print (int(mydict2[cubestr][0])**3)
            break
        mydict2[cubestr].append(i)
        mydict[cubestr] += 1
    else:
        mydict[cubestr] = 1
        mydict2[cubestr] = [i]
    i += 1
