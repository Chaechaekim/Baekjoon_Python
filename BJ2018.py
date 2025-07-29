N = int(input())
start_index=0
end_index=0
sum_num=0
count=0
i=1

while start_index<N//2:
    sum_num+=i
    if sum_num==N:
        count+=1
        start_index+=1
        end_index=start_index+1
        sum_num=0
        i=start_index+1
    elif sum_num>N:
        start_index+=1
        end_index=start_index+1
        sum_num=0
        i=start_index+1
    else:
        end_index+=1
        i+=1
    #print(start_index, end_index)

count+=1

print(count)

"""
N = int(input())
start_index=0
end_index=0
sum_num=0
count=0
i=1

while end_index<N:
    sum_num+=i
    if sum_num==N:
        count+=1
        start_index+=1
        end_index=start_index
        sum_num=0
        i=start_index+1
    elif sum_num>N:
        start_index+=1
        end_index=start_index
        sum_num=0
        i=start_index+1
    else:
        end_index+=1
        i+=1
count+=1

print(count)
"""

"""
N = int(input())
start_index=0
end_index=0
sum_num=0
count=0
num_list=[0]*N
i=0

for i in range(1,N+1):
    num_list[i-1]=i

while end_index!=N:
    sum_num+=num_list[end_index]
    if sum_num==N:
        count+=1
        start_index+=1
        end_index=start_index
        sum_num=0
    elif sum_num>N:
        start_index+=1
        end_index=start_index
        sum_num=0
    else:
        end_index+=1

#print(num_list)
print(count)
"""