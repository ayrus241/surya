N,A,D=map(int,input().split())
if (N>=0 and N<=100000)and(A>=0 and A<=100000)and(D>=0and D<=100000):
    sum=((N/2)*(2*A+(N-1)*D))
    print(int(sum))
