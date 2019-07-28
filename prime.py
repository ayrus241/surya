N=int(input())
for i in range(2,N):
    if (N>=1000)&(N%i==0):
        print("no")
        break
else:
    print("yes")
        
