n=input()
x=0
for i in n:
    x=n.count(i)+x
if(x==len(n)):
    print('Unique Number')
else:
    print('Not Unique Number')