from math import factorial as f
ans = 0
for i in range(10,100000):
    digsum = 0
    for dig in str(i):
        digsum += f(int(dig))
    if digsum == i:
        print (i)
        ans += i

print (ans)
