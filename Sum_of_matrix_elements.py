m=int(input())
n=int(input())
l=[]
s=0
for i in range(m):
    l=list(map(int,input().split()))
    s+=sum(l)
print(s)