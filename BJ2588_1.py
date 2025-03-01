# 2588번 다른 방식으로 풀어보기
num1=int(input())
num2=input()

num3 = num1 * int(num2[2])
num4 = num1 * int(num2[1])
num5 = num1 * int(num2[0])

num6 = num3 + num4 * 10 + num5 * 100
print(num3,num4,num5,num6)