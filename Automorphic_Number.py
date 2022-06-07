n=input()
sq=int(n)*int(n)
b=str(sq)
a=len(n)
if(n==b[-a:]):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')