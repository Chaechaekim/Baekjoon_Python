from collections import deque
N = int(input())
a_list=list(map(int,input().split()))
stack=deque()
num=0
check_list=[-1]*N

for i in range(N-1):
    stack.append(i)
    if a_list[i]<a_list[i+1]:
        check_list[stack.pop()]=a_list[i+1]
        while stack:
            num=stack.pop()
            if a_list[num]<a_list[i+1]:
                check_list[num]=a_list[i+1]
                num=0
            else:
                #print(num)
                stack.append(num)
                break
            
                
#check_list[N-1]=-1

#print(stack)
print(*check_list)

    


"""
N=int(input())
a_list=list(map(int,input().split()))
start_index=0
end_index=start_index+1
check_list=[0]*N


while start_index<N-1:
    if end_index==N:
        check_list[start_index]=-1
        start_index+=1
        end_index=start_index+1
    else:
        if a_list[start_index]<a_list[end_index]:
            check_list[start_index]=a_list[end_index]
            start_index+=1
            end_index=start_index+1
        else:
            end_index+=1
check_list[N-1]=-1

print(*check_list)
"""