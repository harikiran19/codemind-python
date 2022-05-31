def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
m=int(input())
n=int(input())
for i in range(m,n+1):
    if prime(i) and i>1:
        print(i)