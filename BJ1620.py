import sys
input= sys.stdin.readline
pocketmon_dic={}
rev_pocketmon_dic={}
N,M=input().rstrip().split()
N=int(N)
M=int(M)
for i in range(1,N+1):
    pocketmon=input().rstrip()
    pocketmon_dic[i]=pocketmon
    rev_pocketmon_dic[pocketmon]=i
for j in range(M):
    test=input().rstrip()
    if ord(test[0])>=48 and ord(test[0])<=57:
        test=int(test)
        print(pocketmon_dic[test])
    else:print(int(rev_pocketmon_dic[test]))