n = ['1','2','3','4','5','6','7','8','9']
for i in range(100,10000):
    arr = []
    for j in range(1,4):
        arr += list(str(i*j))
        if sorted(arr) == n:
            print (arr)
            print (i)
