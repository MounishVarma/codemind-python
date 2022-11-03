n=int(input())
n=str(n)
c=0
s=1
for i in n:
    c+=int(i)
    s*=int(i)
if c==s:
    print('Spy Number')
else:
    print('Not Spy Number')