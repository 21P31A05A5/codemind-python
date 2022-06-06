n1=int(input())
rev=0
n=abs(n1)
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if(n1>0):
    print(rev)
else:
    print(-rev)
