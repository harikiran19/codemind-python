def prob(n):
    st=str(n)
    r=st[::-1]
    if st==r:
        return True
c=0
n=int(input())
lt=list(map(int,input().split()))
for i in lt:
    if prob(i):
        c+=1
print(c)