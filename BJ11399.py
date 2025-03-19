import sys
N=int(sys.stdin.readline())
p_list=list(map(int,sys.stdin.readline().split()))
sort_list=[]
start=0
sort_list.append(p_list[0])
end=len(sort_list)-1
mid=(len(sort_list)-1)//2
index=0
sum_num=0

for i in range(1,N):
    while start<=end:
        if sort_list[mid]==p_list[i]:
            #p_list.insert(mid,p_list[i])
            index=mid+1
            #print(sort_list[mid])
            break
        elif sort_list[mid]>p_list[i]:
            end=mid-1
            mid=end//2
            index=start
            #print(sort_list[mid])
        elif sort_list[mid]<p_list[i]: 
            start=mid+1
            mid=(end+start)//2
            index=end+1
            #print(index,p_list[i])

    sort_list.insert(index,p_list[i])
    #print(sort_list)
    start=0
    end=len(sort_list)-1
    mid=end//2
    index=0

sum_num=sort_list[0]
for i in range(1,N):
    sum_num+=sum(sort_list[0:i+1])
    #print(sum_num)

#print(sort_list)
print(sum_num)
        
