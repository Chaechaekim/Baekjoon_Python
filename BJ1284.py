import sys
input=sys.stdin.readline
while True:
    count=1
    num=input().rstrip()
    if num=='0':
        break
    for i in range(len(num)):
        if num[i]=='1':
            count+=2
        elif num[i]=='0':
            count+=4
        else:count+=3
        count+=1
    print(count)