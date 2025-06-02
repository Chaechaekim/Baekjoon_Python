import sys
input=sys.stdin.readline
for i in range(100):
    str_list=input().rstrip()
    if str_list=='':
        break
    print(str_list)