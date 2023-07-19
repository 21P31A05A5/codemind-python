import math;
n=int(input())
for i in range(n):
    a=int(input())
    s=math.sqrt(a)
    d=int(s)
    if(d*d==a):
        print("True")
    else:
        print("False")