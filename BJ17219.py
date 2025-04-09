import sys
input=sys.stdin.readline
N,M=input().rstrip().split()
N=int(N)
M=int(M)
pw_dic={}
for i in range(N):
    site,pw=input().rstrip().split()
    pw_dic[site]=pw
for i in range(M):
    find_pw=input().rstrip()
    print(pw_dic[find_pw])