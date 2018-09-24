import collections
import string
from string import printable
def myAtoi(string):
    res = 0

    # Iterate through all characters of input string and
    # update result
    for i in xrange(len(string)):
        res = res*10 + (ord(string[i]) - ord('0'))

    return res
printable = set(string.printable)
f1=open("hashmarkserver1.","r")
f2=open("hashmarkserver2.txt","r")
f1dict={}
f2dict={}

for l in f1:
    l=l.strip(" ")
    l=l.split()
    l[-1]=filter(lambda x: x in printable, l[-1])
    f1dict[myAtoi(l[-1])]=l[2]
for l in f2:
    l=l.strip(" ")
    l=l.split()
    l[-1]=filter(lambda x: x in printable, l[-1])
    f2dict[myAtoi(l[-1])]=l[2]

od1 = collections.OrderedDict(sorted(f1dict.items()))
od2 = collections.OrderedDict(sorted(f2dict.items()))
for i in od1.keys():
    if od1[i]!=od2[i]:
        print "DIFFERENT HASH"
