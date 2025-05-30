import sys
from collections import deque
input=sys.stdin.readline
stack=deque([])
N=int(input().rstrip())
for i in range(N):
    str_num=input().rstrip()
    if str_num[0]=='1':
        x=int(str_num[2:])
        stack.append(x)
    elif str_num[0]=='2':
        if len(stack)==0:
            print(-1)
        else:print(stack.pop())
    elif str_num[0]=='3':
        print(len(stack))
    elif str_num[0]=='4':
        if len(stack)==0:
            print(1)
        else:print(0)
    elif str_num[0]=='5':
        if len(stack)==0:
            print(-1)
        else:print(stack[-1])