num=int(input())
sum=0
temp=num
while num>0:
    digit=num%10
    sum=sum+(digit**3)
    num=num//10
if temp==sum:
    print("yes")
else:
    print("no")
