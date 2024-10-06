n = int(input())
cnt = [2, 4, 6, 8]

for i in range(n):
    for j in range(n):
        print(cnt[(i + j) % 4], end=' ')
    print()