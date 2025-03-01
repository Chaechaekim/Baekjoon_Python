nums = list(map(int,input().split()))
baskets = []
numbers=[]
for i in range(nums[0]):
    baskets.append(i+1)
for _ in range(nums[1]):
    a,b = map(int,input().split())
    if(a-2==-1):
        baskets[a-1:b] = baskets[b-1::-1]
    else:
        baskets[a-1:b] = baskets[b-1:a-2:-1]
#print(baskets)
print(*baskets)
