N=int(input())
num_list=list(map(int,input().split()))
sort_list=sorted(num_list)
start_index=0
mid=N//2
end_index=N-1
index=0
count=0

while index<N:
    if start_index==index :
        start_index+=1
    elif end_index==index:
        end_index-=1

    if start_index<end_index:      
        if sort_list[start_index]+sort_list[end_index]>sort_list[index]:
            end_index-=1
        elif sort_list[start_index]+sort_list[end_index]==sort_list[index]:
            count+=1
            #print(sort_list[index])
            index+=1
            start_index=0
            end_index=N-1
        else:
            start_index+=1
    else:
        index+=1
        start_index=0
        end_index=N-1

print(count)

"""
N=int(input())
num_list=list(map(int,input().split()))
sort_list=sorted(num_list)
start_index=0
i=N-1
end_index=i-1
count=0

while i>1:
    if start_index>=end_index:
        i-=1
        start_index=0
        end_index=i-1
    else:
        if sort_list[i]==(sort_list[start_index]+sort_list[end_index]):
            count+=1
            i-=1
            start_index=0
            end_index=i-1
        elif sort_list[i]>(sort_list[start_index]+sort_list[end_index]):
            start_index+=1
        else:
             end_index-=1
    

print(count)
"""
"""
N=int(input())
num_list=list(map(int,input().split()))
sort_list=sorted(num_list)
start_index=0
i=2
end_index=i-1
count=0

while i<N:
    if start_index>=end_index:
        i+=1
        start_index=0
        end_index=i-1
    if sort_list[i]==(sort_list[start_index]+sort_list[end_index]):
        count+=1
        i+=1
        start_index=0
        end_index=i-1
    elif sort_list[i]>(sort_list[start_index]+sort_list[end_index]):
        start_index+=1
    else:
        end_index-=1

print(count)
"""