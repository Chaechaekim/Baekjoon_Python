import sys
from collections import deque
input=sys.stdin.readline
K=int(input().rstrip())
sum_num=0
stack=deque([])
for i in range(K):
    num=int(input().rstrip()) 
    if num==0:
        stack.pop()
    else:
        stack.append(num)
for i in range(len(stack)):
    sum_num+=stack[i]
print(sum_num)