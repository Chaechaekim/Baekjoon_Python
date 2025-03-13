from collections import deque
n=int(input())
result_list=[0]*n
compare_list=[0]*n
ans_list=[]
index_r=0
index_c=0
no=0
stack=deque()
for i in range(n):
    result_list[i]=int(input())
    compare_list[i]=i+1

while index_r<n:
    if index_c<n:
        if result_list[index_r]>compare_list[index_c]:
            ans_list.append('+')
            stack.append(compare_list[index_c])
            index_c+=1
        elif result_list[index_r]==compare_list[index_c]:
            ans_list.append('+')
            ans_list.append('-')
            stack.append(compare_list[index_c])
            stack.pop()
            index_c+=1
            index_r+=1
        else:
            ans_list.append('-')
            if stack.pop()!=result_list[index_r]:
                no+=1
                break
            index_r+=1
    else:
        ans_list.append('-')
        if stack.pop()!=result_list[index_r]:
            no+=1
            break
        index_r+=1

if no==0:
    for i in range(2*n):
        print(ans_list[i])
else:
    print('NO')     






"""
n=int(input())
result_list=[0]*n
compare_list=[0]*n
ans_list=[]
index_r=0
index_c=0
no=0
for i in range(n):
    result_list[i]=int(input())
    compare_list[i]=i+1

while index_r<n:
    if index_c<n:
        if result_list[index_r]>compare_list[index_c]:
            ans_list.append('+')
            index_c+=1
        elif result_list[index_r]==compare_list[index_c]:
            ans_list.append('+')
            ans_list.append('-')
            index_r+=1
            index_c+=1
            i+=1
        else:
            ans_list.append('-')
            index_r+=1
    else:
        if result_list[index_r] >result_list[index_r-1]:
            no+=1
            break
        ans_list.append('-')
        index_r+=1

if no==0:
    for i in range(2*n):
        print(ans_list[i])
else:
    print('NO')
"""