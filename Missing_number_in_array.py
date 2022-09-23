n=int(input())
i=0
while(i<n):
    r=int(input())
    se=list(map(int,input().split()))
    for j in range(1,(r+1)):
        if j not in se:
            print(j)
    i+=1