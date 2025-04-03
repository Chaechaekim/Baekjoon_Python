import sys
N,K=map(int,sys.stdin.readline().split())
up_num=1
down_num=1
for i in range(N,N-K,-1):
    if N-K==0:
        break
    up_num=up_num*i
for j in range(K,0,-1):
    if N-K==0:
        break
    down_num=down_num*j

print(up_num//down_num)