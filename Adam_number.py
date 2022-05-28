def rev(n):
    r=0
    while n!=0:
        a=n%10
        r=(r*10)+a
        n//=10
    return r 
n=int(input())
m=rev(n)
if(n**2==rev(m**2)):
    print('True')
else:
    print('False')

