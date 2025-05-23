import sys
input=sys.stdin.readline
N=int(input().rstrip())
n_list=list(map(int,input().rstrip().split()))
count=0
num=int(input().rstrip())
for i in range(N):
    if n_list[i]==num:
        count+=1
print(count)