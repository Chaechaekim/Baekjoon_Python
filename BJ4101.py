import sys
input=sys.stdin.readline
while True:
    num1,num2=map(int,input().rstrip().split())
    if num1==0 and num2==0:
        break
    if num1>num2:
        print('Yes')
    else:print('No')