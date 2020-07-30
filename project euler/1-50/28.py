x = 1001
c = 1
sm = 1
for i in range(x//2):
    for j in range(4):
        c += (i+1) * 2
        sm += c
print (sm)
