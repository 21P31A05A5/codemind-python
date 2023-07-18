a=input()
c=0
for ch in a:
    if ch.isdigit():
        c=c+1
if c>1:
    print("Contains",c,"digit")        
else:
    print("Doesn't contain digit")