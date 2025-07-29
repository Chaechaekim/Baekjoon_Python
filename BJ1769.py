import sys
input=sys.stdin.readline
num=input().rstrip().split()
count=0
while True:  
    s_num=0
    count+=1
    if len(num)!=1: 
        for i in range(len(num)):
            s_num+=int(num[i])
        sum_num=str(s_num)
    else:
        sum_num=num
        s_num=[int(x) for x in sum_num]
    
    if len(sum_num)==1:
        if s_num%3==0:
            print(count)
            print('YES')
            break
        else:
            print(count)
            print('NO')
            break