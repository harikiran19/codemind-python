def rev(n):
    r=0
    while n>0:
        a=n%10
        r=(r*10)+a
        n//=10
    return r
n=int(input())
if rev(n)==n:
    print('True')
else:
    print('False')