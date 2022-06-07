n=int(input())
l=[]
while n>0:
    rem=n%10
    l.append(rem)
    n=n//10
l.sort()
print(l[-1])