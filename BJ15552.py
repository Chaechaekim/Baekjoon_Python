import sys
input=sys.stdin.readline
T=int(input().rstrip())
for i in range(T):
    num1,num2=map(int,input().rstrip().split())
    sys.stdout.write(str(num1+num2)+'\n')