n = int(input())

for i in range(1, n + 1):
    if i == 1 or i == n:  # 첫 번째 줄과 마지막 줄은 별을 n개 출력
        print('* ' * n)
    else:  # 중간 줄은 첫 번째 별과 마지막 별 사이에 공백을 포함
        print('* ' * i + '  ' * (n - i - 1) + '*')