n = int(input())

for i in range(1, n+1):
    if i%2==1:
        for j in range(int((i+1)/2)):
            print('*', end=' ')
        print()
    else:
        for j in range(n- int(i/2) + 1):
            print('*', end=' ')
        print()
for i in range(n, 0, -1):
    if i%2==1:
        for j in range(int((i+1)/2)):
            print('*', end=' ')
        print()
    else:
        for j in range(n- int(i/2) + 1):
            print('*', end=' ')
        print()