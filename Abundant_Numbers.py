def fact(n):
    s=0
    for i in range (1,int (n/2)+1):
        if n%i==0:
            s+=i
    return s
n=int(input())
if(fact(n)>=n):
    print('True')
else:
    print('False')