n=int(input())
arr=list(map(int,input().split()))
sum,count=0,0
for i in range (0,n):
    sum+=arr[i]
av=sum//n
for i in range(0,n):
    if arr[i]<=av:
        count+=1
print(count)