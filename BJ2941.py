cro_alpha=input()
#print(len(cro_alpha))
num2=0
num3=0
num1=0
i=0
alpha_num=0
change_alpha = ['c=','c-','d-','lj','nj','s=','z=']

while i<len(cro_alpha):
  if i+2<len(cro_alpha) and cro_alpha[i:i+3]=='dz=':
    i+=3
    num3+=1
  elif i+1<len(cro_alpha) and cro_alpha[i:i+2] in change_alpha:
    i+=2
    num2+=1
  else:
    i+=1
    num1+=1

print(num1+num2+num3)
"""
for i in range(len(cro_alpha)):
    if i==0 and 'dz=' in cro_alpha[i]+cro_alpha[i+1]+cro_alpha[i+2] :
        num3+=1
        i+=3
     #   print(num3)
    elif i+2<len(cro_alpha)-1 and 'dz=' in cro_alpha[i]+cro_alpha[i+1]+cro_alpha[i+2]:
        num3+=1
        i+=3
      #  print(i)
       
    for j in range(len(change_alpha)):
         # print(i)  
         # print( change_alpha[j])
           
        if i+1<len(cro_alpha)-1 and change_alpha[j] in cro_alpha[i]+cro_alpha[i+1]:
             num2+=1
             i+=2
        #    print( change_alpha[j])


print(num2, num3)
alpha_num = len(cro_alpha)-3*num3-2*(num2-num3)+num3+(num2-num3)
print(alpha_num)

"""