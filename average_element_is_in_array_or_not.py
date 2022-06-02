n=int(input())
arr=list(map(int,input().split()))
av=0
a=len(arr)
for i in range (0,a):
    av+=i
av=av/n
for i in arr:
    if i==av:
        print('True')
        break
else:
    print('False')