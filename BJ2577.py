import sys
abc=[]
for i in range(3):
    abc.append(int(sys.stdin.readline()))
num_list=['0','1','2','3','4','5','6','7','8','9']
mul_num=abc[0]*abc[1]*abc[2]
str_mul=str(mul_num)
pri_num=0

for i in range(len(num_list)):
    pri_num=str_mul.count(num_list[i])
    print(pri_num)