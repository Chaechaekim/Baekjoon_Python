import sys
input=sys.stdin.readline
num_list=[]
while True:
    sum_num=0
    num=int(input().rstrip())
    if num==-1:
        break
    for i in range(1,num):
        if num%i==0:
            num_list.append(i)
            sum_num+=i
    if sum_num!=num:
        print(str(num)+" is NOT perfect.")
    else:
        print(str(num)+" =",end=' ')
        for j in range(len(num_list)):
            if j==(len(num_list)-1):
                print(num_list[j])
            else:
                print(num_list[j],end=' ')
                print('+',end=' ')
    num_list.clear()