import sys
from collections import deque
input=sys.stdin.readline
N=int(input().rstrip())
deq=deque([])
for i in range(N):
    str_list=input().rstrip()
    if str_list[0]=='1':
        deq.append(int(str_list[2:]))
    elif str_list[0]=='2':
        deq.appendleft(int(str_list[2:]))
    elif str_list[0]=='3':
        if len(deq)==0:
            print(-1)
        else:print(deq.pop())
    elif str_list[0]=='4':
        if len(deq)==0:
            print(-1)
        else:print(deq.popleft())
    elif str_list[0]=='5':
        print(len(deq))
    elif str_list[0]=='6':
        if len(deq)==0:
            print(1)
        else:print(0)
    elif str_list[0]=='7':
        if len(deq)==0:
            print(-1)
        else:print(deq[-1])
    elif str_list[0]=='8':
        if len(deq)==0:
            print(-1)
        else:print(deq[0])