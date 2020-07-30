ans = 0
for i in range(1000000):
    if sum([int(num)**5 for num in str(i)]) == i:
        ans += i
print (ans-1)
