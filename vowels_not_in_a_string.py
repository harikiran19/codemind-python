s=input()
s=set(s)
t=[]
c=0
v=['a','e','i','o','u']
for i in s:
    if i in v:
        c+=1
        t.append(i)
if len(t)==len(v):
    print(0)
else:
    for i in v:
        if i not in t:
            print(i,end=' ')