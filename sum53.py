j=int(raw_input())
s=[]
while(j>0):
    dig=j%10
    s.append(dig)
    j=j//10
print sum(s)
