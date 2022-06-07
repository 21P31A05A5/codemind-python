n=input()
dec=0
exp=len(n)
for i in n:
    dec=int(i)*8**int(exp-1)+dec
    exp=exp-1
m=dec
bin=''
while m>0:
    r=m%2
    bin=str(r)+bin
    m=m//2
print(bin)