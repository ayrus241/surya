num=int(input())
d=num
rev=0
while(num>0):
    rev=(rev*10)+(num%10)
    num=num//10
if d==rev:
    print("yes")
else:
    print("no")
