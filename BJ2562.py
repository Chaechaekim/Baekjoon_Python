num_list=[0]*9
for i in range(9):
    num_list[i]=(int(input()),i+1)
sort_list=sorted(num_list)
print(sort_list[8][0])
print(sort_list[8][1])