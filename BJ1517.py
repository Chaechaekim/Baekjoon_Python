import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
swap_num = 0

def merge_sort(arr, low, high):
    global swap_num
    if high - low <= 0:
        return
    
    mid = (high + low) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    num = 0
    merged = []
    low_index = low
    high_index = mid + 1

    while low_index <= mid and high_index <= high:
        if arr[low_index] <= arr[high_index]:
            merged.append(arr[low_index])
            low_index += 1
        else:
            merged.append(arr[high_index])
            high_index += 1
            num += (mid - low_index + 1)

    merged += arr[high_index:high + 1]
    merged += arr[low_index:mid + 1]

    swap_num += num
    arr[low:high + 1] = merged  # 정렬된 부분을 원래 배열에 반영

merge_sort(num_list, 0, N - 1)
print(swap_num)
"""
import sys
N=int(sys.stdin.readline())
num_list=list(map(int,sys.stdin.readline().split()))
swap_num=0
def merge_sort(arr):
    if len(arr)<2:
        return arr
    mid=len(arr)//2
    low_arr=merge_sort(arr[:mid])
    high_arr=merge_sort(arr[mid:])
    num=0
    merged=[]
    low_index=0
    high_index=0
    global swap_num

    while low_index<len(low_arr) and high_index<len(high_arr):
        if low_arr[low_index]<=high_arr[high_index]:
            merged.append(low_arr[low_index])
            low_index+=1
        elif low_arr[low_index]>high_arr[high_index]:
            merged.append(high_arr[high_index])
            high_index+=1
            num+=len(low_arr[low_index:])
    merged+=high_arr[high_index:]
    num+=len(high_arr)-high_index
    if low_index==len(low_arr):
        num-=1
    merged+=low_arr[low_index:]
            #num+=1
    #print(num)
    #print(merged)
    swap_num+=num
    return merged

merge_sort(num_list)
sys.stdout.readline(swap_num)
"""
"""
import sys
N=int(sys.stdin.readline())
num_list=list(map(int,sys.stdin.readline().split()))
swap_num=0
def merge_sort(arr):
    if len(arr)<2:
        return arr
    mid=len(arr)//2
    low_arr=merge_sort(arr[:mid])
    high_arr=merge_sort(arr[mid:])
    num=0
    merged=[]
    low_index=0
    high_index=0
    global swap_num

    while low_index<len(low_arr) or high_index<len(high_arr):
        if low_index>=len(low_arr):
            merged.append(high_arr[high_index])
            high_index+=1
        elif high_index>=len(high_arr):
            merged.append(low_arr[low_index])
            low_index+=1
            #num+=len(high_arr)
            num+=1
            if low_index==len(low_arr):
                num-=1
        elif low_arr[low_index]<=high_arr[high_index]:
            merged.append(low_arr[low_index])
            low_index+=1
        elif low_arr[low_index]>high_arr[high_index]:
            merged.append(high_arr[high_index])
            high_index+=1
            num+=len(low_arr[low_index:])
            #num+=1
    #print(num)
    #print(merged)
    swap_num+=num
    return merged

merge_sort(num_list)
print(swap_num)
"""
