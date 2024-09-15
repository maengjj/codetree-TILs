a, b = map(int, input().split())
sum_num = 0
cnt = 0

for i in range(a, b+1):
    if i%5==0 or i%7==0:
        sum_num += i
        cnt += 1

avg_num = round(sum_num/cnt, 1)

print(sum_num, avg_num)