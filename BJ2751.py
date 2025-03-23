import sys
N=int(sys.stdin.readline())
num_list=[]
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
ans_list=[]
def merge_sort(arr):
    if len(arr)<2:
        return arr
    mid=len(arr)//2
    low_arr=merge_sort(arr[:mid])
    high_arr=merge_sort(arr[mid:])

    merged=[]
    low_index=0
    high_index=0

    while low_index<len(low_arr) or high_index<len(high_arr):
        if low_index>=len(low_arr) and high_index<len(high_arr):
            merged.append(high_arr[high_index])
            high_index+=1
            #print(1)
        elif high_index>=len(high_arr) and low_index<len(low_arr):
            merged.append(low_arr[low_index])
            low_index+=1
            #print(2)
        elif low_arr[low_index]<=high_arr[high_index]:
            merged.append(low_arr[low_index])
            low_index+=1
            #print(3)
        elif low_arr[low_index]>high_arr[high_index]:
            merged.append(high_arr[high_index])
            high_index+=1
            #print(4)
    #print(low_index,high_index)
    #low_index=0
    #high_index=0
   
    #print(high_arr)
    #print(low_arr)
    #print(merged)
    return merged

ans_list=merge_sort(num_list)
for i in range(len(ans_list)):
    print(ans_list[i])