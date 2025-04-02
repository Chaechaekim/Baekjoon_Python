import sys
for i in range(3):
    fb=sys.stdin.readline().strip('\n')
    if fb!='FizzBuzz' and fb!='Fizz' and fb!='Buzz':
        num=int(fb)+(3-i)
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:print(num)