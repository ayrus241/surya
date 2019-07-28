a=[]
N=int(input())
a[0:N]=map(int,input().split())
a.sort()
for i in range(0,N):
    print(a[i],end=" ")
    
    
