import sys
input=sys.stdin.readline
swip=input().rstrip()
ball_list=[1,0,0,2]
ans=''
for i in range(len(swip)):
    if swip[i]=='A':
        temp=ball_list[0]
        ball_list[0]=ball_list[1]
        ball_list[1]=temp
    elif swip[i]=='B':
        temp=ball_list[0]
        ball_list[0]=ball_list[2]
        ball_list[2]=temp
    elif swip[i]=='C':
        temp=ball_list[0]
        ball_list[0]=ball_list[3]
        ball_list[3]=temp
    elif swip[i]=='D':
        temp=ball_list[1]
        ball_list[1]=ball_list[2]
        ball_list[2]=temp
    elif swip[i]=='E':
        temp=ball_list[1]
        ball_list[1]=ball_list[3]
        ball_list[3]=temp
    elif swip[i]=='F':
        temp=ball_list[2]
        ball_list[2]=ball_list[3]
        ball_list[3]=temp
for i in range(4):
    if ball_list[i]==1:
        num1=i+1
    elif ball_list[i]==2:
        num2=i+1
print(num1)
print(num2)