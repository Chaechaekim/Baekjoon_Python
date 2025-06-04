import sys
input=sys.stdin.readline
num_list=[]
sum_num=0
for i in range(5):
    num=int(input().rstrip())
    num_list.append(num)
    sum_num+=num
num_list.sort()
print(sum_num//5)
print(num_list[2])