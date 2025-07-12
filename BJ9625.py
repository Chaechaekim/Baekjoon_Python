import sys
input=sys.stdin.readline
num=int(input().rstrip())
a=1
b=0
for i in range(num):
    A=b
    B=a+b
    a=A
    b=B
print(str(A)+' '+str(B))