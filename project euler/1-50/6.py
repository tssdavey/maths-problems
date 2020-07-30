mysum = 0
sqrsum = 0

mysum = sum(range(101))
sqrsum = sum([x**2 for x in range(101)])

print (pow(mysum,2)-sqrsum)
