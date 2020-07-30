def palindrome(n):
    return str(n) == str(n)[::-1]

def iter(n):
    return (n+int(str(n)[::-1]))

c = 0
for n in range(1,10001):
    i = 0
    v = 1
    while i < 50:
        n = iter(n)
        if palindrome(n) == True:
            v = 0
            break
        i += 1
    if v == 1:
        c += 1
print (c)
