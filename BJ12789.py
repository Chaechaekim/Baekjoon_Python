import sys
from collections import deque
input=sys.stdin.readline
stack=deque([])
N=int(input().rstrip())
q=list(map(int,input().rstrip().split()))
q=deque(q)
q1=q
count=1
check=1
while True:
    for i in range(N):
        if q1[i]==count:
            q.popleft()
            count+=1
        else:
            stack.append(q.popleft())
    if len(q)==0:
        for j in range(len(stack)):
            if stack.pop()!=count:
                print("Sad")
                check=0
                break
        if check==0:
            break
        elif len(stack)==0:
            print("Nice")
            break
