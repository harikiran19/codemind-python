st=input()
st=st.split(' ')
n=len(st)
for i in range(n):
    if i%2==0:
        print(st[i][::-1],end=' ')
    else:
        print(st[i],end=' ')