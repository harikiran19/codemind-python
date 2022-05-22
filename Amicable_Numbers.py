m=int(input())
n=int(input())
M=0
N=0
for i in range(1,(n//2)+1):
    if(n%i==0):
        M+=i
for j in range(1,(m//2)+1):
    if(m%j==0):
        N+=j
if (M==m and N==n):
    print('Amicable')
else:
    print('Not Amicable')