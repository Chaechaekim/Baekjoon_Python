import sys
N=int(sys.stdin.readline())
ox_list=[]
sum_num=[]
plus=0
for i in range(N):
    ox_list.append(sys.stdin.readline())
#print(ox_list[0])

for i in range(N):
    for j in range(len(ox_list[i])):
        if ox_list[i][j]=='O':
            plus+=1
            sum_num.append(plus)
        else:
            plus=0
    print(sum(sum_num))
    plus=0
    sum_num.clear()


