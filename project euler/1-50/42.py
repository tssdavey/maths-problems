import csv
import math
filepath = 'C:\\Users\\Tadhg\\Documents\\GitHub\\project-euler\\1-50\\p042_words.txt'
arr = []
with open(filepath,encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        arr = row
print (arr)
a = 0
#arr = ['SKY']
for word in arr:
    x = sum([ord(letter)-64 for letter in word]) * 8 + 1
    if int(math.sqrt(x) + 0.5) ** 2 == x:
        a += 1
print (a)
