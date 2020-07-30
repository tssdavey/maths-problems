m = 0
for i in range (101):
    for j in range(101):
        if sum([int(d) for d in str(i ** j)]) > m:
            m = sum([int(d) for d in str(i ** j)])
            print (i,j)
print (m)
