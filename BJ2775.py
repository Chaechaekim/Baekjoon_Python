import sys
T=int(sys.stdin.readline())
i=0
num_zero=[[]]
sum_num=0
for _ in range(T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())

    num_zero=[[0]*N for _ in range(K+1)]
    for i in range(N):
        num_zero[0][i]=i+1
    for j in range(1,K+1):
        for k in range(N):
            sum_num+=num_zero[j-1][k]
            num_zero[j][k]=sum_num
        sum_num=0
    print(num_zero[K][N-1])