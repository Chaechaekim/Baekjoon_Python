num_size = int(input())
nums=[]


for i in range(num_size):
   # nums=list(map(int,input().split('/n')))
   nums.append(int(input()))
#print(nums)
nums.sort()
print(*nums)