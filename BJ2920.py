import sys
num_list=list(map(int,sys.stdin.readline().split()))
ascending_sort=sorted(num_list)
descending_sort=sorted(num_list,reverse=True)
#print(num_list)
#print(ascending_sort)
if num_list==ascending_sort:
    print('ascending')
elif num_list==descending_sort:
    print('descending')
else:print('mixed')
