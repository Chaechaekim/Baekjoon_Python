N=int(input())
M=int(input())
num_list=list(map(int,input().split()))
sort_list=sorted(num_list)
end_index=N-1
start_index=0
count=0

while start_index<end_index: 
    if sort_list[start_index]+sort_list[end_index]>M:
            #print('처음1','마지막1',sort_list[start_index],sort_list[end_index])
            end_index-=1
    elif sort_list[start_index]+sort_list[end_index]==M:
            #print('처음2','마지막2',sort_list[start_index],sort_list[end_index])
            count+=1
            start_index+=1
            end_index-=1
    else:
            #print('처음3','마지막3',sort_list[start_index],sort_list[end_index])
            start_index+=1
   

print(count)

"""
N=int(input())
M=int(input())
num_list=list(map(int,input().split()))
#print(num_list)
sort_list=sorted(num_list)
#print(sort_list)
end_index=1
start_index=0
sum_num=0
count=0

while start_index<N-1:
    if end_index >= N:
        start_index+=1
        end_index=start_index+1
    
        
    sum_num=sort_list[start_index]+sort_list[end_index]
    if sum_num>M:
            #print('처음1','마지막1',sort_list[start_index],sort_list[end_index],sum_num)
            start_index+=1
            end_index=start_index+1
            sum_num=0
    elif sum_num==M:
            #print('처음2','마지막2',sort_list[start_index],sort_list[end_index],sum_num)
            count+=1
            start_index+=1
            end_index=start_index+1
            sum_num=0
    else:
            #print('처음3','마지막3',sort_list[start_index],sort_list[end_index],sum_num)
            sum_num=0
            end_index+=1
   
    

print(count)
"""

"""
N=int(input())
M=int(input())
num_list=list(map(int,input().split()))
#print(num_list)
end_index=1
start_index=0

sum_num=num_list[start_index]
count=0


while end_index<N:
    sum_num+=num_list[end_index]
    if(sum_num>M):
       # print('sum_num3',sum_num)
        print('처음1','마지막1',num_list[start_index],num_list[end_index],sum_num)
        start_index+=1
        end_index=start_index+1
        sum_num=num_list[start_index]

    elif(sum_num==M):
          #  print('sum_num2',sum_num)
            print('처음2','마지막2',num_list[start_index],num_list[end_index],sum_num)
            count+=1
            sum_num=0
            start_index+=1
            end_index=start_index+1
            sum_num=num_list[start_index]
            #i+=1
    else:
         print('처음3','마지막3',num_list[start_index],num_list[end_index],sum_num)
         #print(sum_num)
         end_index+=1
       
        #i+=1

print(count)
"""