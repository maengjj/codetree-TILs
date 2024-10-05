def print_stars(n):
    for i in range(n):
        # 첫 번째 줄과 마지막 줄은 모두 별로 채움
        if i == 0 or i == n-1:
            print("* " * n)
        # 그 외의 줄은 첫 번째 별 이후로 공백이 포함됨
        else:
            print("* " + "  " * i + "*")

# 입력 받기
n = int(input())

# 출력하기
print_stars(n)