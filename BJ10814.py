import sys
N=int(sys.stdin.readline())
member_list=[]
for i in range(N):
    num,name=sys.stdin.readline().strip('\n').split()
    num=int(num)
    member_list.append((num,i,name))
member_list.sort()
for i in range(N):
    print(member_list[i][0],member_list[i][2])