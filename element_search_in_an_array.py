n=int(input())
arr=list(map(int,input().split()))
se=int(input())
for i in arr:
    if i==se:
        print(True)
        break
else:
    print(False)