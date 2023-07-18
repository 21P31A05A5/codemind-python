a=input()
b=input()
c=0
for ch in a:
    if ch in b:
        e=a.count(ch)
        c=c+1
if c>1:
    print(e)
else:
    print('-1')