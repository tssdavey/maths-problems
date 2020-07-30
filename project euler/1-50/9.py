for i in range(1,998):
    for j in range(i,999):
        k = 1000 - i - j
        if k >= j:
            c = k
            b = j
        else:
            c = j
            b = k
        if i ** 2 + b ** 2 == c ** 2:
            print (i,b,c)
            print (i*b*c)
            break
