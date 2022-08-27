st=input()
st=st.split(' ')
st=st[::-1]
for i in range(len(st)):
    if i%2==0:
        print(st[i][::-1],end=' ')
    else:
        print(st[i][::-1],end=' ')