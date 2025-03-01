import math
num = int(input())
score = list(map(int,input().split()))
max_score = max(score)

for i in range(num):
    score[i] = score[i]/max_score*100
   
sum_score = sum(score)
avg_score = sum_score/num

print(avg_score)






