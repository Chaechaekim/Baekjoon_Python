import sys
input=sys.stdin.readline
M=int(input())
S=[0]*20
for i in range(M):
    parts=list(map(str,input().rstrip().split()))
    if len(parts)==2:
        operater,x=parts
        x=int(x)
    else:
        operater=parts
    if operater=='add':
        if x in S:
            continue
        else:
            S.append(x)
    elif operater=='remove':
        if x in S:
            S.remove(x)
    elif operater=='check':
        if x in S:
            print(1)
        else:print(0)
    elif operater=='toggle':
        if x in S:
            S.remove(x)
        else:S.append(x)
    elif operater==['all']:
        S.clear()
        S.extend([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif operater==['empty']:
        S.clear()