n=int(input())
nn=n*n
s=0
temp=nn
while(temp>0):
    r=temp%10
    s+=r
    temp//=10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")