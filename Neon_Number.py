n=int(input())
c=n*n
s=0
while(c>0):
    r=c%10
    s=s+r
    c=c//10
if(n==s):
    print("Neon Number")
else:
    print("Not Neon Number")