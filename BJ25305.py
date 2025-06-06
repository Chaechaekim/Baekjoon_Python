import sys
input=sys.stdin.readline
N,k=map(int,input().rstrip().split())
num_list=list(map(int,input().rstrip().split()))
num_list.sort(reverse=True)
print(num_list[k-1])