import sys
num1,num2=map(int,sys.stdin.readline().split())
min_num=min(num1,num2)
num=1
i=2
while i<=min_num:
    if num1%i==0 and num2%i==0:
        num=i
    i+=1
div1=num1//num
div2=num2//num
print(num)
print(num*div1*div2)