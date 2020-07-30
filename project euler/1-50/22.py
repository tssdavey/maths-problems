
filepath = 'C:\\Users\\Tadhg\\Desktop\\p022_names.txt'
arr = []

content = open(filepath,'r').read()
arr = ([x.strip('"') for x in content.split(',')])
arr = sorted(arr)
#print (arr)
ans = 0
for i,name in enumerate(arr):
    #print (i,name)
    ans += sum([ord(letter) - 64 for letter in name]) * (i + 1)
print (ans)

'''
with open(filepath,encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        arr.append(row)
'''
