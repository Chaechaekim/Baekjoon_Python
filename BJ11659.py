num=list(map(int, input().split(' ')))
numbers= list(map(int, input().split(' ')))
sections = []
sum_numbers=[]
output=0

for i in range(num[0]):
    if i==0:
        sum_numbers.append(numbers[0])
    else:
        sum_numbers.append(sum_numbers[i-1]+numbers[i])

for j in range(num[1]):
    sections.append(list(map(int, input().split(' '))))
   # sections.append( input().split(' ')) 

for i in range(num[1]):
    if(sections[i][0]==1):
        print(sum_numbers[sections[i][1]-1])
    else:
        output = sum_numbers[sections[i][1]-1]-sum_numbers[sections[i][0]-2]
        print(output)



#print(sections[0])
#print(num)
#print(numbers)
#print(sum_numbers)
#print(sections)