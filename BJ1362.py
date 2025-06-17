import sys
input=sys.stdin.readline
count=0
while True:
    o,w=map(int,input().rstrip().split())
    alive=0
    count+=1
    if o==0 and w==0:
        break
    while True:
        action,number=map(str,input().rstrip().split())
        num=int(number)
        if action=='#' and num==0:
            break
        elif action=='F':
            if alive==0:
                w+=num
        elif action=='E':
            if alive==0:
                w-=num
        if w<=0:
            alive=1
    if alive==1:
        print(count,end=' ')
        print('RIP')
    elif w>(o/2) and w<(o*2):
        print(count,end=' ')
        print(':-)')
    else:
        print(count,end=' ')
        print(':-(')