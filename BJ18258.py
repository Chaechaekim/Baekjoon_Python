import sys
from collections import deque
input=sys.stdin.readline
N=int(input().rstrip())
q=deque([])
for i in range(N):
    str_list=input().rstrip()
    if str_list[:3]=='pop':
        if len(q)==0:
            print(-1)
        else:print(q.popleft())
    elif str_list[:4]=='push':
        q.append(int(str_list[4:]))
    elif str_list[:4]=='size':
        print(len(q))
    elif str_list[:4]=='back':
        if len(q)==0:
            print(-1)
        else:print(q[-1])
    elif str_list[:5]=='front':
        if len(q)==0:
            print(-1)
        else: print(q[0])
    elif str_list[:5]=='empty':
        if len(q)==0:
            print(1)
        else:print(0)