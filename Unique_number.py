n=int(input())
on=0
tw=0
th=0
fo=0
fi=0
si=0
se=0
ei=0
ni=0
while n>0:
    r=n%10
    if(r==1):
        on+=1
    elif(r==2):
        tw+=1
    elif(r==3):
        th+=1
    elif(r==4):
        fo+=1
    elif(r==5):
        fi+=1
    elif(r==6):
        si+=1
    elif(r==7):
        se+=1
    elif(r==8):
        ei+=1
    elif(r==9):
        ni+=1
    n//=10
if on<2 and tw<2 and th<2 and fo<2 and fi<2 and si<2 and se<2 and ei<2 and ni<2:
    print('Unique Number')
else:
    print('Not Unique Number')