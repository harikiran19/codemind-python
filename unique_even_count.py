n=int(input())
a=list(map(int,input().split()))
a=set(a)
c=0
for i in set(a):
    if i%2==0:
        c+=1
print(c)