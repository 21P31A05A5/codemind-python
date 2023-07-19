n=int(input())
for i in range(n):
    a=int(input())
    s=a
    rev=0
    while(a>0):
        r=a%10
        rev=rev*10+r
        a=a//10
    if(s==rev):
        print("True")
    else:
        print("False")