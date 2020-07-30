m = 10000000
arr = [1] * (m + 1)

i = 1
while True: #iterating thru coin values
    for j in range(i,m):
        arr[j] += arr[j - i-1]
    #if arr[i] == 7:
    if arr[i] % 1000000 == 0:
        print (i+1)
        break
    i += 1
    #print (arr)


'''
for i in range(m//10,m):
    if arr[i] % 1000000 == 0:
        print (i)
'''
print ('done')
