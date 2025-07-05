import sys
input=sys.stdin.readline
while True:
    aeiou_count=0
    m3_count=0
    j3_count=0
    s_count=0
    same_count=0

    password=input().rstrip()
    if password=='end':
        break
    for i in range(len(password)):
        if password[i]=='a' or password[i]=='e' or password[i]=='i' or password[i]=='o' or password[i]=='u' :
            aeiou_count=1
            m3_count+=1
            j3_count=0
            if m3_count==3:
                s_count=1
        else:
            j3_count+=1
            m3_count=0
            if j3_count==3:
                s_count=1
        
        if i!=0:
            if password[i]!='e' and  password[i]!='o':
                if password[i]==password[i-1]:
                    same_count=1
                    
    if aeiou_count==0 or s_count!=0 or same_count!=0:
        print('<'+password+'> is not acceptable.')
    else:print('<'+password+'> is acceptable.')