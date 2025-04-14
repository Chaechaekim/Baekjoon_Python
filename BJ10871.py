import sys
input=sys.stdin.readline
N,X=input().rstrip().split()
N=int(N)
X=int(X)
num_list=input().rstrip().split()
ans_list=[]
for i in range(N):
    if int(num_list[i])<X:
        ans_list.append(int(num_list[i]))
print(*ans_list)