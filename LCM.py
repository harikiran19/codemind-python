def lcm(x,y):
    if(x<y):
        g=y
    elif(x>y):
        g=x
    while True:
        if(g%x==0 and g%y==0):
            return g   
            break
        g+=1
m,n=map(int,input().split())
print(lcm(m,n))
