import sys
input=sys.stdin.readline
N=input().rstrip()
sum_num=0
count=1
while True:
    if count>int(N):
        print(0)
        break
    str_count=str(count)
    for i in range(len(str_count)):
        sum_num+=int(str_count[i])
    if int(str_count)+sum_num==int(N):
        print(str_count)
        break
    count+=1
    sum_num=0