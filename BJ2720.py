import sys
from decimal import Decimal
input=sys.stdin.readline
T=int(input().rstrip())
for i in range(T):
    num=int(input().rstrip())
    num=num/100
    print(int(num//0.25),end=' ')
    num1=(Decimal(str(num))-Decimal('0.25')*(Decimal(str(num))//Decimal('0.25')))
    print(int(Decimal(num1)//Decimal('0.10')),end=' ')
    num2=(Decimal(str(num1))-Decimal('0.10')*(Decimal(str(num1))//Decimal('0.10')))
    print(int(Decimal(num2)//Decimal('0.05')),end=' ')
    num3=(Decimal(str(num2))-Decimal('0.05')*(Decimal(str(num2))//Decimal('0.05')))
    print(int(Decimal(num3)//Decimal('0.01')))