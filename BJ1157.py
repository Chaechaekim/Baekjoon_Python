#print(ord('M')+32==ord('m'))
strings=input()
strings=strings.upper()
#sorted_string=''.join(sorted(strings))
string_dict={}

for string in strings:
    if(string in string_dict):
        string_dict[string]+=1
    else:
        string_dict[string]=1




#print(string_dict)
ans=""
for key in string_dict:
    if(string_dict[key]==max(string_dict.values())):
        ans+=key

if len(ans)==1:
    print(ans)
else:
    print('?')