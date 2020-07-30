arr = [0,1,2,3,4,5,6,7,8,9]
#arr = [3,2,1,4]
#arr = [5,2,4,3,1]
#arr = [0,1,2,5,3,3,0]
l = len(arr)
c  = 0
tmp = 0
print (arr)
pivindex = 0
ceilindex = 0
comp = 0
while c < 999999:
    for i in range(l-1,0,-1):
        #print (arr[i-1],arr[i])
        if arr[i-1] < arr[i]:
            pivindex = i - 1
            #print (arr[pivindex])
            minval = 11
            for j in range(pivindex+1,l):
                #print (arr[j])
                comp = arr[j] - arr[pivindex]
                if comp <= minval and comp > 0:
                    ceilindex = j
                    minval = comp
            #print (arr[ceilindex])
            tmp = arr[ceilindex]
            arr[ceilindex] = arr[pivindex]
            arr[pivindex] = tmp
            x = (arr[:pivindex+1])
            y = (arr[1+pivindex:][::-1])
            arr = x + y
            #print (arr)
            break
    c += 1
print (c)
print (*arr,sep='')
#print (pivindex)
#print (ceilindex)
