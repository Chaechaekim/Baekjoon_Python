import sys
input=sys.stdin.readline
N,K=input().split()
N=int(N)
K=int(K)
coin_list=[]
count=0
remain_coin=K
for i in range(N):
    coin=input()
    coin_list.append(int(coin))
while remain_coin>0:
    for i in range(N-1,-1,-1):
        if coin_list[i]<=remain_coin:
            count+=remain_coin//coin_list[i]
            remain_coin=remain_coin%coin_list[i]
            break
print(count)