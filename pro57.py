j,p=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
if p in list:
    count=list.count(p)
    print count
else:
    print 0
