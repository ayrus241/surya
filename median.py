import statistics
a=[]
N=int(input())
a[0:N]=map(int,input().split())
a.sort()
print(statistics.median(a))
    
