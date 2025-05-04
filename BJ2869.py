import sys
import math
input=sys.stdin.readline
A,B,V=map(int,input().rstrip().split())
if (V-A)%(A-B)==0:
    print(int(((V-A)/(A-B))+1))
else:print(int(math.ceil((V-A)/(A-B))+1))