def dn(n):
    c=0
    while n>0:
        a=n%10
        c+=1
        n//=10
    return c
n=int(input())
ct=dn(n)
d=0
temp=n
while temp>0:
    a=temp%10
    d=a**ct+d
    ct-=1
    temp//=10
if d==n :
    print('True')
else:
    print('False')