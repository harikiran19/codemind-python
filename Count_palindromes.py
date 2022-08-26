def rev(n):
    r=0
    temp=n
    while (n>0):
        re=n%10
        r=r*10+re
        n=n//10
    if (r==temp):
        return True
c=0
n=int(input())
lt=list(map(int,input().split()))
for i in lt:
    if rev(i):
        c+=1
print(c)