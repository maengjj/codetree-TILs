n = int(input())

for i in range(0, 2*n, 2):
    for j in range(1, 2*n, 2):
        print(10+j+i, end=' ')
    print()