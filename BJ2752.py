import sys
input=sys.stdin.readline
num_list=list(map(int,input().rstrip().split()))
num_list=sorted(num_list)
print(*num_list)