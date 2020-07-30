iarr = map(str,range(10000))
jarr = map(str,range(10000))
pan = ['1','2','3','4','5','6','7','8','9']
good = True
#iarr = ['39']
#jarr = ['186']
ans = 0
al = {}
for i in iarr:
    jarr = map(str,range(10000))
    for j in jarr:
        if len([letter for letter in i if letter in j]) == 0:
            x = i + j + str(int(i)*int(j))
            if len(x) == 9:
                good = True
                for k in pan:
                    if k not in x:
                        good = False
                        break
                if good == True and int(i)*int(j) not in al:
                    al[int(i)*int(j)] = 1
                    ans += int(i)*int(j)
    if i =='1000':
        break
print (ans)
