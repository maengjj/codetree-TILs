n = int(input())
cond = False

for i in range(2, n):
    if n % i == 0:
        cond=True

if cond==True:
    print("C")
else:
    print("N")