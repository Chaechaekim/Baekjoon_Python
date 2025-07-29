import sys
input=sys.stdin.readline

while True:
    min_num=-1
    min_index=1
    compare_num=0
    B,N=map(int,input().rstrip().split())
    if B==0 & N==0:
        break
    for i in range(1,B):
        compare_num=abs(B-(i)**N)
        compare_num_1=abs(B-(-i)**N)
        if min_num==-1 or min_num>=compare_num or compare_num_1<min_num:
            if compare_num_1<compare_num:
                min_num=compare_num_1
                min_index=-i
            else:
                min_num=compare_num
                min_index=i
        else:
            break
    
    print(min_index)