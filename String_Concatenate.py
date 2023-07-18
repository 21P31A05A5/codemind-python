n=input()
n1=input()
c=n+n1
l=[]
l1=[]
for ch in c:
    l.append(ord(ch))
l.sort()
for i in l:
    l1.append(chr(i))
c="".join(l1)
print(c)
