number = 600851475143
#brute force it is I guess
maxval = 0
for num in range(1,10000):
    if number % num == 0:
        maxval = num
print (maxval)
