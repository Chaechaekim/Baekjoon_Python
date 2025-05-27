import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
num_list=[]
for k in range(N):
    num_list.append(k+1)
for k in range(M):
    i,j=map(int,input().rstrip().split())
    temp=num_list[i-1]
    num_list[i-1]=num_list[j-1]
    num_list[j-1]=temp
print(*num_list)