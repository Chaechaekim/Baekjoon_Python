import sys
input=sys.stdin.readline
num=int(input().rstrip())
n=2
for i in range(0,num):
    n+=(2**i)
print(n**2)