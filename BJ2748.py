import sys
input=sys.stdin.readline
num=int(input().rstrip())
sum_num_1=0
sum_num_2=1
sum_num=0
for i in range(1,num):
    sum_num=sum_num_1+sum_num_2
    sum_num_1=sum_num_2
    sum_num_2=sum_num
if num==0:
    print(0)
elif num==1:
    print(1)
else:
    print(sum_num)