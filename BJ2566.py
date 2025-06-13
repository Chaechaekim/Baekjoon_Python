import sys
input=sys.stdin.readline
num_list=[list(map(int,input().rstrip().split())) for _ in range(9)]
max_num=(-1,0,0)
for i in range(9):
    for j in range(9):
        if max_num[0]<num_list[i][j]:
            max_num=(num_list[i][j],i+1,j+1)
print(max_num[0])
print(max_num[1],end=' ')
print(max_num[2])