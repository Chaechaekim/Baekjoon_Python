score_arr = []
n=20
sum_score=0
total_score=0
for i in range(20):
    score_arr.append(list(input().split()))
    if score_arr[i][2] == 'A+':
        sum_score+=float(score_arr[i][1])*4.5
        total_score+=float(score_arr[i][1])
    elif score_arr[i][2] == 'A0':
        sum_score+=float(score_arr[i][1])*4.0
        total_score+=float(score_arr[i][1])
    elif score_arr[i][2] == 'B+':
        sum_score+=float(score_arr[i][1])*3.5
        total_score+=float(score_arr[i][1])
    elif score_arr[i][2] == 'B0':
        sum_score+=float(score_arr[i][1])*3.0
        total_score+=float(score_arr[i][1])
    elif score_arr[i][2] == 'C+':
        sum_score+=float(score_arr[i][1])*2.5
        total_score+=float(score_arr[i][1])
    elif score_arr[i][2] == 'C0':
        sum_score+=float(score_arr[i][1])*2.0
        total_score+=float(score_arr[i][1])
    elif score_arr[i][2] == 'D+':
        sum_score+=float(score_arr[i][1])*1.5
        total_score+=float(score_arr[i][1])
    elif score_arr[i][2] == 'D0':
        sum_score+=float(score_arr[i][1])*1.0
        total_score+=float(score_arr[i][1])
    elif score_arr[i][2] == 'F':
        sum_score+=float(score_arr[i][1])*0.0
        total_score+=float(score_arr[i][1])
    else:
         total_score+=0

avg_score = sum_score/total_score
print(avg_score)
