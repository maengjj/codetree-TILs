n = int(input())

for i in range(n):
    if i == 0:
        print('* ' * n)
    else:
        print('  ' * (i - 1) + '*', end='')
        if i < n - 1:
            print(' ' * (2 * (n - i - 1) - 1) + '*', end='')
        print()