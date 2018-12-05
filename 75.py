n=raw_input("")
b=len(n)
string=list(n)
if b%2==0:
    middle=b/2 - 1
    string[middle]='*'
    string[middle+1]='*'
else:
    middle=b/2 - 1
    string[middle+1]='*'
print "".join(string)

