M,N,K = [int(x) for x in raw_input().split()]
sum=0
for i in range(K):
 sum+=M+(i*N)
print (sum)
