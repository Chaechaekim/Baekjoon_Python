import sys
input=sys.stdin.readline
T=int(input().rstrip())
for i in range(T):
    num1,num2=map(int,input().rstrip().split())
    print('Case #'+str(i+1)+": "+str(num1)+" + "+str(num2)+" = "+str(num1+num2))