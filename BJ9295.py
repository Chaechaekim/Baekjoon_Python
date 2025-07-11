import sys
input=sys.stdin.readline
num=int(input().rstrip())
for i in range(num):
    num1,num2=map(int,input().rstrip().split())
    print("Case "+str(i+1)+": " +str(num1+num2))