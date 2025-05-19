import sys
input=sys.stdin.readline
n=int(input().rstrip())
if n*0.15-int(n*0.15)<0.5:
    remove=int(n*0.15)
else:remove=int(n*0.15)+1
sum=0
num_list=[]
for j in range(n):
    num_list.append(int(input().rstrip()))
num_list.sort()
for i in range(n):
    if i>remove-1 and i<n-remove:
        sum+=num_list[i]
if n==0:
    print(0)
elif ((sum)/(n-(remove*2)))-int((sum)/(n-(remove*2)))<0.5:
    print(int(((sum)/(n-(remove*2)))))
else:print(int((sum)/(n-(remove*2)))+1)