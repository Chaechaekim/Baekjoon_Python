import sys
input=sys.stdin.readline
N,B=map(str,input().rstrip().split())
B=int(B)
sum_num=0
for i in range(len(N)):
    if N[i]=='A':
        n=10
    elif N[i]=='B':
        n=11
    elif N[i]=='C':
        n=12
    elif N[i]=='D':
        n=13
    elif N[i]=='E':
        n=14
    elif N[i]=='F':
        n=15
    elif N[i]=='G':
        n=16
    elif N[i]=='H':
        n=17
    elif N[i]=='I':
        n=18
    elif N[i]=='J':
        n=19
    elif N[i]=='K':
        n=20
    elif N[i]=='L':
        n=21
    elif N[i]=='M':
        n=22
    elif N[i]=='N':
        n=23
    elif N[i]=='O':
        n=24
    elif N[i]=='P':
        n=25
    elif N[i]=='Q':
        n=26
    elif N[i]=='R':
        n=27
    elif N[i]=='S':
        n=28
    elif N[i]=='T':
        n=29
    elif N[i]=='U':
        n=30
    elif N[i]=='V':
        n=31
    elif N[i]=='W':
        n=32
    elif N[i]=='X':
        n=33
    elif N[i]=='Y':
        n=34
    elif N[i]=='Z':
        n=35
    else:
        n=int(N[i])
    sum_num+=n*(B**(len(N)-i-1))
print(sum_num)