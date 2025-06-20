import sys
input=sys.stdin.readline
g='G'
dot_3='...'
dot_1='.'
dot_2='..'
i='I'
t='T'
s='S'
num=int(input().rstrip())
for k in range(3*num):
    if k<num:
        print(g*num,end='')
        print(dot_3*num)
    elif k<2*num:
        print(dot_1*num,end='')
        print(i*num,end='')
        print(dot_1*num,end='')
        print(t*num)
    else:
        print(dot_2*num,end='')
        print(s*num,end='')
        print(dot_1*num)