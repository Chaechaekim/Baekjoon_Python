import sys
input=sys.stdin.readline
N=int(input().rstrip())
start_index=0
end_index=N-1
num=0
n_list=list(map(int,input().rstrip().split()))
n_list.sort()
M=int(input().rstrip())
m_list=list(map(int,input().rstrip().split()))
for i in range(M):
    while start_index<=end_index:
        mid_index=(start_index+end_index)//2
        if m_list[i]==n_list[mid_index]:
            print(1)
            num=1
            break
        elif m_list[i]<n_list[mid_index]:
            end_index=mid_index-1
        else:start_index=mid_index+1
    if num==0:
        print(0)
    num=0
    start_index=0
    end_index=N-1