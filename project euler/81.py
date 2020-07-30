import os
#80x80
print (os.getcwd())
ddarr = []
m = 80
matrix = open('51-100/p081_matrix.txt','r').read()
for row in (matrix.split('\n')[:-1]):
    ddarr.append(list(map(int,row.split(','))))
#print (*ddarr,sep = '\n')
print (len(ddarr))

for i in range(1,m):
    ddarr[m-1][m-i-1] += ddarr[m-1][m-i]
    ddarr[m-i-1][m-1] += ddarr[m-i][m-1]
    #print (ddarr[m-1][m-i-1])

for i in range(2,m+1):
    for j in range(1,i-1):
        #print (m-j-1,m-i+j)
        #print (ddarr[m-j-1][m-i+j])
        #print (min(ddarr[m-j][m-i+j],ddarr[m-j-1][m-i+j+1]))
        ddarr[m-j-1][m-i+j] += min(ddarr[m-j][m-i+j],ddarr[m-j-1][m-i+j+1])
#print (*ddarr,sep = '\n')

for i in range(1,m):
    for j in range(m-i):
        ddarr[m-i-j-1][j] += min(ddarr[m-i-j-1][j+1],ddarr[m-i-j][j])
print (ddarr)
