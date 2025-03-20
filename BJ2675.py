import sys
T=int(sys.stdin.readline())
t=[]
str_list=[]
for i in range(T):
    num,text=sys.stdin.readline().split()
    for j in range(len(text)):
        str_list.append(int(num)*text[j])
    str_list.append('\n')
    #t.append(tuple(sys.stdin.readline().split()))
    #print(int(t[i][0])*t[i][1])

print(*str_list,sep='')
    
   

