n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1:  # 첫 번째 줄과 마지막 줄
            print('*', end=' ')
        elif j == 0 or j == n - 1 or j == i:  # 중간 줄에서 첫 번째, 마지막, 대각선 위치에 별 출력
            print('*', end=' ')
        else:
            print(' ', end=' ')  # 그 외에는 공백 출력
    print()  # 한 줄이 끝날 때 줄 바꿈