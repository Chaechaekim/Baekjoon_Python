import sys
input=sys.stdin.readline
while True:
    x,y=map(int,input().rstrip().split())
    if x==0 and y==0:
        break
    if x+y==13:
        print("Never speak again.")
    elif y>x:
        print("Left behind.")
    elif x>y:
        print("To the convention.")
    else:print("Undecided.")