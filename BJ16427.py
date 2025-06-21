import sys
input=sys.stdin.readline
n,s=map(int,input().rstrip().split())
s_list=list(map(int,input().rstrip().split()))
max_num=0
max_num=max(s_list)
ans=(max_num*s)
if ans%1000==0:
    print(ans//1000)
else:
    ans=ans//1000
    print(ans+1)