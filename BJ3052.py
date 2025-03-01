nums = []
for _ in range(10):
    nums.append(int(input()))

div=[]

for num in nums:
    if num % 42 in div:
        pass
    else:
        div.append(num%42)

print(len(div))


