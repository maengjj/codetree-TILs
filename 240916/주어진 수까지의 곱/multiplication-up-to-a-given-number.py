a, b = map(int, input().split())

p = 1

for i in range(a, b+1):
    p *= i

print(p)