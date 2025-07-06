import sys
input=sys.stdin.readline
num=int(input().rstrip())
dic={}
for i in range(num):
    word=input().rstrip()
    if word in dic:
        dic[word]+=1
    else:dic[word]=1
dic_list=list(dic.items())
dic_list.sort(key=lambda x:x[0])
print(*dic_list[-1])