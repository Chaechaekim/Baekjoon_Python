import sys
input=sys.stdin.readline
N,K=map(int,input().rstrip().split())
ans_list=[]
for i in range(1,N+1):
    if N%i==0:
        ans_list.append(i)
if len(ans_list)<K:
    print(0)
else:print(ans_list[K-1])