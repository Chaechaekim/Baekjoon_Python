s,p=map(int,input().split())
dna_list=list(input())
a,c,g,t=map(int,input().split())
start_index=0
end_index=p
count_num=0
a_count=0
c_count=0
g_count=0
t_count=0
trash=0

for k in range(start_index,end_index):
        if dna_list[k]=='A':
            a_count+=1
        elif dna_list[k]=='C':
            c_count+=1
        elif dna_list[k]=='G':
            g_count+=1
        elif dna_list[k]=='T':
            t_count+=1
        else:trash+=1
        #print(a_count,c_count,g_count,t_count,trash)

if a_count>=a and c_count>=c and g_count>=g and t_count>=t and trash==0:
          count_num+=1
while end_index<s:
    
    if dna_list[start_index]=='A':
         a_count-=1
    elif dna_list[start_index]=='C':
         c_count-=1
    elif dna_list[start_index]=='G':
         g_count-=1
    elif dna_list[start_index]=='T':
         t_count-=1
    else:
         trash-=1
    start_index+=1
    end_index+=1

    if dna_list[end_index-1]=='A':
         a_count+=1
    elif dna_list[end_index-1]=='C':
         c_count+=1
    elif dna_list[end_index-1]=='G':
         g_count+=1
    elif dna_list[end_index-1]=='T':
         t_count+=1
    else:trash+=1
    #print(a_count,c_count,g_count,t_count,trash)
    if a_count>=a and c_count>=c and g_count>=g and t_count>=t and trash==0:
          count_num+=1
  
print(count_num)
"""
s,p=map(int,input().split())
dna_list=list(input())
a,c,g,t=map(int,input().split())
start_index=0
end_index=p
count_num=0
a_count=0
c_count=0
g_count=0
t_count=0
trash=0

while end_index<=s:
    for i in range(start_index,end_index):
        if dna_list[i]=='A':
            a_count+=1
        elif dna_list[i]=='C':
            c_count+=1
        elif dna_list[i]=='G':
            g_count+=1
        elif dna_list[i]=='T':
            t_count+=1
        else:trash+=1
    
    if a_count>=a and c_count>=c and g_count>=g and t_count>=t and trash==0:
        count_num+=1

    start_index+=1
    end_index+=1
    a_count=0
    c_count=0
    g_count=0
    t_count=0
    trash=0
  
print(count_num)
"""
"""
s,p=map(int,input().split())
dna_list=list(input())
a,c,g,t=map(int,input().split())
start_index=0
end_index=p
count_num=0

while end_index<=s:
    if a==dna_list[start_index:end_index].count('A') and c==dna_list[start_index:end_index].count('C') and g==dna_list[start_index:end_index].count('G') and t==dna_list[start_index:end_index].count('T'):
        count_num+=1

    start_index+=1
    end_index+=1
  
print(count_num)
"""