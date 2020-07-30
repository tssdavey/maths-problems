num = 3
c = 2
while c < 10002:
    prime = True
    c += 1
    for i in range(2,num // 2):
        if num % i == 0:
            c -= 1
            prime = False
            break
    num += 2
print (num-2)
print (c-1)
