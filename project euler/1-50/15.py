'''
at each point your choices are either to go right or down
until you have gone right or down 10 times, at that point your only choice is to do the other
ie number of unique permutations of the list [0,0...,0,1,1,...,1]
which is 40C20
'''

from math import factorial as f
print (f(40) // f(20) // f(20))
