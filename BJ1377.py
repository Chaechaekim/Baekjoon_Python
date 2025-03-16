import sys
N=int(sys.stdin.readline())
num_list=[]
sort_list=[]
num_index_list=[]
sort_index_list=[]
sub_index_list=[]
num_sort=[]
num=0
n=0
num_index_list


for i in range(N):
    #num_list.append(list(map(int,sys.stdin.readline().split())))
    n=int(input())
    num_list.append(n)
    sort_index_list.append(i)
    num_index_list.append((n,i))


sort_list=sorted(num_list)
num_sort=sorted(num_index_list)


for i in range(N):
    #print(num_sort[i][1])
    if num<num_sort[i][1]-sort_index_list[i]:
        num=(num_sort[i][1]-sort_index_list[i])
        
 
print(num+1)
#print(num_sort)

#print(num_index_list)


"""
from collections import deque
N = int(input())
num_list=[]
count=0
stack=deque()
for i in range(N):
    num_list.append(int(input()))

for i in range(N-1):
    stack.append(num_list[i])
    if stack and num_list[i]>num_list[i+1]:
        stack.pop()
        count+=1

print(count+1)
"""






"""
N=int(input())
num_list=[]
changed=False
num=N-1
temp=0

for i in range(N):
    num_list.append(int(input()))

for i in range(N-1):
    changed=False
    for j in range(num):
        if num_list[j]>num_list[j+1]:
            temp=num_list[j]
            num_list[j]=num_list[j+1]
            num_list[j+1]=temp
            changed=True
    if changed==False:
        print(i+1)
        break
    num-=1
"""


