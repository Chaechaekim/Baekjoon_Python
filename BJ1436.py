import sys
input=sys.stdin.readline
N=int(input().rstrip())
ans=666
count=0
while True:
    if '666' in str(ans):
        count+=1
    if count==N:
        print(ans)
        break
    ans+=1