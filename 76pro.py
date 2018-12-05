n=int(raw_input(""))
c=0
if n>1:
    for i in range(2,n):
        if n%i==0:
            c=c+1
if c>1:
    print "yes"
else:
    print "no"
