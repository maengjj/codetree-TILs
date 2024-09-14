a, b = input().split()
b = int(b)

if a == 'A':
    for i in range(b):
        print(i+1, end=' ')
elif a == 'D':
    while b > 0 :
        print(b, end=' ')
        b -= 1