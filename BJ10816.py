import sys
input=sys.stdin.readline
N=int(input().rstrip())
dic={}
ans_list=[]
num_list=list(map(int,input().rstrip().split()))
for i in range(N):
    if num_list[i] in dic:
        dic[num_list[i]]+=1
    else:dic[num_list[i]]=1
M=int(input().rstrip())
num1_list=list(map(int,input().rstrip().split()))
for j in range(M):
    if num1_list[j] in dic:
        ans_list.append(dic[num1_list[j]])
    else:ans_list.append(0)
print(*ans_list)