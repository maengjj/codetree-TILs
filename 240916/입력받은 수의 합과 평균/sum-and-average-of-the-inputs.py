n = int(input())

sum_num = 0
cnt = 0

for i in range(n):
    num = int(input())
    sum_num += num
    cnt += 1

avg_num = round(sum_num/cnt, 1)

print(sum_num, avg_num)