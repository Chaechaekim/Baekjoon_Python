from collections import deque
N=int(input())
stack=deque()
ans=0
for i in range(N,0,-1):
    stack.append(i)
while stack:
    ans=stack.pop()
    if stack:
        stack.appendleft(stack.pop())


#print(stack)
print(ans)
