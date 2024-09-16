n = int(input())

cnt = 0
for i in range(1, n+1):
    if n // i > 1:
        n = n//i
        cnt +=1
        continue
    if n// i <= 1:
        cnt +=1
        break

print(cnt)