import math
def ishex(n):
    calc = (1 + math.sqrt(1+8*n))/4
    if calc == int(calc):
        return True
    return False

def ispen(n):
    calc = (1 + math.sqrt(1+24*n))/6
    #print (calc)
    if calc == int(calc):
        return True
    return False

i = 280
t = (i * (i + 1)) // 2
i = 286
t = (i * (i + 1)) // 2
while ispen(t) == False or ishex(t) == False:
    i += 1
    t = (i * (i + 1)) // 2

#print (ispen(3))
#print (ishex(3))
print (i,t)
