import sys
input=sys.stdin.readline
X=int(input().rstrip())
N=int(input().rstrip())
sum_num=0
for i in range(N):
    cost,count=map(int,input().rstrip().split())
    sum_num+=(cost*count)
if X==sum_num:
    print('Yes')
else:print('No')