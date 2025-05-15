import sys
input=sys.stdin.readline
N=int(input())
type_list=[]
for i in range(N//4):
    type_list.append('long')
type_list.append('int')
print(*type_list)