import sys
input=sys.stdin.readline
num=int(input().rstrip())
dic={}
for i in range(num):
    name,el=input().rstrip().split()
    if el=='enter':
        dic[name]=el
    else:del dic[name]

dic_list=list(dic.items())
dic_list.sort(key=lambda x:x[0],reverse=True)
for i in range(len(dic_list)):
    print(dic_list[i][0])