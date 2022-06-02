n=int(input())
arr=list(map(int,input().split()))
od=0
for i in range(n):
    if arr[i]%2!=0:
        od=i
print(od)