N, M = map(int, input().split())
a_list = list(map(int, input().split()))

count = 0
prefix_mod = [0] * M  # 나머지를 저장하는 배열
prefix_sum = 0

for i in range(N):
    prefix_sum +=a_list[i]
    mod = prefix_sum % M
    count+=prefix_mod[mod]
    prefix_mod[mod]+=1

count+=prefix_mod[0]

print(count)
"""
for i in range(N):
    prefix_sum += a_list[i]
    mod = prefix_sum % M  # 현재 누적합의 나머지 계산
    count += prefix_mod[mod]  # 이전에 같은 나머지가 나온 개수만큼 count 증가
    prefix_mod[mod] += 1  # 현재 나머지 개수 증가

# 나머지가 0인 경우(처음부터 현재 위치까지 합이 M의 배수인 경우)도 포함해야 함
count += prefix_mod[0]

print(count)
"""


"""
N,M=map(int,input().split())
a_list=list(map(int,input().split())) 
sum_list=[]
count=0
c=0
r_list=[]
sum_list.append(0)
for i in range(1,N+1):
    sum_list.append(sum_list[i-1]+a_list[i-1])
    if(sum_list[i]%3==0):
        c+=1

print((2**c)-1)
"""
            
#print(c)
"""
N,M=map(int,input().split())
a_list=list(map(int,input().split())) 
sum_list=[]
count=0
sum_list.append(0)

for i in range(1,N+1):
    sum_list.append(sum_list[i-1]+a_list[i-1])
    for j in range(i):
        if (sum_list[i]-sum_list[j])%M==0:
            count+=1
            
print(count)
"""
