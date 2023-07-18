a=input()
sum=0
for ch in a:
    if ch.isdigit():
        sum=sum+int(ch)
print(sum)