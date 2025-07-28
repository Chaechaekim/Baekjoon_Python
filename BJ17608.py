import sys
input=sys.stdin.readline
num=int(input().rstrip())
count=0
num_list=[]
for i in range(num):
    num_list.append(int(input().rstrip()))
num_list.reverse()
for j in range(num):
    if j==0:
        compare=num_list[j]
        count+=1
    elif num_list[j]>compare:
        compare=num_list[j]
        count+=1
print(count)