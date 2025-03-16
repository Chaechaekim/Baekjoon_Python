N=int(input())
num_list=[]
num=N-1
temp=0
for i in range(N):
    num_list.append(int(input()))

for j in range(N-1):
    for k in range(num):
        if  num_list[k]>num_list[k+1]:
            temp = num_list[k]
            num_list[k]=num_list[k+1]
            num_list[k+1]=temp
    num-=1

for i in range(N):
    print(num_list[i])
               