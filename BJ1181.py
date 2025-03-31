import sys
N=int(sys.stdin.readline())
sort_list=[]
for i in range(N):
    input_str=sys.stdin.readline().strip('\n')
    if (len(input_str),input_str) in sort_list:
        continue
    else:sort_list.append((len(input_str),input_str))
sort_list.sort()
for i in range(len(sort_list)):
    print(sort_list[i][1])