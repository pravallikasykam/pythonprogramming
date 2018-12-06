import math
j,p=map(int,raw_input().split())
a=j * p
if math.sqrt(a).is_integer():
    print "yes"
else:
    print "no"
