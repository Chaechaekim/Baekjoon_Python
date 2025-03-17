num=list(input())
max_num=0
max_index=0
sort_num=''
int_num=0
temp=''
count=0
same_num=0
for i in range(len(num)):
    for j in range(i,len(num)):
        int_num=int(num[j])
        if max_num<int_num:
            max_index=j
            max_num=int_num
            #print(max_num)
        elif max_num==int_num:
            count+=1
            same_num=int_num
    if count==(len(num)-i) and same_num==max_num:
        break
    temp=num[i]
    num[i]=num[max_index]
    num[max_index]=temp
    max_num=0
    count=0
    #print(num)
         
print(*num,sep='')
"""
num=list(input())
max_num=0
max_index=0
sort_num=''
int_num=0
temp=''
count=0
for i in range(len(num)):
    for j in range(i,len(num)):
        int_num=int(num[j])
        if max_num<int_num:
            max_index=j
            max_num=int_num
            #print(max_num)
        elif max_num==int_num:
            count+=1
    if count==(len(num)-i+1):
        break
    temp=num[i]
    num[i]=num[max_index]
    num[max_index]=temp
    max_num=0
    #print(num)
         
print(*num,sep='')
"""