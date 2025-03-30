import sys
num=''
ans=0
while num!='0':
    #num=input()
    num=sys.stdin.readline().strip('\n')
    if num=='0':
        break
    
    start_index=0
    end_index=len(num)-1
    ans=0
    while start_index<end_index:
        if num[start_index]!=num[end_index]:
            ans+=1     
        start_index+=1
        end_index-=1
    if ans!=0:
        print('no')
    else:
        print('yes')