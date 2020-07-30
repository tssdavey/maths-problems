#the stmart way to do this seems to me me to notice that all primes numbers etc will have all fractions, and for other numbers some of the fractions will already be in the set but simplified
#BUT python has a fraction library which makes it not too bad to brute force
from fractions import Fraction

m = 1000000
myset = set()
for i in range(2,m+1):
    for j in range(1,i):
        if Fraction(j,i) not in myset:
            myset.add(Fraction(j,i))
print (len(myset))
