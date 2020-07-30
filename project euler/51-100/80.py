import math
import decimal
#print (sum([int(x) for x in str(decimal.Decimal(2).sqrt(decimal.Context(prec=100)))]))

ans = 0
for n in range(1,100):
    x = math.sqrt(n)
    if x == int(x):
        continue
    print (n)
    #n = 4
    #print (*[x for x in str(decimal.Decimal(n).sqrt(decimal.Context(prec=100)))][len(str(int(math.sqrt(n))))+1:],sep='\n')
    #if n % 2 != 0 and n != 5 != 0:
    #len(str(int(math.sqrt(n))))+1
    arr = [x for x in str(decimal.Decimal(n).sqrt(decimal.Context(prec=170))) if x != '.'][:100]
    print (len(arr))
    print (*arr,sep='')
    print (sum([int(x) for x in arr]))
    ans += (sum([int(x) for x in arr]))
print (ans)

#414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572
'''
a = '414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572'
print (sum([int(x) for x in a]))
'''
