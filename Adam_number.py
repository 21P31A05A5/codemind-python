import math
a=int(input())
rev=0
rev1=0
s=a**2
while a>0:
    r=a%10
    rev=rev*10+r
    a=a//10
s1=rev**2
while s1>0:
    r1=s1%10
    rev1=rev1*10+r1
    s1=s1//10
if(s==rev1):
    print("True")
else:
    print("False")