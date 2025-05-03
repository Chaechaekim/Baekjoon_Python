import sys
input=sys.stdin.readline
num=int(input().rstrip())
alpha_list=input().rstrip()
sum_num=0
for i in range(num):
    sum_num+=(ord(alpha_list[i])-96)*(31**i)
print(sum_num%1234567891)