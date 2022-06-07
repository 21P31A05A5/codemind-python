n=int(input())
m=int(input())
sum=0
i=1
while n>i:
    if n%i==0:
        sum=sum+i
    i=i+1    
if(m==sum):
    print('Amicable')
else:
    print('Not Amicable')