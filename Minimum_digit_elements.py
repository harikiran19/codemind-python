def ct(n):
    if (n>9):
        c=0
        while(n>0):
            n//=10
            c+=1
        return c
    return 1
n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(ct(a[i]))
x=min(l)
print(l.count(x))