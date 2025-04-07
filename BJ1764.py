import sys
input=sys.stdin.readline
N,M=input().split()
N=int(N)
M=int(M)
listen_list=[]
see_list=[]
for i in range(N):
    listen_list.append(input().rstrip())
for i in range(M):
    see_list.append(input().rstrip())
listen_set=set(listen_list)
see_set=set(see_list)
ans_set=listen_set & see_set
ans_set=sorted(ans_set)
print(len(ans_set))
for i in range(len(ans_set)):
    print(ans_set[i])

"""import sys
input=sys.stdin.readline
N,M=input().split()
N=int(N)
M=int(M)
listen_see_list=[]
ans_list=[]
for i in range(N+M):
    name=input().rstrip()
    if name in listen_see_list:
        ans_list.append(name)
    else:
        listen_see_list.append(name)
ans_list.sort()
print(len(ans_list))
for i in range(len(ans_list)):
    print(ans_list[i])
"""