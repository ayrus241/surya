a=input()
count1=0
count2=0
for i in a:
    if(i.isdigit())or(i.isalpha()):
        count1=count1+1
    else:
        count2=count2+1
print(count2)
