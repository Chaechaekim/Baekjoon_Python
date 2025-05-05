num=int(input())
n=0
ans=0
for i in range(1,num):
    if num-1<=6*n:
        break
    else:
        n+=i
        ans=i
print(ans+1)