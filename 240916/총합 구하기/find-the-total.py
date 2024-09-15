a, b = map(int, input().split())
sum_num = 0

for i in range(a, b+1):
    if i%6==0 and i%8!=0:
        sum_num += i

print(sum_num)