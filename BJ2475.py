num1,num2,num3,num4,num5=input().split()
num1=int(num1)
num2=int(num2)
num3=int(num3)
num4=int(num4)
num5=int(num5)
sum_num=num1**2+num2**2+num3**2+num4**2+num5**2
valid=sum_num%10
print(valid)