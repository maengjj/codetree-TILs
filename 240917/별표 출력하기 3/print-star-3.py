n = int(input())

for i in range(n, 0, -1):
    for j in range(2*n-2*i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end=' ')
    print()