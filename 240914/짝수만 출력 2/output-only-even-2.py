b, a = map(int, input().split())

if b % 2 ==0:
    while b-a >= 0:
        print(b, end=' ')
        b -= 2
else:
    b = b-1
    while b-a >= 0:
        print(b, end=' ')
        b -= 2