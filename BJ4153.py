import sys
while True:
    A,B,C=map(int,sys.stdin.readline().split())
    if A==0 and B==0 and C==0:
        break
    if A==0 or B==0 or C==0:
        print('wrong')
    elif A**2+B**2==C**2 :
        print('right')
    elif A**2+C**2==B**2:
        print('right')
    elif B**2+C**2==A**2:
        print('right')
    else:print('wrong')