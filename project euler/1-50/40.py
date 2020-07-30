c = 1
arr = []
m = 7
while len(arr) < 10 ** m + 1 :
    arr += list(str(c))
    c += 1
a = 1
for i in range(m):
    print (arr[10 ** i - 1])
    a *= int(arr[10 ** i - 1])
print (a)
