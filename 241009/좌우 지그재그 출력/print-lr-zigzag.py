n = int(input())
cnt = 1

for i in range(1, n+1):
    if i % 2 == 1:
        for j in range(n):
            print(cnt, end=' ')
            cnt += 1
        print()
    else:
        for j in range(n, 0, -1):
            print(n+j, end=' ')
            cnt += 1
        print()