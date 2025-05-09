from collections import deque
import sys
input=sys.stdin.readline
stack=deque([])
N=int(input().rstrip())
for i in range(N):
    word=input().rstrip()
    if word=='top':
        if len(stack)==0:
            print(-1)
        else:print(stack[-1])
    elif word=='size':
        print(len(stack))
    elif word=='empty':
        if len(stack)==0:
            print(1)
        else: print(0)
    elif word=='pop':
        if len(stack)==0:
            print(-1)
        else:print(stack.pop())
    else:
        word,num=word.split()
        if word=='push':
            stack.append(int(num))


        
