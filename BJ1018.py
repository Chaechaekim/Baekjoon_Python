import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
wb_list=[]
count_wb=0
count_bw=0
count=[]
for _ in range(N):
    wb_list.append(input().rstrip())
for k in range(M-8+1):
    for a in range(N-8+1):
        for i in range(8): 
            for j in range(8):
                #wb
                if i%2==0 and j%2==0 and wb_list[i+a][j+k]=='B':
                    count_wb+=1
                elif i%2==0 and j%2==1 and wb_list[i+a][j+k]=='W':
                    count_wb+=1
                elif i%2==1 and j%2==0 and wb_list[i+a][j+k]=='W':
                    count_wb+=1
                elif i%2==1 and j%2==1 and wb_list[i+a][j+k]=='B':
                    count_wb+=1
        
                #bw
                if i%2==0 and j%2==0 and wb_list[i+a][j+k]=='W':
                    count_bw+=1
                elif i%2==0 and j%2==1 and wb_list[i+a][j+k]=='B':
                    count_bw+=1
                elif i%2==1 and j%2==0 and wb_list[i+a][j+k]=='B':
                    count_bw+=1
                elif i%2==1 and j%2==1 and wb_list[i+a][j+k]=='W':
                    count_bw+=1
                #print(i,j,count_bw) 
        count.append(count_bw)
        count.append(count_wb) 
        count_bw=0
        count_wb=0   
count.sort()
print(count[0])