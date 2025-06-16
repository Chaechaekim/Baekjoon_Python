import sys
input=sys.stdin.readline
n=int(input().rstrip())
for i in range(n):
    y,m,d=map(int,input().rstrip().split())
    if 2007-y>18:
        print('Yes')
    elif 2007-y==18:
        if m<2:
            print('Yes')
        elif m==2:
            if d<=27:
                print('Yes')
            else:print('No')
        else:print('No')
    else:print('No')