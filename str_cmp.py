a,b=map(str,input().split())
if len(a)>len(b):
    print(a)
elif len(a)==len(b):
    c=a or b
    print(c)
else:
    print(b)
