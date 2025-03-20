import sys
S=sys.stdin.readline()
alphabet_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
return_list=[]
for i in range(len(alphabet_list)):
    return_list.append(S.find(alphabet_list[i]))
print(*return_list)