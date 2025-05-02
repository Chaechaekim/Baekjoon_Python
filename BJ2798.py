import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
num_list=list(map(int,input().rstrip().split()))
start_index=0
middle_index=1
end_index=2
sum_max=0
while start_index<N-2:
    if start_index>=N-2 and middle_index>=N-1 and end_index>=N:
        break
    sum_num=num_list[start_index]+num_list[middle_index]+num_list[end_index]
    if sum_num>sum_max and sum_num<=M:
        sum_max=sum_num
    if end_index < N - 1:
        end_index += 1
    elif middle_index < N - 2:
        middle_index += 1
        end_index = middle_index + 1
    else:
        start_index += 1
        middle_index = start_index + 1
        end_index = middle_index + 1
    """   
    if sum_max==M:
        break
    if end_index==N-1:
        middle_index+=1
        end_index=middle_index+1
    if middle_index==N-2:
        start_index+=1
        middle_index=start_index+1
        end_index=middle_index+1
    end_index+=1
    """
print(sum_max)