n=int(input())
a=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if(a==rev):
    print("True")
else:
    print("False")