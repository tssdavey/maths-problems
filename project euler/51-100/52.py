n = 1
x = 6
while True:
    valid = True
    for i in range(1,7):
        if sorted(str(n*i)) != sorted(str(n)):
             valid = False
             break
    if valid == True:
        print (n)
        break
    n += 1
#this is a roating digits of multiples of 7 thing
