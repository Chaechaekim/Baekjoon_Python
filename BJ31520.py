import sys
input=sys.stdin.readline
num=input().rstrip()
count=0
for i in range(0,len(num)):
    if int(num[i])==i+1:
        count+=1
    else:break
if count==len(num):
    print(count)
else:print(-1)