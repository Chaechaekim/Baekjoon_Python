import sys
input=sys.stdin.readline
count=0
try:
    while True:
        str_list=input().rstrip()
        count+=1
except:print(count)