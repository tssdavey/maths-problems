maxval = 0
for i in range(100,1000):
    for j in range(i,1000):
        x = i*j
        if str(x) == str(x)[::-1] and x > maxval:
            maxval = x
print (maxval)
