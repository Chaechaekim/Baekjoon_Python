import sys
num=int(sys.stdin.readline())
count=0
def factorial(n):
    if n==1:
        return n
    if n==0:
        return 1
    return n*factorial(n-1)

ans=factorial(num)
str_ans=str(ans)
for i in range(len(str_ans)-1,-1,-1):
    if str_ans[i]=='0':
        count+=1
    else:
        break

print(count)