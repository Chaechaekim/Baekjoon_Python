import sys
input=sys.stdin.readline
N=int(input())
num_arr=[0]*10000

for i in range(N):
    num=int(input())
    num_arr[num-1]+=1
for i in range(10000):
    if num_arr[i]!=0:
        for j in range(num_arr[i]):
            print(i+1)