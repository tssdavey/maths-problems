arr = [1,2]
answer = 0
while arr[len(arr)-1] < 4000000:
    arr.append(arr[len(arr)-2]+arr[len(arr)-1])
    if arr[len(arr)-1] % 2 == 0:
        answer += arr[len(arr)-1]
print (answer)
a
