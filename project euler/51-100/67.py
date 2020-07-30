filepath = 'C:\\Users\\Tadhg\\Documents\\Github\\project-euler\\51-100\\p067_triangle.txt'
import csv
arr = []
with open(filepath,encoding="utf8") as csv_file: #well i guess if it works it works
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        arr.append(list(map(int,row[0].split(' '))))

arr.reverse()
print (arr[len(arr)-1])

for i in range(1,len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] += max(arr[i-1][j],arr[i-1][j+1])
print (arr[-1:])
