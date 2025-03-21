import sys
N,K=map(int,sys.stdin.readline().split())
a_list=list(map(int,sys.stdin.readline().split()))

a_list.sort()

print(a_list[K-1])
"""
import sys
N,K=map(int,sys.stdin.readline().split())
a_list=list(map(int,sys.stdin.readline().split()))
#pivot=a_list[N//2]
#start_index=0
#end_index=N-1
sort_list=[]



def partition(sub_list):
    if len(sub_list)<=1:
        return sub_list
    
    pivot=sub_list[len(sub_list)//2]
    left=[x for x in sub_list if x<pivot]
    middle=[x for x in sub_list if x==pivot]
    right=[x for x in sub_list if x>pivot]

    return partition(left)+middle+partition(right)
sort_list=partition(a_list)
#print(sort_list)
print(sort_list[K-1])
"""
"""
import sys
N,K=map(int,sys.stdin.readline().split())
a_list=list(map(int,sys.stdin.readline().split()))
#pivot=a_list[N//2]
#start_index=0
#end_index=N-1
num1=0
num2=0
p=0
p1=0
mid=(N-1)//2
r_list=[]


def partition(start_index,end_index,sub_list):
    pivot=(start_index+end_index)//2
    p=pivot
    #pivot=round((start_index+end_index)/2)
    #print(pivot)
    sub_list.append(sub_list[pivot])
    sub_list.remove(sub_list[pivot])
    pivot=-1
    end_index-=1
    pivot_index=0
    p1=0
    ans_list=[]
    

    
    
    #print(sub_list)
    while start_index<end_index:
        if sub_list[start_index]<sub_list[pivot]:
            start_index+=1
        elif sub_list[end_index]>sub_list[pivot]:
            end_index-=1
        elif sub_list[end_index]<sub_list[pivot] and sub_list[start_index]>sub_list[pivot]:
            sub_list[end_index],sub_list[start_index]=sub_list[start_index],sub_list[end_index]
            start_index+=1
            end_index+=1
    
    sub_list.insert(start_index,sub_list[pivot])
    sub_list.pop()
    #print(sub_list)
    pivot_index=start_index
    start_index=0
    end_index=len(sub_list)
    if len(sub_list[start_index:pivot_index])>0:
        partition(start_index,pivot_index-1,sub_list[start_index:pivot_index])
    if len(sub_list[pivot_index+1:end_index+1])>0:
        partition(0,len(sub_list[pivot_index+1:end_index])-1,sub_list[pivot_index+1:end_index])
 
    print(sub_list)
    return sub_list

pivot=partition(0,N-1,a_list)
print(pivot)


#partition(start_index,pivot-1,a_list[start_index:pivot])
#print(end_index)
#print(pivot+1)
#partition(pivot+1,end_index,a_list[pivot+1:end_index+1])
"""
"""
while len(a_list[start_index:end_index-1])>1:
    end_index=pivot-1
    start_index=0
    partition(start_index,end_index,a_list[start_index:end_index])
    start_index=pivot
    end_index=N-1
    partition(start_index,end_index,a_list[start_index:end_index])
""" 

#print(pivot)

    




