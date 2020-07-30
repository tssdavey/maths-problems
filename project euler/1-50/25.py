f1 = 1
f2 = 1
c = 2
while len(str(f2)) < 1000:
    tmp = f2
    f2 += f1
    f1 = tmp
    c += 1
print (c)
