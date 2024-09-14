N = int(input())

numbers=[]

for i in range(N):
    number = int(input())
    numbers.append(number)

for i in numbers:
    if i % 2 ==1 and i % 3 ==0:
        print(i)