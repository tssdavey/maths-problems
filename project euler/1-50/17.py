lngth = 0
for i in range(1,1000):
    prv = lngth
    unitsdict = {'0':0,'1':3,'2':3,'3':5,'4':4,'5':4,'6':3,'7':5,'8':5,'9':4}
    tensdict = {'0':0,'1':3,'2':6,'3':6,'4':5,'5':5,'6':5,'7':7,'8':6,'9':6}
    teensdict = {'11':6,'12':6,'13':8,'14':8,'15':7,'16':7,'17':9,'18':8,'19':8}
    i = str(i)
    if len(i) == 1:
        lngth += unitsdict[i]
    elif len(i) == 2:
        if int(i) > 19 or int(i) < 11:
            lngth += unitsdict[i[1]]
            lngth += tensdict[i[0]]
        else:
            lngth += teensdict[i]
    elif len(i) == 3:
        if int(i[1:]) > 19 or int(i[1:]) < 11:
            lngth += unitsdict[i[2]]
            lngth += tensdict[i[1]]
            lngth += unitsdict[i[0]]
            lngth += 10
        else:
            lngth += unitsdict[i[0]]
            lngth += teensdict[i[1:]]
            lngth += 10
    print (i,lngth-prv,sep=':')

#add one thoughsand
#minus the 'one hundered and' which should be one hundered
print(lngth + 11 - 3 * 9)
#print (lngth)
