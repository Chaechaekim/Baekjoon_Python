import sys
input=sys.stdin.readline
num=int(input().rstrip())
num_list=list(map(int,input().rstrip().split()))
sum_num=0
for i in range(num):
    sum_num+=num_list[i]
    sum_num+=8
sum_num-=8
print(str(sum_num//24)+' '+str(sum_num%24))