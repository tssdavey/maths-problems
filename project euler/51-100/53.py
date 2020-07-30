from math import factorial as f
n = 100
c = 0
for i in range(1,n+1):
    for j in range(1,(i+1)//2+1):
        if f(i) // f(j) // f(i-j) > 1000000:
            c += i - 2*j + 1
            break
print (c)
