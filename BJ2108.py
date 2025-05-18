import sys
input=sys.stdin.readline
N=int(input().rstrip())
sum=0
max_count=1
count=1
mode_num=0
j=0
num_dic={}
num_list=[]
for i in range(N):
    num=int(input().rstrip())
    sum+=num
    num_list.append(num)
mean=round(sum/N)
num_list.sort()
median=num_list[((1+N)//2)-1]
range_num=num_list[N-1]-num_list[0]
num_list.append(4001)
for i in range(0,N):
    if num_list[i]==num_list[i+1]:
        count+=1
    else:
        num_dic[num_list[i]]=count
        count=1
num_dic=sorted(num_dic.items(), key=lambda x:x[1], reverse=True)
print(mean)
print(median)
if N==1:
    print(num_list[0])
elif num_dic[0][1]!=num_dic[1][1]:
    print(num_dic[0][0])
else:
    print(num_dic[1][0])
print(range_num)