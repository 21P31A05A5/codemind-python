n=int(input())
for i in range(n):
    a=input()
    c=0
    for ch in a:
        if(ch.isdigit()):
            c=1
            print("Yes")
            break;
    if(c==0):
        print("No")