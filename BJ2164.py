from collections import deque
N=int(input())
q=deque()
ans=0
for i in range(N,0,-1):
    q.append(i)
while q:
    ans=q.pop()
    if q:
        q.appendleft(q.pop())


print(ans)