n = int(input())

num1 = 0
for i in range(1, 101):
    num1 += i
    if num1 >= n:
        print(i)
        break