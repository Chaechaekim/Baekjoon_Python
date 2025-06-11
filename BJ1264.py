import sys
input=sys.stdin.readline
alpha=['a','e','i','o','u','A','E','I','O','U']
while True:
    sum=0
    str_list=input().rstrip()
    if str_list=='#':
        break
    for i in range(10):
        sum+=str_list.count(alpha[i])
    print(sum)