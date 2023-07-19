a=int(input())
ec=0
oc=0
while a>0:
    r=a%10
    if(a%2==0):
        ec=ec+1
    else:
        oc=oc+1
    a=a//10
if ec!=0 and oc==0:
    print("Even")
elif oc!=0 and ec==0:
    print("Odd")
elif oc>0 and ec>0:
    print("Mixed")