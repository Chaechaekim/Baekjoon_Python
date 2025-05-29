import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
num_list=[]
ans_list=[]
count=1
max_num=N
q=deque([])
ans_list=deque([])
for i in range(N):
    num_list.append(i+1)
num1_list=num_list
while True:
    if len(num1_list)==0:
        break
    for j in range(max_num):
        if count==M:
            q.append(j)
            ans_list.append(num1_list[j])
            count=1
        else:
            count+=1
    for k in range(len(q)):
        num1_list.remove(num1_list[q.pop()])
    max_num=len(num1_list) 
for i in range(len(ans_list)+2):
    if i==0:
        print('<',end='')
    elif i==len(ans_list)+1:
        print('>')
    elif i==len(ans_list):
        print(ans_list[i-1],end='')
    else:
        print(ans_list[i-1],end=', ')