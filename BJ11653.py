import sys
input=sys.stdin.readline
N=int(input().rstrip())
index=2
num=N
while True:
    if index>N:
        break
    if num%index==0:
        print(index)
        num=num//index
    else:
        index+=1    