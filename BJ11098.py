import sys
input=sys.stdin.readline
n=int(input().rstrip())
for i in range(n):
    p=int(input().rstrip())
    compare=0
    com_name=''
    for j in range(p):
        mon,name=map(str,input().rstrip().split())
        money=int(mon)
        if money>compare:
            compare=money
            com_name=name
    print(com_name)