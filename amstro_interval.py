N,Q=map(int,input().split())
for i in range(N+1,Q):
    sum=0
    temp=i
    while (i>0):
        digit=i%10
        sum=sum+(digit**3)
        i=i//10
    if temp==sum:
        print(sum,end=" ")
