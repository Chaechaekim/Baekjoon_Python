import sys
input=sys.stdin.readline
num=int(input().rstrip())
num_list=[]
ans_list=[]
ans=1
for i in range(num):
    w,h=map(int,input().rstrip().split())
    num_list.append((w,h))
for j in range(num):
    for k in range(num):
        if num_list[j][0]==num_list[k][0] and num_list[j][1]==num_list[k][1]:
            continue
        elif num_list[j][0]<num_list[k][0] and num_list[j][1]<num_list[k][1]:
            ans+=1
    ans_list.append(ans)
    ans=1
print(*ans_list)