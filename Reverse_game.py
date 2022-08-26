def rev(n):
    r=0
    while (n>0):
        re=n%10
        r=r*10+re
        n//=10
    return r
    
c=0
n=int(input())
lt=list(map(int,input().split()))
for i in lt:
    print(rev(i),end=' ')