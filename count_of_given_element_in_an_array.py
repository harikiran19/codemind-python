n=int(input())
arr=list(map(int,input().split()))
se=int(input())
od=0
for i in arr:
    if i==se:
        od+=1
print(od)