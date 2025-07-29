import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
if N-M<0:
    print((-1)*(N-M))
else:print(N-M)