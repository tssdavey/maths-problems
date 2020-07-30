#sum of a mythagorean triple is 2(m)(m+n) where triple is (m^2 - n^2) + 2mn = m^2 + n^2
#2m(m+n) = x => n = x/2m - m so then need to test if n in an integer
import math
for num in range(1,50):
    #print(num)
    for m in range(1,int(math.sqrt(num//2))+1):
        n = num/2/m - m
        if n == int(n) and m >= n and n != 0 and n != m:
            print (num, ':',m**2 -  n**2, 2*m*n, m**2 + n**2)
