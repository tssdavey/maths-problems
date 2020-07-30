num = 3
ans = 0
while num < 2000000:
    if (num+1) % 100000 == 0:
        print (num)
        print (ans)
    prime = True
    for i in range(3,num // 2,2):
        if num % i == 0:
            prime = False
            break
    if prime == True:
        ans += num
    num += 2

print (ans+2)

#399999
#6458901529

'''
499999
9914236193


599999
14071226344


699999
18910286310

799999
24464863437

'''
