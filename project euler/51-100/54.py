filepath = 'C:\\Users\\Tadhg\\Documents\\Github\\project-euler\\51-100\\p054_poker.txt'
import csv
from collections import Counter

def fix(hand):
    valdict = {'2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14}
    for i,(n,s) in enumerate(hand):
        hand[i] = (valdict[n],s)
    return hand

def straight(hand):
    nums = [n for n,s in hand]
    numsa = [n if n != 14 else 1 for n in nums]
    if sorted(nums) == list(range(min(nums),max(nums)+1)):
        return (True,min(nums))
    elif sorted(numsa) == list(range(min(numsa),max(numsa)+1)):
        return (True,min(nums))
    return False

def flush(hand):
    suits = [s for n,s in hand]
    return all(x == suits[0] for x in suits)

def count(hand,check):
    nums = [n for n,s in hand]
    c = Counter(nums)
    return (check in c.values(),[n for n in c if c[n] == check])

def compare(hands):
    #0 - draw, 1 - hand1, 2 - hand2
    hand1 = [(x[0],x[1]) for x in hands[0].split(' ')[:5]]
    hand2 = [(x[0],x[1]) for x in hands[0].split(' ')[5:]]
    print (hand1,hand2)
    hand1 = fix(hand1)
    hand2 = fix(hand2)
    #[,Straight,Flush,4]
    hand1result = [0]*8
    hand2result = [0]*8
    try:
        hand1result[1] = straight(hand1)[0]
    except TypeError:
        hand1result[1] = False
    try:
        hand2result[1] = straight(hand2)[0]
    except TypeError:
        hand2result[1] = False
    hand1result[2] = flush(hand1)
    hand2result[2] = flush(hand2)
    print (hand1result,hand2result)
    if hand1result[1] == True and hand1result[2] == True:
        if hand2result[1] == False or hand2result[2] == False:
            return 1
        elif straight(hand1)[1] > straight(hand2)[1]:
            return 1
        elif straight(hand1)[1] < straight(hand2)[1]:
            return 2
        else:
            return 0
    if count(hand1,4)[0] == True:
        if count(hand2,4)[0] == False:
            return 1
        elif count(hand1,4)[1] > count(hand2,4):
            return 1
        elif count(hand1,4)[1] < count(hand2,4):
            return 2
        else:
            return 0
    if count(hand1,3)[0] == True and count(hand1,2)[0] == True:
        if count(hand2,3)[0] == False or count(hand2,2)[0] == False:
            return 1
        elif count(hand1,3)[1] > count(hand2,3)[1]:
            return 1
        elif count(hand1,3)[1] < count(hand2,3)[1]:
            return 2
        else:
            if count(hand1,2) > count(hand2,2):
                return 1
            elif count(hand1,2) < count(hand2,2):
                return 2
            else:
                return 0
    if hand1result[2] == True:
        if hand2result[2] == False:
            return 1
        else:
            return 0




with open(filepath,encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        print (compare(row))
        break
