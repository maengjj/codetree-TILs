triangle = [
    [0 for _ in range(15)]
    for _ in range(15)
]

n = int(input())
	
for i in range(n):
	triangle[i][0] = 1
	triangle[i][i] = 1

for i in range(n):
	for j in range(1, i):
		triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

for i in range(n):
	for j in range(i + 1):
		print(triangle[i][j], end=" ")
	print()