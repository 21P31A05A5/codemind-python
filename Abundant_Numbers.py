a=int(input())
rev=0
i=1
while i<a:
    r=a%i
    if(r==0):
        rev=rev+i
    i=i+1
if rev>a:
    print("True")
else:
    print("False")