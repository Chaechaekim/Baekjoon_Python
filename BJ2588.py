#https://www.acmicpc.net/problem/2588
num1 = int(input())
num2 = int(input())

num3 = num1*(num2%10)
print(num3)
num4 = num1*((num2%100)//10)
print(num4)
num5 = num1*(num2//100)
print(num5)

answer = num3 + num4*10 + num5*100
print(answer)