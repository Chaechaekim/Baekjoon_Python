import sys
input=sys.stdin.readline
T=int(input().rstrip())
num=0
for i in range(T):
    PS=input().rstrip()
    for j in range(len(PS)):
        if PS[j]=='(':
            num+=1
        else:num-=1
        if num<0:
            break
    if num==0:
        print('YES')
    else:print('NO')
    num=0