from collections import deque
import sys
input=sys.stdin.readline
queue=deque([])
N=int(input().rstrip())
for i in range(N):
    word=input().rstrip()
    if word=='pop':
        if len(queue)==0:
            print(-1)
        else:print(queue.popleft())
    elif word=='size':
        print(len(queue))
    elif word=='empty':
        if len(queue)==0:
            print(1)
        else:print(0)
    elif word=='front':
        if len(queue)==0:
            print(-1)
        else:print(queue[0])
    elif word=='back':
        if len(queue)==0:
            print(-1)
        else:print(queue[-1])
    else:
        w,x=word.split()
        queue.append(int(x))